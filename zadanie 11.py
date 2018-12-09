x = int(input("Podaj pozycje gracza X:"))
y = int(input("Podaj pozycje gracza Y:"))

# czy jest poza planszą
if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jestes poza plansza")
elif x > 90 and  y > 90:
    print(" Jestes w gornym prawym rogu")
elif x > 90 and y < 10:
    print("Jestes w dolnym prawym rogu")
elif x < 10 and y < 10:
    print("Jestes w dolnym lewym rogu")
elif x < 10 and y > 90:
    print("Jestes w gornym lewym rogu")
elif x < 10:
    print("Jestes na lewej krawedzi")
elif x > 90:
    print("Jestes na prawej krawedzi")
elif y < 10:
    print ("Jestes na dolnej krawedzi")
elif y > 90:
    print("Jestes na gornej krawedzi")
else:
    print ("Jestes w centrum")

