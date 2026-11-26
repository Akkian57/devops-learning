## Assignment 2 ##
# 3. Write to a File
# 11. Write a program to create a text file and write some content to it, using file functions like open() and write().

# 4. Read from a File
# 12. Open the file in read mode and use file.read() to read and display its content.


with open("D:\\devops-learning\\python\\test.txt", "w", encoding="utf-8") as file:
    file.write("This file has been created and written by python code")

with open("D:\\devops-learning\\python\\test.txt", "r", encoding="utf-8") as file:
    print(file.read())
