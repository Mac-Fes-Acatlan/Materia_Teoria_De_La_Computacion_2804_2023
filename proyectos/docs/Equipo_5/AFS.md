#Biblioteca AFS

<div class=text-justify>
Como se habia mencionado anteriormente esta biblioteca hace uso de la biblioteca pila, la manera en que lo hace es utilizando cada uno de los metodos que se mostraron anteriormente los cuales eran apilar,desapilar, el verificador de si una pila esta en la cima o si esta se encuentra vacia:
</div>
***

``` python
    class Autopi:
        def __init__(self,palabra):
            self.pila = pila.Pila()
            self.resultado=[]
            self.transiciones=[]
            self.estado_1 = True
            self.estado_2 = False
            self.estado_final = False
            self.palabra=palabra

        def getEstado_1(self):
            return self.estado_1
        def getEstado_2(self):
            return self.estado_2
        def getEstado_final(self):
            return self.estado_final

        def activaEstado_1(self):
            self.estado_1=True
            self.estado_2=False
            self.estado_final=False

        def activaEstado_2(self):
            self.estado_2=True
            self.estado_1=False
            self.estado_final=False

        def activaEstado_final(self):
            self.estado_final=True
            self.estado_1=False
            self.estado_2=False
```
***
<div class=text-justify>
En la siguiente parte del codigo se explica como se emplea la pila para dar seguimiento alas transiciones de b, asi mismo tambien en ese codigo se encuentran las transiciones de  a y de c, se utilizan los metodos de quitar es decir remover el ultimo elemento de la pila y luego si esta requiere alguna apilacion lo hace, para posteriormente verificar en que estamos:
</div>
``` python
    #transiciones con b
    def b_b_bb(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('b')
        self.activaEstado_1()

    def b_a_ab(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('b')
        self.activaEstado_1()
    def b_n_nb(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('b')
        self.activaEstado_1()
```