meters = float(input("Введіть кількість метрів: "))

print("1 - Метри в милі")
print("2 - Метри в дюйми")
print("3 - Метри в ярди")

choice = input("Ваш вибір: ")

if choice == "1":
    mil = meters / 1609.344
    print(meters, "метрів =", mil, "миль")
elif choice == "2":
    inches = meters * 39.37
    print(meters, "метрів =", inches, "дюймів")
elif choice == "3":
    yards = meters * 1.0936
    print(meters, "метрів =", yards, "ярдів")
else:
    print("Неправильно введено число, спробуйте iншу комбiнацiю.")
