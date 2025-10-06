import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python_file import *
from functions.write_file import *
from call_function import *

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read the content of a file
    - Write to a file (create or update)
    - Run a Python files with optional arguments
    When the user asks about code project - they are referring to the working directory. So, you should typically start by looking at the projects files, and figuring out how to run the project and 
    how to run its tests. You'll always want to test the tests and the actual project to verify that the behavior is working.
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    print("Args", sys.argv)
    if len(sys.argv) <2:
        print(" I need a prompt!")
        sys.exit(1)

    verbose_flag = False

    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True

    prompt = sys.argv[1]

    messages = [
        types.Content(role="user",
                      parts=[types.Part(text=prompt)]
                      )
    ]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=types.Content(
            role="system",
            parts=[types.Part(text=system_prompt)]))

    max_iters = 20
    for i in range(0, max_iters):

        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=config)

        if response is None or response.usage_metadata is None:
            print("Response is malformed")
            return


        if verbose_flag:
            print(f"Users question: {prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        ### puts all of the functions models wants to call in an array
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)

        ### here we are going to actually call the functions in the array
        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part, verbose_flag)
                messages.append(result)

        if not response.function_calls:
            # final agent text message
            print(response.text)
            return

        for function_call_part in response.function_calls:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")

main()
