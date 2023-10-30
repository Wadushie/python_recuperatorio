"""
Leer los datos de demo-invoice-data.xlsx
1.- Mostrar la tabla leida.
2.- Ingresar nombre de cliente, y listar solamente las facturas de ese cliente.
3.- Sumar por año las los valores de factura.
4.- Guardar Total por año en un archivo.
"""
import csv

def getArithmeticOperation(operation):
    if operation == 1:
        return mostrar_tabla
    if operation == 2:
        return mostrar_datos
    if operation == 3:
        return suma_valores
    if operation == 4:
        return guardar_suma

def mostrar_tabla():
    with open('demo-invoice-data.csv', 'r') as archivo:
        lista_tabla = list(csv.reader(archivo, delimiter=","))
        for linea in lista_tabla:
            print(linea)
        archivo.close()
def mostrar_datos():
    cliente = input('Ingrese el cliente deseado: ')
    try:
        with open('demo-invoice-data.csv', 'r') as archivo_datos:
            lista_datos = csv.reader(archivo_datos, delimiter=",")
            for fila in lista_datos:
                if fila[3] == cliente:
                    print(fila)
    finally:
        archivo_datos.close()
def suma_valores():
    anho_elegido = input('Ingrese el anho deseado para guardar: ')
    suma_anho = 0
    try:
        with open('demo-invoice-data.csv', 'r') as archivo_anho:
            lista_datos = list(csv.reader(archivo_anho, delimiter=","))
            sorted(lista_datos[1][-2])
            for linea in lista_datos:
                if linea[1][-2:] == anho_elegido:
                    print(linea)
                    suma_anho+= float(linea[6])
        print("La suma total del anho elegido es: ",suma_anho, " $")
    finally:
        archivo_anho.close()
def guardar_suma():
    anho_elegido = input('Ingrese el anho deseado: ')
    suma_anho = 0
    try:
        with open('demo-invoice-data.csv', 'r') as archivo_anho:
            lista_datos = list(csv.reader(archivo_anho, delimiter=","))  # lo que lee le convierte en lista
            sorted(lista_datos[1][-2])
            for linea in lista_datos:
                if linea[1][-2:] == anho_elegido:
                    print(linea)
                    suma_anho += float(linea[6])
        print("La suma total del anho elegido es: ", suma_anho, " $")
    finally:
        archivo_anho.close()

    with open('suma_total.csv', 'w') as archivo_guardado:
        writer = csv.writer(archivo_guardado)
        writer.writerow(['La suma total del anho elegido es: ', suma_anho, " $"])
    archivo_guardado.close()


while True:
    print('Menu')
    print('1. Mostrar Tabla')
    print('2. Mostrar los datos de un nombre en especifico')
    print('3. Saber que ocurrio en el anho (02/03/07/09)')
    print('4. Guardar la suma del anho seleccionado en un archivo')
    print('0. Salir')
    operation = int(input('Ingrese una opcion del menu: '))
    if(operation == 0):
        break
    func = getArithmeticOperation(operation)
    result = func()

    print('The result is :', result)

