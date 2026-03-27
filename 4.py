def make_payment(P):
    '''Checks if the payment amount is valid'''
    if P < 20:
        print("Повторить попытку: Минимальный платёж $20")
    elif P > 1000:
        print("Повторить попытку: Превышен кредитный лимит $1000")
    else:
        print("Успех")

P = float(input())
make_payment(P)
