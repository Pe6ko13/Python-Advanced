from os import path


# 1

if path.exists("file.txt"):
    print("File found")
else:
    print('File not found')


# 2

try:
    open("file.txt")
    print('File found')
except:
    print('File not found')
