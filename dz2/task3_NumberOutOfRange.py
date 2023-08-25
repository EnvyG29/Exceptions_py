# Задача 3

class DivisionByZeroException(Exception):
    pass


class NumberOutOfRangeException(Exception):
    pass


class NumberSumException(Exception):
    pass


def check_numbers(num1, num2, num3):

    if num1 > 100:
        raise NumberOutOfRangeException("Первое число вне допустимого диапазона")
    if num2 < 0:
        raise NumberOutOfRangeException("Второе число вне допустимого диапазона")
    if num1 + num2 < 10:
        raise NumberSumException("Сумма первого и второго чисел слишком мала")
    if num3 == 0:
        raise DivisionByZeroException("Деление на ноль недопустимо")
    else:
        print("Проверка пройдена успешно")


def task3():
    print("task3")
    try:
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
        number3 = int(input("Введите третье число: "))
        check_numbers(number1, number2, number3)
    except NumberOutOfRangeException as e:
        print(e)
    except NumberSumException as e:
        print(e)
    except DivisionByZeroException as e:
        print(e)
