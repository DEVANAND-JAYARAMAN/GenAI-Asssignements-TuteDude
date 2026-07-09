filename = input("Enter File Name : ")
try:
    file = open(filename, "r")
    print(file.readline(), end = "")
    print(file.readline(), end = "")
    print(file.readline(), end = "")
    file.close()

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("\nFile operation attempted.")