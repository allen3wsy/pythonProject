# creates 26 empty lists, acting as "buckets" for each letter of the alphabet (a through z).
from sorting import my_list

heads = [[] for _ in range(26)]

print(heads)
print('\n')

###########################
# iter() and next()
###########################

my_iterator = iter([10, 20, 30])

print(my_iterator) # <list_iterator object at 0x1005050c0>
print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
print(next(my_iterator))  # Output: 30
# print(next(my_iterator)) # Raises StopIteration

# Example with default value:
# print(next(my_iterator)) #  StopIteration Error
print(next(my_iterator, "END")) # Output: END (No StopIteration error)

# list
a = list(range(5))
c = range(5)

print(a)
print(c)

#### they are the same
for _ in a:
    print("haha")

for _ in c:
    print("qq")


###########################
### tuples vs list ###
###########################

# Create a list
my_list = [1, 'b', 3.0]
print(f"Original list ID: {id(my_list)}")

# Change an element
my_list[1] = 2
print(f"After change: {my_list}") # Output: [1, 2, 3.0]

# Add an element
my_list.append(4)
my_list.remove(3) # removes 3.0
print(f"After append: {my_list}") # Output: [1, 2, 4]
print(f"New list ID (same object): {id(my_list)}") # ID remains the same

# Create a tuple
my_tuple = (1, 'b', 3.0)

# Attempt to change an element (will fail)
# my_tuple[1] = 2
# Output: TypeError: 'tuple' object does not support item assignment
print(f"my tuple is: {my_tuple}")