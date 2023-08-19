import random

class Orden:
    
    def __init__(self, total, direccion, nombre):
        self.numero_compra = random.randint(1, 10000)
        self.total = total
        self.IVA = total * 0.18
        self.nombre = nombre
        self.direccion = direccion
        
    def display_factura(self):
        return (f"""
              Numero Factura: {self.numero_compra}
              Nombre: {self.nombre}
              Total: {self.total}
              Impuesto: {self.IVA}
              Direccion: {self.direccion}
              """)