# Tienda_Ropa_POOBootcamp
Tienda_Ropa_POOBootcamp
# Tienda de Ropa

## Descripción
Este proyecto es una tienda de ropa en línea que permite a los usuarios seleccionar productos y realizar compras. Utiliza la Programación Orientada a Objetos (POO) en Python para gestionar productos, categorías y el carrito de compras.

## Estructura del Proyecto
- `sistema_compra_ropa.py`: Archivo principal donde se ejecuta la aplicación.
- `producto`: Contiene la clase base `Producto`, que representa un producto general.
- `ropa`: Clase que hereda de `Producto` y añade características específicas de la ropa.
- `camisa`, `pantalon`, `zapato`: Clases específicas que heredan de `Ropa` y añaden atributos particulares.
- `carrito`: Clase que gestiona el carrito de compras.
- `README.md`: Este archivo.

## Clases Implementadas

### Producto
- **Descripción**: Clase base que representa un producto general.
- **Atributos**:
  - `nombre`: Nombre del producto.
  - `precio`: Precio del producto.
  
### Ropa (hereda de Producto)
- **Descripción**: Clase que añade características específicas de la ropa.
- **Atributos**:
  - `talla`: Talla de la ropa.
  - `tipo_de_tela`: Tipo de tela utilizada.

### Camisa (hereda de Ropa)
- **Descripción**: Clase que representa una camisa.
- **Atributos**:
  - `manga`: Longitud de la manga (corta, larga).

### Pantalon (hereda de Ropa)
- **Descripción**: Clase que representa un pantalón.
- **Atributos**:
  - `tipo`: Tipo de pantalón (jeans, chinos).

### Zapato (hereda de Ropa)
- **Descripción**: Clase que representa un zapato.
- **Atributos**:
  - `talla_zapato`: Talla del zapato.
  - `tipo_de_zapato`: Tipo de zapato (de vestir, deportivo).

### Carrito
- **Descripción**: Clase que maneja los productos seleccionados por el usuario.
- **Métodos**:
  - `agregar_producto`: Agrega un producto al carrito.
  - `calcular_total`: Calcula el precio total de los productos en el carrito.

## Principios de Programación Orientada a Objetos (POO)

### 1. Abstracción
La abstracción permite ocultar los detalles internos y mostrar solo la información necesaria al usuario. En este proyecto:
- La clase `Carrito` gestiona todos los detalles de agregar productos y calcular el total, permitiendo al usuario interactuar solo con la selección de productos y la visualización del total, sin preocuparse por cómo se realizan esos cálculos internamente.

### 2. Encapsulamiento
El encapsulamiento consiste en restringir el acceso directo a algunos componentes del objeto. Se logró utilizando métodos getter y setter:
- En las clases, los atributos (como `nombre`, `precio`, `talla`, etc.) son privados y se accede a ellos a través de métodos.
- Por ejemplo, en la clase `Producto`, se puede tener métodos como `obtener_precio()` y `establecer_precio(nuevo_precio)` que permiten obtener y modificar el precio de un producto de forma controlada.

### 3. Herencia
La herencia permite crear nuevas clases basadas en clases existentes. En este proyecto:
- La clase `Ropa` hereda de `Producto`, lo que significa que hereda atributos como `nombre` y `precio`, además de añadir atributos específicos como `talla` y `tipo_de_tela`.
- Clases como `Camisa`, `Pantalon` y `Zapato` heredan de `Ropa`, lo que permite crear productos más específicos mientras reutilizan el código de las clases padres.

### 4. Polimorfismo
El polimorfismo permite que una función o método opere en diferentes tipos de datos. En este proyecto:
- Cada clase hija (como `Camisa`, `Pantalon` y `Zapato`) tiene su propia implementación del método `mostrar_info()`, que sobrescribe el método de la clase base.
- Esto permite que al llamar a `mostrar_info()` en un objeto de tipo `Ropa`, se ejecute la implementación correcta dependiendo de si el objeto es una `Camisa`, un `Pantalon` o un `Zapato`.

## Instrucciones de Uso
1. Clona el repositorio a tu máquina local.
2. Abre una terminal y navega al directorio del proyecto.
3. Ejecuta el archivo `sistema_compra_ropa.py` para iniciar la tienda de ropa.
4. Sigue las instrucciones en pantalla para seleccionar productos y realizar una compra.
