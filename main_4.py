a, b, *rest = range(5)

print(a)
print(b)
print(rest)
print(*rest)

print(bin(5))

print(bin(5).count('1'))
print("0b101".count('1'))

# binary to decimal:
print(int("0b101", 2))
print(int("101", 2))
print(int("101", 10)) # 101
print(int("101", 16)) # 257
print(int("101", 8)) # 65
print(int("101", 2)) # 5
print(int("101", 2)) # 5

# decimal to binary:
print(bin(101)) # 0b1100101
