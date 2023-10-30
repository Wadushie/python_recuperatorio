# mostrar factura de la persona/comanhia
"""
EJERCICIO 1
crear clase factura
cargar los datos en la clase
mostrar las facturas de una fecha seleccionada
mostrar las facturas de un cliente seleccionado

EJERCICIO 2
crear clase cliente
cargar los datos en la clase
cargar el saldo de facturación utilizan un método de la clase
mostrar el saldo del cliente utilizando un método




"""
import csv
import codecs

class documento:
    def __init__(self, INVOICE_ID,DATEINVOICED, DOCUMENTONO, BPNAME):
        self.id_documento = INVOICE_ID
        self.fecha_emision_documento = DATEINVOICED
        self.numero_de_documento = DOCUMENTONO
        self.nombre_cliente = BPNAME
    """
        def actualizar_precio(self, GRANDTOTAL, nuevo_GRANDTOTAL):
        self.precio = GRANDTOTAL
        self.precio_nuevo = nuevo_GRANDTOTAL"""

    def show(self): # la funcion dentro de una clase se llama metodo, la diferencia con una funcion es que accede a los atributos de una clase
        print(f"id: {self.id_documento} / fecha: {self.fecha_emision_documento} / numero documento: {self.numero_de_documento} / nombre de cliente-companhia: {self.nombre_cliente}")
        #imprime toodo lo que se encuentra dentro sin tener el print entero
class plata:
    def __init__(self, TAXID, ISO_CODE, GRANDTOTAL):
        self.id_impuesto = TAXID    # ???????????
        self.codigo_moneda = ISO_CODE
        self.cantidad_plata = GRANDTOTAL


def mostrar_tabla():
    with open('prueba2.csv', encoding = 'utf8') as archivo: # al escribir un texto en windows, se graba de una forma a diferencia de linux
        lectura_csv = csv.reader(archivo, delimiter=',')
        for linea in lectura_csv:
            print(linea)
        archivo.close()
def factura_fecha():
    fecha = input("Para saber las facturas de una fecha en especifico, Ingrese la fecha deseado (ej = 12/01/03): ")
    with open('prueba1.csv', encoding = 'utf8') as factura:
        lista_fecha = list(csv.reader(factura, delimiter=','))
        sorted(lista_fecha[1])  # mostrara / buscara solo la seccion de la fecha (15/01/02) --> (02)
        for linea in lista_fecha:
            #print(linea[1],fecha)
            if linea[1] == fecha:
                cliente1 = documento(linea[0],linea[1],linea[2],linea[3])
                plata1 =plata(linea[4],linea[5],linea[6])
                print(linea)
                #print(f"El cliente: {cliente1.nombre_cliente} obtuvo {plata1.grandtotal} % de {plata1.iso_code} en el anho {cliente1.fecha_emision_documento}")

def factura_nombre():
    nombre = input("Para saber la factura de una persona/companhia en especifico, Ingrese el nombre: ")
    with codecs.open('prueba2.csv', "r", "utf-8") as factura: # se usa encoding diferente por el teclado que interfiere el SO
        #codecs = abre el archivo y respeta la codificacion del archivo (porque la fuente de datos esta en utf-8 y el windows de esta maquina esta en cp850)
        lista_nombre = list(csv.reader(factura, delimiter=','))
        sorted(lista_nombre[3])
        for linea in lista_nombre:
           if linea[3] == nombre:
            cliente1 = documento(linea[0], linea[1], linea[2], linea[3])
            plata1 = plata(linea[4], linea[5], linea[6])
            #print("Forma 1 de impresion")
            #print(cliente1.id_documento, cliente1.fecha_emision_documento, cliente1.numero_de_documento, cliente1.nombre_cliente)
            print("Forma 2 de impresion")
            cliente1.show() # llama el metodo show para imprimir
while True:
    print("Menu")
    print("1 = Mostrar Tabla")
    print("2 = Mostrar facturas de una fecha en especifico")
    print("3 = Mostrar facturas de un cliente en especifico")
    print("0 = Salir")
    decision = input()
    print("Ingrese un numero: ",decision)
    if decision == "1":
        mostrar_tabla()
    elif decision == "2":
        factura_fecha()
    elif decision == "3":
        factura_nombre()
    elif decision == "0":
        print("saliendo del programa")
        break
    else:
        print("Opcion no valida, Ingrese un numero devuelta")