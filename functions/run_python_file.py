# run_python_file.py

import os
import subprocess 

def run_python_file(working_directory, file_path) -> str:
    
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

    try:
        #with open(target, 'r') as file:
        completed_process = subprocess.run(["python", target], capture_output=True, text=True, cwd=os.path.dirname(target), timeout=30)
    except Exception as e:
        return f"Error executing Python file: {e}"

    output_string = f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}\n'

    return output_string
