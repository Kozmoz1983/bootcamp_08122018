a = input("Podaj pierwsza liczbe:")
b = input(" Podaj druga liczbe:")
operacja = input(" Podaj rodzaj operacji")

# Rozwiązanie najprostsze

if operacja == "+":
    print(a + b)
elif operacja == '-':
    print(a-b)
elif operacja =='/':
    if b == 0:
        print ("Operacja niedozwolona")
    else:
        print(a/b)
elif operacja == '*':
    print(a*b)
else:
    print ("Operacja nie jest wspierana")

print(eval(f"{a}{operacja}{b}"))

