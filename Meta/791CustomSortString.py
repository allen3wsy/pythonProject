from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result_list = []

        for c in order:
            if c in freq:
                result_list.append(c * freq[c])
                
                # Alternatively: del freq[c]
                freq[c] = 0  # Set the count to 0, it won't be picked up in the next loop

        for char_remaining, count in freq.items():
            if count > 0: # Only append if the count is greater than 0
                result_list.append(char_remaining * count)
            
        return "".join(result_list)