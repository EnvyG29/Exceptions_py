class InsufficientFundsException(Exception):
    pass


class MaxBalanceExceededException(Exception):
    pass


class BankAccount:
    def __init__(self, account_number: str, max_balance: int):
        self.account_number = account_number
        self.max_balance = max_balance
        self.balance = 0

    def deposit(self, amount):
        """
        Метод для пополнения счета.
        Проверяет, не превышает ли сумма пополнения максимально допустимый баланс.
        """
        if self.balance + amount > self.max_balance:
            raise MaxBalanceExceededException("Переполнение лимита хранения средств")
        self.balance += amount

    def withdraw(self, amount):
        """
        Метод для снятия денег со счета.
        Проверяет, достаточно ли средств на счете для снятия указанной суммы.
        """
        if amount > self.balance:
            raise InsufficientFundsException("Недостаточно средств")
        self.balance -= amount


class Bank:
    def __init__(self):
        import threading
        self._accounts = dict()
        self._lock = threading.Lock()

    def create_account(self, account_number: str, max_balance: int):
        """
        Метод для создания нового банковского счета.
        """
        self._accounts[account_number] = BankAccount(account_number, max_balance)

    def deposit(self, account_number, amount):
        """
        Метод для пополнения счета указанного пользователя.
        """
        with self._lock:
            if account_number not in self._accounts:
                raise ValueError("Не верный номер аккаунта")
            account = self._accounts[account_number]
            account.deposit(amount)

    def withdraw(self, account_number, amount):
        """
        Метод для снятия денег со счета указанного пользователя.
        """
        with self._lock:
            if account_number not in self._accounts:
                raise ValueError("Не верный номер аккаунта")
            account = self._accounts[account_number]
            account.withdraw(amount)
