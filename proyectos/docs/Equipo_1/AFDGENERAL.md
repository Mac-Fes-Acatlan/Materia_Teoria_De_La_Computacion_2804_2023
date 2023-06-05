#Biblioteca AFD GENERAL

<div class=text-justify>
Esta biblioteca sera complemento de la biblioteca AFD, se explica a continuacion el codigo de esta y posteriormente se explicara cada uno de los metodos:
</div>
***

```
import copy
from collections import deque
import tools.automata.af as af
import tools.base.excepciones as excepciones
import logging

logging.basicConfig(level=logging.INFO)


class AFD(af.AF):
    def __init__(
        self,
        estados: set,
        input_simbolos: set,
        transiciones: dict,
        estado_inicial: set,
        estados_finales: set,
    ):
        self.estados = estados.copy()
        self.input_simbolos = input_simbolos.copy()
        self.transiciones = copy.deepcopy(transiciones)
        self.estado_incial = estado_inicial
        self.estados_finales = estados_finales.copy()
        self.validacion_parametros()

    def _validacion_comparacion_missing_estado_transiciones(self):

        for estado in self.estados:
            if estado not in self.transiciones:
                raise excepciones.EstadoMissingError(
                    f"El estado {estado}, no se encuentra definido en las transiciones"
                )

    def _validacion_comparacion_invalido_estado_estados(self, estado_transicion, path):

        for estado in path.values():
            if estado not in self.estados:
                raise excepciones.EstadoInvalidoError(
                    f"""Para el estado {estado_transicion} con transicion a {estado},
                    el estado {estado} no se encuentra definido en el conjuto de estados"""
                )

    def _validacion_comparacion_missing_simbolo_transiciones(
        self, estado_transicion, path
    ):

        for input_simbolo in self.input_simbolos:
            if input_simbolo not in path:
                raise excepciones.SimboloMissingError(
                    f"El simbolo {input_simbolo} no se encuentra definido en las transicion {estado_transicion}"
                )

    def _validacion_comparacion_invalido_simbolo_entradas(
        self, estado_transicion, path
    ):

        for input_simbolo in path.keys():
            if input_simbolo not in self.input_simbolos:
                raise excepciones.SimboloInvalidoError(
                    f"""Para el estado {estado_transicion} con procesamiento al simbolo {input_simbolo}
                    no se tiene definido dentro del conjunto de entradas"""
                )

    def _validacion_transiciones(self, estado, path):
        self._validacion_comparacion_missing_simbolo_transiciones(estado, path)
        self._validacion_comparacion_invalido_simbolo_entradas(estado, path)
        self._validacion_comparacion_invalido_estado_estados(estado, path)

    def validacion_parametros(self) -> bool:

        self._validacion_comparacion_missing_estado_transiciones()

        for estado_transicion, path in self.transiciones.items():
            self._validacion_transiciones(estado_transicion, path)

        self._validacion_estado_inicial()
        self._validacion_estados_finales()

        return True

    def lectura_paso_a_paso(self, input_str: str):

        estado_actual = self.estado_incial
        yield estado_actual

        for input_simbolo in input_str:

            estado_actual = self._get_siguiente_estado_actual(
                input_str, estado_actual, input_simbolo
            )
            yield estado_actual

        self._rechazo_de_cadena(estado_actual)

    def _get_siguiente_estado_actual(self, input_str, estado_actual, input_simbolo):

        if input_simbolo in self.transiciones[estado_actual]:
            return self.transiciones[estado_actual][input_simbolo]
        else:
            raise excepciones.RechazoException(
                f"Para la cadena {input_str} , el simbolo {input_simbolo} no es valido"
            )

    def _rechazo_de_cadena(self, estado_actual):

        if estado_actual not in self.estados_finales:

            raise excepciones.RechazoException(
                "La cadena procesada no es aceptada por el automata"
            )
        else:
            logging.info(f" Cadena procesada, con estado final : {estado_actual}\n")
```
***






#Explicación



## Implementación de un Autómata Finito Determinista (AFD)

El siguiente código representa una implementación de una clase `AFD` (Autómata Finito Determinista) que simula el funcionamiento de un autómata finito determinista.

### Descripción

El código proporcionado es una implementación de la clase `AFD` que hereda de una clase base `AF`. El objetivo de esta implementación es representar y simular un autómata finito determinista.

### Estructura del código

#### Importaciones

Se importan los siguientes módulos:

- `copy`: utilizado para realizar operaciones de copia.
- `deque`: utilizado para crear una cola.
- `tools.automata.af`: módulo que contiene la clase base `AF`.
- `tools.base.excepciones`: módulo que contiene las excepciones personalizadas.
- `logging`: módulo utilizado para el registro de información.

#### Clase `AFD`

La clase `AFD` tiene los siguientes métodos:

- `__init__(self, estados, input_simbolos, transiciones, estado_inicial, estados_finales)`: constructor que inicializa los atributos de la clase con los parámetros proporcionados.
- `validacion_parametros(self)`: método que realiza validaciones en los parámetros proporcionados al autómata para asegurarse de que estén correctamente definidos.
- `lectura_paso_a_paso(self, input_str)`: método que simula la lectura paso a paso de una cadena de entrada en el autómata.
- `_get_siguiente_estado_actual(self, input_str, estado_actual, input_simbolo)`: método interno que devuelve el siguiente estado actual dado el estado actual y el símbolo de entrada.
- `_rechazo_de_cadena(self, estado_actual)`: método interno que verifica si el estado actual indica el rechazo de la cadena.

### Conclusiones

El código implementa un AFD y proporciona métodos para validar los parámetros del autómata y simular la lectura paso a paso de una cadena de entrada. Las excepciones personalizadas ofrecen información detallada sobre posibles errores. Es importante destacar que este código se puede utilizar como base para construir y trabajar con autómatas finitos deterministas.


