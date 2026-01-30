from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List


def safe_average(grades: List[int]) -> int | None:
    if not grades:
        return None
    return sum(grades) // len(grades)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "students.json"
    dst = here / "students_with_avg.json"

    if not src.exists():
        raise FileNotFoundError(f"Source JSON not found: {src}")

    data = load_json(src)

    if not isinstance(data, list):
        raise TypeError("students.json must contain a JSON list of students")

    updated: List[Dict[str, Any]] = []
    for student in data:
        if not isinstance(student, dict):
            raise TypeError("Each student must be a JSON object")

        grades = student.get("grades", [])
        if grades is None:
            grades = []
        if not isinstance(grades, list):
            raise TypeError("Student 'grades' must be a list")

        numeric_grades: List[int] = []
        for g in grades:
            try:
                numeric_grades.append(int(g))
            except (TypeError, ValueError):
                continue

        avg = safe_average(numeric_grades)

        s2 = dict(student)
        s2["average_grade"] = None if avg is None else round(avg, 2)
        updated.append(s2)

    save_json(dst, updated)
    print(f"Done. Updated JSON saved to: {dst}")
    print("Original students.json preserved.")


if __name__ == "__main__":
    main()
