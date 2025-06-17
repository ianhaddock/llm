# write_file.py

import os

def write_file(working_directory, file_path, content) -> str:
    
    working_path = os.path.abspath(working_directory) 
    target = os.path.abspath(os.path.join(working_path, file_path))
    #print(working_path)
    #print(target)

    if not target.startswith(working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target):
        try:
            os.makedirs(os.path.dirname(target), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(target) and os.path.isdir(target):
            return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(target, 'w') as file:
            file.write(content)
    except Exception as e:
        return f"Error reading file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
