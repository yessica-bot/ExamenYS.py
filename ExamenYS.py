productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
    'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

def stock_marca(marca):
    marca = marca.lower()
    print(f"Stock de la marca {marca}:")
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            print(f"Modelo: {modelo}, Stock: {stock[modelo][1]}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, datos in productos.items():
        precio, cantidad = stock[modelo]
        if p_min <= precio <= p_max and cantidad > 0:
            resultados.append(f"{datos[0]}--{modelo}")
    
    if resultados:
        resultados.sort()
        print("Modelos en el rango de precios:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No hay notebooks en ese rango de precios.")

def ordenar_productos():
    if not productos:
        print("No hay notebook disponibles para mostrar")
        return
    
    print("Listado de productos:")
    for modelo, datos in productos.items():
        print(f"{datos[0]} - {modelo} - {datos[2]} - {datos[3]} ({datos[4]})")

def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            marca = input("Ingrese la marca: ")
            stock_marca(marca)
        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese el precio mínimo: "))
                    p_max = int(input("Ingrese el precio máximo: "))
                    busqueda_precio(p_min, p_max)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        elif opcion == '3':
            ordenar_productos()
        elif opcion == '4':
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción válida!!")

main()
