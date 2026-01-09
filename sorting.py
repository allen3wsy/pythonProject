s = 'hi'
print(s[1])  ## i
print(len(s))  ## 2
print(s + ' there')  ## hi there


#### list.sort()
print("list.sort(key=lambda item: item[i]): sorting in-place " )
# sort: array
my_list = [[1, 'apple'], [3, 'banana'], [2, 'cherry']]
my_list.sort(key=lambda item: item[1])  # Sort by the 2nd element of each array
print(my_list)
# Output: [(1, 'apple'), (3, 'banana'), (2, 'cherry')]


# sort: tuple
my_list = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
my_list.sort(key=lambda item: item[0])  # Sort by the 1st element of each tuple
# my_list.sort(key=lambda item:item[0], reverse=True)
b = my_list.sort(key=lambda item:item[0], reverse=True)

print("b is: ", b)
print(my_list)
# Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]


#### sorted(list, key=lambda item: item[i])
### The sorted() function returns a new sorted list, leaving the original iterable unchanged.
print("\nsorted(list, key=lambda item: item[i]) ")
my_list = [(1, 'kale'), (3, 'banana'), (2, 'cherry')]

# Sort by the first element of each tuple: descending order
sorted_list = sorted(my_list, key=lambda item: item[0], reverse=True)


print(sorted_list)
print(my_list) # Original list remains unchanged

