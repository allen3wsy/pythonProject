class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        current_number = 0
        last_number = 0
        result = 0
        operation = '+'

        for i, char in enumerate(s):
            # Build the current number
            if char.isdigit():
                current_number = (current_number * 10) + int(char)

            # Process operation if char is an operator, or if we are at the end of the string
            if (not char.isdigit() and not char.isspace()) or i == length - 1:
                if operation == '+' or operation == '-':
                    result += last_number
                    last_number = current_number if operation == '+' else -current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    # Java: Integer division truncates toward zero (e.g., -3 / 2 equals -1).
                    # Python: The floor division operator // rounds toward negative infinity (e.g., -3 // 2 equals -2).
                    # Python: that's why we use int (-3 / 2) = - 1
                    last_number = int(last_number / current_number)

                operation = char
                current_number = 0

        result += last_number
        return result


solution = Solution()
print(solution.calculate("3+2*2"))

print(-3 // 2)
print(int(-3 / 2))
