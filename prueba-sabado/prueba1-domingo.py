"""
crea una lista 3 columnas[numero, par, num_primo] desde 1 al 100
crear una clase con numero, par, primo
clasificar cada numero si es par y si es numero primo

la clasificacion debe de ser realizado mediante el metodo de la clase
"""
class tipos_numeros:
    def __init__(self, numero, num_par, num_primo):
        self.numero = numero
        self.numero_par = num_par
        self.numero_primo = num_primo

lista = []
for linea in range(1,100):
    lista.append(linea)
    print(lista)
    if linea % 2==0:
        numero_par = linea
    print(numero_par)
        #tipos_numeros1 = tipos_numeros

        #tipos_numeros1 = [[tipos_numeros.numero],[tipos_numeros.numero_par],[tipos_numeros.numero_primo]]






