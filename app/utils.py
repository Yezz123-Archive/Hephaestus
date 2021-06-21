def nth_fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


def factorial(n):
    fact = 1

    if n == 0:
        return fact
    else:
        for num in range(2, n + 1):
            fact *= num
        return fact
