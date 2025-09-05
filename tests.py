from functions.get_files_info import *

def main():
    working_dir = "calculator"
    root_contents = get_files_info(working_dir, ".")
    print(root_contents)

    pkg_contents = get_files_info(working_dir, "pkg")
    print(pkg_contents)

    bin_contents = get_files_info(working_dir, "/bin")
    print(bin_contents)

    dot_contents = get_files_info(working_dir, "../")
    print(dot_contents)
main()