import os
import tarfile

def generate_tree(directory, prefix=''):
    items = os.listdir(directory)
    items.sort()

    for index, item in enumerate(items):
        item_path = os.path.join(directory, item)
        is_last = index == len(items) - 1

        if is_last:
            print(f"{prefix}└── {item}")
            new_prefix = f"{prefix}    "
        else:
            print(f"{prefix}├── {item}")
            new_prefix = f"{prefix}│   "

        if os.path.isdir(item_path):
            generate_tree(item_path, new_prefix)

def extract_tar_gz(file_path, extract_to):
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=extract_to)

def main():
    file_path = input("Enter the path to the .tar.gz file: ").strip()

    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    # Create a directory to extract the contents
    extract_to = os.path.splitext(file_path)[0]  # Remove .tar.gz extension
    os.makedirs(extract_to, exist_ok=True)

    # Extract the .tar.gz file
    extract_tar_gz(file_path, extract_to)

    # Print the directory tree
    print(f"Directory tree for extracted contents of '{file_path}':")
    generate_tree(extract_to)

if __name__ == '__main__':
    main()
