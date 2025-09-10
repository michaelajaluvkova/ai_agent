from functions.get_files_info import *
from functions.get_file_content import *
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from functions.run_python_file import run_python_file

working_dir = "calculator"

def main():
    print(run_python_file(working_dir, "main.py"))
    print(run_python_file(working_dir, "tests.py"))
    print(run_python_file(working_dir, "../main.py"))
    print(run_python_file(working_dir, "nonexistent.py"))
    print(run_python_file(working_dir, "main.py", ["3 + 5"]))

def test_write_file():
    print(write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file(working_dir, "/tmp/temp.txt", "this should not be allowed"))
    print(write_file(working_dir, "pkg2/temp.txt", "this should be allowed"))

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