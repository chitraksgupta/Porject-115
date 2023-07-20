import os

#source file path
source = "main.txt"

#destination file path
dest = "file.txt"

os.rename(source, dest)
print("source path renamed so to destination path sucessfully")