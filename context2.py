import os
import sys

def compile_codebase(directory, output_file, ignore_list=None):
    """
    Traverses a directory, including subfolders, and saves the content of all files
    into a single text file, with headers for each file path.

    Args:
        directory (str): The path to the root directory to start traversal from.
        output_file (str): The name of the text file to save the compiled code to.
        ignore_list (list, optional): A list of files or directories to ignore.
                                      Defaults to a list of common unnecessary files.
    """
    script_name = os.path.basename(sys.argv[0])

    if ignore_list is None:
        ignore_list = [
            '.git', '.vscode', '__pycache__', 'node_modules',
            '.DS_Store', 'package-lock.json', 'yarn.lock',
            output_file,
            script_name
        ]
    
    # NEW: List of image extensions to exclude
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico']

    directory = os.path.abspath(directory)
    print(f"Starting compilation from: {directory}")

    try:
        with open(output_file, 'w', encoding='utf-8', errors='ignore') as f_out:
            for root, dirs, files in os.walk(directory, topdown=True):
                dirs[:] = [d for d in dirs if d not in ignore_list]

                for filename in files:
                    # Skip files in the main ignore list
                    if filename in ignore_list:
                        continue
                    
                    # NEW: Skip files with image extensions
                    if any(filename.lower().endswith(ext) for ext in image_extensions):
                        print(f"  -> Ignoring image: {filename}")
                        continue

                    file_path = os.path.join(root, filename)
                    relative_path = os.path.relpath(file_path, directory)

                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f_in:
                            content = f_in.read()

                        header = f"--- START OF FILE: {relative_path} ---\n"
                        footer = f"\n--- END OF FILE: {relative_path} ---\n\n"

                        f_out.write(header)
                        f_out.write(content)
                        f_out.write(footer)
                        print(f"  -> Added: {relative_path}")

                    except Exception as e:
                        print(f"  -> Error reading file {file_path}: {e}")

        print(f"\n✅ Codebase successfully compiled into '{output_file}'")

    except IOError as e:
        print(f"❌ Error: Could not write to output file '{output_file}': {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == '__main__':
    OUTPUT_FILENAME = 'codebase_context_no_images.txt'
    
    # The '.' tells the script to start in the current directory.
    compile_codebase('.', OUTPUT_FILENAME)
