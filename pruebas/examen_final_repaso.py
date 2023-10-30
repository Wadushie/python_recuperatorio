"""
Una tienda en línea quiere contar con un programa que procese las ventas de productos que
realiza durante el mes. Por cada venta se registran varios datos:
id_cliente, nombre_cliente, teléfono_cliente, id_producto, , fecha_hora_venta,
estado_venta, numero_factura, id_vendedor, nombre_vendedor, , costo_envio,
comentarios, , precio_unitario, total_venta
1. Elija las variables que crea conveniente
2. Genere un archivo de entrada con al menos 10 filas
3. Implemente un menú con 2 funcionalidades utilizando programación orientada a objetos



"nombre_cliente","nombre_producto","direccion_envio","precio_unitario","descuento"
"Joaquin","Zapato","Ciudad del Este",160,0.25
"Rogelio","Termo","Encarnacion",20,0.10
"Ivonne","Pulsera","Buenos Aires",5,0.05
"Gianluca","Jugo","Misiones",3,0.50
"Ivan","Bufanda","Paraguari",16,0.15
"Andres","Collar","Montevideo",500,0.35
"Paulo","Mouse","Asuncion",50,0.75
"Jeronimo","Teclado","Boqueron",40,0.05
"Cinthia","Notebook","Brasilia",1000,0.10
"Maria","Lego","Concepcion",365,0.12
"""
import csv

class cliente:
    def init(self, nombre_cliente, nombre_producto, descuento):
        self.nombre_cliente = nombre_cliente
        self.nombre_producto = nombre_producto
        self.descuento_obtenido = descuento
archivo = list([["nombre_cliente","nombre_producto","direccion_envio","precio_unitario","descuento"],
["Joaquin","Zapato","Ciudad del Este",160,0.25],
["Rogelio","Termo","Encarnacion",20,0.10],
["Ivonne","Pulsera","Buenos Aires",5,0.05],
["Gianluca","Jugo","Misiones",3,0.50],
["Ivan","Zapato","Paraguari",16,0.15],
["Andres","Collar","Montevideo",500,0.35],
["Paulo","Mouse","Asuncion",50,0.75],
["Jeronimo","Teclado","Boqueron",40,0.05],
["Cinthia","Notebook","Brasilia",1000,0.10],
["Maria","Lego","Concepcion",365,0.12]])

def mostrar_tabla():
    csv_examen = open('practicaexamen.csv', 'w')
    csv_writer = csv.writer(csv_examen, delimiter=',')
    csv_writer.writerows(archivo)
    for i in archivo:
        print(i)
    csv_examen.close()
def datos_cliente():
    nombre_cliente = input("De que persona quiere saber su informacion. Ingrese su nombre: ")
    with open('practicaexamen.csv', 'r') as archivo_datos:
        lista_datos = list(csv.reader(archivo_datos, delimiter=","))
        for linea in lista_datos:
            if len(linea) > 0: # se puso para esquivar las lineas en blanco dependiendo del teclado de windows
                if linea[0] == nombre_cliente:
                    cliente1 = cliente()
                    cliente1.nombre_cliente = linea[0]
                    print(linea)
                    print(cliente1.nombre_cliente)
    archivo_datos.close()
def calcular_descuento():
    nombre_cliente = input("De que persona quiere saber su informacion y cuanto es su descuento. Ingrese su nombre: ")
    with open('practicaexamen.csv', 'r') as archivo_datos:
        lista_datos = list(csv.reader(archivo_datos, delimiter=","))
        for linea in lista_datos:
            if len(linea) > 0: # se puso para esquivar las lineas en blanco dependiendo del teclado de windows
                if linea[0] == nombre_cliente:
                    cliente1 = cliente()
                    cliente1.nombre_cliente = linea[0]
                    cliente1.descuento_obtenido = float(linea[3]) * float(linea[4])
                    print(linea)
                    print(f"El cliente: {cliente1.nombre_cliente} obtuvo {cliente1.descuento_obtenido} % de descuento")
    archivo_datos.close()
while True:
    print("Elija una de las opciones")
    print("1 = Observar Tabla")
    print("2 = Datos de un cliente en especifico")
    print("3 = Calcular descuento")
    print("0 = Salir")
    decision = input()
    print("Ingrese un numero: ", decision)

    if decision == "1":
        mostrar_tabla()
    elif decision == "2":
        datos_cliente()
    elif decision == "3":
        calcular_descuento()
    elif decision == "0":
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida, Ingrese devuelta")