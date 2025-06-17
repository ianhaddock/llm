# main.py

import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

from functions.get_files_info import get_files_info

def get_files():
	get_files_info('calculator', '.')
	get_files_info('calculator', 'pkg')
	get_files_info('calculator', '/bin')
	get_files_info('calculator', 'tests.py')
	get_files_info('calculator', 'pkg/../../')


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
	get_files()
