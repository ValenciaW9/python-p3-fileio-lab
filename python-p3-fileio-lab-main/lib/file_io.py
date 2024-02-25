import os

def write_file(file_name, file_content):
    lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    file_path = os.path.join(lib_dir, f"{str(file_name)}.txt")
    with open(file_path, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    file_path = os.path.join(lib_dir, f"{str(file_name)}.txt")
    with open(file_path, "a") as file:
        file.write(append_content)

def read_file(file_name):
    lib_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    file_path = os.path.join(lib_dir, f"{str(file_name)}.txt")
    with open(file_path, "r") as file:
        content = file.read()
    return content