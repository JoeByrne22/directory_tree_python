import os

def generate_tree(directory, indent=" "):
    """
    Recursively generates and prints the directory tree.
    """
    print(indent + os.path.basename(directory) + "/")  # Print the current directory name

    items = os.listdir(directory)

    for item in sorted(items):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            generate_tree(item_path, indent + "  ")
        else:
            print(indent + " " + item)

if __name__ == "__main__":
    root_directory = input("Enter the path of the root directory: ")
    generate_tree(root_directory)