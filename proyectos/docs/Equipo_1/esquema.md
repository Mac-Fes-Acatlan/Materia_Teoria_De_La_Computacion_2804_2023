#Esquema de funcionamiento

<div class=text-justify>
    El siguiente esquema es para dar a conocer el programa desde su funcionamiento como AFD, gunto con el grafico de transiciones para un mejor entendimiento:
</div>

1. **Alfabeto de entrada**: {A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

2. **Alfabeto de pila**: {A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, #}

3. **Conjunto de estados**:
    - Q0: Estado inicial
    - Q1, Q2, Q3, Q4: Estados de lectura de letras
    - Q5, Q6, Q7, Q8, Q9, Q10: Estados de lectura de números
    - Q11: Estado de aceptación
    - Q12: Estado de rechazo

4. **Reglas de transición**:
   a) Desde el estado Q0:
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q1 y se apila el símbolo leído.
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q12 (rechazo).

   b) Desde el estado Q1:
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q2 y se apila el símbolo leído.
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q12 (rechazo).

   c) Desde el estado Q2:
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q3 y se apila el símbolo leído.
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q12 (rechazo).

   d) Desde el estado Q3:
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q4 y se apila el símbolo leído.
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q12 (rechazo).

   e) Desde el estado Q4:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q5 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   f) Desde el estado Q5:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q6 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   g) Desde el estado Q6:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q7 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   h) Desde el estado Q7:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q8 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   i) Desde el estado Q8:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q9 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   j) Desde el estado Q9:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q10 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   k) Desde el estado Q10:
   - Si se lee un dígito (0, 1, ..., 9), se realiza una transición hacia el estado Q11 y se apila el símbolo leído.
   - Si se lee una letra (A, B, C, ..., Z), se realiza una transición hacia el estado Q12 (rechazo).

   l) Desde el estado Q11:
   - Cualquier símbolo leído se consume sin hacer transición.

   m) Desde el estado Q12:
   - Cualquier símbolo leído se consume sin hacer transición.


![Esquema](img/AFD-RFC.png)
