# lib/file_io.py

def write_file(file_name, file_content):
    # Convert file_name to a string and add the .txt extension
    with open(str(file_name) + ".txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Convert file_name to a string and add the .txt extension
    with open(str(file_name) + ".txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    # Convert file_name to a string and add the .txt extension
    with open(str(file_name) + ".txt", "r") as file:
        return file.read()

# use write_file function. 
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")