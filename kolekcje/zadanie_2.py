i = 0
while i < 10:

     liczba = input("Podaj liczbe lub k by zakonczyc:")
     if liczba == 'k':
          break
     liczba = int(liczba)
     liczby.append(liczba)
     i += 1

print("Srednia wynosi: ", sum(liczby)/len(liczby))



