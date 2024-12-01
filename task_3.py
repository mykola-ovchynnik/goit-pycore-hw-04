import sys
from pathlib import Path
import colorama

colorama.init(autoreset=True)


def print_directory_structure(directory, prefix=""):
    try:
        for path in sorted(directory.iterdir()):
            if path.is_dir():
                print(f"{prefix}{colorama.Fore.BLUE}{path.name}")
                print_directory_structure(path, prefix + "    ")
            else:
                print(f"{prefix}{colorama.Fore.GREEN}{path.name}")
    except PermissionError:
        print(f"{prefix}{colorama.Fore.RED}Permission Denied")


def main():
    # python hw03.py <directory_path>
    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{colorama.Fore.RED}Error: The path '{directory_path}' does not exist.")
        exit(1)

    if not directory_path.is_dir():
        print(
            f"{colorama.Fore.RED}Error: The path '{directory_path}' is not a directory."
        )
        exit(1)

    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()
