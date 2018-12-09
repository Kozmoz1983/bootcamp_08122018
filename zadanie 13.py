ILE_DNI = 7

temp = 0
i = 0

while i < ILE_DNI :

    komenda = input(f"Podaj temperature w dniu {i} lub [k] by zakonczyc: ")
    if komenda == 'k':
        break
    temp_i = float(komenda)
    temp += temp_i
    i += 1

print("Srednia temperatura wynosila: ", temp/i)


