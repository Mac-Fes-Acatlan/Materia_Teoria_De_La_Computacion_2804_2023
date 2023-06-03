#Codigo principal
<div class=text-justify>
En esta parte es necesario importar la biblioteca AFD que se trato en la sección anterior para el correcto funcionamiento del Automata.
</div>

``` python
from tools.automata.afd import AFD
```
<div class=text-justify>
    Ahora se pide por teclado la cadena que sera procesada como tarjeta bancaría y se verifica que esta sea valida.

</div>

``` python
print("\nDeterminara si la tarjeta ingresada consiste en una tarjeta MasterCard, Visa o AMEX si es expedida en México \n")

tarjeta = input("Ingrese el número de la tarjeta\n")

while(tarjeta.isdigit() == False or (len(tarjeta) !=16 and len(tarjeta)!=15)):   #Se encarga de verificar que la tarjeta cumpla con los digitos
    tarjeta = input("Ingrese el número de la taarjeta valido\n")

```
<div class=text-justify>
    Se crea el AFD
</div>

``` python
valida_tarjeta = AFD(   #Creamos el automata para verificar las cadenas
    estados={'q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','e1','e2','e3'},
    input_simbolos={'0','1','2','3','4','5','6','7','8','9'},
    transiciones={
        'q0':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'q10' , '5':'q8' , '6':'e1' ,'7':'e1' ,'8':'e1' ,'9':'e1'},
        'q1':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'e1' , '5':'e1' , '6':'e1' ,'7':'q2' ,'8':'e1' ,'9':'e1' },
        'q2':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'e1' , '5':'e1' , '6':'q3' ,'7':'e1' ,'8':'e1' ,'9':'e1' },
        'q3':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'e1' , '5':'q4' , '6':'e1' ,'7':'q6' ,'8':'e1' ,'9':'e1' },
        'q4':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'e1' , '5':'e1' , '6':'q5' ,'7':'q5' ,'8':'q5' ,'9':'q5' },
        'q5':{'0':'q5' ,'1':'q5' ,'2':'q5' ,'3':'q5' ,'4':'q5' , '5':'q5' , '6':'q5' ,'7':'q5' ,'8':'q5' ,'9':'q5' },
        'q6':{'0':'e2' ,'1':'q7' ,'2':'e2' ,'3':'e2' ,'4':'e2' , '5':'e2' , '6':'e2' ,'7':'e2' ,'8':'e2' ,'9':'e2' },
        'q7':{'0':'e2' ,'1':'e2' ,'2':'e2' ,'3':'e2' ,'4':'e2' , '5':'e2' , '6':'e2' ,'7':'e2' ,'8':'e2' ,'9':'q5' },
        'q8':{'0':'e3' ,'1':'q9' ,'2':'q9' ,'3':'q9' ,'4':'q9' , '5':'q9' , '6':'e3' ,'7':'e3' ,'8':'e3' ,'9':'e3' },
        'q9':{'0':'q9' ,'1':'q9' ,'2':'q9' ,'3':'q9' ,'4':'q9' , '5':'q9' , '6':'q9' ,'7':'q9' ,'8':'q9' ,'9':'q9' },
        'q10':{'0':'q10' ,'1':'q10' ,'2':'q10' ,'3':'q10' ,'4':'q10' , '5':'q10' , '6':'q10' ,'7':'q10' ,'8':'q10' ,'9':'q10' },
        'e1':{'0':'e1' ,'1':'e1' ,'2':'e1' ,'3':'e1' ,'4':'e1' , '5':'e1' , '6':'e1' ,'7':'e1' ,'8':'e1' ,'9':'e1' },
        'e2':{'0':'e2' ,'1':'e2' ,'2':'e2' ,'3':'e2' ,'4':'e2' , '5':'e2' , '6':'e2' ,'7':'e2' ,'8':'e2' ,'9':'e2' },
        'e3':{'0':'e3' ,'1':'e3' ,'2':'e3' ,'3':'e3' ,'4':'e3' , '5':'e3' , '6':'e3' ,'7':'e3' ,'8':'e3' ,'9':'e3' },
    },
    estado_inicial='q0',
    estados_finales={'q5','q9','q10'}
    
)
``` 
<div class=text-justify>
    Se procesa la cadena y se da el resultado de que tipo es la cadena desplegando el mensaje correspondiente.
</div>

``` python
#Determina dependiendo de donde cayo que marca es la tarjeta
value = valida_tarjeta.lectura_input(tarjeta)
if value == 'q9':
    print("La tarjeta es Mastercard")
elif value == 'q10':
    print("La tarjeta es Visa")
elif value == 'q5':
    print("La tarjeta es AMEX")
else:
    print("tarjeta no valida")

``` 
<div class=text-justify>
    Nota: El AFD puede ser ampliado para poder determinar mas tarjetas que las presentadas en esta sección.
</div>
