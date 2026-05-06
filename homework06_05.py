with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    flag = True

    file.readline()

    while flag:
        line = file.readline()

        if not line:
            flag = False
            continue

        parts = line.strip().split(';')

        if len(parts) > 5 and parts[5] == 'UA':
            print(parts[2])