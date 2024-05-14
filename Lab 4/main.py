
#1
list = ["paine", "lapte", "apa", "cartofi"]

def afisare():
    print(list)
def adaugare():
    x = input("Adauga un produs in lista: ")
    list.append(x)

def stergere():
       x = input("Sterge un produs din lista: ")
       if x in list:
        list.remove(x)

       else:
            print("Acest produs nu este in lista")
       afisare()

menu = '''1. Afiseaza lista de produse.
2. Adauga un produs in lista.
3. Sterge un produs din lista.
4. Exit.'''
while True:
    print("Alege o optiune:")
    print(menu)
    t = input()
    match t:
        case "1":
            afisare()
        case "2":
            adaugare()
        case "3":
            stergere()
        case "4":
            break

#2
#a
s=0
for i in range(1, 101):
    s += i
print('Suma numerelor de 1 la 100 este:', s)

s = 0
i = 1
while i <= 100:
    s += i
    i += 1
print('Suma numerelor de la 1 la 100 este:', s)

#b
x = int(input("introdu un nr de la tastatura: "))
if x % 2 == 0:
    print("numarul este par")
else:
    print("numarul nu este par")

#c
list = []
for i in range(1, 6):
    list.append(i)
print("List:", list)

set = set()
for i in range(1, 6):
    set.add(i)
print("Set:", set)

#d
tupl = (3, 1, 4, 1, 5, 9, 2, 6)
sort = sorted(tupl)
s = sum(tupl)
print("Tuplul sortat:", sort)
print("Suma elementelor sortate:", s)

#e
list1 = set([1, 2, 3, 4, 5])
list2 = set([4, 5, 6, 7, 8])
comun = list1.intersection(list2)
print("Elementele comune din cele două liste sunt:", comun)


#3
nr = [5, 2, 8, 3, 1, 4]
print("numarul de elemente din lista:", len(nr))
print(nr)
print("lichidam elementele din lista:", nr.clear())
print(nr)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Intersecția:", set1.intersection(set2))
print("Diferența:", set1.difference(set2))

elevi = {"Ion": 8, "Maria": 9, "Ana": 7, "George": 6}
sort = sorted(elevi.values())
print("Dicționarul sortat după note:", sort)
maxim = max(elevi.values())
print("Nota maximă din dicționar:", maxim)
for elev in elevi.keys():
    print(elev)

#4
i = sum = 0
while i <= 4:
    sum += i
    i = i+1
print(sum)

for char in 'PYTHON STRING':
  if char == ' ':
      break
  print(char, end='')
  if char == 'O':
      continue
  print('*', end='')