# -*- coding: cp1251 -*-
num1 = float(input("Введiть 1 число: "))
num2 = float(input("Введiть 2 число: "))
num3 = float(input("Введiть 3 число: "))

choice = input("виберiть розв'язок (+ чи *): ")

if choice == "+":
    result = num1 + num2 + num3
    print("Сумма трьох чисел рiвна:", result)
elif choice == "*":
    result = num1 * num2 * num3
    print("Добуток трьох чисел рiвна", result)
else:
    print("Сталася помилка, спробуйте виконати iншу комбiнацiю.")