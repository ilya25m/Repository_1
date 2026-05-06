from functions import calculate, change_text, sum_from_string


print('--- positional arguments ---')
print(calculate(10, 5, "sub"))
print(change_text("hello world", False))
print(sum_from_string("1,2,3"))


print('\n--- named arguments ---')
print(calculate(a=10, b=5, operation="sum"))
print(change_text(text="python", upper=True))
print(sum_from_string(numbers="4,5,6", separator=","))


print('\n--- dict unpacking ---')
calc_data = {
    "a": 20,
    "b": 10,
    "operation": "sub"
}

text_data = {
    "text": "Hello",
    "upper": True
}

sum_data = {
    "numbers": "7,8,9",
    "separator": ","
}

print(calculate(**calc_data))
print(change_text(**text_data))
print(sum_from_string(**sum_data))