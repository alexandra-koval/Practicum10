def print_numbers_with_digits(A, B):
    if A > B:
        A, B = B, A

    allowed = {'1', '3', '4', '8', '9'}

    for num in range(A, B + 1):
        if all(digit in allowed for digit in str(num)):
            print(num, end=" ")

    print()


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print_numbers_with_digits(A, B)
