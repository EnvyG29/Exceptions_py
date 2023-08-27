class InvalidDataError(Exception):
    pass


class Person:
    def __init__(self, surname: str, name: str, patronymic: str,
                 birthdate: str, phone_number: int, gender: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.gender = gender

    def to_string(self) -> str:
        return f"{self.surname} | {self.name} | {self.patronymic} |" \
               f" {self.birthdate} | {self.phone_number} | {self.gender}"


def parse_data(data: str) -> Person:
    data_list = data.split()
    if len(data_list) != 6:
        raise InvalidDataError("Invalid number of data elements")

    surname, name, patronymic, birthdate, phone_number, sex = data_list

    # Проверка формата данных
    if not birthdate.count('.') == 2 or not birthdate.replace('.', '').isdigit():
        raise InvalidDataError("Invalid birthdate format")
    if not phone_number.isdigit():
        raise InvalidDataError("Invalid phone number format")
    if sex not in ['ж', 'м']:
        raise InvalidDataError("Invalid sex format")

    return Person(surname, name, patronymic, birthdate, int(phone_number), sex)


def save_to_file(person: Person):
    filename = f"{person.surname}.txt"
    with open(filename, 'a') as file:
        file.write(person.to_string() + '\n')


def main():
    from time import sleep
    print("Ввод одной строкой через пробел\n"
          "Фамилия Имя Отчество, дата рождения, номер телефона, пол(м/ж)\n"
          "Пример: Иванов Иван Иванович 01.01.1990 79001234567 м\n"
          "Для завершения программы нажмите enter в пустой строке")
    while True:
        print("Введите данные пользователя: ")
        data = input(">>> ")
        if data == "":
            print("this device will self-destruct in")
            for i in range(10, 0, -1):
                sleep(1)
                print(i)
            sleep(2)
            print("\\\\!!KABOOM!!!//")
            break
        try:
            person = parse_data(data)
            save_to_file(person)
            print("Данные успешно сохранены в файл.")
        except InvalidDataError as e:
            print(f"Ошибка валидации данных: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
