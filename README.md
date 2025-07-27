# chmod-775
This task demonstrates how to use a Python script to change file permissions on Linux using the chmod command, specifically setting them to rwxrwxr-x (775)


# Files Used:

 `taskfile.py`A Python script that uses `os.chmod()` to change file permissions

 `myfile.py` A sample file whose permissions are modified using the script


# Objective:
Understand and apply file permissions on Linux using Python

The script updates permissions to: `rwxrwxr-x` (which means `775` in octal)




# What is `rwxrwxr-x`?
Owner: read, write, execute 
Group: read, write, execute 
Others: read, execute ( write is  not allowed)



# How It Works:
	1.Create both files:
       `touch myfile.py`
        `touch taskfile.py`
    2.Run the script:
       python3 taskfile.py
	3.Check the permissions:
        ls -l myfile.py

# output:
<img width="1129" height="932" alt="لقطة شاشة 2025-07-27 183503" src="https://github.com/user-attachments/assets/8f4cc503-1d6d-42ae-bd3d-67c4c0df74f5" />
