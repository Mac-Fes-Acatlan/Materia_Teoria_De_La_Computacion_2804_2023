#Biblioteca Pila
<div class=text-justify>
    Esta biblioteca sera complemento de la biblioteca AFS se explica a continuacion el codigo de esta y posteriormente se explicara cada uno de los metodos:
</div>
***

``` python
class Pila:
    def __init__(self):
        self.pila= []
        self.pila.append('#')

    def apilar(self, x):
        self.pila.append(x)

    def quitar(self):
        if(self.vacia()):
            print('la pila esta vacia')
        else:
            return self.pila.pop()

    def cima(self):
        return self.pila[len(self.pila)-1]

    def vacia(self):
        if (self.pila == []):
            return True
        else:
            return False
```
***

##Apilar
<div class=text-justify>
    En este fragmento del codigo es en el unico que tenemos dos parametros el de nuestra pila que es el primero, y el segundo es el valor x, gracias al metodo append podemos agregar un elemento al final de una pila, por consiguiente recibe el funcionamiento es el siguiente recibe la pila y al final de esta agrega un elemento :
</div>

``` python
 def apilar(self, x):
        self.pila.append(x)
```
***

##Quitar o desapilar
<div class=text-justify>
    En este fragmento de codigo pasa lo siguiente recibe de parametro nuestra pila si esta se encuentra vacia nos arrojara un mensaje de la pila esta vacia en caso de que esta contenga algun elemento eliminara o retornara un elemento de esta pila en dado caso de no especificar el indice que sale por defecto retorna el ultimo elemento de la pila:
</div>
``` python
def quitar(self):
        if(self.vacia()):
            print('la pila esta vacia')
        else:
            return self.pila.pop()
```
***

##Cima
<div class=text-justify>
En este fragmento de codigo vamos a retornar un valor la cima para esto pasamos el parametro de la pila dentro de la pila tomamos el valor de esta menos recordando que normalmente los vectores inician en cero por lo cual hay un elemento que se cuenta de más:
</div>
``` python
def cima(self):
        return self.pila[len(self.pila)-1]
```

***
##Vacia
<div class=text-justify>
En este fragmento del codigo se hacen 2 cosas primero comprobamos si la pila es vacia si es el caso nos retornada un verdadero, de caso contrario retornara un falso:
</div>
``` python
def vacia(self):
        if (self.pila == []):
            return True
        else:
            return False
```


###Notas sobre init y self
!!! Note "¿Que es Self?"

    Hace referencia al nombre del objeto en el que se encuentra escrito. Lo podrías reemplazar por el nombre de la clase


!!! Note "¿Que es init?"

    Sirve para inicializar valores de ciertas variables, es decir, los de los atributos. por lo que de este modo, siempre tendrás una serie de valores asignados por defecto al instanciar un objeto.
