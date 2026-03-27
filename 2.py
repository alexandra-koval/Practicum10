def fibonacci(n):
    """Prints the first N numbers of the Fibonacci sequence"""
    a = 1
    b = 1

    for i in range(n):
        if i == n - 1:
            print(a)
        else:
            print(a, end=", ")

        a, b = b, a + b


n = int(input("Enter the number of Fibonacci numbers: "))
fibonacci(n)
