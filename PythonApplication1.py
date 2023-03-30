num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

choice = input("Введіть 1 для знаходження максимуму, 2 для знаходження мінімуму або 3 для знаходження середнього арифметичного: ")

if choice == "1":
    result = max(num1, num2, num3)
    print("Максимум з трьох чисел:", result)
elif choice == "2":
    result = min(num1, num2, num3)
    print("Мінімум з трьох чисел:", result)
elif choice == "3":
    result = (num1 + num2 + num3) / 3
    print("Середнє арифметичне з трьох чисел:", result)
else:
    print("Помилка: неправильно введено число.")

