try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful:", result)  # Output: Division successful: 5.0

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always execute.")  # Output: This will always execute.

# reading a File
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# writing to a file
with open("file.txt", "w") as file:
    file.write("Hello, file!")