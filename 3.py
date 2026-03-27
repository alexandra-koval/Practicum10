def calculate_final_price(price, has_discount_card, is_holiday):
    '''Calculates the final price after applying all discounts'''
    if price > 30000:
        discount = 10
    elif price > 20000:
        discount = 7
    elif price > 15000:
        discount = 5
    elif price > 5000:
        discount = 3
    else:
        discount = 0

    if has_discount_card:
        discount += 5

    if is_holiday:
        discount += 3

    if discount > 15:
        discount = 15

    return round(price * (100 - discount) / 100, 2)


price = float(input())
has_card = input().lower() == "да"
is_holiday = input().lower() == "да"

result = calculate_final_price(price, has_card, is_holiday)
print(f"Итоговая стоимость: {result} руб.")
