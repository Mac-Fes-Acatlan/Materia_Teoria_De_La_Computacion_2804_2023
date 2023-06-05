# Definiciones

Definición

Un autómata finito determinista (AFD) es un modelo matemático que representa un sistema que se mueve entre diferentes estados en respuesta a una serie de entradas. Tiene estados, transiciones y reglas deterministas para cambiar de estado. Se inicia en un estado inicial y puede tener estados de aceptación. No hay ambigüedad ni elección en las transiciones. Es una forma de representar sistemas que siguen un conjunto de reglas fijas y predecibles.


## Definición Matemática

Un AFD se define formalmente como una 5-tupla (Q, Σ, δ, q₀, F), donde:

- Q es un conjunto finito de estados.
- Σ es un conjunto finito de símbolos de entrada, llamado alfabeto.
- δ: Q x Σ -> Q es una función de transición que mapea un estado y un símbolo de entrada a otro estado.
- q₀ ∈ Q es el estado inicial.
- F ⊆ Q es un conjunto de estados finales o de aceptación.


## Definición del autómata aplicado a email

Implementamos un autómata finito determinista (AFD) que verifica si una cadena de caracteres (email) cumple con ciertas reglas para ser considerada una dirección de correo electrónico válida.

En términos matemáticos, el autómata se puede definir como una 5-tupla (Q, Σ, δ, q₀, F), donde:

- Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q6'} es el conjunto de estados del autómata.
- Σ es el conjunto de símbolos de entrada, que en este caso corresponde a los caracteres individuales de la cadena de email, que pueden ser {a...z, A...Z, 0...9, _}.
- δ: Q x Σ -> Q es la función de transición que especifica cómo el autómata cambia de estado en respuesta a un símbolo de entrada.
- q₀ = 'q0' es el estado inicial del autómata.
- F = {'q5', 'q6'} es el conjunto de estados de aceptación o finales del autómata.


<p>La función de transición, implementada en el método <code>transicion</code>, establece las reglas para cambiar de estado según el estado actual y el símbolo de entrada. A continuación, se presentan las reglas de transición del autómata:</p>

<ol>
    <li>
        Si el estado actual es 'q0':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata pasa al estado 'q1'.</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
    <li>
        Si el estado actual es 'q1':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata permanece en el estado 'q1'.</li>
            <li>Si el símbolo de entrada es '@', el autómata pasa al estado 'q2'.</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
</ol>

<ol start="3">
    <li>
        Si el estado actual es 'q2':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata pasa al estado 'q3'.</li>
            <li>Si el símbolo de entrada es '.', el autómata pasa al estado 'q6' (estado de error).</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
    <li>
        Si el estado actual es 'q3':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata permanece en el estado 'q3'.</li>
            <li>Si el símbolo de entrada es '.', el autómata pasa al estado 'q4'.</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
</ol>

<ol start="5">
    <li>
        Si el estado actual es 'q4':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata pasa al estado 'q5'.</li>
            <li>Si el símbolo de entrada es '.', el autómata pasa al estado 'q6' (estado de error).</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
    <li>
        Si el estado actual es 'q5':
        <ul>
            <li>Si el símbolo de entrada es alfanumérico o '_', el autómata permanece en el estado 'q5'.</li>
            <li>Si el símbolo de entrada es '.', el autómata pasa al estado 'q4'.</li>
            <li>De lo contrario, el autómata pasa al estado 'q6' (estado de error).</li>
        </ul>
    </li>
</ol>



