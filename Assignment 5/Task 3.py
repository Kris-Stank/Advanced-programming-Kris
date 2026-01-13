from __future__ import annotations


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}. I'm {self.age} years old."

    def __str__(self) -> str:
        return self.introduce()


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, gpa: float) -> None:
        super().__init__(name, age)
        self.__student_id = student_id
        self.__gpa = gpa

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def gpa(self) -> float:
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float) -> None:
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0")
        self.__gpa = value

    def introduce(self) -> str:
        return (
            f"Hi, I'm {self.name} (Student ID: {self.__student_id}). "
            f"I'm {self.age} years old. GPA: {self.__gpa:.2f}."
        )


def demo_polymorphism(people: list[Person]) -> None:
    for p in people:
        print(p.introduce())


def main() -> None:
    p1 = Person("Alex", 30)
    s1 = Student("Dana", 19, "AITU-2026-001", 3.6)

    people: list[Person] = [p1, s1]

    print("Polymorphism demo:")
    demo_polymorphism(people)

    print("\nEncapsulation demo:")
    print("Student ID (via property):", s1.student_id)
    print("GPA (via property):", s1.gpa)
    s1.gpa = 3.8
    print("Updated GPA:", s1.gpa)


if __name__ == "__main__":
    main()
