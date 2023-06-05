#Biblioteca AFD

<div class=text-justify>
Como se habia mencionado anteriormente esta biblioteca hace uso de la biblioteca automata finito determinista
</div>
***

``` python
     class Automaton:
     def __init__(self):
```
<div class=text-justify>
Definición de los estados y transiciones del autómata
</div>
***
```
        self.states = {
            'Q0': {'letter': 'Q1', 'number': 'Qr', 'other': 'Qr'},
            'Q1': {'letter': 'Q2', 'number': 'Qr', 'other': 'Qr'},
            'Q2': {'letter': 'Q3', 'number': 'Qr', 'other': 'Qr'},
            'Q3': {'letter': 'Q4', 'number': 'Qr', 'other': 'Qr'},
            'Q4': {'letter': 'Qr', 'number': 'Q5', 'other': 'Qr'},
            'Q5': {'letter': 'Qr', 'number': 'Q6', 'other': 'Qr'},
            'Q6': {'letter': 'Qr', 'number': 'Q7', 'other': 'Qr'},
            'Q7': {'letter': 'Qr', 'number': 'Q8', 'other': 'Qr'},
            'Q8': {'letter': 'Qr', 'number': 'Q9', 'other': 'Qr'},
            'Q9': {'letter': 'Qr', 'number': 'Q10', 'other': 'Qr'},
            'Q10': {'letter': 'Q11', 'number': 'Q11', 'other': 'Qr'},
            'Q11': {'letter': 'Q12', 'number': 'Q12', 'other': 'Qr'},
            'Q12': {'letter': 'Q12', 'number': 'Q12', 'other': 'Qr'},
```
<div class=text-justify>
Estado de rechazo
</div>
***
``` 
            'Qr': {}  
        }
```
<div class=text-justify>
Estado de aceptación
</div>
***
```        
        self.accept_states = ['Q12']  # Estados de aceptación

        def check_string(self, string):
```
<div class=text-justify>
Estado inical
</div>
***
```
          current_state = 'Q0' 
          for character in string:
```
<div class=text-justify>
Verifica el tipo de caracter (letra, número u otro) y realiza la transición de estado correspondiente
</div>
***
```
              if character.isalpha():
                  current_state = self.states[current_state].get('letter', 'Qr')
              elif character.isdigit():
                  current_state = self.states[current_state].get('number', 'Qr')
              else:
                  current_state = self.states[current_state].get('other', 'Qr')

        return current_state in self.accept_states
```
<div class=text-justify>
Ejecuta el programa
</div>
***
```

        automaton = Automaton()
        rfc = input('Introduce un RFC: ')
        print(automaton.check_string(rfc.upper()))
```
