from functions.get_files_info import *
from functions.get_file_content import *

working_dir = "calculator"

def main():
    pass

def test_get_content():
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content(working_dir, "main.py"))
    print(get_file_content(working_dir, "pkg/calculator.py"))
    print(get_file_content(working_dir, "pkg/nonexistent.py"))
    print(get_file_content(working_dir, "/bin/cat"))


def test_get_info():
    root_contents = get_files_info(working_dir, ".")
    print(root_contents)

    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)

    bin_contents = get_files_info(working_dir, "/bin")
    print(bin_contents)

    dot_contents = get_files_info(working_dir, "../")
    print(dot_contents)

main()