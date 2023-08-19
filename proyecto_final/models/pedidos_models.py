import sqlite3

db = sqlite3.connect("shopping.db")

def retriver_id():
    cursor = db.execute("select Max(id_producto) from pedidos")
    return cursor.fetchone()[0]

def insert_pedido(id_customer, id_producto, id_carrito, status):
    db.execute("insert into pedidos (id_custumer, id_producto, id_carrito, status) values (?,?,?, ?)", (id_customer, id_producto, id_carrito, status))
    db.commit()
    
def pedidos(id):
    cursor = db.execute(""" 
           Select i.nombre, i.precio, p.status from pedidos as p 
           inner join item as i on p.id_producto = i.id_producto where p.id_custumer = ?
           """, (id, ))
    
    lines = cursor.fetchall()
    
    return lines

