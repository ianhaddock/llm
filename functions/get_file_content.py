# get_file_content.py

import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path) -> str:
    
    working_path = os.path.abspath(working_directory) 
    target = os.path.abspath(os.path.join(working_path, file_path))
    #print(working_path)
    #print(target)

    if not target.startswith(working_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target):
        return f'Error: File not found or not a regular file: "{file_path}"'

    try:
        with open(target, 'r') as file:
            file_content_string = file.read(MAX_CHARS)
    except Exception as e:
        return f"Error reading file: {e}"

    if len(file_content_string) == MAX_CHARS:
        file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string
