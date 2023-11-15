# ParcialMutantes
* Nombre y Apellido: Manuel Rodriguez Sasschetti
* Legajo: 51635
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

Luego se creo la función isMutant que recibe el array de strings como parametro. Adentro se crea a variable secuencias_encontradas que se utiliza para contar cuántas secuencias de cuatro letras iguales se encuentran en la cadena de ADN. Para que sea mutante se deben encontrar como minimo 2 cadenas de letras iguales. Tambien se implementa la variable letras_usadas que es un conjunto que almacena las letras que ya han sido utilizadas en alguna secuencia para evitar contar la misma letra en varias secuencias.

Se utiliza un bucle for para recorrer cada fila de la matriz dna y un bucle for anidado para iterar sobre las subcadenas de longitud 4 en cada fila buscando en secuencias horizontales, verticales y diagonales. Si se encuentran más de una secuencia, la función devuelve True, caso contrario, devuelve False.

## Casos de Prueba
Se realizan los siguientes casos de prueba para el correcto funcionamiento del codigo.
Para Correrlo al iniciar el Programa se te pedira que ingrese la fila nr1, nr2 , .....
Se puede copiar y pegar fila por fila en cada caso, o copiar directamente todos los Strings del caso, pegarlos en la consola y automaticamente corre.

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


Caso 5: Mutante
GTGCGA
CGGTAC
ATGAAT
AGAGAG
CCGGGA
TCACTG

```