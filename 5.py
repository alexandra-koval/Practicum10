def calculate_card_value():
    '''
    Calculates the total value of a phone card including bonus
    Available card values: $5, $10, $25, $50, $100
    '''
    try:
        price = int(input("Cтоимость карты: "))
    except ValueError:
        print("Ошибка")
        return None

    if price == 5 or price == 10:
        bonus = 0
        total = price + bonus
        print(f"Карта ${price}: без бонуса")

    elif price == 25:
        bonus = 3
        total = price + bonus
        print(f"Карта ${price}: бонус ${bonus}")

    elif price == 50:
        bonus = 8
        total = price + bonus
        print(f"Карта ${price}: бонус ${bonus}")

    elif price == 100:
        bonus = 20
        total = price + bonus
        print(f"Карта ${price}: бонус ${bonus}")

    else:
        print("Ошибка: Неверная стоимость карты.")
        return None

    print(f"Итого: ${total}")
    return total


calculate_card_value()
