def average(a, b, c):
    return round((a + b + c) / 3, 2)


def is_even_and_gt_10(num) -> bool:
    return num % 2 == 0 and num > 10


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    return sum(1 for char in text.lower() if char in vowels)