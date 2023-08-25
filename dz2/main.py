import dz2.task2_DivisionByZero
import dz2.task1_positive_num
import dz2.task3_NumberOutOfRange
import dz2.task4_bank


if __name__ == '__main__':
    dz2.task1_positive_num.task1()
    dz2.task2_DivisionByZero.task2()
    dz2.task3_NumberOutOfRange.task3()

    acc = dz2.task4_bank.Bank()
    acc.create_account("4512", 10_000)
    acc.deposit("4512", 5_000)
    # раскомментировать, чтобы получить ошибку
    # переполнение лимита хранения средств
    # acc.deposit("4512", 6_000)
    # не верный аккаунт
    # acc.withdraw("4588", 5_000)

    acc2 = dz2.task4_bank.BankAccount("4500", 10_000)
    acc2.deposit(2_000)
    # недостаточно средств
    # acc2.withdraw(3_000)






