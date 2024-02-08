def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def number_of_groups(n, k):
    fak_n = factorial(n)
    result = factorial(n-k)*factorial(k)
    return fak_n // result

print(number_of_groups(n=50,k=7))
