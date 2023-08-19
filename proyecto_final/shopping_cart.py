from ordene_de_compra import Orden


class Shopping_cart:
    
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.list_item = []
        self.total = 0
        self.nombre = nombre
        self.direccion = direccion
        
    def set_total(self, total):
        self.total = total
    
    def set_list_item(self):
        self.list_item = []
        
    def get_id(self):
        return self.id
    
    
    def add_item(self, item, cantidad):
        self.list_item.append([item, cantidad])
        self.total += item.get_precio() * cantidad

    def get_total(self):
        return self.total
    
  
        
    def get_list_item(self):
        return self.list_item
        
    def remove_item(self, id):
        
        for item in self.list_item:
           
            if(item[0].get_id() == id):
                self.total = self.total - item[0].get_precio() * item[1]
                self.list_item.pop(id-1)
             
    def set_quantity(self, id, cantidad):
        for item in self.list_item:
           
            if(item[0].get_id() == id):
                self.total = self.total - item[0].get_precio() * item[1]
                item[1] = cantidad
                self.total +=  item[0].get_precio() * item[1]
    
    def purchase(self, opcion):
                
        if opcion == "yes":
            orden = Orden(self.get_total(), self.direccion, self.nombre)
            return orden.display_factura()
        else:
            return "Haz cancelado la compra!!"


         
