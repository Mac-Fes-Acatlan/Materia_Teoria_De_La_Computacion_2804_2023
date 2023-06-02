#Biblioteca AFS

<div class=text-justify>
Como se habia mencionado anteriormente esta biblioteca hace uso de la biblioteca AFD biblioteca encargada de la construcción de un objeto tipo AFD que recibe como parametros el estado inicial, estados finales, alfabeto, función de trancisión.
<br>
<br>
A continuación se presenta un ejemplo de la construcción de un AFD con esta libreria.
<br>
<br>

``` python
from tools.automata.afd import AFD
    dfa = AFD(
        estados={"q0", "q1", "q2"},     #Estados del AFD
        input_simbolos={"0", "1"},      #Alfabeto del AFD
        transiciones={                  #Función de trancision para el AFD
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q0", "1": "q2"},
            "q2": {"0": "q2", "1": "q1"},
        },  
        estado_inicial="q0",            #Estado inicial del AFD
        estados_finales={"q2"},         #Estados de aceptación del AFD
    )
```
<br>

<div class=text-justify>
En la siguiente parte del codigo se describe el funcionamiento de la evaluación de los estados, como identifica el termino del AFD y la precaución de simbolos equivocados en las entradas.
</div>
<br>
<br>

``` python
#Encuentra que los estados sean validos para la trancisiones definidas.
    def _validacion_comparacion_missing_estado_transiciones(self):

        for estado in self.estados:
            if estado not in self.transiciones:
                raise excepciones.EstadoMissingError(
                    f"El estado {estado}, no se encuentra definido en las transiciones"
                )
#Encuentra el siguiente estado a pasar del automata siguiendo su función de transcisión.
    def _get_siguiente_estado_actual(self, input_str, estado_actual, input_simbolo):
       if input_simbolo in self.transiciones[estado_actual]:
           return self.transiciones[estado_actual][input_simbolo]
       else:
           raise excepciones.RechazoException(
               f"Para la cadena {input_str} , el simbolo {input_simbolo} no es valido"
           )

#Indica si la cadena que se proceso es correcta o no es aceptada por el AFD.
    def _rechazo_de_cadena(self, estado_actual):

        if estado_actual not in self.estados_finales:

            raise excepciones.RechazoException(
                "La cadena procesada no es aceptada por el automata"
            )
        else:
            logging.info(f" Cadena procesada, con estado final : {estado_actual}\n")
#Funcion encargada de leer la cadena insertada haciendo uso de "lectura_paso_a_paso"
    def lectura_input(self, input_str):

    validacion_generada = self.lectura_paso_a_paso(input_str)
        for config in validacion_generada:
            pass
        return config
#Valida que se encuentre el estado inicial dentro de las transciciones
    def _validacion_estado_inicial(self):

        if self.estado_incial not in self.transiciones:
            raise excepciones.EstadoInicialError(
                "El estado inicial no se tiene determinado en la funcion de transición"
            )
#Valida que el estado final se encuentre entre los estados de transcicion.
    def _validacion_estados_finales(self):

        estados_invalidos = self.estados_finales - self.estados
        if estados_invalidos:
            raise excepciones.EstadosFinalesError(
                "El estado final , no es elemento del conjunto de estados "
            )

```