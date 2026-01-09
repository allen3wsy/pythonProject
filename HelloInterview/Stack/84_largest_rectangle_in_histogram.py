# Meta tag (hard), but unvetted
# similar to next_smaller_element


def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            right = i - 1
            left = stack[-1] if stack else -1
            area = heights[top] * (right - left)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        width = i - stack[-1] - 1 if stack else i
        area = heights[top] * width
        max_area = max(max_area, area)
    return max_area


print(largest_rectangle_area([2, 8, 5, 6, 2, 3]))
print(largest_rectangle_area([1, 3, 3, 4, 2]))

# def answer(heights):
#     def next_smaller_element(nums):
#         n = len(nums)
#
#         # next_smaller_element on both ways
#         result_left, result_right = [-1] * n, [-1] * n
#         stack = []
#         for j in range(n):
#             while stack and nums[j] < nums[stack[-1]]:
#                 index = stack.pop()
#                 result_right[index] = nums[j]
#             stack.append(j)
#
#         for j in range(n - 1, -1, -1):
#             while stack and nums[j] < nums[stack[-1]]:
#                 index = stack.pop()
#                 result_left[index] = nums[j]
#             stack.append(j)
#
#         return result_right, result_left
#
#     smaller_right, smaller_left = next_smaller_element(heights)
#
#     max_area = 0
#     r_width, l_width = 0, 0
#
#     for i in range(len(heights)):
#         if smaller_right[i] == -1:
#             r_width = len(heights) - i
#         else:
#             r_width = smaller_right[i] - i
#
#         if smaller_left[i] == -1:
#             total_width = r_width
#         else:
#             total_width = r_width + i - smaller_left[i] - 1
#
#         max_area = max(max_area, heights[i] * total_width)
#
#     return max_area
#
#
# print(answer([5, 4, 3]))
