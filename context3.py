import os

def collect_codebase(output_filename='codebase_context.txt'):
    # 1. CONFIGURATION
    # Files to strictly exclude based on your request
    excluded_extensions = {'.txt', '.py', '.mp3'}
    
    # Directories to ignore (improves performance and reduces noise)
    excluded_dirs = {'.git', '__pycache__', 'node_modules', 'venv', 'env', '.idea', '.vscode'}
    
    # Files to ignore specifically (including the output file itself to prevent loops)
    excluded_filenames = {output_filename, '.DS_Store'}

    cwd = os.getcwd()
    
    print(f"Starting scan in: {cwd}")
    print(f"Output file: {output_filename}")
    print(f"Ignoring extensions: {excluded_extensions}")

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        file_count = 0
        
        # Walk through directory
        for root, dirs, files in os.walk(cwd):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                file_path = os.path.join(root, file)
                _, ext = os.path.splitext(file)
                
                # Check exclusions
                if (ext.lower() in excluded_extensions or 
                    file in excluded_filenames):
                    continue
                
                # Create a relative path for the header (cleaner for LLMs)
                relative_path = os.path.relpath(file_path, cwd)

                try:
                    # Try to read the file as text
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Write the Header
                    outfile.write("=" * 50 + "\n")
                    outfile.write(f"FILE PATH: {relative_path}\n")
                    outfile.write("=" * 50 + "\n")
                    
                    # Write the content
                    outfile.write(content + "\n\n")
                    
                    print(f"Added: {relative_path}")
                    file_count += 1
                    
                except UnicodeDecodeError:
                    # Skip binary files (images, compiled code, etc.) that aren't explicitly excluded
                    print(f"Skipped (Binary/Encoding Issue): {relative_path}")
                except Exception as e:
                    print(f"Error reading {relative_path}: {e}")

    print(f"\nDone! Compiled {file_count} files into '{output_filename}'.")

if __name__ == "__main__":
    collect_codebase()