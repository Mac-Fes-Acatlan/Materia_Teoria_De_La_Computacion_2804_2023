## Solución

Es posible resolver este problema usando un automata de pila, basta con designar un simbolo diferente en el lenguaje de la pila para cada delimitador, a continuación se detalla mas a fondo la solución.

Sea el AFD de pila:

1. $\Sigma = \{[, \{, (, ), \}, ], \epsilon \}$
2. $\Gamma = \{ X ,Y, W, z_0 \}$
3. $q_0 = q_0$
4. $Z_0 = z_0$
4. $F = \{q_3, q_1\}$

Con transiciones:

|  Transiciones             |||
| :----------------: | :------: | :----: |
| $\delta(q_1, (, Z_0) = ( q_1, XZ_0 )$          |  $\delta(q_2, (, Z_0) = ( q_2, XZ_0 )$             
| $\delta(q_1, (, X) = ( q_1, XX )$              |  $\delta(q_2, (, X) = ( q_2, XX )$                 
| $\delta(q_1, (, Y) = ( q_1, XY )$              |  $\delta(q_2, (, Y) = ( q_2, XY )$                 
| $\delta(q_1, (, W) = ( q_1, XW )$              |  $\delta(q_2, (, W) = ( q_2, XW )$                 
| $\delta(q_1, [, Z_0) = ( q_1, YZ_0 )$          |  $\delta(q_2, [, Z_0) = ( q_2, YZ_0 )$             
| $\delta(q_1, [, X) = ( q_1, YX )$              |  $\delta(q_2, [, X) = ( q_2, YX )$                 
| $\delta(q_1, [, Y) = ( q_1, YY )$              |  $\delta(q_2, [, Y) = ( q_2, YY )$                 
| $\delta(q_1, [, W) = ( q_1, YW )$              |  $\delta(q_2, [, W) = ( q_2, YW )$                 
| $\delta(q_1, \{, Z_0) = ( q_1, WZ_0 )$         |  $\delta(q_2, \{, Z_0) = ( q_2, WZ_0 )$            
| $\delta(q_1, \{, X) = ( q_1, WX )$             |  $\delta(q_2, \{, X) = ( q_2, WX )$                
| $\delta(q_1, \{, Y) = ( q_1, WY )$             |  $\delta(q_2, \{, Y) = ( q_2, WY )$                
| $\delta(q_1, \{, W) = ( q_1, WW )$             |  $\delta(q_2, \{, W) = ( q_2, WW )$                
| $\delta(q_1, ), X) = ( q_2, \epsilon )$        |  $\delta(q_2, ), X) = ( q_2, \epsilon )$           
| $\delta(q_1, ], Y) = ( q_2, \epsilon )$        |  $\delta(q_2, ], Y) = ( q_2, \epsilon )$           
| $\delta(q_1, \}, W) = ( q_2, \epsilon )$       |  $\delta(q_2, \}, W) = ( q_2, \epsilon )$          
| $\delta(q_1, \epsilon, W) = ( q_2, \epsilon )$ |  $\delta(q_2, \epsilon, z_0) = ( q_3, \epsilon )$    

Con grafo : 

![Transiciones](/assets/equipo_2_grafo.png){ align=left }

