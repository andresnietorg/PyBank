import os

def find_file(filename, search_path):
    for root, dir, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Search for main.py starting from your OneDrive folder
search_path = r"C:\Users\Andres Nieto\OneDrive"
file_path = find_file("main.py", search_path)

if file_path:
    print(f"main.py found at: {file_path}")
else:
    print("main.py not found in the search path.")