class Producto:
    def __init__(self,nombre, precio, año) -> None:
        self.nombre=nombre
        self.precio=precio
        self.año=año
        print('Se añadio el producto:', self.nombre)
    def __str__(self):
        return '{}({})=${}'.format(self.nombre,self.año,self.precio)  

class Catalogo:
    productos=[]
    def __init__(self,productos=[]) -> None:
        self.productos=productos
    def agregar(self,p):
        self.productos.append(p)
    def mostrar(self):
        for p in self.productos:
            print(p)

    def filtro(self,año):
        p_filtrados = [producto for producto in self.productos if producto.año == año]
        if not p_filtrados:
            print(f"No hay productos del año {año} en el catálogo.")
        else:
            print(f"Productos del año {año}:")
            for producto in p_filtrados:
                print(producto)

pt1=Producto('Puerta', precio=75, año=2012)
pt2=Producto('Espejo', precio=34, año=2015)
pt3=Producto('Faros', precio=80, año=2017)

catalogo_autopartes=Catalogo([pt1,pt2,pt3])

catalogo_autopartes.mostrar()

catalogo_autopartes.agregar(Producto(nombre='Cajuela', precio=123, año=2017))
catalogo_autopartes.mostrar()

catalogo_autopartes.filtro(2017)