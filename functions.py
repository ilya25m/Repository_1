def calculate(a: int | float = 0, b: int | float = 0, operation: str = "sum") -> float:
    result = 0

    if operation == "sub":
        result = a - b
    else:
        result = a + b

    result = result * 1.0
    result = round(result, 2)

    return result


def change_text(text: str = "", upper: bool = True) -> str:
    result_text = ""

    if upper:
        result_text = text.upper()
    else:
        result_text = text.lower()

    return result_text


def sum_from_string(numbers: str = "", separator: str = ",") -> float:
    if not numbers:
        return 0.0

    parts = numbers.split(separator)

    total = 0
    for part in parts:
        number = float(part)
        total = total + number

    total = total * 1.0
    total = round(total, 2)

    return total
