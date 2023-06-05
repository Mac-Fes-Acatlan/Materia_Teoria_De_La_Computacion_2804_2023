## Implementación
 El codigo esta usa la clase `AF` como base, en su mayoria usa los mismos metodos que la clase base.

```python
class AFDP(af.AF):
    ...
```

## Representación de la pila 
Al constructor de la clase del automata de pila (`AFDP`), se agregan propiedades nuevas : 
```python
def __init__ (
    self, 
    alfabeto_pila : set,
    estado_inicial_pila : str) :

    self.estado_inicial_pila = estado_inicial_pila
    self.alfabeto_pila = alfabeto_pila
    self.pila = [EPSILON  ,estado_inicial_pila]
 ```

 Para simular la _pila_ fue necesario agregar clases nuevas, estas clases nos permiten representar las acciones que la pila puede hacer, `Pop`, `Pila`, `Continue`

```python
class AccionPila:
    ...

@dataclass
class Continue(AccionPila):
    ...

@dataclass
class Pop(AccionPila):
    ...

@dataclass
class Push(AccionPila):
    valor : str

@dataclass(unsafe_hash=True)
class Transicion:
    accion_pila : AccionPila
    destino : str
```
## Representación de las transiciones 
La forma en la que  especifican las transiciones al automata difieren a la clase base, tome por ejemplo el siguiente estado de transición :
$$
    \delta( q_0, a, X) = (q_1, XX)
$$

Se lee como :
>si estamos en el estado $q_0$, con una transición $a$ y $X$ en el tope de la pila, cambie el estado $q_0$ a $q_1$ e ingrese el simbolo $X$ a la pila

En nuestro código la transición mencionada se especifica como :
```python
transicion = {
    "q_0" : {
        "a" : {
            "X" : Transicion( accion_pila=Push(valor="X"), destino="q1")
        }
    }
}
```
Notese que si tenemos la misma transición por medio de $a$ pero con otro operacion que afetca a la pila, basta con usar alguna de las clases de `AccionPila`, por ejemplo si agregamos mas transiciones al ejemplo anterior :

1. $\delta( q_0, a, z_0) = (q_3, \epsilon)$
2. $\delta( q_0, a, Y) = (q_1, YY)$
3. $\delta( q_1, b, Y) = (q_1, YY)$

```python
transicion = {
    "q_0" : {
        "a" : {
            "X" : Transicion( accion_pila=Push(valor="X"), destino="q1"),
            "z0" : Transicion( accion_pila=Pop(), destino="q3"),
            "Y" : Transicion( accion_pila=Push(valor="Y"), destino="q1"),
        }
    },
    "q_1" : {
        "b" : {
            "Y" : Transicion(accion_pila=Push(valor="Y"), destino="q_1")
        }
    }
}
```
## Sobre la implementación

Una ventaja de ocupar clases para representar las acciones de la pila es la forma en la que podemos saber que acción ejercer sobre la pila, tomando ventaja del operador `match` introuddcido en `python3.10` 

```python
match pila_accion:
    case Transicion(destino=_,accion_pila = Push(valor = valor) ):
        self.pila.append(valor) 
    case Transicion( destino=_, accion_pila = Pop() ):
        if tope_pila != 'e' :
            self.pila.pop()
    case Transicion(destino=_, accion_pila = Continue()):
        ...
```

