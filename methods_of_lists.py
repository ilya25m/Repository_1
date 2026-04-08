numbers = [3, 7, 2, 9, 4, 6, 1, 8]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

doubled_even = []

for num in even_numbers:
    doubled_even.append(num * 2)

print(doubled_even)

is_8_present = 8 in doubled_even
print(is_8_present)

if is_8_present:
    doubled_even.remove(8)

print(doubled_even)

words = ["apple", "banana", "kiwi", "pear", "banana", "plum"]

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print(unique_words)

long_words = []

for word in unique_words:
    if len(word) > 4:
        long_words.append(word)

print(long_words)

upper_words = []

for word in long_words:
    upper_words.append(word.upper())

print(upper_words)

is_banana_present = "BANANA" in upper_words
print(is_banana_present)