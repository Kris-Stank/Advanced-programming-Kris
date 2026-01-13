from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    _salary: float

    def get_salary(self) -> float:
        return self._salary

    def get_role(self) -> str:
        return "Employee"


@dataclass
class Manager(Employee):
    bonus_rate: float = 0.10

    def get_role(self) -> str:
        return "Manager"

    def get_bonus(self) -> float:
        return self._salary * self.bonus_rate


def print_employee_report(employees: list[Employee]) -> None:
    for e in employees:
        role = e.get_role()
        salary = e.get_salary()

        print(f"{e.name}: {role}, salary = {salary:.2f}")

        if isinstance(e, Manager):
            print(f"  bonus = {e.get_bonus():.2f}")


def main() -> None:
    staff: list[Employee] = [
        Employee("Ivan", 1200),
        Manager("Amina", 2000, bonus_rate=0.15),
        Employee("Maks", 1500),
    ]
    print_employee_report(staff)


if __name__ == "__main__":
    main()
