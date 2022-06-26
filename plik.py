
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

szukane = zapyt.split(",") # lista z zapytaniami
lista_wyst =[] # przechowuje liste z występowaniem zapytania w konkretnym numerze dokumentu 
for el in range(len(szukane)):
  for doc in range (len(lista_dokumentow)):
      if szukane[el -1] in lista_dokumentow[doc -1]:
        lista_wyst.append(doc)
      else:
        pass
  print(lista_wyst)
