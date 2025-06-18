# get_files_info.py

import os
from google.genai import types


def get_files_info(working_directory, directory=None) -> str:
    
    working_path = os.path.abspath(working_directory) 
    target = working_path
    if directory:
        target = os.path.abspath(os.path.join(working_path, directory))
    #print(working_path)
    #print(target)

    if not target.startswith(working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory.'

    return_string = ''
    try:
        with os.scandir(target) as target:
            for item in target:
                return_string += f'{item.name}: file_size: {item.stat().st_size} bytes, is_dir={item.is_dir()}\n'
        return return_string
    except Exception as e:
        return f"Error listing files: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

