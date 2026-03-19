import massages

bread = input(massages.MSG_INPUT_BREAD).strip().lstrip("0          ")
print(bread)
is_correct_bread = bread.isdigit()
print(is_correct_bread)
true = True
false = False

if is_correct_bread:
    print(massages.MSG_INPUT_BREAD_TRUE)
    print(massages.FINISH)
else:
    print(massages.MSG_INPUT_BREAD_FALSE)
