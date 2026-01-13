from __future__ import annotations


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__owner = owner
        self.__balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds: withdrawal exceeds balance")
        self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"BankAccount(owner={self.__owner}, balance={self.__balance:.2f})"


def main() -> None:
    acc = BankAccount("Ice Nice gospodin", 100.0)
    print(acc)

    acc.deposit(50)
    print("After deposit:", acc.get_balance())

    acc.withdraw(30)
    print("After withdraw:", acc.get_balance())


if __name__ == "__main__":
    main()
