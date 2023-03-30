num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
operation = input("Виберіть операцію (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    print("Невірна операція!")
    result = None

if result is not None:
    print("Результат операції:", result)

