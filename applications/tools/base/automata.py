import abc

import tools.base.excepciones as excepciones


class Automata(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def lectura_paso_a_paso(self, input_str: str):
        raise NotImplementedError

    def lectura_input(self, input_str):

        validacion_generada = self.lectura_paso_a_paso(input_str)
        for config in validacion_generada:
            pass
        return config

    def _validacion_estado_inicial(self):

        if self.estado_incial not in self.transiciones:
            raise excepciones.EstadoInicialError(
                "El estado inicial no se tiene determinado en la funcion de transición"
            )

    def _validacion_estados_finales(self):

        estados_invalidos = self.estados_finales - self.estados
        if estados_invalidos:
            raise excepciones.EstadosFinalesError(
                "El estado final , no es elemento del conjunto de estados "
            )
