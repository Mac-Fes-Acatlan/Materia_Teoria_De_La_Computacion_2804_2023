# Validación del Orden del RFC
### Descripción
El proyecto "Autómatas Finitos Deterministas para Validar el Orden de un RFC" tiene como objetivo verificar si el orden de un Registro Federal de Contribuyentes (RFC) es correcto.

### Ejemplos
#### Ejemplo 1: Orden Correcto
RFC: AUCL940808KC1
Resultado esperado: Correcto
En este ejemplo, se proporciona un RFC válido con el orden correcto. Se espera que el programa indique que el orden del RFC es correcto.
![True](https://i.ibb.co/QM4FjCT/0c38b1db-5a59-4fa1-91b9-83ba4b6d06df.png "True")


### Ejemplo 2: Orden Incorrecto
#### RFC: 940808KC1AUCL
Resultado esperado: Incorrecto
En este ejemplo, se proporciona un RFC con un orden incorrecto. Se espera que el programa detecte que el orden del RFC no es válido y lo marque como incorrecto.
![False](https://i.ibb.co/HzZ1gRr/e73ac9b0-67a2-4da3-81cc-351ce7d53d53.png "False")

#####  Instrucciones de Uso Instrucciones de Uso
Clona el repositorio del proyecto desde [enlace al repositorio].
Abre el archivo [nombre del archivo].py en tu entorno de desarrollo de Python.
Ejecuta el código en tu intérprete de Python para iniciar el programa.
Ingresa el RFC que deseas validar.
Observa el resultado en la salida del programa, que indicará si el orden del RFC es correcto o incorrecto.