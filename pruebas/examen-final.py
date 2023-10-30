import csv


class Cliente:
    def _init_(self, id_cliente, nombre_cliente):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente


class Vendedor:
    def _init_(self, id_vendedor, nombre_vendedor):
        self.id_vendedor = id_vendedor
        self.nombre_vendedor = nombre_vendedor


class Producto:
    def _init_(self, id_prod, nombre_prod, precio_unitario):
        self.id_prod = id_prod
        self.nombre_prod = nombre_prod
        self.precio_unitario = precio_unitario


class Venta:
    def _init_(self, id_cliente, nombre_cliente, id_prod, nombre_prod, numero_factura, id_vendedor,
                 nombre_vendedor, precio_unitario, total_venta):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.id_prod = id_prod
        self.nombre_prod = nombre_prod
        self.numero_factura = numero_factura
        self.vendedor = id_vendedor
        self.nombre_vendedor = nombre_vendedor
        self.precio_unitario = precio_unitario
        self.total_venta = total_venta


def ingresar_informe_mes(a):
    print('Importar del archivo: ', a)
    array_input = []
    try:
        with open(a, 'r') as lista_datos:
            lector_csv = csv.reader(lista_datos, delimiter=";")
            for fila in lector_csv:
                array_input.append(fila)

        nombre_archivo_salida = f'archivo_lectura_{a.split(".")[0]}.csv'

        with open(nombre_archivo_salida, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(array_input)
    finally:
        lista_datos.close()


def observar_informe_mes(a):
    print('Exportar del archivo: ', a)
    array_input = []
    try:
        with open(a, 'r') as lista_datos:
            lector_csv = csv.reader(lista_datos, delimiter=";")
            for fila in lector_csv:
                print(fila)
                array_input.append(fila)
    finally:
        lista_datos.close()

    nombre_archivo_salida = f'archivo_observado_{a.split(".")[0]}.csv'

    with open(nombre_archivo_salida, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(array_input)

    return nombre_archivo_salida


def crear_archivo_clientes(a):
    try:
        with open(a, 'r') as lista_datos:
            lector_csv = csv.reader(lista_datos, delimiter=",")

            encabezados = next(lector_csv)

            idx_id_cliente = encabezados.index('id_cliente')
            idx_nombre_cliente = encabezados.index('nombre_cliente')

            info_clientes = []

            for fila in lector_csv:
                id_cliente = fila[idx_id_cliente]
                nombre_cliente = fila[idx_nombre_cliente]

                info_clientes.append([id_cliente, nombre_cliente])

        # Escribir la información de los clientes en el nuevo archivo
        with open('informacion_clientes.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id_cliente', 'nombre_cliente'])
            writer.writerows(info_clientes)
            for fila in info_clientes:  # forma de procesar x linea
                writer.writerow(fila)
                print(fila, end='\n')
            print("----")
            print("id_cliente', 'nombre_cliente")   # forma de procesar en el que escribe todas las lineas con titulos
            for fila in info_clientes:
                print(fila, end='\n')
        print('Archivo de clientes creado: informacion_clientes.csv')
        print('Proceso completado.')

    except FileNotFoundError:
        print(f'El archivo no fue encontrado.')

def getArithmeticOperation(operation):
    if operation == 1:
        return ingresar_informe_mes
    if operation == 2:
        return observar_informe_mes
    if operation == 3:
        return crear_archivo_clientes

while True:
    print('Menu :)))')
    print("1. Ingresar informe del mes")
    print("2. Observar informe del mes")
    print("3. Crear archivo de clientes")
    print('0. Salir')
    operation = int(input('Ingrese una opcion del menu : '))
    if operation == 0:
        break
    func = getArithmeticOperation(operation)
    a = str(input('Nombre de Archivo : '))
    result = func(a)
    print('The result is :', result)