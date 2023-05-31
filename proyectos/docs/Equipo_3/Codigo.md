#Codigo principal
<div class=text-justify>
    La primera parte del programa importamos la biblioteca instrucciones que como se menciona en informacion sobre esta, es la que nos da el contexto generalizado sobre que es lo que pasa por detras, y con la biblioteca AFS que depende a su vez de la biblioteca pila la cual hace todos los cambios de apilamiento,sacar elementos, y asu vez verificar si una pila esta vacia o si se encuentra en la cima,una vez tenemos esto y que ya sabemos como funciona por detras, unimos todo en este codigo principal,importando primero nuestras bibliotecas AFS, e instrucciones , adicional a esto importamos la bilbioteca tkinter que no es otra cosa que una biblioteca para crear aplicaciones graficas:
</div>

``` python
import AFS
import instrucciones

import tkinter
from tkinter import Label
from tkinter import *
from tkinter import ttk
```
<div class=text-justify>
    Ahora vamos a crear una clase principal a esta se le cargaran diferentes funciones cada una de ellas es esencial para el programa:
</div>

``` python
class Principal:
```
<div class=text-justify>
    Agrega a la ventana principal el texto y le da formato de visualización:
</div>

``` python
    def __init__(self,descripcion):
            self.resultado=None
            self.tran=None
            self.descri=descripcion
            self.ventana=tkinter.Tk()
``` 
<div class=text-justify>
    La segunda funcion manda los resultados correspondientes al recuadro de operaciones y el recuadro de las transiciones del grafo :
</div>

``` python
    def cargar_resultado(self,listbox,listbox2):
        for r in self.resultado:
            listbox.insert(END,r)
        for t in self.tran:
            listbox2.insert(END, t))
``` 
<div class=text-justify>
    La tercera funcion le da formato a los dos recuadros de resultados:
</div>

``` python
    def sgda_ventana(self):
        segunda_ventana=tkinter.Toplevel(self.ventana)
        segunda_ventana.title('Ventana de procedimiento')
        segunda_ventana.minsize(width=600,height=500)
        
        scrollbar = Scrollbar(segunda_ventana)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        listbox = Listbox(segunda_ventana)
        listbox.config( width=60, height=30,yscrollcommand=scrollbar.set,font=("Courier", 10))
        scrollbar.config(command=listbox.yview)
        
        
        listbox['bg'] = 'black'
        listbox['fg'] = "#38EB5C"
    
        listbox2 = Listbox(segunda_ventana)
        listbox2.config( width=40, height=30,yscrollcommand=scrollbar.set,font=("Courier", 10))
        listbox2['bg'] = 'black'
        listbox2['fg'] = "#38EB5C"
        
        self.cargar_resultado(listbox,listbox2)
   
        listbox.pack(side=LEFT, fill=Y)
        listbox2.pack()
        self.ventana.iconify()
``` 
<div class=text-justify>
    La cuarta funcion es la encargada de hacer las evaluaciones y ya es donde entra nuestra bilbioteca AFS que fue descrita anteriormente lo unico que pasa, es que se le pasan parametros a esta y activa los modulos que estan dentro de esta biblioteca para poder hacer las transciciones:
</div>

``` python
    def  evaluar(self):
        auto=AFS.Autopi(self.text.get())
        auto.validar()
        self.resultado=auto.resultado
        self.tran=auto.transiciones
        self.sgda_ventana()
``` 
<div class=text-justify>
    La quinta y ultima funcio es la que nos mantiene en la ventana principal se mantiene un loop para que esta jamas se cierre si no es con el boton de cerrado, y nos da gran ventaja para poder introducir mas datos tambien se cargan las imagenes y modelos a esta que es nuestra ventana principal:
</div>

``` python
def main(self):
        self.ventana.title('Ventana principal')
        img = PhotoImage(file="img.gif")
        widget = Label(self.ventana, image=img).pack()

        plbra=tkinter.Entry(self.ventana)
        plbra.pack()
        self.text=plbra
        
        boton = tkinter.Button(self.ventana, text="Validar", command=self.evaluar, bg="#38EB5C",relief="groove")
        boton['bg'] = 'black'
        boton['fg'] = "#38EB5C"
        boton.pack()
        
     
        listbox = Listbox(self.ventana)
        listbox.place(relwidth=1 ,relheight=-0.50)
        listbox['bg'] = 'black'
        listbox['fg'] = "#38EB5C"
    
        
        for des in self.descri:
            listbox.insert(END, des)
            
        listbox.pack(fill=X, expand=1)
        
        scrollbar = Scrollbar(self.ventana)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        listbox.config(yscrollcommand=scrollbar.set , font=("Courier", 14))
        scrollbar.config(command=listbox.yview)

        self.ventana.minsize(width=600,height=500)
        self.ventana.mainloop()


``` 
<div class=text-justify>
    Aqui primero llamamos a la biblioteca instrucciones para poder hacer el llenado de la ventana posteriormente en la main es donde empieza toda la magia que va por detras descrita en las bibliotecas AFS y Pila de las que depende enteramente todos los resultados y procesos:
</div>

``` python
des = instrucciones.des
p = Principal(des)
p.main()
``` 
