class Solution:
    def min_remove_to_make_valid(self, s: str) -> str:

        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0

            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        # first pass: remove all preceding ")"
        s = delete_invalid_closing(s, "(", ")")

        # second pass: reverse the result and then remove all preceding "("
        s = delete_invalid_closing(s[::-1], ")", "(")

        # reverse it back again to original order
        return s[::-1]

solution = Solution()
print(solution.min_remove_to_make_valid("))ab( c )dddd("))
print(solution.min_remove_to_make_valid("(h(e)ll(o)"))