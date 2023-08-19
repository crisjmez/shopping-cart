import sqlite3

db = sqlite3.connect("shopping.db")
    
def recuperar_customer(user, passw):
    cursor = db.execute("Select * from customers where user_name = ? and passw = ?", (user,passw))
    fila = cursor.fetchone()
    if fila != None:
            return (fila, True)
    else:
        return (fila, False)


def edit_customer(id,nombre, user, passw, tarjeta, direccion):
    db.execute("UPDATE customers set nombre = ?, user_name = ?, passW = ?, tarjeta = ?, direccion = ? where id_customer = ?", (nombre, user, passw, tarjeta,direccion, id))
    db.commit()
    
    
def insert_customer(nombre, id_shopping_car, user_name, passW, tarjeta, direccion):
    db.execute("INSERT INTO customers (nombre, id_shopping_car, user_name, passW, tarjeta, direccion) values (?,?,?,?,?,?)", (nombre, id_shopping_car, user_name, passW, tarjeta, direccion))
    db.commit()
    
def id():
    cursor = db.execute("select Max(id_shopping_car) from customers")
    return cursor.fetchone()[0]
