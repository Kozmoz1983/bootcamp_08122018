import datetime

current_year = datetime.datetime.now().year

bd_year = int(input("Podaj rok urodzenia: "))

if current_year - bd_year >= 18:
    print ("Jestes pelnoletni. Mozesz isc do pracy")

else:
    print ("Mozesz bumelowac. Rodzice placa")
