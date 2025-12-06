#5. Sum of all prime numbers between 1 to n
def is_prime(x):
    if x<=1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

def sum_prime(n):
    s = 0
    for i in range(2, n+1):
        if is_prime(i):
            s+=i
    return s

n=int(input("Enter n: "))
print("sum of primes:", sum_prime(n))
