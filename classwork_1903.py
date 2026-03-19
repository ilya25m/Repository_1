name = "               alex    bush!-+      "
name = name.strip()
print(name)

name = name.strip("!-+")
print(name)

name = name.title()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

name = name.capitalize()
print(name)

name = name.replace("   ", "")
print(name)

name = name.replace("Alex    bush", "Alex Bush")
print(name)

german = "ß"
german_s_lower = german.lower()
print(german_s_lower)
german_s_upper = german_s_lower.upper()
print(german_s_upper)