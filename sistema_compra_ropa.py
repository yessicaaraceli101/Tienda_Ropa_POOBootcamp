# Clase base Producto
class Producto:
    """
    Clase base que representa un producto general.
    Atributos:
        - _nombre: nombre del producto.
        - _precio: precio del producto.
    """

    # Constructor de la clase Producto (Uso de Constructores)
    def __init__(self, nombre, precio):
        # Atributos encapsulados (_nombre y _precio) (Encapsulamiento)
        self._nombre = nombre
        self._precio = precio

    # Método para obtener el precio (Encapsulamiento con método getter)
    def obtener_precio(self):
        return self._precio

    # Método mostrar_info, que se sobrescribirá en clases hijas (Polimorfismo)
    def mostrar_info(self):
        return f"Producto: {self._nombre}, Precio: {self._precio} Gs"


# Clase Ropa, que hereda de Producto (Herencia)
class Ropa(Producto):
    """
    Clase que hereda de Producto y añade características específicas de la ropa.
    Atributos:
        - _talla: talla de la prenda.
        - _tipo_tela: tipo de tela de la prenda.
    """

    # Constructor que inicializa los atributos de Ropa
    def __init__(self, nombre, precio, talla, tipo_tela):
        # Llamada al constructor de la clase base Producto (Herencia)
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    # Método sobrescrito mostrar_info (Polimorfismo)
    def mostrar_info(self):
        # Mostrar información específica de la ropa
        return (f"Ropa: {self._nombre}, Precio: {self._precio} Gs, "
                f"Talla: {self._talla}, Tipo de tela: {self._tipo_tela}")


# Clase Camisa, que hereda de Ropa (Herencia)
class Camisa(Ropa):
    """
    Clase que hereda de Ropa y añade características específicas de las camisas.
    Atributos:
        - _tipo_manga: tipo de manga de la camisa.
    """

    # Constructor que inicializa los atributos de Camisa
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_manga):
        # Llamada al constructor de la clase base Ropa (Herencia)
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_manga = tipo_manga

    # Método sobrescrito mostrar_info (Polimorfismo)
    def mostrar_info(self):
        # Mostrar información específica de la camisa
        return (f"Camisa: {self._nombre}, Precio: {self._precio} Gs, "
                f"Talla: {self._talla}, Tipo de tela: {self._tipo_tela}, Tipo de manga: {self._tipo_manga}")


# Clase Pantalon, que hereda de Ropa (Herencia)
class Pantalon(Ropa):
    """
    Clase que hereda de Ropa y añade características específicas de los pantalones.
    Atributos:
        - _tipo_pantalon: tipo de pantalón.
    """

    # Constructor que inicializa los atributos de Pantalon
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_pantalon):
        # Llamada al constructor de la clase base Ropa (Herencia)
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_pantalon = tipo_pantalon

    # Método sobrescrito mostrar_info (Polimorfismo)
    def mostrar_info(self):
        # Mostrar información específica del pantalón
        return (f"Pantalón: {self._nombre}, Precio: {self._precio} Gs, "
                f"Talla: {self._talla}, Tipo de tela: {self._tipo_tela}, Tipo de pantalón: {self._tipo_pantalon}")


# Clase Zapato, que hereda de Producto (Herencia)
class Zapato(Producto):
    """
    Clase que hereda de Producto y añade características específicas de los zapatos.
    Atributos:
        - _talla: talla del zapato.
        - _material: material del zapato.
    """

    # Constructor que inicializa los atributos de Zapato
    def __init__(self, nombre, precio, talla, material):
        # Llamada al constructor de la clase base Producto (Herencia)
        super().__init__(nombre, precio)
        self._talla = talla
        self._material = material

    # Método sobrescrito mostrar_info (Polimorfismo)
    def mostrar_info(self):
        # Mostrar información específica del zapato
        return (f"Zapato: {self._nombre}, Precio: {self._precio} Gs, "
                f"Talla: {self._talla}, Material: {self._material}")


# Clase Carrito que maneja los productos seleccionados por el usuario
class Carrito:
    """
    Clase que representa un carrito de compras.
    Atributos:
        - productos: lista que almacena los productos seleccionados.
    """

    # Constructor para inicializar una lista de productos vacía
    def __init__(self):
        self.productos = []

    # Método para agregar un producto al carrito
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para calcular el precio total de los productos en el carrito
    def calcular_total(self):
        # Suma los precios de todos los productos en el carrito
        return sum([producto.obtener_precio() for producto in self.productos])

    # Método para mostrar un resumen de los productos en el carrito
    def mostrar_resumen(self):
        if not self.productos:
            return "El carrito está vacío."
        resumen = "Resumen de la compra:\n"
        for producto in self.productos:
            resumen += producto.mostrar_info() + "\n"
        resumen += f"Total a pagar: {self.calcular_total()} Gs"
        return resumen


# Clase Tienda que maneja la interacción con el usuario y los productos disponibles
class Tienda:
    """
    Clase que maneja los productos disponibles y las compras en la tienda.
    Atributos:
        - productos_disponibles: lista de productos que se pueden comprar.
    """

    # Constructor que inicializa los productos disponibles en la tienda
    def __init__(self):
        self.productos_disponibles = [
            Camisa("Camisa Formal", 100000, "M", "Algodón", "Larga"),
            Pantalon("Pantalón Jeans", 150000, "L", "Denim", "Slim Fit"),
            Zapato("Zapatos de Cuero", 300000, 42, "Cuero")
        ]

    # Método para mostrar el menú de productos disponibles
    def mostrar_menu(self):
        print("Bienvenido a la Tienda de Ropa")
        print("Por favor, seleccione un producto:")
        for i, producto in enumerate(self.productos_disponibles, 1):
            print(f"{i}. {producto.mostrar_info()}")
        print("Escriba 'salir' para terminar la compra.")

    # Método para iniciar el proceso de compra (Interacción con el Usuario)
    def iniciar_compra(self):
        # Instancia de la clase Carrito
        carrito = Carrito()
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione el número del producto o 'salir': ")
            if opcion.lower() == 'salir':
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(self.productos_disponibles):
                producto_seleccionado = self.productos_disponibles[int(opcion) - 1]
                carrito.agregar_producto(producto_seleccionado)
                print(f"{producto_seleccionado._nombre} ha sido agregado al carrito.\n")
            else:
                print("Opción no válida, por favor intente nuevamente.\n")
        
        # Mostrar el resumen de la compra al finalizar
        print(carrito.mostrar_resumen())


# Ejecutar el programa
tienda = Tienda()
tienda.iniciar_compra()