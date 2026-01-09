# Meta
class Solution:

    # s = "3[a2[c]]"
    # output = "accaccacc"
    @staticmethod
    def decode_string(s: str):
        curr_number = 0
        curr_string = ""
        stack = []

        for char in s:
            # 2[c]: number must be immediately before [
            # that's why we append str, num. then pop num, str
            if char == "[":
                stack.append(curr_string)
                stack.append(curr_number)
                curr_string = ""
                curr_number = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop() #
                curr_string = prev_string + num * curr_string
            elif char.isdigit(): # 23 -> 20+3
                curr_number = curr_number * 10 + int(char)
            else: # letter
                curr_string += char
        return curr_string

s_1 = "3[a]2[bc]"
s_2 = "3[a2[c]]"
print(Solution().decode_string(s_1))
print(Solution().decode_string(s_2))