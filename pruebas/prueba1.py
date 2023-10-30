import csv
happy = open("happy.txt",'r')
lista = list(csv.reader(happy, delimiter=","))
print(lista)
happy.close()

happy = open("happy.txt",'r')
lista = list(csv.reader(happy, delimiter=","))
print(lista)
happy.close()

# escribir archivo con writerows
new_happy = open("new_happy.csv", 'w')
writer = csv.writer(new_happy)
writer.writerows(lista)
new_happy.close()

# es lo mismo que writerows pero con un ciclo que recorre las lineas
new_happy2 = open("new_happy.csv", 'w')
writer = csv.writer(new_happy2)
for linea in lista: # recorre cada linea dentro del archivo
    writer.writerow(linea)
new_happy2.close()
