import sqlite3

db =  sqlite3.connect("shopping.db")

def add_to_cart(id_cart, id_customer, item, cantidad):
    db.execute("insert into carts (id_cart, id_customer, item, cantidad_producto, status) values (?, ?, ?, ?,1)", (id_cart, id_customer, item, cantidad))
    db.commit()
    
def get_items_from_Cart(id):
    
    cursor = db.execute("Select i.nombre, i.precio, ca.cantidad_producto, i.id_producto, i.stock from carts as ca inner join item as i on ca.item = i.id_producto where ca.id_customer = ? and ca.status = 1", (id,))
    lines = cursor.fetchall()
    
    return lines

def set_status(id_customer, id_producto):
    db.execute("update carts set status = 2 where id_customer = ? and item = ? and status = 1", (id_customer, id_producto))
    db.commit()
        
def delete_item_from_cart(id_customer, id_producto, id_cart):
    db.execute("delete from carts where id_customer = ? and item = ? and id_cart = ? and status = 1", (id_customer, id_producto, id_cart))
    db.commit()