# ParcialMutantes
* Nombre y Apellido: Manuel Rodriguez
* Legajo: 
* Email: mln204manu@gmail.com
## De que va el proyecto

En este proyecto se pide que se realice una funcion que recibe un Array de strings que ingresa el usuario y se determine si la cadena de adn es mutante. Para esto tiene que cumplir ciertas consignas.
* Cada elemento del Array de Strings representa una fila de una tabla 6x6.
* Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.
* La longitud del String tiene que ser de 6 caracteres.
* La funcion que hay que programar es:
```
boolean isMutant(String[] dna);
```
* Esta funcion devuelve true  si encuentra MAS DE UNA SECUNCIA de cuatro letras iguales, de forma oblicua, horizontal o vertical

## Como se resolvio

En base a las consignas del proyecto primero se realiza la interfaz que le pide al usuario que vaya ingresando por consola cada fila.
Esta se logra con un bucle for para cargar 6 filas. Se agrega tambien un bucle while que verifique que se ingresen letras validas y que la longitud sea de 6 letras.

## Casos de Prueba
```
Caso 1: Mutante
ATGCGA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG

Caso 2: No Mutante
ATGCCA
CTGTGC
TTATGT
CGAAGG
CCACTA
TCAATG

Caso 3: No mutante
ATGCGA
CGGTGC
TTCTAT
AGAAGG
CCCTTA
TCACTG

Caso 4: Mutante
ATGCGA
AGGTGC
ATCTAT
AGAAGG
CCCCTA
TCACTG

```