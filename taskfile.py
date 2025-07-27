import os

file_path = "myfile.py"
os.chmod(file_path, 0o775)
print("Permissions updated to rwxrwxr-x")