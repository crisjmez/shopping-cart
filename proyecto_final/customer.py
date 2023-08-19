from shopping_cart import Shopping_cart

class Customer:
    
    def __init__(self):
        self.nombre = None
        self.tarjeta = None
        self.direccion = None
        self.user = None
        self.passw = None
        self.cart = None
        self.id = None
        self.id_carrito = None
        
    def set_id(self, id):
        self.id = id
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def set_tarjeta(self, tarjeta):
        self.tarjeta = tarjeta
    
    def set_direccion(self, direccion):
        self.direccion = direccion
    
    def set_user(self, user):
        self.user = user
    
    def set_passw(self, passw):
        self.passw = passw
    
    def set_id_cart(self, id_cart):
        self.id_carrito = id_cart
        
    def set_cart(self):
        self.cart = Shopping_cart(self.get_id_carrito(), self.get_nombre(),self.get_direccion())
    
    def get_id(self):
        return self.id
           
    def get_nombre(self):
        return self.nombre
        
    def get_tarjeta(self):
        return self.tarjeta
    
    def get_direccion(self):
        return self.direccion
    
    def get_carrito(self):
        return self.cart
    
    
    def get_user(self):
        return self.user
    
    def get_passw(self):
        return self.passw
    
    def get_id_carrito(self):
        return self.id_carrito
    
    def display_comprador(self):
        

        print(f"""
              
                Nombre: {self.nombre}
                Direccion: {self.direccion}
              """)