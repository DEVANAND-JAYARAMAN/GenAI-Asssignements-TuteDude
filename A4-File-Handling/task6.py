import os
filename = input("Enter File Name : ")
if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found. Please check the filename.")