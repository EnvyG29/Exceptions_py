class InvalidNumberException(Exception):
    pass


def check_positive_number(num):
    if num <= 0:
        raise InvalidNumberException("Некорректное число")
    else:
        print("Число корректно")


def task1():
    print("task1")
    try:
        number = int(input("Введите число: "))
        check_positive_number(number)
    except InvalidNumberException as e:
        print(e)
