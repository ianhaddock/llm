# call_functions.py

import os
from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call_part, verbose=False):
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    print(f" - Calling function: {function_call_part.name}")

    full_args = {'working_directory', './calculator'}
    full_args.update(function_call_part.args)
    
    commands = {
            'get_file_contents': get_file_content(**full_args),
            'get_files_info': get_files_info(**full_args),
            'run_python_file': run_python_file(**full_args),
            'write_file': write_file(**full_args),
            }            

    if function_call_part.name not in commands:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_result = commands["function_call_part.name"]
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

