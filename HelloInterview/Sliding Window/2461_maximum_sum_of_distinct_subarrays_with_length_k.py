def max_sum(nums: list[int], k: int):
    # Your code goes here
    start = 0
    curr_sum = 0
    max_sum = 0
    seen = set()

    for end in range(len(nums)):
        while nums[end] in seen:
            curr_sum -= nums[start]
            seen.remove(nums[start])
            start += 1

        curr_sum += nums[end]
        seen.add(nums[end])

        # now window has no dups and of size k
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            # don't forget to move the start pointer forward !!!
            curr_sum -= nums[start]
            seen.remove(nums[start])
            start += 1

    return max_sum

nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
print(max_sum(nums, 4))