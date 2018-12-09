i = 0
while True:
    if i == 5:
        continue
    print(i)
    i +=1
    if i == 100:
        break

i = 0
while True:
    komenda = input ("Podaj komende: ")
    if komenda == "koniec":
        break

# Napisy

tekst =  "Ala ma kota"
         #012345678910

print(tekst[-1])

# przykład
from random import randint


x = randint(1, 10)
y = randint(1, 10)

i=0
while i < len(tekst):
    print(tekst [i])
    i += 1


for litera in tekst:
    print(litera)

for i, litera in enumerate(tekst)
    print(i, litera)

for i in range(10):
    print(i)


krotka = (1, 2, 3)
print(type(krotka))
print(krotka)
print(krotka[0])

for el in krotka:
    print(el)

print(dir(krotka))
print(krotka.count(1))

krotka2 = ("Napis 1", "Napis 2 ", "Napis 1", 1, 2, 3)
print(krotka2.index("Napis 1"))
print(krotka2.count("Napis 1"))

# listy

lista = [1,3,5,7,9,2,4,6,8]
print (type(lista))
print(lista[1:5])
print(dir(lista))

print(lista)
lista.append("AA")
print(lista)
print(id(lista))
lista.extend(['a', 'b'])
print(lista)
lista.append(['a', 'b'])
print(lista)
print(lista[-1][-1])
print("Jak dziala pop())
print(lista)

# print ([] .pop())
lista = [1,5,2,7,4,9]
print(lista)
print("Sortowanie")
print(lista.sort())




