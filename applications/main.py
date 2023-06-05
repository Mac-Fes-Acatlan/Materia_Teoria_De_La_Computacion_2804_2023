from tools.automata.afd import AFD

if __name__ == "__main__":

    print("\n---------------------- EJEMPLO AUTÓMATA FINITO DETERMINISTA ----------------------\n")
    dfa = AFD(
        estados={"q0", "q1", "q2"},
        input_simbolos={"0", "1"},
        transiciones={
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q0", "1": "q2"},
            "q2": {"0": "q2", "1": "q1"},
        },
        estado_inicial="q0",
        estados_finales={"q2"},
    )
    value = dfa.lectura_input("1")

