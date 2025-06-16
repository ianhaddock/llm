# main.py

import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv





def main():
	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	args = sys.argv[1:]

	if not args:
		print("ERROR: submit with the prompt: main.py 'why is the sky blue?'")
		sys.exit(1)

	if args[-1] == "--verbose":
		user_prompt = ' '.join(args[:-1])
	else:
		user_prompt = ' '.join(args)

	messages = [
		types.Content(role="user", parts=[types.Part(text=user_prompt)]),
	]

	response = client.models.generate_content(
		model='gemini-2.0-flash-001', 
		contents=messages,
	)

	if args[-1] == "--verbose":
		print(f"User prompt: {user_prompt}")
		print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
		print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
		print("Response:")
		print(response.text)
	else:
		print(response.text)	


if __name__ == "__main__":
	main()

