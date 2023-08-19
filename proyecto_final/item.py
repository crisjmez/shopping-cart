class Item:
    
    def __init__(self):
        self.nombre = None
        self.id = None
        self.price = None
        self.stock = None
    
    def set_id(self, id):
        self.id = id 
        
    def set_nombre(self, nombre):
        self.nombre= nombre
        
    def set_precio(self, precio):
        self.price = precio   
        
    def set_stock(self, stock):
        self.stock = stock   
        
    def display_item(self):
        print(
            f"""
                ID: {self.id}
                Nombre: {self.nombre}
                Precio: {self.price}
                Stock: {self.stock}
            """
        )
        
    def get_nombre(self):
        return self.nombre
    
    def get_id(self):
        return self.id
    
    def get_precio(self):
        return self.price
    
    def update_stock(self, cantidad):
        
        self.stock -= cantidad
    