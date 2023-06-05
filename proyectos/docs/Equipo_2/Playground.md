<head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
</head>

## Probando el código

 
En este apartado puedes probar el codigo como si fuera un REPL de python, haciendo uso de [pyscript](https://pyscript.net/).

Presiona `Shift`+`Enter` para ejecutar el código, si exploras las herramientas de navegador puedes ver el archivo de python en la pestaña de sources.

<div id="py">
    <py-config>
        packages = ["dataclasses"]
    </py-config>
    <py-script src="http://localhost:8000/assets/equipo_2_pila.py"> </py-script>

    <py-repl output="output">
          test_parentesis('()()[]') # puedes escribir aqui
    </py-repl>
    <py-terminal></py-terminal>
    <div id="output"></div>
</div>
