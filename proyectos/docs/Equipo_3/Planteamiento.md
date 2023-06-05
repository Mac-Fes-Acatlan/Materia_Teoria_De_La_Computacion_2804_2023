#Reconocimiento de tarjetas de credito / debito con BIN (Número de Identificación Bancaria)
***
###Tarjetas Bancarias:
<div class=text-justify>

El número de tarjeta bancaria es el que se encuentra en las tarjetas de pago, en las tarjetas de crédito, en las tarjetas de débito, en las tarjetas de prepago, en las tarjetas de regalo y en otras tarjetas similares.

 Algunos emisores de tarjetas se refieren al número de tarjeta con el número de cuenta primario o PAN (primary account number). Tienen cierto niveles de estructura interna y comparten un esquema de numeración común. Los números de tarjetas bancarias se asignan de acuerdo con la norma ISO / IEC 7812. El número de tarjeta bancaria se limita a identificar la tarjeta, que luego se asocia electrónicamente, a través de la organización emisora, con uno de sus clientes y luego con la cuenta bancaria del cliente. En el caso de las tarjetas de tipo de valor almacenado, no existe una asociación necesaria con un cliente en particular. 
</div>
***

###La norma ISO / IEC 7812:
<div class=text-justify>

La identificación de emisores fue publicada por primera vez por la Organización Internacional de Normalización (ISO) en 1989. Es la norma internacional que especifica "Un sistema de numeración para la identificación de los emisores de tarjetas, el formato del número de identificación del emisor (IIN) y el número de cuenta principal (PAN) ".


Una manera de identificar la industría a la cual es perteneciente la tarjeta bancaría es fijandonos en el primer digito de esta y utilizar la siguiente tabla.

<br>
<br>
<br>
<br>

<center>
<style type="text/css">
.tg  {border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;margin:0px auto;}
.tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-ys1t{background-color:#ece1c3;border-color:inherit;color:#000000;text-align:center;vertical-align:top}
.tg .tg-u7fs{background-color:#ece1c3;color:#000000;text-align:center;vertical-align:top}
.tg .tg-4waw{background-color:#195e63;font-family:inherit;font-weight:bold;position:-webkit-sticky;position:sticky;
  text-align:center;top:-1px;vertical-align:top;will-change:transform}
.tg .tg-rqt1{background-color:#195e63;border-color:inherit;font-family:inherit;font-weight:bold;position:-webkit-sticky;
  position:sticky;text-align:center;top:-1px;vertical-align:top;will-change:transform}
.tg .tg-mmu5{background-color:#ece1c3;color:#000000;font-family:inherit;text-align:center;vertical-align:top}
.tg-sort-header::-moz-selection{background:0 0}
.tg-sort-header::selection{background:0 0}.tg-sort-header{cursor:pointer}
.tg-sort-header:after{content:'';float:right;margin-top:7px;border-width:0 5px 5px;border-style:solid;
  border-color:#404040 transparent;visibility:hidden}
.tg-sort-header:hover:after{visibility:visible}
.tg-sort-asc:after,.tg-sort-asc:hover:after,.tg-sort-desc:after{visibility:visible;opacity:.4}
.tg-sort-desc:after{border-bottom:none;border-width:5px 5px 0}@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
<div class="tg-wrap"><table id="tg-xzgC7" class="tg">
<thead>
  <tr>
    <th class="tg-4waw">Valor del primer digito</th>
    <th class="tg-rqt1">Categoría emisor</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-ys1t">0</td>
    <td class="tg-ys1t">ISO / TC 68 y otras asignaciones futuras de la industria</td>
  </tr>
  <tr>
    <td class="tg-ys1t">1</td>
    <td class="tg-ys1t">Aerolíneas</td>
  </tr>
  <tr>
    <td class="tg-ys1t">2</td>
    <td class="tg-ys1t">Aerolíneas y otras tareas futuras de la industria</td>
  </tr>
  <tr>
    <td class="tg-ys1t">3</td>
    <td class="tg-ys1t">Viajes, entretenimiento y bancario / financiero</td>
  </tr>
  <tr>
    <td class="tg-u7fs">4</td>
    <td class="tg-u7fs">Bancos y financiera</td>
  </tr>
  <tr>
    <td class="tg-u7fs">5</td>
    <td class="tg-u7fs">Bancos y financiera</td>
  </tr>
  <tr>
    <td class="tg-u7fs">6</td>
    <td class="tg-u7fs">Diseño de mercado y bancario / financiero</td>
  </tr>
  <tr>
    <td class="tg-u7fs">7</td>
    <td class="tg-u7fs">Petróleo y otras asignaciones de la industria futuras</td>
  </tr>
  <tr>
    <td class="tg-u7fs">8</td>
    <td class="tg-u7fs">Asistencia sanitaria, telecomunicaciones y otras asignaciones futuras de la industria</td>
  </tr>
  <tr>
    <td class="tg-u7fs">9</td>
    <td class="tg-mmu5">Trabajo Nacional</td>
  </tr>
</tbody>
</table></div>
<script charset="utf-8">var TGSort=window.TGSort||function(n){"use strict";function r(n){return n?n.length:0}function t(n,t,e,o=0){for(e=r(n);o<e;++o)t(n[o],o)}function e(n){return n.split("").reverse().join("")}function o(n){var e=n[0];return t(n,function(n){for(;!n.startsWith(e);)e=e.substring(0,r(e)-1)}),r(e)}function u(n,r,e=[]){return t(n,function(n){r(n)&&e.push(n)}),e}var a=parseFloat;function i(n,r){return function(t){var e="";return t.replace(n,function(n,t,o){return e=t.replace(r,"")+"."+(o||"").substring(1)}),a(e)}}var s=i(/^(?:\s*)([+-]?(?:\d+)(?:,\d{3})*)(\.\d*)?$/g,/,/g),c=i(/^(?:\s*)([+-]?(?:\d+)(?:\.\d{3})*)(,\d*)?$/g,/\./g);function f(n){var t=a(n);return!isNaN(t)&&r(""+t)+1>=r(n)?t:NaN}function d(n){var e=[],o=n;return t([f,s,c],function(u){var a=[],i=[];t(n,function(n,r){r=u(n),a.push(r),r||i.push(n)}),r(i)<r(o)&&(o=i,e=a)}),r(u(o,function(n){return n==o[0]}))==r(o)?e:[]}function v(n){if("TABLE"==n.nodeName){for(var a=function(r){var e,o,u=[],a=[];return function n(r,e){e(r),t(r.childNodes,function(r){n(r,e)})}(n,function(n){"TR"==(o=n.nodeName)?(e=[],u.push(e),a.push(n)):"TD"!=o&&"TH"!=o||e.push(n)}),[u,a]}(),i=a[0],s=a[1],c=r(i),f=c>1&&r(i[0])<r(i[1])?1:0,v=f+1,p=i[f],h=r(p),l=[],g=[],N=[],m=v;m<c;++m){for(var T=0;T<h;++T){r(g)<h&&g.push([]);var C=i[m][T],L=C.textContent||C.innerText||"";g[T].push(L.trim())}N.push(m-v)}t(p,function(n,t){l[t]=0;var a=n.classList;a.add("tg-sort-header"),n.addEventListener("click",function(){var n=l[t];!function(){for(var n=0;n<h;++n){var r=p[n].classList;r.remove("tg-sort-asc"),r.remove("tg-sort-desc"),l[n]=0}}(),(n=1==n?-1:+!n)&&a.add(n>0?"tg-sort-asc":"tg-sort-desc"),l[t]=n;var i,f=g[t],m=function(r,t){return n*f[r].localeCompare(f[t])||n*(r-t)},T=function(n){var t=d(n);if(!r(t)){var u=o(n),a=o(n.map(e));t=d(n.map(function(n){return n.substring(u,r(n)-a)}))}return t}(f);(r(T)||r(T=r(u(i=f.map(Date.parse),isNaN))?[]:i))&&(m=function(r,t){var e=T[r],o=T[t],u=isNaN(e),a=isNaN(o);return u&&a?0:u?-n:a?n:e>o?n:e<o?-n:n*(r-t)});var C,L=N.slice();L.sort(m);for(var E=v;E<c;++E)(C=s[E].parentNode).removeChild(s[E]);for(E=v;E<c;++E)C.appendChild(s[v+L[E-v]])})})}}n.addEventListener("DOMContentLoaded",function(){for(var t=n.getElementsByClassName("tg"),e=0;e<r(t);++e)try{v(t[e])}catch(n){}})}(document)</script>
</center>

</div>
***
!!! Question "¿Para que nos es útil conocer como identificar una tarjeta bancaria?"
    La utilidad de evitar falsificaciones de tarjetas bancarias comprobando correctamente el banco del que supuestamente son emitidas, reconocer si cierta tarjeta puede ser aceptada por un establecimiento o también podría ser útil para identificar el publico objetivo de promociones especiales, como una tarjeta de credito que ofrezca promociones sobre viajes cuando el cliente use una tarjeta emitida por el sector de aerolineas.

***
<center>
!!! Question "Identificación de tarjetas bancarias"

    ![texto alternativo](img/IdentificarTarjetas.jpg) 
</center>

