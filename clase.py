class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("error: El precio y la cantidad deben ser valores positivos.")
            return


        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                producto["cantidad"] += cantidad
                print(f"se han agregado {cantidad} unidades al producto '{nombre}'.")
                return

        nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        self.productos.append(nuevo_producto)
        print(f"producto '{nombre}' agregado con éxito.")

    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if cantidad > producto["cantidad"]:
                    print(f"error: Stock insuficiente de '{nombre}'. Disponible: {producto['cantidad']}.")
                else:
                    producto["cantidad"] -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de '{nombre}'.")
                return
        print(f" error: el producto '{nombre}' no existe en el inventario.")

    def mostrar_inventario(self):
        if not self.productos:
            print(" el inventario está vacío.")
            return
        print(f"inventario de {self.nombre_tienda}:")
        for producto in self.productos:
            print(f"- {producto['nombre']}: ${producto['precio']} (Cantidad: {producto['cantidad']})")

    def producto_mas_caro(self):
        if not self.productos:
            print("no hay productos en el inventario.")
            return
        mas_caro = max(self.productos, key=lambda p: p["precio"])
        print(f"producto más caro: {mas_caro['nombre']} - ${mas_caro['precio']}")

def menu():
    print("MENÚ DE OPCIONES")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Consultar producto más caro")
    print("5. Salir")
    return input("elige una opción: ")


tienda = InventarioTienda("mi Tienda")

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("nombre del producto: ")
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            tienda.agregar_producto(nombre, precio, cantidad)
        except ValueError:
            print("error: Ingresa valores numéricos válidos para precio y cantidad.")

    elif opcion == "2":
        nombre = input("nombre del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
            if cantidad <= 0:
                print(" error: La cantidad debe ser positiva.")
            else:
                tienda.vender_producto(nombre, cantidad)
        except ValueError:
            print(" error: Ingresa un número válido para la cantidad.")

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        tienda.producto_mas_caro()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("error, Opción inválida, intenta de nuevo.")