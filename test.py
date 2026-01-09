from ctypes import pythonapi
from typing import List, Union


a = [1, 'b']
user_names: List[str] = ["App", 123]

print(a)
# works but not good. will fail type checking
print(user_names)

# Option 1: Fix the list contents (preferred if homogeneity is desired)
user_names_fixed: List[str] = ["App", "123"]

# Option 2: Fix the type hint to allow mixed types (Union/pipe operator)
# Or List[str | int] in Python 3.10+
user_names_mixed: List[str | int] = ["App", 123]
# user_names_mixed: List[Union[str, int]] = ["App", 123]


print(user_names_fixed)
print(user_names_mixed)

