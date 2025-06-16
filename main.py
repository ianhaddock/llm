# main.py

import os
import sys
from google import genai
from dotenv import load_dotenv





def main():
	load_dotenv()
	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	args = sys.argv[1:]

	if not args:
		print("ERROR: submit with the prompt: main.py 'why is the sky blue?'")
		sys.exit(1)

	user_prompt = ' '.join(args)

	response = client.models.generate_content(
		model='gemini-2.0-flash-001', 
		contents=user_prompt
	)

	print(" >> -- << ")
	print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
	print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
	print("Response:")
	print(response.text)


if __name__ == "__main__":
	main()

