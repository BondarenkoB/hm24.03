# -*- coding: cp1251 -*-
num1 = float(input("����i�� 1 �����: "))
num2 = float(input("����i�� 2 �����: "))
num3 = float(input("����i�� 3 �����: "))

choice = input("�����i�� ����'���� (+ �� *): ")

if choice == "+":
    result = num1 + num2 + num3
    print("����� ����� ����� �i���:", result)
elif choice == "*":
    result = num1 * num2 * num3
    print("������� ����� ����� �i���", result)
else:
    print("������� �������, ��������� �������� i��� ����i���i�.")