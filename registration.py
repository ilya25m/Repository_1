import massages

name = input(massages.MSG_INPUT_NAME)
name = name.strip()
name_ok = massages.MSG_NAME_OK
if name.isalpha():
    print(name_ok.format(name = name.title()))
else:
    print(massages.MSG_NAME_ERROR)

age = input(massages.MSG_INPUT_AGE)
age = age.strip().lstrip("0")
if age.isdigit():
    print(massages.MSG_AGE_OK.format(age = age))
else:
    print(massages.MSG_AGE_ERROR)

phone = input(massages.MSG_INPUT_PHONE)
phone = phone.strip()
if phone.isdigit():
    print(massages.MSG_PHONE_OK.format(phone = phone))
else:
    print(massages.MSG_PHONE_ERROR)

print(massages.MSG_FINISH)
