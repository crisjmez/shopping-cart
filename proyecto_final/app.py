from tkinter import * 
import models.customers_models as c
import models.items_module as i
import models.cart_models as ca
from customer import Customer
from item import Item
from tkinter import messagebox
import models.pedidos_models as p

class App:
    
    def __init__(self):
        self.root = Tk()
        self.user_v = StringVar()
        self.pass_v = StringVar()
        self.customer = Customer()
        self.gris = "#cca"
        self.azulC = "#333c87"
        self.white = "#ffffff"
        self.leon = "#bc8e47"
    
    def show_root(self):
        self.root.geometry("800x600")
        self.root.config(bg=self.leon)
        self.root.title("Carrito by Cristian")
        self.root.mainloop()
        
    def show_frame_login(self): 
        
        list = self.root.winfo_children()
        
        if len(list) == 0:
            
            self.frame_login = Frame(self.root)
            self.frame_login.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)
            self.frame_login.config(relief="solid", border=5, bg=self.azulC)
            
            #label titulo
            title_label = Label(self.frame_login, text="Inicio de Sesion")
            title_label.pack(pady=25)
            title_label.config(font=("ariel", 18), bg=self.azulC, foreground=self.white)
            label_user_wrong = Label(self.frame_login ,text="")
            label_user_wrong.pack(pady=5)
            label_user_wrong.config(bg=self.azulC, foreground=self.white, font=(14))
            
            #input and label user and pass
            user_label = Label(self.frame_login, text="Usuario")
            user_label.pack()
            user_label.config(bg=self.azulC, foreground=self.white, font=(12))
            user = Entry(self.frame_login, textvariable=self.user_v, justify="center")
            user.pack(pady=10, ipady=5, ipadx=5)
            pass_label = Label(self.frame_login, text="Contaseña")
            pass_label.pack()
            pass_label.config(bg=self.azulC, foreground=self.white, font=(12))
            passW = Entry(self.frame_login, textvariable=self.pass_v, show="*", justify="center")
            passW.pack(pady=10, ipady=5, ipadx=5)
            
            def validar_login():
                
                if( self.user_v.get() == "" or self.pass_v.get()== ""):
                    label_user_wrong.config(text= "Los campos no pueden estar vacios", foreground=self.white)
                    
                else:  
                    
                    user = c.recuperar_customer(self.user_v.get(), self.pass_v.get())
                    if user[1] == True:
                        self.customer.set_id(user[0][0])
                        self.customer.set_nombre(user[0][1])
                        self.customer.set_id_cart(user[0][2])
                        self.customer.set_user(user[0][3])
                        self.customer.set_passw(user[0][4])
                        self.customer.set_tarjeta(user[0][5])
                        self.customer.set_direccion(user[0][6])
                        self.customer.set_cart()
                
                        self.frame_login.destroy()
                        self.show_home()
                    else:
                        label_user_wrong.config(text= "Usuario o contraseña incorrecta", foreground=self.white)
            def call_validate(event):
               validar_login()
            ingresar = Button(self.frame_login, text="Ingresar", command= validar_login, width=15)
            ingresar.pack(ipadx=2, ipady=2)
            ingresar.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")
            passW.bind("<Return>", call_validate)
            user.bind("<Return>", call_validate)
            registrar = Button(self.frame_login, text="Click para registrarse", command= self.show_register, width=15)
            registrar.pack(pady=10, ipadx=2, ipady=2)
            registrar.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")
            
            self.user_v.set("")
            self.pass_v.set("")
        else:
            list[0].destroy()
            self.show_frame_login()
        
    def show_home(self):
        
        self.frame_home = Frame(self.root, border=2, relief="raised")
        self.frame_home.pack(pady=2)
        self.frame_home.config(bg=self.leon)
    
        button1 = Button(self.frame_home, text="Comprar", cursor="hand2", width=18, command= self.show_frame_purchase)
        button1.grid(row=0, column=0, ipady=5, padx=2)
        button1.config(border=3, relief="groove", font=("ariel", 10))
        
        button2 = Button(self.frame_home, text="Ver Pedidos", cursor="hand2", width=18, command=self.ver_pedidos)
        button2.grid(row=0, column=1,ipady=5)
        button2.config(border=3, relief="groove", font=("ariel", 10))
        
        button3 = Button(self.frame_home, text="Mi perfil", cursor="hand2", width=18, command=self.show_profile)
        button3.grid(row=0, column=2, ipady=5, padx=2)
        button3.config(border=3, relief="groove", font=("ariel", 10))
        
        button4 = Button(self.frame_home, text="Carrito", cursor="hand2", width=18, command=self.show_carrito)
        button4.grid(row=0, column=3, ipady=5, padx=2)
        button4.config(border=3, relief="groove", font=("ariel", 10))
        
        def cerra_sesion():
            self.customer = Customer()
            list = self.root.winfo_children()
            if len(list) == 1:
                list[0].destroy()
            else:
                list[0].destroy()
                list[1].destroy()  
            self.show_frame_login()
            
        button5 = Button(self.frame_home, text="Cerrar Sesion", cursor="hand2", width=18, command=cerra_sesion)
        button5.grid(row=0, column=4,ipady=5, padx=2)
        button5.config(border=3, relief="groove", font=("ariel", 10))
        
    def show_profile(self):
        
        list = self.root.winfo_children()
    
        if len(list) == 1:
            self.frame_profile = Frame(self.root)
            self.frame_profile.place(relx=0.5, rely=0.5, anchor="center",  width=400, height=400)
            self.frame_profile.config(relief="solid", border=5, bg=self.azulC)
            
            nombre = StringVar()
            tarjeta = StringVar()
            user = StringVar()
            passw = StringVar()
            direccion = StringVar()
            
            nombre.set(self.customer.get_nombre())
            tarjeta.set(self.customer.get_tarjeta())
            user.set(self.customer.get_user())
            passw.set(self.customer.get_passw())
            direccion.set(self.customer.get_direccion())
            
            label_title = Label(self.frame_profile, text="Mi perfil")
            label_title.pack(pady=10)
            label_title.config(font=("arial", 18), bg=self.azulC, foreground=self.white)
            
            label_nombre = Label(self.frame_profile, text="Nombre")
            label_nombre.pack()
            label_nombre.config(bg=self.azulC, foreground=self.white)
            entry_nombre = Entry(self.frame_profile, text="Nombre", textvariable=nombre, width=25, justify="center")
            entry_nombre.config(state="disabled")
            entry_nombre.pack(pady=2, ipady=2, ipadx=2)
            
            label_tarjeta = Label(self.frame_profile, text="Numero de Tajeta")
            label_tarjeta.pack()
            label_tarjeta.config(bg=self.azulC, foreground=self.white)
            entry_tarjeta = Entry(self.frame_profile, textvariable=tarjeta, width=25, justify="center")
            entry_tarjeta.pack(pady=2, ipady=2, ipadx=2)
            entry_tarjeta.config(state="disabled")
            
            label_user= Label(self.frame_profile, text="Nombre de usuario")
            label_user.pack()
            label_user.config(bg=self.azulC, foreground=self.white)
            entry_user= Entry(self.frame_profile, textvariable=user, width=25, justify="center")
            entry_user.pack(pady=2, ipady=2, ipadx=2)
            entry_user.config(state="disabled")
            
            label_passw = Label(self.frame_profile, text="Contraseña")
            label_passw.pack()
            label_passw.config(bg=self.azulC, foreground=self.white)
            entry_passw = Entry(self.frame_profile, textvariable=passw, width=25, justify="center")
            entry_passw.pack(pady=2, ipady=2, ipadx=2)
            entry_passw.config(state="disabled")
            
            label_direccion = Label(self.frame_profile, text="Direccion")
            label_direccion.pack()
            label_direccion.config(bg=self.azulC, foreground=self.white)
            entry_direccion = Entry(self.frame_profile, textvariable=direccion, width=25, justify="center")
            entry_direccion.pack(pady=2, ipady=2, ipadx=5)
            entry_direccion.config(state="disabled")
            
            def edit_profile():
                entry_nombre.config(state="normal")
                entry_tarjeta.config(state="normal")
                entry_direccion.config(state="normal")
                entry_user.config(state="normal")
                entry_passw.config(state="normal")
                
            btn_edit = Button(self.frame_profile, text="Editar", command=edit_profile, width=20)
            btn_edit.pack(pady=7, ipadx=2, ipady=2)
            btn_edit.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")
            
            
            def save_new_data():
                c.edit_customer(self.customer.get_id(), nombre.get(), user.get(), passw.get(), tarjeta.get(), direccion.get())
                entry_nombre.config(state="disabled")
                entry_tarjeta.config(state="disabled")
                entry_direccion.config(state="disabled")
                entry_user.config(state="disabled")
                entry_passw.config(state="disabled")
                
            btn_save = Button(self.frame_profile, text="Guardar", command=save_new_data, width=20)
            btn_save.pack(pady=7, ipadx=2, ipady=2)
            btn_save.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")
            
        else:
            list[1].destroy()
            self.show_profile()    
   
    def show_frame_purchase(self):
        list = self.root.winfo_children()
        
        if len(list) == 1:
            self.frame_purchase= Frame(self.root, border=2, relief="sunken")
            self.frame_purchase.pack(fill="both", expand=True)
            self.frame_purchase.config(bg=self.azulC)
        
            items = i.recuperarItems()
            r= 1
            j= 1
            
            def add_items():
                
                if(cantidad_v.get() =="" or id_v.get() == ""):
                    messagebox.showerror("Producto", "Los campos cantidad y id\n no pueden estar vacios")
                else:
                    try:
                        item = i.item_by_id(int(id_v.get()))
                        if(item[3]== 0):
                            messagebox.showwarning("Producto", f"El producto {item[1]} no esta disponible")
                        else:
                            ca.add_to_cart(self.customer.get_id_carrito(), self.customer.get_id(), item[0], int(cantidad_v.get()))
                            messagebox.showinfo("Producto", "El producto ha sido ingresado correctamnete")
                    except Exception:
                        messagebox.showerror("Producto", "El id o la cantidad debe ser un numero")
                        
                        
               
            frame_buscar = Frame(self.frame_purchase, width=10)
            frame_buscar.pack(ipady=10, ipadx=5, fill="x")
            frame_buscar.config(border=2, relief="ridge", bg=self.azulC)
            
            cantidad_v = StringVar()
            id_v = StringVar()
            label_id_item = Label(frame_buscar, text="Id del elemento que desea comprar")
            label_id_item.pack()
            label_id_item.config(font=("ariel", 11), bg=self.azulC, fg=self.white)
            id = Entry(frame_buscar, textvariable=id_v, justify="center")
            id.pack(ipady=2, ipadx=2)
            
            label_cantidad = Label(frame_buscar, text="Cantidad que desea comprar")
            label_cantidad.pack()
            label_cantidad.config(font=("ariel", 11), bg=self.azulC, fg=self.white)
            cantidad = Entry(frame_buscar, textvariable=cantidad_v, justify="center")
            cantidad.pack(ipady=2, ipadx=2)
            
            buttom_add = Button(frame_buscar, text="Agregar al carrito", cursor="hand2", command= add_items)
            buttom_add.config(border=3, relief="raised", font=("ariel", 10), bg=self.leon, fg=self.white)
            buttom_add.pack(pady=3, ipadx=2, ipady=2)
            
            frame_items = Frame(self.frame_purchase, width=10)
            frame_items.pack(fill="both", expand=True)
            frame_items.config(bg=self.leon)
            title_label = Label(frame_items, text="Productos")
            title_label.grid(row = 0, column=0, columnspan=1 ,pady=10)
            title_label.config(font=("ariel", 15), bg=self.azulC, foreground=self.white)
            for item in items:
                frame_item = Frame(frame_items, width=10, border=2, relief="solid")
                frame_item.grid(ipadx=7, ipady=5, row=r, column=j, padx=5, pady=5)
                label_item_id = Label(frame_item, text=f"ID: {item[0]}")
                label_item_id.pack()
                label_item_nombre = Label(frame_item,text=item[1])
                label_item_nombre.pack()
                label_item_precio = Label(frame_item,text=f"Precio: {item[2]}")
                label_item_precio.pack()
                label_item_stock = Label(frame_item)
                if(item[3] > 0):
                    label_item_stock.config(text="Disponible", foreground="Green")
                else:
                    label_item_stock.config(text="No disponible", foreground="Red")
                label_item_stock.pack()
               
        
                j+=1
        else:
            list[1].destroy()
            self.show_frame_purchase()

    def show_carrito(self):
        
        list = self.root.winfo_children()
        
        if len(list) == 1:
            self.frame_carrito = Frame(self.root)
            self.frame_carrito.pack(fill="both", expand="True")
            self.frame_carrito.config(border=2, relief="ridge", bg=self.leon)

            frame_title = Frame(self.frame_carrito, border=1, relief="raised")
            frame_title.pack(fill="x")
            frame_title.config(bg=self.azulC)
            
            label_title = Label(frame_title, text="Carrito")
            label_title.pack(pady=10)
            label_title.config(font=("ariel", 18), bg=self.azulC, foreground=self.white)
            
            frame_items = Frame(self.frame_carrito)  
            frame_items.config(bg=self.leon) 
            frame_items.place(x=15, y=60)
            
            i= 0
            j = 0
            
            for item in ca.get_items_from_Cart(self.customer.get_id()):
                
                    item_o = Item()
                    item_o.set_id(item[3])
                    item_o.set_nombre(item[0])
                    item_o.set_precio(item[1])
                    item_o.set_stock(item[4])
                    self.customer.cart.add_item(item_o, item[2])

                    frame_item = Frame(frame_items, border=2, relief="solid")
                    frame_item.grid(row=i, column=j, ipadx=5, ipady=5, padx=5, pady=5)
                    label_item_nombre = Label(frame_item,text=f"ID: {item[3]}")
                    label_item_nombre.pack()
                    label_item_nombre = Label(frame_item,text=item[0])  
                    label_item_nombre.pack()
                    label_item_precio = Label(frame_item,text=f"Precio: {item[1]}")
                    label_item_precio.pack()
                    label_item_cantidad = Label(frame_item,text=f"Cantidad: {item[2]}")
                    label_item_cantidad.pack()
                    i += 1
                    if i == 4:
                        i = 0
                        j+=1

                
            frame_precio = Frame(self.frame_carrito)
            frame_precio.place(relx=0.8, rely=0.12, width=150, height=125)
            frame_precio.config(bg=self.azulC)

            label_total = Label(frame_precio, text="Total a pagar")
            label_total.pack(pady=10)
            label_total.config(bg=self.azulC, fg=self.white, font=("ariel", "12"))
            Label_precio = Label(frame_precio, text=f"$ {self.customer.cart.get_total()}")
            Label_precio.pack()
            Label_precio.config(bg=self.azulC, fg=self.white,font=("ariel", "10"))
            
            frame_delete = Frame(self.frame_carrito)
            frame_delete.place(relx=0.8, rely=0.7, width=150, height=125)
            frame_delete.config(bg=self.azulC)
            
            id_v = StringVar()
            label_id_item = Label(frame_delete, text="Id del elemento \nque desea eliminar\n del carrito")
            label_id_item.pack()
            label_id_item.config(font=("ariel", 11), bg=self.azulC, fg=self.white)
            id = Entry(frame_delete, textvariable=id_v, justify="center")
            id.pack(ipady=2, ipadx=2)
            
            def eliminar():
                try:
                    ca.delete_item_from_cart(self.customer.get_id(), id_v.get(), self.customer.get_id_carrito())
                    self.customer.cart.remove_item(id_v.get())
                    self.show_carrito()
                except Exception:
                    messagebox.showerror("Carrito", "El id debe ser un numero")
            
            buttom_delete = Button(frame_delete, text="Eliminar del carrito", cursor="hand2", command= eliminar)
            buttom_delete.config(border=3, relief="raised", font=("ariel", 10), bg=self.leon, fg=self.white)
            buttom_delete.pack(pady=3, ipadx=2, ipady=2)

            
            def pagar():
                res = messagebox.askquestion("Comprar", f"El total es de {self.customer.cart.get_total()}\n de sea realizar la compra? ")
                messagebox.showinfo("Factura", self.customer.cart.purchase(res))
                if(res =="yes"): 
                    for item in self.customer.cart.get_list_item():
                        p.insert_pedido(self.customer.get_id(), item[0].get_id(),self.customer.get_id_carrito(), 1)
                        ca.set_status(self.customer.get_id(), item[0].get_id())  
                        frame_items.destroy()
                        Label_precio.config(text="0")
                
                self.customer.cart.set_list_item()    
                                         
                    
            btn_pagar = Button(frame_precio, text="Pagar", command=pagar)
            btn_pagar.pack(ipadx=2, ipady=2, pady=5)
            btn_pagar.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")
            

        else:
            list[1].destroy()
            self.customer.cart.set_total(0)
            self.show_carrito()
    
    def ver_pedidos(self):
        
        list = self.root.winfo_children()
        
        if len(list) == 1:
            self.frame_pedidos = Frame(self.root)
            self.frame_pedidos.pack(fill="both", expand=True)
            self.frame_pedidos.config(border=2, relief="ridge", bg=self.azulC)
            
            frame_title = Frame(self.frame_pedidos, border=1, relief="raised")
            frame_title.pack(fill="x")
            frame_title.config(bg=self.azulC)
            
            frame_pedidos = Frame(self.frame_pedidos, border=2, relief="solid")
            frame_pedidos.config(bg=self.leon)
            frame_pedidos.pack(fill="both", expand=True)
            
            label_title = Label(frame_title, text="Pedidos")
            label_title.pack(pady=10)
            label_title.config(font=("ariel", 18), bg=self.azulC, foreground=self.white)
            
            
            pedidos = p.pedidos(self.customer.get_id())
            i= 0
            j = 0
                
            for pedido in pedidos:
                
                frame_item = Frame(frame_pedidos,border=2, relief="solid")
                frame_item.grid(row=i, column=j, padx=5, pady=5)
                label_item_nombre = Label(frame_item,text=f"Nombre: {pedido[0]}")
                label_item_nombre.pack()
                label_item_precio = Label(frame_item,text=f"Precio: {pedido[1]}")
                label_item_precio.pack()
                label_item_status = Label(frame_item)
                label_item_status.pack()
                if(pedido[2]==1):
                    label_item_status.config(text="Pendiente de envio", fg="#f00")
                else:
                    label_item_status.config(text="Paquete enviado")
                j += 1
                if j == 6:
                    j = 0
                    i+=1
        else:
            list[1].destroy()
            self.ver_pedidos()
            
    def show_register(self):
          
        list = self.root.winfo_children()
        list[0].destroy()
 
        if len(list) == 1:
            nombre = StringVar()
            tarjeta = StringVar()
            user = StringVar()
            passw = StringVar()
            direccion = StringVar()
            
            self.frame_register = Frame(self.root)
            self.frame_register.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)
            self.frame_register.config(relief="solid", border=5, bg=self.azulC)
                
            label_title = Label(self.frame_register, text="Registro de nuevo cliente")
            label_title.pack(pady=10)
            label_title.config(font=("arial", 18), bg=self.azulC, foreground=self.white)
            
            label_user_wrong = Label(self.frame_register ,text="")
            label_user_wrong.config(bg=self.azulC, foreground=self.white, font=("ariel", 12))
            label_user_wrong.pack(pady=2)
            
            label_nombre = Label(self.frame_register, text="Nombre")
            label_nombre.pack()
            label_nombre.config(bg=self.azulC, foreground=self.white)
            entry_nombre = Entry(self.frame_register, text="Nombre", textvariable=nombre, width=20, justify="center")
            entry_nombre.pack(pady=2, ipady=2, ipadx=2)
            
            label_tarjeta = Label(self.frame_register, text="Numero de Tajeta")
            label_tarjeta.pack()
            label_tarjeta.config(bg=self.azulC, foreground=self.white)
            entry_tarjeta = Entry(self.frame_register, textvariable=tarjeta, width=20, justify="center")
            entry_tarjeta.pack(pady=2, ipady=2, ipadx=2)
            
            label_user= Label(self.frame_register, text="Nombre de usuario")
            label_user.pack()
            label_user.config(bg=self.azulC, foreground=self.white)
            entry_user= Entry(self.frame_register, textvariable=user, width=20, justify="center")
            entry_user.pack(pady=2, ipady=2, ipadx=2)
            
            label_passw = Label(self.frame_register, text="Contraseña")
            label_passw.pack()
            label_passw.config(bg=self.azulC, foreground=self.white)
            entry_passw = Entry(self.frame_register, textvariable=passw, width=20, justify="center")
            entry_passw.pack(pady=2, ipady=2, ipadx=2)
            
            label_direccion = Label(self.frame_register, text="Direccion")
            label_direccion.pack()
            label_direccion.config(bg=self.azulC, foreground=self.white)
            entry_direccion = Entry(self.frame_register, textvariable=direccion, width=20, justify="center")
            entry_direccion.pack(pady=2, ipady=2, ipadx=2)
            
            def data_customer():
                if(nombre.get() == "" or tarjeta.get() == ""  or user.get() == "" or passw.get() == ""or direccion.get() == ""):
                    label_user_wrong.config(text= "Los campos no pueden estar vacios", foreground=self.white)
                else:
                    id = c.id() + 1
                    c.insert_customer(nombre.get(), id, user.get(), passw.get(),tarjeta.get(), direccion.get())
                    self.show_frame_login()
                    
            registrar = Button(self.frame_register, text="Registrarse", command=data_customer, width=16)
            registrar.pack(pady=7, ipadx=2, ipady=2)
            registrar.config(border=1, fg=self.white, bg=self.leon, cursor="hand2")

          


            