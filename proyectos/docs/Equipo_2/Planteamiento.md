# Planteamiento

## Problema

En el desarrollo de editores de texto para programar(IDE), un _feature_ que es imprescindible es el balance de llaves, es decir que el editor indique cuando una llave esta cerrada o abierta.

```cpp
#include<iostream>
using namespace std;
int main() {
    for( int idx = ; idx < 12 ;idx++
                             ~~~~~~~^~~~~~
                            Error, missing parentheses
}
```
Por lo tanto el problema a tratar es validar una cadena que contenga multiple delimitadores :

    {} , (), []

Y saber si esa una cadena correcta.

Podemos definir entonces la validez de una cadena como :

1. Una cadena vacia es valida.

2. Si $X$ es una cadena valida entonces $(X)$, $\{X\}$, $[X]$, son cadenas validas

3. Si $X$ y $Y$ son cadenas validas entonces la concatenacion de $X$ y $Y$ es una cadena valida.

Ejemplos de cadenas valida:

    [{()}][()()()]
    [()()()()()]
    [{}{}{()()}]()

Ejemplo de cadenas invalidas :

    ()()()(
    [(){}](]
    ][][][
