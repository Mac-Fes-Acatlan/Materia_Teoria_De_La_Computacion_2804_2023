#Sobre Los Autómatas Finitos Deterministas

!!! Note ""
    Un AFD es una máquina que puede leer símbolos de un alfabeto y cambiar de estado según reglas predefinidas. Puede comenzar en un estado inicial, moverse de estado en estado y, al finalizar, puede llegar a un estado de aceptación indicando que ha reconocido una secuencia válida de símbolos.

    Definiendo esto podemos usar los AFD para determinar si una secuencia númerica como la de las tarjetas de credito expedidas por cierto banco es valido o no.

## Definiendo matemáticamente un AFD.


Definición: Un Autómata Finito Determinista (AFD) se define como una 5-tupla (Q, Σ, δ,  q₀, F), donde:

- Q es un conjunto finito de estados.
- Σ es un alfabeto finito de símbolos de entrada.
- δ es la función de transición, δ: Q x Σ → Q, que especifica la transición de un estado a otro dado un símbolo de entrada.
- q₀ es el estado inicial,  q₀ ∈ Q.
- F es un conjunto de estados de aceptación, F ⊆ Q.

## Definiendo un AFD de manera gráfica.

Un AFD puede ser definido por medio de un diagrama que exprese los saltos que hay entre sus estados, o una tabla de transiciones. A continuación se da el ejemplo de un AFD que acepta cadenas compuestas por números naturales (estas cadenas pueden ser vistas como números enteros positivos) y con sus transiciones determinará si este número entero positivo es divisible entre tres.
<br>
<br>
<br>
![transiciones](img/tabla_transiciones_divisible.png)
<br>
<center>
![entrada acab](img/diagrama_1.png)
</center>

## Propuesta de Automata Finito Determinista.

!!! Success "Requerimiento"
    En un establecimiento de comida solo es admitido los pagos con tarjeta de credito o debito si es que son emitidas por American Express, Visa o MasterCard ya que es un establecimiento muy exclusivo, el establecimiento solo puede aceptar pagos de American Express si esta fue expedida en México, mientras que para Visa o MasterCard no tiene ningun problema.
    <br>
    Es necesario crear un autómata finito determinista que sea capaz de determinar si una tarjeta entrante de 16 digitos es del grupo American Express y esta expedida en México o bien si es del grupo Visa o MasterCard.

### Lista de tarjetas aceptadas.

Consultando la siguiente pagina que filtra los codigos BIN'S por banco expedido y país de procedencía, encontramos la siguiente lista de codigos asignados a día de hoy para México que puede utilizar American Express.

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;margin:0px auto;}
.tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-5kiu{background-color:#ece1c3;border-color:inherit;color:#000000;font-family:inherit;text-align:center;vertical-align:top}
.tg .tg-2z80{background-color:#ece1c3;border-color:inherit;font-family:inherit;text-align:left;vertical-align:top}
.tg .tg-n715{background-color:#195e63;border-color:inherit;font-family:inherit;font-weight:bold;position:-webkit-sticky;
  position:sticky;text-align:left;top:-1px;vertical-align:top;will-change:transform}
.tg .tg-rqt1{background-color:#195e63;border-color:inherit;font-family:inherit;font-weight:bold;position:-webkit-sticky;
  position:sticky;text-align:center;top:-1px;vertical-align:top;will-change:transform}
.tg-sort-header::-moz-selection{background:0 0}
.tg-sort-header::selection{background:0 0}.tg-sort-header{cursor:pointer}
.tg-sort-header:after{content:'';float:right;margin-top:7px;border-width:0 5px 5px;border-style:solid;
  border-color:#404040 transparent;visibility:hidden}
.tg-sort-header:hover:after{visibility:visible}
.tg-sort-asc:after,.tg-sort-asc:hover:after,.tg-sort-desc:after{visibility:visible;opacity:.4}
.tg-sort-desc:after{border-bottom:none;border-width:5px 5px 0}@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table id="tg-yourt" class="tg">
<thead>
  <tr>
    <th class="tg-rqt1">Número Bin</th>
    <th class="tg-rqt1">País</th>
    <th class="tg-n715">Banco Emisor</th>
    <th class="tg-n715">Tipo de Tarjeta</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-5kiu">376560 - 376599</td>
    <td class="tg-5kiu">México</td>
    <td class="tg-2z80">AMERICAN EXPRESS</td>
    <td class="tg-2z80">CREDITO</td>
  </tr>
  <tr>
    <td class="tg-5kiu">376719 </td>
    <td class="tg-5kiu">México</td>
    <td class="tg-2z80">AMERICAN EXPRESS</td>
    <td class="tg-2z80">CREDITO</td>
  </tr>
</tbody>
</table></div>
<script charset="utf-8">var TGSort=window.TGSort||function(n){"use strict";function r(n){return n?n.length:0}function t(n,t,e,o=0){for(e=r(n);o<e;++o)t(n[o],o)}function e(n){return n.split("").reverse().join("")}function o(n){var e=n[0];return t(n,function(n){for(;!n.startsWith(e);)e=e.substring(0,r(e)-1)}),r(e)}function u(n,r,e=[]){return t(n,function(n){r(n)&&e.push(n)}),e}var a=parseFloat;function i(n,r){return function(t){var e="";return t.replace(n,function(n,t,o){return e=t.replace(r,"")+"."+(o||"").substring(1)}),a(e)}}var s=i(/^(?:\s*)([+-]?(?:\d+)(?:,\d{3})*)(\.\d*)?$/g,/,/g),c=i(/^(?:\s*)([+-]?(?:\d+)(?:\.\d{3})*)(,\d*)?$/g,/\./g);function f(n){var t=a(n);return!isNaN(t)&&r(""+t)+1>=r(n)?t:NaN}function d(n){var e=[],o=n;return t([f,s,c],function(u){var a=[],i=[];t(n,function(n,r){r=u(n),a.push(r),r||i.push(n)}),r(i)<r(o)&&(o=i,e=a)}),r(u(o,function(n){return n==o[0]}))==r(o)?e:[]}function v(n){if("TABLE"==n.nodeName){for(var a=function(r){var e,o,u=[],a=[];return function n(r,e){e(r),t(r.childNodes,function(r){n(r,e)})}(n,function(n){"TR"==(o=n.nodeName)?(e=[],u.push(e),a.push(n)):"TD"!=o&&"TH"!=o||e.push(n)}),[u,a]}(),i=a[0],s=a[1],c=r(i),f=c>1&&r(i[0])<r(i[1])?1:0,v=f+1,p=i[f],h=r(p),l=[],g=[],N=[],m=v;m<c;++m){for(var T=0;T<h;++T){r(g)<h&&g.push([]);var C=i[m][T],L=C.textContent||C.innerText||"";g[T].push(L.trim())}N.push(m-v)}t(p,function(n,t){l[t]=0;var a=n.classList;a.add("tg-sort-header"),n.addEventListener("click",function(){var n=l[t];!function(){for(var n=0;n<h;++n){var r=p[n].classList;r.remove("tg-sort-asc"),r.remove("tg-sort-desc"),l[n]=0}}(),(n=1==n?-1:+!n)&&a.add(n>0?"tg-sort-asc":"tg-sort-desc"),l[t]=n;var i,f=g[t],m=function(r,t){return n*f[r].localeCompare(f[t])||n*(r-t)},T=function(n){var t=d(n);if(!r(t)){var u=o(n),a=o(n.map(e));t=d(n.map(function(n){return n.substring(u,r(n)-a)}))}return t}(f);(r(T)||r(T=r(u(i=f.map(Date.parse),isNaN))?[]:i))&&(m=function(r,t){var e=T[r],o=T[t],u=isNaN(e),a=isNaN(o);return u&&a?0:u?-n:a?n:e>o?n:e<o?-n:n*(r-t)});var C,L=N.slice();L.sort(m);for(var E=v;E<c;++E)(C=s[E].parentNode).removeChild(s[E]);for(E=v;E<c;++E)C.appendChild(s[v+L[E-v]])})})}}n.addEventListener("DOMContentLoaded",function(){for(var t=n.getElementsByClassName("tg"),e=0;e<r(t);++e)try{v(t[e])}catch(n){}})}(document)</script>


[Bin Check Online](https://bincheck.io/es/mx/american-express)

!!! Note "" 

    Adicionalmente sabemos que las tarjetas mundialmente de Visa empiezan siempre por el digito __4__ mientras que las MasterCard empiezan por los digitos __51 - 55__.



### Definiendo el autómata finito determinista.
Podemos definir el automata finito determinista con los siguientes elementos:

- Q = {q<sub>0</sub>, q<sub>1</sub>, q<sub>2</sub>, q<sub>3</sub>, q<sub>4</sub>, q<sub>5</sub>, q<sub>6</sub>, q<sub>7</sub>, q<sub>8</sub>, q<sub>9</sub>, q<sub>10</sub>, e<sub>1</sub>, e<sub>2</sub>, e<sub>3</sub>}.
- Σ = {0,1,2,3,4,5,6,7,8,9}
- q<sub>0</sub> es el estado inicial donde q<sub>0</sub> ∈ Q.
- F = {q<sub>5</sub>, q<sub>9</sub>, q<sub>10</sub>} es un conjunto de estados de aceptación, F ⊆ Q.

Damos su función de transcisión de una manera tabular como mostramos arriba de la siguiente forma:
<style type="text/css">
.tg  {border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;margin:0px auto;}
.tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-fwci{background-color:#ece1c3;border-color:inherit;font-family:inherit;text-align:center;vertical-align:top}
.tg .tg-v1t9{background-color:#195e63;border-color:inherit;color:#ffffff;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-5kiu{background-color:#ece1c3;border-color:inherit;color:#000000;font-family:inherit;text-align:center;vertical-align:top}
.tg .tg-jqsm{background-color:#ECE1C3;border-color:inherit;color:#000000;font-family:inherit;text-align:center;vertical-align:top}
.tg .tg-w0xu{background-color:#ECE1C3;border-color:inherit;font-family:inherit;text-align:center;vertical-align:top}
.tg .tg-rqt1{background-color:#195e63;border-color:inherit;font-family:inherit;font-weight:bold;position:-webkit-sticky;
  position:sticky;text-align:center;top:-1px;vertical-align:top;will-change:transform}
.tg .tg-mnbu{background-color:#195e63;border-color:inherit;font-weight:bold;position:-webkit-sticky;position:sticky;
  text-align:center;top:-1px;vertical-align:top;will-change:transform}
.tg .tg-uwry{background-color:#195e63;border-color:inherit;color:#ffffff;font-family:inherit;font-weight:bold;text-align:center;
  vertical-align:top}
.tg .tg-popv{background-color:#ece1c3;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-9k4j{background-color:#ECE1C3;border-color:inherit;text-align:center;vertical-align:top}
.tg-sort-header::-moz-selection{background:0 0}
.tg-sort-header::selection{background:0 0}.tg-sort-header{cursor:pointer}
.tg-sort-header:after{content:'';float:right;margin-top:7px;border-width:0 5px 5px;border-style:solid;
  border-color:#404040 transparent;visibility:hidden}
.tg-sort-header:hover:after{visibility:visible}
.tg-sort-asc:after,.tg-sort-asc:hover:after,.tg-sort-desc:after{visibility:visible;opacity:.4}
.tg-sort-desc:after{border-bottom:none;border-width:5px 5px 0}@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table id="tg-IVwFI" class="tg">
<thead>
  <tr>
    <th class="tg-rqt1">Estado / Entrada</th>
    <th class="tg-rqt1">0</th>
    <th class="tg-rqt1">1</th>
    <th class="tg-rqt1">2</th>
    <th class="tg-mnbu">3</th>
    <th class="tg-mnbu">4</th>
    <th class="tg-mnbu">5</th>
    <th class="tg-mnbu">6</th>
    <th class="tg-mnbu">7</th>
    <th class="tg-mnbu">8</th>
    <th class="tg-mnbu">9</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-uwry">q<sub>0</sub></td>
    <td class="tg-5kiu">e<sub>1</sub></td>
    <td class="tg-fwci">e<sub>1</sub></td>
    <td class="tg-fwci">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>1</sub></td>
    <td class="tg-popv">q<sub>10</sub></td>
    <td class="tg-popv">q<sub>8</sub></td>
    <td class="tg-popv">e<sub>1</sub></td>
    <td class="tg-popv">e<sub>1</sub></td>
    <td class="tg-popv">e<sub>1</sub></td>
    <td class="tg-popv">e<sub>1</sub></td>
  </tr>
  <tr>
    <td class="tg-uwry">q<sub>1</sub></td>
    <td class="tg-jqsm">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>4</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>6</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>4</sub></td>
    <td class="tg-popv">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-9k4j">e<sub>1</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
    <td class="tg-9k4j">q<sub>5</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>6</sub></td>
    <td class="tg-popv">e<sub>2</sub></td>
    <td class="tg-popv">q<sub>7</sub></td>
    <td class="tg-popv">e<sub>2</sub></td>
    <td class="tg-popv">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>7</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-9k4j">e<sub>2</sub></td>
    <td class="tg-popv">q<sub>5</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>8</sub></td>
    <td class="tg-popv">e<sub>3</sub></td>
    <td class="tg-popv">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-popv">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
    <td class="tg-9k4j">q<sub>9</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">q<sub>10</sub></td>
    <td class="tg-popv">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
    <td class="tg-9k4j">q<sub>10</sub></td>
  </tr>
  <tr>
    <td class="tg-uwry">e<sub>1</sub></td>
    <td class="tg-fwci">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
    <td class="tg-w0xu">e<sub>1</sub></td>
  </tr>
  <tr>
    <td class="tg-uwry">e<sub>2</sub></td>
    <td class="tg-fwci">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
    <td class="tg-w0xu">e<sub>2</sub></td>
  </tr>
  <tr>
    <td class="tg-v1t9">e<sub>3</sub></td>
    <td class="tg-popv">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
    <td class="tg-9k4j">e<sub>3</sub></td>
  </tr>
</tbody>
</table></div>
<script charset="utf-8">var TGSort=window.TGSort||function(n){"use strict";function r(n){return n?n.length:0}function t(n,t,e,o=0){for(e=r(n);o<e;++o)t(n[o],o)}function e(n){return n.split("").reverse().join("")}function o(n){var e=n[0];return t(n,function(n){for(;!n.startsWith(e);)e=e.substring(0,r(e)-1)}),r(e)}function u(n,r,e=[]){return t(n,function(n){r(n)&&e.push(n)}),e}var a=parseFloat;function i(n,r){return function(t){var e="";return t.replace(n,function(n,t,o){return e=t.replace(r,"")+"."+(o||"").substring(1)}),a(e)}}var s=i(/^(?:\s*)([+-]?(?:\d+)(?:,\d{3})*)(\.\d*)?$/g,/,/g),c=i(/^(?:\s*)([+-]?(?:\d+)(?:\.\d{3})*)(,\d*)?$/g,/\./g);function f(n){var t=a(n);return!isNaN(t)&&r(""+t)+1>=r(n)?t:NaN}function d(n){var e=[],o=n;return t([f,s,c],function(u){var a=[],i=[];t(n,function(n,r){r=u(n),a.push(r),r||i.push(n)}),r(i)<r(o)&&(o=i,e=a)}),r(u(o,function(n){return n==o[0]}))==r(o)?e:[]}function v(n){if("TABLE"==n.nodeName){for(var a=function(r){var e,o,u=[],a=[];return function n(r,e){e(r),t(r.childNodes,function(r){n(r,e)})}(n,function(n){"TR"==(o=n.nodeName)?(e=[],u.push(e),a.push(n)):"TD"!=o&&"TH"!=o||e.push(n)}),[u,a]}(),i=a[0],s=a[1],c=r(i),f=c>1&&r(i[0])<r(i[1])?1:0,v=f+1,p=i[f],h=r(p),l=[],g=[],N=[],m=v;m<c;++m){for(var T=0;T<h;++T){r(g)<h&&g.push([]);var C=i[m][T],L=C.textContent||C.innerText||"";g[T].push(L.trim())}N.push(m-v)}t(p,function(n,t){l[t]=0;var a=n.classList;a.add("tg-sort-header"),n.addEventListener("click",function(){var n=l[t];!function(){for(var n=0;n<h;++n){var r=p[n].classList;r.remove("tg-sort-asc"),r.remove("tg-sort-desc"),l[n]=0}}(),(n=1==n?-1:+!n)&&a.add(n>0?"tg-sort-asc":"tg-sort-desc"),l[t]=n;var i,f=g[t],m=function(r,t){return n*f[r].localeCompare(f[t])||n*(r-t)},T=function(n){var t=d(n);if(!r(t)){var u=o(n),a=o(n.map(e));t=d(n.map(function(n){return n.substring(u,r(n)-a)}))}return t}(f);(r(T)||r(T=r(u(i=f.map(Date.parse),isNaN))?[]:i))&&(m=function(r,t){var e=T[r],o=T[t],u=isNaN(e),a=isNaN(o);return u&&a?0:u?-n:a?n:e>o?n:e<o?-n:n*(r-t)});var C,L=N.slice();L.sort(m);for(var E=v;E<c;++E)(C=s[E].parentNode).removeChild(s[E]);for(E=v;E<c;++E)C.appendChild(s[v+L[E-v]])})})}}n.addEventListener("DOMContentLoaded",function(){for(var t=n.getElementsByClassName("tg"),e=0;e<r(t);++e)try{v(t[e])}catch(n){}})}(document)</script>

Por ultimo podemos ver el AFD como un diagrama:
<center>

![transiciones diagrama](img/diagrama_2.png)

</center>




