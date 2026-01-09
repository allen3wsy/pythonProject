import math

def is_prime(n):
    if n <= 1:
        return False
    # 2 is the only even prime number.
    if n == 2:
        return True
    # All other even numbers are not prime.
    if n % 2 == 0:
        return False

    # Check for divisors from 3 up to the square root of n.
    # We can skip even numbers by incrementing by 2.
    # We only need to check up to the square root because if a number `n`
    # has a divisor `d` larger than its square root, it must also have
    # a divisor `n/d` which is smaller than its square root.
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    # If no divisors were found, the number is prime.
    return True

# --- Example Usage ---
print(f"Is 7 a prime number? {is_prime(7)}")
print(f"Is 10 a prime number? {is_prime(10)}")
print(f"Is 29 a prime number? {is_prime(29)}")
print(f"Is 1 a prime number? {is_prime(1)}")
print(f"Is 2 a prime number? {is_prime(2)}")
print(f"Is 97 a prime number? {is_prime(97)}")
