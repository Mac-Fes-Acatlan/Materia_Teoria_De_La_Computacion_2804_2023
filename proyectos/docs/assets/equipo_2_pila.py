class excepciones:
    class AutomataExcepcion(Exception):
        pass
    
    
    class EstadoInicialError(AutomataExcepcion):
        pass
    
    
    class EstadosFinalesError(AutomataExcepcion):
        pass
    
    
    class RechazoException(AutomataExcepcion):
        pass
    
    
    class EstadoInvalidoError(AutomataExcepcion):
        pass
    
    
    class EstadoMissingError(AutomataExcepcion):
        pass
    
    
    class SimboloInvalidoError(AutomataExcepcion):
        pass
    
    
    class SimboloMissingError(AutomataExcepcion):
        pass
    
    
    class EstadoinvalidooError(AutomataExcepcion):
        pass
    
    
    class SimboloinvalidooError(AutomataExcepcion):
        pass
    
    
    class DesplazamientoinvalidoError(AutomataExcepcion):
        pass
    
    class TransicionPilaError(AutomataExcepcion):
        pass
    

EPSILON = ''

class AccionPila:
    ...

class Continue(AccionPila):
    ...

class Pop(AccionPila):
    ...

class Push(AccionPila):
    def __init__(self, valor):
        self.valor = valor

class Transicion:
    def __init__(self, accion_pila, destino):
        self.accion_pila = accion_pila
        self.destino = destino

class AFDP:
    def __init__(
            self, 
            estados: set, 
            input_simbolos : set, 
            transiciones : dict , 
            estado_inicial : str, 
            alfabeto_pila : set,
            estados_finales : set,
            estado_inicial_pila : str,
        ) -> None:

        self.estados         = estados.copy()
        self.input_simbolos  = input_simbolos.copy()
        self.transiciones    =  transiciones
        self.estado_inicial  = estado_inicial
        self.estado_incial   = estado_inicial
        self.estados_finales = estados_finales.copy()

        self.estado_inicial_pila = estado_inicial_pila
        self.alfabeto_pila = alfabeto_pila
        self.pila = [EPSILON  ,estado_inicial_pila]

        # self.validacion_parametros() 

    def _validacion_transiciones(self, estado, path):
        self._validacion_comparacion_missing_simbolo_transiciones(estado, path) #done
        self._validacion_comparacion_invalido_simbolo_entradas(estado, path)
        self._validacion_comparacion_invalido_estado_estados(estado, path)

    def _validacion_comparacion_invalido_estado_estados(self, estado_transicion, path):

        for topes_de_pila in path.values():
            if topes_de_pila : 
                for transicion in topes_de_pila.values():
                    estado = transicion.destino

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

    def _validacion_comparacion_missing_estado_transiciones(self):

        for estado in self.estados:
            if estado not in self.transiciones:
                raise excepciones.EstadoMissingError(
                    f"El estado {estado}, no se encuentra definido en las transiciones"
                )

    def validacion_parametros(self) -> bool:

        self._validacion_comparacion_missing_estado_transiciones() #done

        for estado_transicion, path in self.transiciones.items():
            self._validacion_transiciones(estado_transicion, path)

        #self._validacion_estado_inicial() #done
        #self._validacion_estados_finales() #done 

        return True

    def lectura_paso_a_paso(self, input_str : str):
        self.pila = [EPSILON  ,self.estado_inicial_pila]
        estado_actual = self.estado_inicial

        yield estado_actual


        for input_simbolo in input_str:
            estado_actual = self._get_siguiente_estado_actual(
                    input_str, estado_actual, input_simbolo
                    )
            yield estado_actual

        estado_actual = self._get_siguiente_estado_actual( 
            input_str= input_str, 
            estado_actual = estado_actual, 
            input_simbolo = EPSILON)

        self._rechazo_de_cadena(estado_actual)

    def _get_siguiente_estado_actual(self, input_str, estado_actual, input_simbolo):

        transiciones = self.transiciones[estado_actual]
        transicion = transiciones.get(input_simbolo) 

        if transicion is None:
            raise excepciones.RechazoException(
                f"Para la cadena {input_str} , el simbolo {input_simbolo} no es valido"
            )

        tope_pila = self.pila[-1]
        pila_accion = transicion.get(tope_pila)

        if pila_accion is None:
            raise excepciones.TransicionPilaError(f"No existe la transicion con el tope de pila {tope_pila}, y el simbolo {input_simbolo} con estado {estado_actual}")

        match pila_accion:
            case Transicion(destino=_,accion_pila = Push(valor = valor) ):
                self.pila.append(valor) 
            case Transicion( destino=_, accion_pila = Pop() ):
                if tope_pila != 'e' :
                    self.pila.pop()
            case Transicion(destino=_, accion_pila = Continue()):
                ...

        return pila_accion.destino

    def _rechazo_de_cadena(self, estado_actual):

        if estado_actual not in self.estados_finales:
            raise excepciones.RechazoException(
                   "La cadena procesada no es aceptada por el automata"
                )
        else:
            print(f" Cadena procesada, con estado final : {estado_actual}\n")
def test_parentesis(s): 
    transiciones = { "q1" : { "(" : { 'z0' : Transicion( accion_pila = Push(valor="X")   , destino = "q1"), 'X' : Transicion( accion_pila = Push(valor="X")   , destino = "q1"), 'Y' : Transicion( accion_pila = Push(valor="X")   , destino = "q1"), 'W' : Transicion( accion_pila = Push(valor="X")   , destino = "q1"), }, "[" : { 'z0' : Transicion( accion_pila = Push(valor="Y")   , destino = "q1"), 'Y' : Transicion( accion_pila = Push(valor="Y")   , destino = "q1"), 'X' : Transicion( accion_pila = Push(valor="Y")   , destino = "q1"),
                    'W' : Transicion( accion_pila = Push(valor="Y")   , destino = "q1"),
                },
            "{" : { 
                    'z0' : Transicion( accion_pila = Push(valor="W")   , destino = "q1"),
                    'Y' : Transicion( accion_pila = Push(valor="W")   , destino = "q1"),
                    'X' : Transicion( accion_pila = Push(valor="W")   , destino = "q1"),
                    'W' : Transicion( accion_pila = Push(valor="W")   , destino = "q1"),
                },

            ")" : {
                'X':Transicion( accion_pila = Pop() , destino = "q2"),
                },
            "]" : {
                'Y':Transicion( accion_pila = Pop() , destino = "q2"),
                },
            "}" : {
                'W':Transicion( accion_pila = Pop() , destino = "q2"),
                },

            EPSILON : None
            },
        "q2" : {
            ")" : {
                'X': Transicion(accion_pila = Pop() , destino = "q2"),
                },
            "]" : {
                'Y': Transicion(accion_pila = Pop() , destino = "q2"),
                },
            "}" : {
                'W': Transicion(accion_pila = Pop() , destino = "q2"),
                },

            "(" : {
                'X': Transicion(accion_pila = Push(valor="X") , destino = "q2"),
                'W': Transicion(accion_pila = Push(valor="X") , destino = "q2"),
                'Y': Transicion(accion_pila = Push(valor="X") , destino = "q2"),
                'z0': Transicion(accion_pila = Push(valor="X") , destino = "q2"),
                },
            "[" : {
                'W': Transicion(accion_pila = Push(valor="Y") , destino = "q2"),
                'X': Transicion(accion_pila = Push(valor="Y") , destino = "q2"),
                'Y': Transicion(accion_pila = Push(valor="Y") , destino = "q2"),
                'z0': Transicion(accion_pila = Push(valor="Y") , destino = "q2"),
                },
            "{" : {
                'W': Transicion(accion_pila = Push(valor="W") , destino = "q2"),
                'X': Transicion(accion_pila = Push(valor="W") , destino = "q2"),
                'Y': Transicion(accion_pila = Push(valor="W") , destino = "q2"),
                'z0': Transicion(accion_pila = Push(valor="W") , destino = "q2"),
                },

            EPSILON : {
                'z0': Transicion( accion_pila = Continue() , destino = "q3"),
                },
        },
        "q3" : {
            '(' : None,
            '[' : None,
            '{' : None,

            ')' : None,
            ']' : None,
            '}' : None,

            EPSILON : None
         },
    }
    dfa = AFDP(
            estados={"q1", "q2", "q3"},
            input_simbolos={"(", ")", "[", "]","{","}",""},
            transiciones=transiciones,
            alfabeto_pila={"X","Y","W", "z0"},
            estado_inicial="q1",
            estados_finales={"q3"},
            estado_inicial_pila = "z0" 
        )
    return list(dfa.lectura_paso_a_paso(s))
