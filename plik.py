
# https://github.com/RaVolejnik/Poprawka_ASI_2022.git
print("podaj liczbę dokumentów do przetworzenia")
n = input()
lista_dokumentow = []

print("wpisz dokumenty")
for i in range(int(n)):
   i = input()
   lista_dokumentow.append(i)

print(lista_dokumentow)

print("podaj liczbe zapytań do przetworzenia")
m = input()
print("podaj zapytania rozdzielone przecinkami")
zapyt = input()
