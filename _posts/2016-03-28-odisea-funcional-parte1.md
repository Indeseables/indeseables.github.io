---
layout: post
title: Odisea Funcional (Parte 1)
comments: True
---


Un título muy acertado pues estudiar el paradigma funcional es cuanto menos una odisea, **preciosa o no dependiendo de a quíen preguntes.**  

Me apoyaré en apuntes de la universidad en la que estudio, luego el lenguaje utilizado será el mismo, **C#, funcional no puro**, pero trataré de comentar **diferencias con un funcional puro como Haskell** para que se entiendan mejor los conceptos estudiados.

**Se pretende** que en esta odisea naveguemos entre los siguientos puntos:  
* **Cálculo lambda**
* **Funciones como entidades de primer orden**
* Cláusulas  
* Currificación  
* Aplicación Parcial  
* Continuaciones  
* Evaluación Perezosa  
* Transparencia Referencial  
* Pattern Matching  
* Funciones de Orden Superior  
* Listas por comprensión  

Recalco el ***"Se pretende"*** porque no estoy seguro de si podre escribir sobre todo sin que me demoré demasiado, el motivo principal de escribir esta odisea es que me sirva a la vez de estudio.

En esta primera parte se estudiará el contenido ***más teorico*** puesto que abarca una introducción a la programación funcional y un breve estudio de la base desde la que empezó todo, el **lambda cálculo**

**PD**: Intentaré que esta primera parte sea lo menos aburrida posible, pero no hay todo sin nada, y en este caso el contenido que leereis será prácticamente una copia, síntesis o como lo queráis llamar de los apuntes de mi universidad. (Que por cierto, no se si puedo adjuntar en formato PDF al final del post, por lo que por si acaso no se me permite, no lo haré)

## ¿Qué es el paradigma funcional?
> Paradigma declarativo basado en la utilización de funciones que manejan **datos inmutables**
* Los datos nunca se modifican
* En lugar de cambiar un dato, se llama a una función que devuelve el dato modificado sin modificar el original

> Un programa se define mediante un conjunto de funciones invocándose entre sí  
* Las funciones no generan efectos secundarios
* El valor de una expresión depende únicamente de los valores de los parámetros
* (Devolviendo siempre el mismo valor en función de éstos -> Paradigma funcional puro)

## Lambda cálculo o cálculo lambda
> Es un sistema formal basado en la definición de funciones (abstracción) y su aplicación (invocación), origen de la programación funcional cuando fue definido por **Church y Kleene** alla por los años 30.

* Hace uso exhaustivo de la recursión
* Se considera el lenguaje más pequeño universal de computación
* ***Frecuentemente utilizado por investigadores y diseñadores de lenguajes***

### Expresiones lambda
Se definen como:
* Una abstracción lambda ***λx.M (M, N, M1, M2, ...)***
donde **x** es una **variable/parámetro**, y **M** es una **λ-expresión/cuerpo de la función**
* Una aplicación **M N** , donde **M y N son λ-expresiones**

Ejemplos de abstracciones:
* Función identidad **f(x) = x** puede representarse como: **λx.x**
* Función doble g(x) = x+x puede representarse como: **λx.x+x**

*PD: No tendría que ser necesario decir que el símbolo "+" podría escribirse en código lambda, pero con fines académicos vamos a considerar las operaciones básicas como "disponibles" en nuestro "intérprete de lambda cálculo"*

### Reducción-β ó Aplicación
La aplicación representa su invocación ( la de la función ) y se define del siguiente modo:
* ```(λx.M)N -> M[x:=N]   (o M[N/x])```

Donde X es la variable, M y N son las λ-expresiones y **M[x:=N] (o M[N/x]) representa la expresión lambda M, donde todas las x son sustituidas por la expresión lambda N.**

**A esta sustitución se le denomina reducción-β**, uds. más que nadie deben saber que el mundo de la ciencia esta rodeado por terminología confusa para de alguna manera espantar al que no se atreva a leer un párrafo entero.

Ejemplos:
* ```(λx.x + x)3 -> 3 + 3```
* ```(λx.x) λy.y*2 -> λy.y*2```

### Teorema de Church-Rosser
> Establece que el orden en el que se apliquen estas reducciones no afecta al resultado final
* ``` (λx.x)(λy.y*2)3 -> (λy.y*2)3  -> 3*2 ```
* ``` (λx.x)(λy.y*2)3 -> (λx.x)(3*2) -> 3*2 ```

De modo que los paréntesis son usados normalmente para **delimitar términos lambda**  
Por ejemplo: ``` (λx.x)(λy.y) ```  
Al evaluarse ```(λy.y)``` se reduce, esto podría explicarse de manera muy coloquial: el resultado de la función se aplica como parámetro a otra función y realmente queda reducida a una sola.

Sin embargo: ```λx.xλy.y``` es una sola abstracción (función)  

### Variables libres y ligadas
Sea una abstracción ```λx.xy``` se dice que:
* > ```x``` esta **ligada**
* > ```y``` es **libre**

En una ***reducción-β*** ó ***sustitución*** sólo se sustituyen las variables libres  
```(λx.x(λx.2+x)y)M``` **→**  ```x(λx.2+x)y[x:=M] = M(λx.2+x)y```

El que sea la primera vez que lea sobre lambda cálculo y pueda leer esta línea sin llorar por dentro, bravo, pero normalmente y por experiencia propia, suele pasar que crees entender como lo hiciste y cuando se te da el problema sin la solución no estas tan seguro de lo que estas haciendo.

[Añadir explicación paso a paso de la reducción]

Para evitar estos conflictos en las reducciones se creó la **conversión-α**  
* Todas las apariciones de una variable **ligada** en una misma abstracción se pueden renombrar a una **nueva** variable
* Incapié en **nueva**, ```funcional = variables inmutables```

``` (λx.x(λx.2+x)y)M == (λx.x(λz.2+z)y)M → x(λz.2+z)y[x:=M] = M(λz.2+z)y  ```  
 y si deseas, lo puedes volver a renombrar ``` ==  M(λx.2+x)y ```, ambas son soluciones válidas.
 
### conversión-α
* ```λx.xy == λz.zy```
* ```λx.xy != λy.yy```

Nótese la diferencia, ```y``` es una variable libre, no puede renombrarse:
> Todas las apariciones de una variable **ligada** en una misma abstracción se pueden renombrar a una **nueva** variable

* ```λx.2+x == λy.2+y```
* ```xy(λx.2+x) == xy(λz.2+z)```
* ...

## Isomorfismo Curry-Howard
Este apartado lo voy a saltar por alto, lo que si voy a hacer es dejaros el enlace a la Wikipedia y resumir un poco brevemente de lo que trata.  

Básicamente debeís saber que al igual que en **Ingeniería civil se fundamentan en el cálculo para hacer sus demostraciones**, en **Ingeniería del Software nos fundamentamos en la lógica** para hacer inferencia y demostraciones.

Por ejemplo:  
> **Verificación de programas**: demostrar que un programa es correcto conforme a una especificación:
* Un algoritmo de ordenación será correcto cuando se demuestre:  
1. `` Tras su invocación, todos los elementos están ordenados.``
2. `` Para cualquier entrada pasada al algoritmo (Infinitas).``
> El isomorfismo o correspondencia de Curry-Howard establece una **relación directa entre programas software y demostraciones matemáticas**

Para más información: [Wikipedia- Isomorfismo - Curry-Howard](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)


## Funciones, Entidades Primer Orden
> En **paradigma funcional**, las funciones son entidades de primer orden, esto significa que las **funciones son un tipo más**, pudiendose por ejemplo, instanciar variables de tipo función en estructuras de datos, pasarlas como parámetros o retornarlas.

### Funciones de orden superior
Se dice que una función es de orden superior si:
* recibe alguna función como parámetro
* retorna alguna función como resultado
* Y por conclusión, si recibe y retorna, ¿lógico no?

Por ejemplo, la función ``doble``: `λf.(λx.f(fx))` sería una función de orden superior.

En lenguajes funcionales puros como haskell, esto es nativo, todo son funciones, esto quiere decir que operadores como `` + - / ...`` son funciones infijas que curiosamente tambien pueden ser invocadas con [notación polaca inversa](https://es.wikipedia.org/wiki/Notaci%C3%B3n_polaca_inversa) ``+ 1 2`` = ``3``.

El problema viene en lenguajes que siguen muy a raja tabla el paradigma orientado a objetos (Veáse Java...), como instancias funciones?, en Java 8 ya se han implementados cosas de funcional pero sigue siendo un completo desastre.  

### Delegados
C# usa algo llamado **delegados**, los delegados son funciones que son **entidades de primer orden**. (al igual que las lambda-expresiones).

>Un delegado constituye un **tipo que representa un método** ya sea de instancia o de clase (``static``)

Un poco de código para entender el concepto:

```C#
public delegate int Comparacion(Persona p1, Persona p2);
```
Comparación es un método que recibe dos ``Persona`` y devuelve un ``ìnt``

Ahora por ejemplo, podriamos definir un método ``OrdenarPersonas`` independientemente del criterio de ordenación que se escoja.

```C#
static public void OrdenarPersonas(Persona[] vector, Comparacion comparacion){
    //... Iterando el vector ...
    if(comparacion(vector[i], vector[j]) > 0){
        Persona aux = vector[i];
        vector[i] = vector[j];
        vector[j] = aux;
    }
    //...
}
```

### Tipos de delegados predefinidos
> .Net tiene un conjunto de delegados predefinidos que hacen uso de la potencia de la **genericidad**

Los más utilizados son ``Func``, ``Action`` y ``Predicate``.
* > ``Func<T>``: Método sin parámetros que retorna un ``T``
* > ``Func<T1, T2>``: Método que recibe un parámetro ``T1`` y retorna un ``T2``
* > ``Action``: Método sin parámetros ni retorno
* > ``Action<T>``: Método con un parámetro ``T`` sin retorno
* > ``Predicate<T>``: Método que retorna un ``bool`` y recibe un ``T``

### Delegados Anónimos
> En la programación funcional es común **poder escribir la función en el momento de pasar ésta como parámetro**  

```C#
Persona[] personas = ListadoPersonas.CrearPersonasAleatorias();
Persona[] mayoresEdad = Array.FindAll(personas, 
                            delegate(Persona p) { return p.Edad >= 18; }
                        );
```

C# lanzó una buena solución al problema pero la sintaxis seguia siendo dificil de tratar, y por eso decidio implementar **expresiones lambda**, que básicamente mejoraban los **delegados anónimos**

### Expresiones lambda
> permiten **escribir el cuerpo de funciones completas como expresiones**

```C#
//El ejemplo de función de orden superior que veiamos antes
Func<Func<int, int>, int, int> dobleAplicacion = (f, n) => f(f(n));
Console.WriteLine(dobleAplicacion(n => n+n, 3));

//Convertimos el ejemplo de los delegados anónimos
Persona[] personas = ListadoPersonas.CrearPersonasAleatorias();
Persona[] mayoresEdad = Array.FindAll(personas, persona => persona.Edad >= 18);
```

En Haskell se utiliza esta sintaxis (Desde el intérprete):
```Haskell
-- DobleAplication de 3 -> 12
Prelude> (\f n -> f (f n)) (\x -> x+x) 3
12
```
Haskell tiene inferencia de tipos, pero tiene la característica de poder definir una cabecera con los tipos
```Haskell
factorial :: Integer -> Integer
factorial n = product [1..n]
```

### Bucles y Recursividad
Me imagino que ya os habreís pegado con el concepto de recursividad más veces, y en parte, como **C# es un lenguaje funcional no puro, puede usar estructuras de control de flujo iterativas cuando sea oportuno**, pero los **lenguajes puros como Haskell hacen uso exhaustivo de la recursión**

Por ejemplo, imaginate que los operadores: `if`-`then`-`else`, `=`, `-`, `*`los tenemos codificados en lambda cálculo y podemos usarlos.

> Función factorial en lambda cálculo:
`λf.λx. if x=0 or x=1 then 1 else x*f(x-1)`

Hay una función de orden superior muy conocida en haskell: `fix` ó **combinador de punto fijo** que suele ser muy utilizada y que podremos aplicar tambien en lambda cálculo si estuviera definida previamente.  
> `fix f -> f (fix f)`
* al aplicar `fix` a `f (fix f)`
    1. Se retorna f  
    2. Pasando una nueva invocación a `fix f` como primer parámetro
    

## Ejercicios para prácticar lo aprendido
* Aplica reducción y conversión a: `(λf.λx.f(fx))(λx.x+x)n`
* Usando funciones de orden superior, preferiblemente, usando lambda expresiones, construye tu propia "Calculadora funcional" con las operaciones básicas de : ``suma``, ``resta``, ``multiplicación`` y ``divisiòn``

## Soluciones
* Lambda cálculo - solución: [Github: Imágen](https://github.com/Indeseables/indeseables.github.io/blob/master/_codigos/entrada_funcional1/555df00550955abc13e4cec1400672c7.png)
* Calculadora funcional: [Github: Haskell](https://github.com/Indeseables/indeseables.github.io/blob/master/_codigos/entrada_funcional1/calculator.hs) [Github: C#](https://github.com/Indeseables/indeseables.github.io/blob/master/_codigos/entrada_funcional1/calculator.cs)

## Siguiente post
* **Cláusulas, Currificación y Aplicación Parcial**

## Referencias
* **Códigos de ejemplo y Teoria casi en su totalidad extraidos de las diapositivas de la Escuela de Ingeneria Informática de Uniovi**, **autor** según indícan las diapositivas: **Francisco Ortín Soler**
* Famoso libro de haskell : [Aprende Haskell](http://aprendehaskell.es)


## Autoría
Apuntes de Tecnología y Paradigmas de la programación escritos por: **Esteban Montes Morales**
* Perfil de Github: [Click para ir al sitio](http://github.com/sankosk)
* Twitter: @SankoSK
* Perfil de Linkedin: [Click para ir al sitio](https://www.linkedin.com/in/esteban-montes-morales-59257366)

___

{% include twitter_plug.html %}
