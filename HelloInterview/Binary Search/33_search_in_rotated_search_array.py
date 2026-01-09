def search(nums, target):
  left = 0
  right = len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    # 1st kind of rotation array, left side is ascending
    if nums[left] <= nums[mid]:
      if nums[left] <= target and target < nums[mid]:
        right = mid - 1
      else:
        left = mid + 1
    else: # 2nd kind of rotation array, right side is ascending
       # same as "elif nums[mid] <= nums[right]:"
       # because that's equivalent to  "nums[left] > nums[mid]"
      if nums[mid] < target and target <= nums[right]:
        left = mid + 1
      else:
        right = mid - 1
  return -1

# return the index of the found element

# num[left] <= num[mid]
print(search([1, 3, 5, 6, 7], 7))

# num[left] > num[mid]
print(search([6, 7, 1, 3, 5], 7))

# not found: return -1
print(search([1, 3, 5, 6, 7], 100))
