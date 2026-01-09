from collections import OrderedDict, defaultdict

# Create an OrderedDict
d = OrderedDict([('apple', 1), ('banana', 2), ('cherry', 3)])

print("Original order:")
for key, value in d.items():
    print(f"{key}: {value}")


# Output:
# apple: 1
# banana: 2
# cherry: 3

print("\nReversed order (iterating over keys):")
for key in reversed(d):
    print(key, d[key])
# Output:
# cherry 3
# banana 2
# apple 1

print("\nReversed order (iterating over items):")
for key, value in reversed(d.items()):
    print(f"{key}: {value}")
# Output:
# cherry: 3
# banana: 2
# apple: 1


###########################################################################################

nested_dict = defaultdict(lambda: defaultdict(int))
nested_dict['A']['count'] += 1
nested_dict['A']['sum'] += 5
nested_dict['B']['count'] += 1

print(nested_dict)
# Output: defaultdict(<function <lambda> at 0x...>, {'A': defaultdict(<class 'int'>, {'count': 1, 'sum': 5}), 'B': defaultdict(<class 'int'>, {'count': 1})})


###########################################################################################