# Задача 2
class DivisionByZeroException(Exception):
    pass


def divide_numbers(num1, num2):
    if num2 == 0:
        raise DivisionByZeroException("Деление на ноль недопустимо")
    else:
        result = num1 / num2
        print("Результат деления:", result)


def task2():
    print("task2")
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
        divide_numbers(number1, number2)
    except DivisionByZeroException as e:
        print(e)
