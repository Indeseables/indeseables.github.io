---
layout: post
title: Lógica difusa y fuzzy clustering.
comments: True
author: Overxfl0w13
tags: [Aprendizaje automático,Inteligencia artificial]
---

¿Cómo determinamos si una persona es alta o baja? ¿y si la temperatura resulta fria, agradable o caliente? ¿y si algo es barato o caro?. Lo normal en estos casos, cuando no se conoce la lógica difusa que trataremos en esta entrada, es pensar en separarlo mediante rangos perfectamente delimitados. Pero esto no es lo más adecuado y de hecho, no es lo que más se ajusta al mundo real como veremos.

___

### Lógica difusa

La lógica difusa (fuzzy logic) nos permite lidiar con cualquier tipo de información imprecisa e.g. datos conocidos aproximadamente, precisión en las medidas, etc

Un caso particular de este tipo de lógica son los conjuntos difusos (Zadeh, 1979). 
La diferencia entre los [conjuntos clásicos](https://es.wikipedia.org/wiki/Conjunto) y los [conjuntos difusos](https://es.wikipedia.org/wiki/Conjunto_difuso) radica en la forma de afirmar si un elemento pertenece a un conjunto. Más concretamente:

* Conjuntos clásicos: un elemento pertenece, o no pertenece a un conjunto.
    * Predicado de pertenencia  ![](https://latex.codecogs.com/gif.latex?P%28x%29%3AU%5Crightarrow%20%5Cleft%20%5C%7B%200%2C1%20%5Cright%20%5C%7D)
* Conjuntos difusos: un elemento pertenece en mayor o menor medida a un conjunto (la frontera de los cojuntos es [difusa](https://gyazo.com/4c1133e4a1fd294ac558ac13efa37e22).
   * Función de pertenencia  ![](https://latex.codecogs.com/gif.latex?%5Cmu%20_%7BA%7D%3AU%5Crightarrow%20%5B0%2C1%5D)

Para ver un caso más claro, tomaremos el ejemplo de la estatura mencionado al principio de la entrada. Si lo dividimos de la forma trivial usando rangos bien delimitados, podríamos considerar algo así:

* [-inf,1.60]  : **Baja**
* [1.61,1.75] : **Media**
* [1.75,inf] : **Alta**

Realmente, si una persona que mide 1.75 crece 1cm, ¿pasa a ser alta de repente?. Podemos considerar que dicha persona tiene una posibilidad de pertenencia a **Baja** de 0.25 , a **Media** de 0.9 y a **Alta** de 0.25 (hay que tener presente que se habla de posibilidades de pertenencia no de probabilidades - los conjuntos difusos inducen una distribución de posibilidades -, de ello se encarga el [razonamiento probabilístico](https://ccc.inaoep.mx/~jagonzalez/AI/Sesion12_RazonamientoProbabilistico.pdf)). 

Estas funciones de pertenencia se suelen especificar mediante funciones **f** que se ajusten a trapecios (no tienen porque ser únicamente trapecios), definiendo cada una de estas funciones un conjunto difuso - partición -. ([Ejemplo](https://i.gyazo.com/c961a07b07d23d37079537d282c55a13.png)).
Deben cumplir 2 propiedades: 

* Completitud: garantizar que ningún valor quede excluido de todas las particiones fuzzy, por lo que dado cualquier elemento del universo **U** empleado, su posibilidad de pertenencia debe ser >0 en alguna de las particiones.

* Partición fuerte: la suma de las funciones de pertenencia de un elemento de **U** en cada una de las particiones es 1.

También es posible modificar las funciones de pertenencia para tener en cuenta conceptos más complejos modificando los valores difusos e.g. X es extremadamente A, X es más o menos A, etc. Estos modificadores se denominan modificadores linguísticos y existen estándares para su definición. Algunos ejemplos son [éstos](https://i.gyazo.com/2059ec8733b503452b6a12323c251203.png).

Del mismo modo que sobre los conjuntos clásicos hay definidas una serie de operaciones, también las hay en los conjuntos difusos, dados 2 conjuntos difusos A y B, se definen:

* Igualdad de conjuntos (A=B): decimos que 2 conjuntos A y B son iguales cuando para todo elemento **x** del universo **U** las funciones de pertenencia de **x** en ambos vale lo mismo ![](https://i.gyazo.com/2e66f0a8a5a494eaff16e92e2d97c7d2.png)

* Complemento: El complementario de un elemento **x** en un conjunto difuso A es 1 - la función de pertenencia de **x** al conjunto A  ![](https://i.gyazo.com/550c75653c1fb003ab9006f1bed7de6d.png)

* Inclusión (A contenido en B): Decimos que A está contenido en B cuando para todo elemento **x** del universo **U** la función de pertenencia de **x** en A es menor o igual que la función de pertenencia de **x** en B  ![](https://i.gyazo.com/342cae7269a1a990dfe27a1c18fe7ea2.png)

* Intersección (A intersección B): ![](https://i.gyazo.com/4128013c2e3da71ec1d30e6bcc9c837f.png)

* Unión (A unión B): ![](https://i.gyazo.com/479b2cb008bbd3c22b314af3e27df039.png)

También se definen operaciones aritméticas como: suma, resta, multiplicación y división, que no comentaremos en esta entrada porque no nos serán de utilidad para el caso páctico de [clustering difuso](https://es.wikipedia.org/wiki/Fuzzy_clustering), tampoco veremos otros aspectos clave como el proceso de [inferencia difusa](https://i.gyazo.com/69ed756e0cd1fa1278d0fdb11ebb3fd2.png) aplicando reglas y hechos difusos por el mismo motivo, sin embargo, es muy posible que comente en próximas entradas todos esos aspectos.

Por último, destacar que este tipo de métodos está muy extendido y son muchos los [dispositivos y aplicaciones](https://i.gyazo.com/a6941f428a90b7fdc918826383f13274.png) que hacen uso de dichos métodos, algunos de ellos son:

* Control de spam (Mozilla)
* Cámara autofoco (Canon)
* Control de frenado
* Acondicionador de aire doméstico (Mitsubishi)
* Aprendizaje automático (e.g. clustering difuso)

___

### Fuzzy clustering

[TODO]

___

{% include twitter_plug.html %}

___
