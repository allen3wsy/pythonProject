
print('=======')

import math

# Assuming my_number is a float or can be converted to one
my_number = float('nan')

print(math.isnan(my_number))
# Output: True

print(float('inf')+1)
# inf

print(float('nan') - float('inf'))
# nan

print(1 ** float('inf'))
# 1.0

print(1 * float('inf'))
# inf

print(float('nan') == float("NaN") )
# False

print(1.0 == 1)
# True

print(type(1))  
# <class 'int'>
print(type(1.0))
# <class 'float'>

