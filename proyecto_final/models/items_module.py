import sqlite3

db = sqlite3.connect("shopping.db")


def recuperarItems():
    
    cursor = db.execute("Select * from item")
    items = cursor.fetchall()
    
    return items

def item_by_id(id):
    
    cursor = db.execute("Select * from item where id_producto = ?", (id, ))
    items = cursor.fetchone()
    
    return items
    

