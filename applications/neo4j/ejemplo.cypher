CREATE ( S:SimboloInicial
        {
          name: "Simbolo S"
        })

CREATE ( S_copy:SimboloNoTerminal
        {
          name: "Simbolo S"
        })

CREATE ( A_uno:SimboloNoTerminal
        {
          name: "Simbolo A uno"
        })


CREATE ( A_dos:SimboloNoTerminal
        {
          name: "Simbolo A dos"
        })


CREATE ( B:SimboloNoTerminal
        {
          name: "Simbolo B"
        })

CREATE ( a:SimboloTerminal
        {
          name: "Simbolo a"
        })

CREATE ( b:SimboloTerminal
        {
          name: "Simbolo b"
        })

CREATE ( c:SimboloTerminal
        {
          name: "Simbolo c"
        })

CREATE ( d:SimboloTerminal
        {
          name: "Simbolo d"
        })


MATCH (a:SimboloInicial), (b:SimboloNoTerminal)
WHERE a.name = "Simbolo S" 
AND b.name = "Simbolo A uno"
CREATE (a)-[deriv_uno:DERIVACION]->(b)


MATCH (a:SimboloInicial), (b:SimboloNoTerminal)
WHERE a.name = "Simbolo S" 
AND b.name = "Simbolo B"
CREATE (a)-[deriv_uno:DERIVACION]->(b)


MATCH (a:SimboloInicial), (b:SimboloNoTerminal)
WHERE a.name = "Simbolo S" 
AND b.name = "Simbolo S"
CREATE (a)-[deriv_uno:DERIVACION]->(b)








