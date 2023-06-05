
<p align="center">
    <img src="https://i.makeagif.com/media/4-24-2020/LeAsku.gif" alt="Turing & The Halting Problem - Computerphile" width="800">
</p>



#Codigo principal
<div class=text-justify>
    Para empezar creamos una clase Verificador la cual va a ser nuestro autómata.
</div>

``` python
class Verificador:
```
<div class=text-justify>
    Después en el constructor creamos una lista con los estados, una variable para guardar el estado actual y otra lista para los posibles estado de aceptación.
    El estado q5 va a ser nuestro estado de aceptación con respuesta positiva y el estado q6 va a ser nuestro estado de aceptación con respuesta negativa.
</div>

``` python
    def __init__(self):
        self.estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'q6']
        self.estados_de_aceptacion = ['q5','q6']
        self.estado_actual = 'q0'
```
<div class=text-justify>
    A continuación se crea un metodo para verificar que el email siga las reglas del autómata.
</div>

``` python        
    def verifica(self, email):
        for char in email:
            self.transicion(char)
        
        return self.estado_actual if self.estado_actual in self.estados_de_aceptacion else "error"
```
<div class=text-justify>
    Definimos las transiciones del autómata.
</div>

``` python    
    def transicion(self, char):
        if self.estado_actual == 'q0':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q1' # Siguiente estado
            else:
                self.estado_actual = 'q6' # Estado invalido
        
        elif self.estado_actual == 'q1':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q1' # Mantiene el estado actual
            elif char == '@':
                self.estado_actual = 'q2' # Siguiente estado
            else:
                self.estado_actual = 'q6'  # Estado invalido
        
        elif self.estado_actual == 'q2':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q3' # Siguiente estado
            elif char == '.':
                self.estado_actual = 'q6' # Estado invalido
            else:
                self.estado_actual = 'q6'  # Estado invalido
        
        elif self.estado_actual == 'q3':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q3' # Mantiene el estado actual
            elif char == '.':
                self.estado_actual = 'q4' # Siguiente estado
            else:
                self.estado_actual = 'q6'  # Estado invalido
        
        elif self.estado_actual == 'q4':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q5' # Siguiente estado
            elif char == '.':
                self.estado_actual = 'q6'  # Estado invalido
            else:
                self.estado_actual = 'q6'  # Estado invalido
        
        elif self.estado_actual == 'q5':
            if char.isalnum() or char == '_':
                self.estado_actual = 'q5' # Mantiene el estado actual
            elif char == '.':
                self.estado_actual = 'q4' # Siguiente estado
            else:
                self.estado_actual = 'q6'  # Estado invalido
```
