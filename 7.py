def print_common_multiples(A, B, N):
    """Prints common multiples of A and B up to N in ascending order"""
    for i in range(1, N + 1):
        if i % A == 0 and i % B == 0:
            print(i, end=" ")
    print()


A = int(input())
B = int(input())
N = int(input())

print_common_multiples(A, B, N)
