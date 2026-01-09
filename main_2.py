# 1. Import necessary libraries
import sys


# 2. Define helper functions
def greet(name: str) -> str:
    """A simple function that returns a greeting string."""
    return f"Hello, {name}! Welcome to the script."


# 3. Define the main function (where logic starts)
def main(args: list[str]) -> None:
    """
    The main entry point for the script.

    Args:
        args: A list of command-line arguments (excluding the script name).
    """
    # Check if any arguments were passed
    if not args:
        print(greet("World"))
        return

    # Use the first argument as the name
    user_name = args[0]
    message = greet(user_name)
    print(message)


def sum_three(a, b, c):
    return a + b + c



# 4. The Conditional Execution Block
if __name__ == "__main__":
    # This is the entry point that calls the main function.
    # sys.argv[1:] gets all command-line arguments after the script name.
    main(sys.argv[1:])

    ### Unpacking with * operator ###
    data = [10, 20, 30]

    # Without *: TypeError: sum_three() takes 3 positional arguments but 1 was given
    # With *: The list is unpacked into three separate arguments: 10, 20, 30
    total = sum_three(*data)

    print(total) # Output: 60
    ### Unpacking with * operator ###