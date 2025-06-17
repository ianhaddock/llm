# main.py

import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


def get_files():
    print(get_files_info('calculator', '.'))
    print(get_files_info('calculator', 'pkg'))
    print(get_files_info('calculator', '/bin'))
    print(get_files_info('calculator', 'tests.py'))
    print(get_files_info('calculator', 'pkg/../../'))

def get_contents():
    print(get_file_content('calculator', 'main.py'))
    print(get_file_content('calculator', 'pkg/calculator.py'))
    print(get_file_content('calculator', '/bin/cat'))

def write_to_files():
    print(write_file('calculator', 'lorem.txt', "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file('calculator', '/tmp/temp.txt', "this should not be allowed"))


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = "--verbose" in sys.argv

    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("ERROR: submit with the prompt: main.py 'why is the sky blue?'")
        print("Add '--verbose' at the end for more info")
        sys.exit(1)

    user_prompt = ' '.join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
    )

    if verbose:
        print(f"User prompt: {user_prompt}\n")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response:")
        print(response.text)
    else:
        print("Response:")
        print(response.text)    


if __name__ == "__main__":
    # main()
    # get_files()
    # get_contents()
    write_to_files()
