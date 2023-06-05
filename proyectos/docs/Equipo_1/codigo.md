# Proyecto Autómatas Finitos Deterministas

## Descripción
Este proyecto consiste en la implementación de un autómata finito determinista (AFD) para validar el orden de un Registro Federal de Contribuyentes (RFC). El AFD verifica si una cadena de texto dada cumple con las reglas de formación de un RFC válido.

## Clase `Automaton`
La clase `Automaton` representa el autómata finito determinista y contiene los siguientes métodos y atributos:

### Atributos
- `states`: Diccionario que define el conjunto de estados y las transiciones entre ellos.
- `accept_states`: Lista de estados de aceptación.

### Métodos
- `__init__(self)`: Constructor de la clase. Inicializa los estados y las transiciones del autómata.
- `check_string(self, string)`: Método que verifica si una cadena es válida de acuerdo al autómata. Recibe como parámetro la cadena a verificar y retorna un valor booleano indicando si la cadena es válida o no.

## Uso del autómata
Para utilizar el autómata y verificar un RFC, sigue los siguientes pasos:

1. Crea una instancia del autómata: `automaton = Automaton()`
2. Solicita un RFC al usuario: `rfc = input('Introduce un RFC: ')`
3. Verifica el RFC utilizando el autómata: `is_valid = automaton.check_string(rfc.upper())`
4. Imprime el resultado de la verificación: `print(is_valid)`

Recuerda que el RFC debe ingresarse en mayúsculas para que el autómata funcione correctamente.

---
