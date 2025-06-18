# run_python_file.py

import os
import subprocess 
from google.genai import types


def run_python_file(working_directory, file_path, args=None) -> str:
    
    working_path = os.path.abspath(working_directory) 
    target = os.path.abspath(os.path.join(working_path, file_path))
    #print(working_path)
    #print(target)

    if not target.startswith(working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
         return f'Error: "{file_path}" is not a Python file.'

    commands = ["python", target]
    if args:
        commands.extend(args)

    try:
        result = subprocess.run(
                commands, 
                capture_output=True, 
                text=True, 
                cwd=working_path,
                timeout=30
                )
        output = []
        if result.stdout:
            output.append(f'STDOUT:\n{result.stdout}')
        if result.stderr:
            output.append(f'STDERR:\n{result.stderr}')
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')

    except Exception as e:
        return f"Error executing Python file: {e}"

    output_string = "\n".join(output) if output else "No output produced."

    return output_string


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a python file in a subprocess, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                    ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)

