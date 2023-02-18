tickets_quantity = int(input("Введите количество билетов, которое хотите приобрести: "))
age = []
for i in range(0, tickets_quantity):
    age_ = int(input(f"Введите возраст человека # {i + 1 }: "))
    age.append(age_)
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return  1390
    full_price = sum(map(price,age))
    discount_price = int(full_price * 0.9)
    if tickets_quantity > 3:
        print("------------------------------")
        print("Общая стоимость билетов со скидкой: ", discount_price, "RUB")
        print("------------------------------")
    else:
        print("Общая стоимость билетов: ", full_price, "RUB")