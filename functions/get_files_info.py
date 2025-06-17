# get_files_info.py

import os

def get_files_info(working_directory, directory=None) -> str:
    
    working_path = os.path.abspath(working_directory) 
    target = os.path.join(working_path, directory)
    #print(working_path)
    #print(target)

    if working_path not in target or "../" in directory:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory.'

    return_string = ''
    with os.scandir(target) as target:
        for item in target:
            return_string += f'{item.name}: file_size: {item.stat().st_size} bytes, is_dir={item.is_dir()}\n'
    return return_string
