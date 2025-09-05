import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from functions.get_files_info import *

def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

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

    model_name = "gemini-2.0-flash-001"
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
            model=model_name,
            contents=messages
        )
    print(response.text)
    if verbose_flag:
        print(f"Users question: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

main()
