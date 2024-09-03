import os

def print_directory_contents(directory):
    # Get list of files and directories in the specified directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Example usage:
directory_path = "/path/to/your/directory"  # Replace with your directory path
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)