from tools.automata.afd_pila_equipo_2 import (
    AFDP,
    EPSILON,
    Transicion,
    Pop,
    Continue,
    Push,
)
from tools.base.excepciones import AutomataExcepcion


def test_parentesis():
    transiciones = {
        "q1": {
            "(": {
                "z0": Transicion(accion_pila=Push(valor="X"), destino="q1"),
                "X": Transicion(accion_pila=Push(valor="X"), destino="q1"),
                "Y": Transicion(accion_pila=Push(valor="X"), destino="q1"),
                "W": Transicion(accion_pila=Push(valor="X"), destino="q1"),
            },
            "[": {
                "z0": Transicion(accion_pila=Push(valor="Y"), destino="q1"),
                "Y": Transicion(accion_pila=Push(valor="Y"), destino="q1"),
                "X": Transicion(accion_pila=Push(valor="Y"), destino="q1"),
                "W": Transicion(accion_pila=Push(valor="Y"), destino="q1"),
            },
            "{": {
                "z0": Transicion(accion_pila=Push(valor="W"), destino="q1"),
                "Y": Transicion(accion_pila=Push(valor="W"), destino="q1"),
                "X": Transicion(accion_pila=Push(valor="W"), destino="q1"),
                "W": Transicion(accion_pila=Push(valor="W"), destino="q1"),
            },
            ")": {
                "X": Transicion(accion_pila=Pop(), destino="q2"),
            },
            "]": {
                "Y": Transicion(accion_pila=Pop(), destino="q2"),
            },
            "}": {
                "W": Transicion(accion_pila=Pop(), destino="q2"),
            },
            EPSILON: {
                "z0": Transicion(accion_pila=Continue(), destino="q1"),
            }
        },
        "q2": {
            ")": {
                "X": Transicion(accion_pila=Pop(), destino="q2"),
            },
            "]": {
                "Y": Transicion(accion_pila=Pop(), destino="q2"),
            },
            "}": {
                "W": Transicion(accion_pila=Pop(), destino="q2"),
            },
            "(": {
                "X": Transicion(accion_pila=Push(valor="X"), destino="q2"),
                "W": Transicion(accion_pila=Push(valor="X"), destino="q2"),
                "Y": Transicion(accion_pila=Push(valor="X"), destino="q2"),
                "z0": Transicion(accion_pila=Push(valor="X"), destino="q2"),
            },
            "[": {
                "W": Transicion(accion_pila=Push(valor="Y"), destino="q2"),
                "X": Transicion(accion_pila=Push(valor="Y"), destino="q2"),
                "Y": Transicion(accion_pila=Push(valor="Y"), destino="q2"),
                "z0": Transicion(accion_pila=Push(valor="Y"), destino="q2"),
            },
            "{": {
                "W": Transicion(accion_pila=Push(valor="W"), destino="q2"),
                "X": Transicion(accion_pila=Push(valor="W"), destino="q2"),
                "Y": Transicion(accion_pila=Push(valor="W"), destino="q2"),
                "z0": Transicion(accion_pila=Push(valor="W"), destino="q2"),
            },
            EPSILON: {
                "z0": Transicion(accion_pila=Continue(), destino="q3"),
            },
        },
        "q3": {
            "(": None,
            "[": None,
            "{": None,
            ")": None,
            "]": None,
            "}": None,
            EPSILON: None,
        },
    }
    dfa = AFDP(
        estados={"q1", "q2", "q3"},
        input_simbolos={"(", ")", "[", "]", "{", "}", ""},
        transiciones=transiciones,
        alfabeto_pila={"X", "Y", "W", "z0"},
        estado_inicial="q1",
        estados_finales={"q3","q1"},
        estado_inicial_pila="z0",
    )

    def is_balanced_str(s):
        try:
            _ = dfa.lectura_input(s)
            return True
        except AutomataExcepcion as e:
            print(str(e))
            return False

    assert is_balanced_str("()[]{{}}") == True
    assert is_balanced_str("{{}}[]") == True
    assert is_balanced_str("[()[[]]]") == True
    assert is_balanced_str("[(){[]}[[]]]") == True
    assert is_balanced_str("][][") == False
    assert is_balanced_str("]]]]") == False
    assert is_balanced_str("") == True


if __name__ == "__main__":
    test_parentesis()
