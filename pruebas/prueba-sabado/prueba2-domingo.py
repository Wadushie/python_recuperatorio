"""
crear una lista con [nombre_cliente, facturano, fecha, total], cada cliente debe tener minimo 2 facturas

Generar un alista de la sgte forma
nombre_cliente  cantidad_facturas   suma_total

debe clasificarse utilizando metodo de clase
"""
import csv
class factura:
    def __init__(self, nombre_cliente, facturanro, fecha, nombre_producto, total):
        self.nombre_cliente = nombre_cliente
        self.numero_factura = facturanro
        self.fecha_emision_factura = fecha
        self.nombre_producto = nombre_producto
        self.total_dinero = total
def mostrar_tabla():
    with open('clientes_factura.csv','r') as archivo:
        lista_tabla = list(csv.reader(archivo, delimiter=","))
        for linea in lista_tabla:
            print(linea)
        archivo.close()
def factura_nombre():
    nombre_cliente = input("Ingrese el nombre de la persona en la que desea ver su factura")
    suma_cantidad_factura = 0
    suma_cantidad_total = 0
    with open('clientes_factura.csv', 'r') as archivo:
        lista_tabla = list(csv.reader(archivo, delimiter=","))
        for linea in lista_tabla:
            #print(linea)
            if linea[0] == nombre_cliente:
                factura1 = factura(linea[0], linea[1], linea[2], linea[3],linea[4])
                factura1.nombre_cliente = linea[0]
                factura1.numero_factura = linea[1]
                factura1.nombre_producto = linea[3]
                factura1.total_dinero = linea[4]
                suma_cantidad_factura += float(linea[1])
                suma_cantidad_total += float(linea[4])
               # print(linea)
                print("-----------------")
                print(f"El cliente {factura1.nombre_cliente} tiene las siguientes facturas: {factura1.numero_factura}, con el producto: {factura1.nombre_producto} de precio: {factura1.total_dinero}")
                print(f"La cantidad de facturas que tiene el cliente {factura1.nombre_cliente} es: ",suma_cantidad_factura)
        print("#############")
        print(f"La cantidad total del precio es: {suma_cantidad_total}")
while True:
    print("menu")
    print("1 = Mirar Tabla")
    print("2 = Factura a nombre de cliente")
    print("0 = Salir")
    decision = input()
    print("Ingrese el siguiente numero")
    if decision == "1":
        mostrar_tabla()
    elif decision == "2":
        factura_nombre()
    elif decision == "0":
        print("Saliendo del programa")
        break
    else:
        print("Input incorrecto, vuelva a intentar")