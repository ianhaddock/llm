# write_file.py

import os
from google.genai import types


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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a single file, constrained files inside the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

