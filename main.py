import os
from dotenv import load_dotenv
import google.generativeai as genai
import sys

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    genai.configure(api_key=api_key)
    print("Args", sys.argv)
    if len(sys.argv) <2:
        print(" I need a prompt!")
        sys.exit(1)

    prompt = sys.argv[1]

    client = genai.GenerativeModel()
    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content(contents=prompt)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
