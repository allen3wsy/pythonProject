# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

def outer_function():
    count = 99  # Variable in the enclosing scope

    def inner_function():
        nonlocal count  # Declare 'count' as nonlocal
        count += 1      # Modify the 'count' from outer_function
        print(f"Inner function count: {count}")

    inner_function()
    print(f"Outer function count: {count}")

outer_function()


# wrong: will raise TypeError: can only concatenate str (not "int") to str
# r = "The answer is: " + 5
result = "The answer is: " + str(5)
print(result)
result2 = f"The answer is: {5}"
print(result2)