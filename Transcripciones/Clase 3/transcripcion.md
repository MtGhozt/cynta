---
clase: "Clase 3"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1411551452.m4a
modelo: large-v3
idioma: es
duration_sec: 6223.0
---

## [00:00:02]

La vez pasada les decía que el en el paradigma lógico todo lo tratamos de describir con sentencias lógicas y en lugar de ejecutar cosas o de evaluar o sea de ejecutar instrucciones de evaluar funciones demostramos sentencias ok para hacer eso yo les decía hay varios requisitos. O sea, consta una cosa, nos estamos acercando a la programación de lógica desde un punto de vista muy formal.

## [00:00:54]

Entonces, es una forma bastante difícil de entender este paradigma, para ser honestos. La mayor parte de la gente entra más bien por otro lado, a saber, les enseñamos un lenguaje lógico como prologue. Y, este... medio les enseñamos cómo programar en Prolog y de ahí vamos hacia atrás. Pero como estamos hablando de los paradigmas y no de los lenguajes, entonces, y además, Prolog no es el único lenguaje lógico. Y para ser honestos con ustedes, hasta cierto punto, el paradigma lógico es un poquitito menos, podríamos decir, consolidado, que los otros paradigmas yo les explico si no en esta sesión en la próxima en que consiste esa sentencia que acabo de decir pero en todo caso decíamos que el paradigma lógico se fundamenta entonces en el cálculo de predicados del primer ángulo entonces la vez pasada lo que yo quería era traer a su mente lo que suponía yo que debieron haber

## [00:02:23]

aprendido debieron haberles enseñado más bien no me corrijo debieron haberles enseñado en el curso de este estructuras discretas a saber el lenguaje del cálculo de predicados de primer orden la destreza de simbolizar, o sea, de traducir oraciones de un lenguaje natural a el lenguaje del cálculo de predicados de primer orden Y después, asumiendo que ustedes conocen las reglas de inferencia, entonces pueden llevar a cabo demostraciones. Donde en este curso, por reglas de inferencia, estamos entendiendo el conjunto de veintitantas reglas de inferencia que dejó escritas Irving Coppe en su famosísimo libro de lógica simbólica donde este conjunto que están viendo es apenas el conjunto de las nueve reglas las que ya propiamente son reglas de inferencia las nueve reglas de inferencia las diez reglas de reemplazo o de sustitución a las cuales entonces aquí ya tenemos 19

## [00:05:00]

tenemos que sumarle las cuatro reglas de cuantificación y con eso ya tenemos 23 más las dos reglas de negación del cuantificador ya tenemos ahí 25 y podríamos agregar como hace copy estar agregando cuatro reglas adicionales para el manejo de la relación identidad o sea 29 reglas en total ok también la vez pasada hicimos un par de ejercicios de simbolización para refrescar todos estos conceptos hoy les voy a proponer uno más que ya nos mete ya en materia y disculpen voy a creo que me equivoqué de archivo con lo que quería enseñarles creo que estoy aquí ok para mantener un punto de referencia constante bueno, un punto de referencia si no fuera constante no sería punto de referencia, para mantener un punto de referencia vamos a trabajar otra vez más con nuestro sencillo, muy sencillo ejemplo del mínimo común múltiplo

## [00:07:55]

¿Cómo se vería en el paradigma lógico el cálculo del mínimo común múltiplo?

## [00:08:23]

Recordemos que el mínimo común múltiplo tenemos que calcularlo con, dados dos números enteros a y b, el mínimo como múltiplo lo estamos calculando como el producto de esos parámetros dividido entre el máximo común divisor de esos parámetros so far so good partíamos de aquí para ver en el paradigma imperativo hicimos tres versiones de este proceso de este cálculo una en Pascal otra en C y una más en COBOL pero lo que queríamos señalar en esta comparación de lenguajes no es tanto en lo mucho que se diferencian los lenguajes que tenemos aquí bueno Pascal y C no se diferencian tanto COBOL si se sale del canasto más bien lo que queríamos poner énfasis recordemos es en lo que se parecen en cómo hacemos la división en módulos y cada módulo es perfectamente programable en cualquiera de los tres y utilizando el mismo diseño y eso es lo que yo quiero recalcar utilizando el mismo diseño

## [00:10:04]

porque pertenecen al mismo paradigma bueno en el paradigma funcional tenemos que definir bueno definimos un máximo como un divisor de esta forma y ustedes saben que yo no tengo la menor idea de por qué no definir el mínimo como un múltiplo también como una función, bueno es que se parece al que habíamos visto antes pero bueno pongámoslo para hacer esto más completo aunque ya estaba en la forma de función más arriba esto recalca su carácter aquí ya de que estoy diseñando como una función este programa, bueno este algoritmo aunque esto es idéntico que teníamos arriba, no importa porque si no queda muy raro de esta función aquí sonta donde ahora el diseño de máximo común divisor lo hacemos como una función y me interesa que veamos esto porque, ¿cómo describimos esto usando lógica? ¿cómo describimos estas funciones usando cálculo de predicados del primer orden? es por ahí

## [00:12:03]

por donde tenemos que empezar este en este paradigma tenemos que empezar describiendo si ustedes quieren podemos verlo de esta forma en este caso que tenemos que evaluar una función en este caso entonces necesitamos describir la función que debemos evaluar mediante cálculo de predicados pongo entre paréntesis el que sea de primer orden porque en realidad diseñar un prolog de una manera como un lenguaje muy poderoso porque prolog puede manejar el cálculo de predicados de segundo orden inclusive otros lenguajes lógicos no tienen tanto poder pero prolog sí entonces por eso los paréntesis muy bien entonces por dónde tenemos que empezar hagámoslo de una manera similar a cómo estábamos simbolizando sentencias en lenguaje natural. ¿Cuál es el primer paso para simbolizar? Que dicho sea de paso, este es un paso, por así decirlo,

## [00:14:26]

que pertenece a un área muy específica de la lógica que se llama teoría de modelos.

## [00:14:36]

Hasta ahí vamos a ver de ese punto. ¿Por dónde empezamos? Por simbolizar, por encontrar, o sea, por simbolizar, no, disculpen, por encontrar una interpretación, por darnos una interpretación. Entonces, en primer lugar, debemos formular una interpretación. O sea, un conjunto de letras utilizando las convenciones del cálculo de predicados de primer orden que tienen una relación funcional con los objetos y situaciones del mundo que queremos describir. o con esta situación del mundo que queremos describir ok, nuestro mundo en este momento es la teoría de números o sea el ámbito de las sentencias matemáticas que podemos decir sobre el conjunto de los números enteros ok ok ¿qué deberíamos decir?

## [00:16:27]

¿en qué sentido? ¿cuál sería nuestra interpretación? Bueno, voy a empezar yo para darles un empujón.

## [00:16:44]

En este punto voy a ponerme muy estricto para acercarme más a la matemática que a la programación, para ser honesto con ustedes. Después vamos a poder tomarnos unas pequeñas libertades, pero por ahora vamos a ponernos estrictos. ZX significa X es un número entero ok, ¿qué más necesitamos?

## [00:17:37]

recuerden que lo que estamos tratando de simbolizar es esto entonces ¿cómo describiríamos con predicados esto? o bueno, los elementos importantes de estas sentencias Tenemos que definir MCD Calculo yo Tenemos que qué perdón Definir MCD Sí, cómo haríamos eso Bueno, es muy sencillo en realidad Este A mí se me ocurrió esta simbolización Bueno, esta interpretación MDXYZ Significa X Es el Este mínimo como un múltiplo de Y.

## [00:18:57]

Ya voy a poner esto para que se vea un poco más distinto.

## [00:19:13]

Tal vez así, para que se distinga un poquitito más.

## [00:19:24]

No se vea tan raro.

## [00:19:31]

Para distinguir la Y de la variable de la Y de la conjunción. Ok, entonces, ahora sí, creo que ustedes han llegado a la conclusión de que entonces el siguiente sería dyz, para decir que dx, yz, voy a darme esto para tanto, traerme todas las cosas que hay aquí, x es el máximo común divisor de yz. Ok, bueno, creo que ya tenemos todo lo necesario para nuestra interpretación Porque el cálculo de predicados de primer orden es un lenguaje que contempla funciones O sea, yo puedo tener funciones en el cálculo de predicados entonces las operaciones fundamentales suma, resta, multiplicación, división son funciones perdón y por lo tanto vamos a usarlos con los símbolos canónicos o sea la X para el producto la raya horizontal para la división vamos a ocupar un predicado especial vamos a ocupar el predicado de igualdad en su característica de que es verdad que estos dos objetos son idénticos

## [00:21:27]

pero ese es un predicado que ya podemos dar por estándar o sea, estamos usando el sistema extendido de copy entonces, dado eso no necesitamos más, muy bien, así que bueno, técnicamente ya podemos empezar ¿por dónde empezamos a describir lógicamente esto? bueno, aquí hay un detalle que ustedes no conocen y este bueno, es parte de su educación en el paradigma lógico y es una cosa, si el, si aquí se trata de demostrar cosas como hago para calcular algo verdad porque se supone que cuando yo demuestro algo es para saber si una sentencia que en la conclusión a donde yo quiero llegar es verdadera precisamente construyendo la demostración permítame por favor aclarar este punto que es muy muy importante El fundamento de la lógica y lo que nos ha permitido tener ciencia, tener tecnología, es un principio que se puede enunciar de una manera muy sencilla.

## [00:23:31]

Y por eso es impresionante que si este principio es tan sencillo, nos pueda dar un poder tan inmenso. Disculpen en esto, por favor, pero es que yo no puedo cansarme de admirarle y mostrarle mi admiración al hecho de que piénsenlo de esta forma. Piensen, en este momento hay tres telescopios, cada cual en grado que siente de poder, lanzados al espacio y de los cuales recibimos imágenes del espacio, del espacio profundo. el primero fue este ahí se me olvida el primero el que se lanzó el que en este momento que está ocupando el segundo punto de la grange es el James Webb y se acaba de lanzar otro telescopio espacial que también creo que va a estar en un punto de la grange y estos telescopios primero la tecnología para crear estos telescopios es extraordinariamente si este extraordinariamente sofisticada y no solo eso sino que estamos lanzando estos telescopios al espacio para darnos imágenes

## [00:25:19]

de de de objetos espaciales ah el Hubble el telescopio Hubble fue el primero y el que acaban de lanzar es el Nancy Grace Roman permítanme presentárselos de esta forma este ¿alguno de ustedes vio la película Interstellar?

## [00:26:00]

sí profe ok, gracias Matías bueno, no sé si lo sabes pero la imagen que se ve ahí en esa película del agujero negro sí, sí, Manuel, muy buena bueno, Andrés espero que esto no sea un spoiler muy feo la imagen del agujero negro que en la película le llaman Gargantúa este ellos creo que fue James Nolan Christopher Nolan Christopher Nolan muchas gracias te agradezco que me corrigieras creo que fue el director y como se ve un agujero negro que es uno de los puntos esenciales del argumento le preguntaron a un físico ganador del premio Nobel de Física en determinados aspectos de astronomía ¿cómo se vería según la teoría ¿cómo se vería un agujero enéreo si fotografiamos alguno? ok el mage hizo sus cálculos por cierto, este sujeto salió en Big Bang Theory hizo un cameo en la serie y Christopher Nolan él fue el asesor científico bueno, se vería así ¿y por qué se ve? ¿qué es ese? ¿por qué

## [00:27:39]

si se ve? ¿por qué hay un círculo de tan brillante alrededor de él? Ah, no, es que ese es el anillo de acreción del agujero negro que debería tener, o sea, que cuando está capturando materia y está demasiado cerca, pero no está en el horizonte de eventos La teoría dice, o sea, según la teoría combinada de Einstein y Hawking, que entonces esa materia debería empezar a girar alrededor del agujero nereo a velocidades cercanas a la velocidad de la luz. porque hay materia entonces no puede estar en la velocidad de la luz antes de que entonces la materia más cercana del anillo de acreción cuando se acerca al horizonte de eventos entonces ahora sí es atrapada por el agujero nervioso, es absorbida por él ¿pero por qué se le ve una parte de arriba? ah no, es que es la que está detrás es la parte de atrás pero la luz que está emanando pues resulta que el agujero negro obviamente está creando

## [00:28:47]

una deformación del espacio-tiempo y la parte que lo que está detrás no lo tapa el agujero sino que esa luz se pasa por la curvatura de la deformación del espacio-tiempo entonces qué maravilla cuando al fin se le logró tomar una fotografía por así decirlo a un agujero negro y eso fue después de la película y se veía exactamente igual a como lo había descrito la teoría. O sea, se ve como en la película. Y a nadie le sorprendió, pero en realidad eso era sorprendente. De que en realidad la película era solamente una teoría. Era solamente una hipótesis. Y resulta que la fotografía que al final se tomó, efectivamente confirmó la teoría. ¡Qué maravilla! Y todo eso basado en un principio, que es el principio del rock bottom de la lógica. Y es este. Si mis premisas son verdaderas y mi razonamiento es válido, mi conclusión debe ser verdadera. Debe, obligatoriamente.

## [00:30:21]

este principio une como pueden ver los dos aspectos importantísimos que obviamente ambos son fundamentales también para la lógica que es el de este veritativo el de ser veritativo el de ser verdadero más bien y el de ser válido entonces mi conclusión debe ser verdadera puse debe no porque esté gritando sino porque para ponerle énfasis, ya que no tengo negritas entonces sustituyo las negritas con las mayúsculas ese es el enorme poder de la lógica ok, este entonces volvamos a nuestro a nuestra tarea que es la de simbolizar algo tan sencillo y tan humilde como el cálculo del mínimo como múltiplo Ah, les decía, aquí parece que tenemos un pequeño primer problema y es si en lógica se trata de saber si algo es demostrable y eso se hace pues encontrando la demostración, usando las reglas de inferencia, ¿cómo calculo yo algo? ¿Cómo se ve un cálculo? parece raro, ¿verdad? porque calcular

## [00:32:33]

es simplemente, denme unos los parámetros yo hago operaciones matemáticas y salgo con un resultado ¿y qué tiene eso que ver con lógica?

## [00:32:45]

¿a ustedes qué les parece? ¿qué se les ocurre que podemos hacer para este transformar un cálculo en una demostración?

## [00:33:17]

con igualdades quizás ir modificando un número y que tenga que dar igual a algo y demostrar que esa igualdad es cierta ok en realidad tomamos por un camino ligeramente diferente que ese, si es cierto vamos a tener que usar igualdades pero al decir una igualdad es de alguien contra alguien y si yo tengo los parámetros y hago los cálculos con los parámetros de pronto surge precisamente el valor que yo quiero calcular pero como introduzco la noción de ese valor que yo quiero calcular pero si va un poco por donde lo estas diciendo yo recuerdo que nosotros en discreta habíamos visto una noción ahí de demostración pero de divisibilidad entonces tal vez como hay que dividir entre el mcd y demás hacerlo alguna cantidad de veces y con igualdad llegar a un punto para poder demostrar que sí existe ese K, digamos. Un momentito, ¿qué fue lo último que dijiste?

## [00:34:54]

Realizar varias veces una secuencia de igualdades. No. Lo siguiente que dijiste es la clave. Poder decir que sí existe el K. Exactamente. Demostrar que existe el elemento que satisface esas relaciones.

## [00:35:12]

Así es como se hace. Para describir un cálculo mediante lógica, yo digo, bueno, hay que demostrar que existe un X que satisface estas relaciones. O sea, lo que tenemos que decir es que tenemos que demostrar. La vez pasada no lo hice muy bien. Resulta que esto hay que escribirlo también entre paréntesis. Voy a ponerme muy estricto con el lenguaje lógico. perdón, aquí voy a cambiar el nombre de mi variable para todo A y para todo B existe un X tal que bueno, es más, debería ser así en realidad para todo A y para todo B si A es un entero bueno, ahorita me pongo el otro símbolo y B es un entero están aquí, están acá eso implica pueden suponer, voy a usar la herradura eso implica que existe un x tal que x es el este x es el máximo común divisor de a y b eso es lo que tengo que demostrar ahora, de esta forma lo que tengo que hacer es una demostración constructiva o sea, ¿cómo demuestro yo

## [00:38:26]

que existe un x tal que cumple eso encuéntrelo encuentre por lo menos un x que satisface eso y estampeselo en la cara que le está preguntando por así decirlo y de esa forma lo demuestra eso se llama una demostración constructiva entonces los cálculos en los lenguajes lógicos se muestran o aparecen como demostraciones constructivas. Insisto en esto, y es que en el fondo, cuando uno está trabajando ya en lenguajes lógicos, uno no entra necesariamente por una forma, de una manera tan formal. Sí la tiene en la mente, eso sí, uno sí está pensando en eso, pero no tiene que ponerla por escrito así, de una manera explícita siempre es igual que cuando uno tiene ya una cierta soltura en un lenguaje de programación hay muchas cosas que uno las hace sin necesariamente diseñarlas de una manera estricta, aunque debería entonces aquí estamos entrándole de la manera más primero

## [00:39:48]

más general, porque no estamos usando todavía ningún lenguaje lógico y segundo de una manera muy estricta, muy formal ok, eso es lo que hay que hacer ok entonces ahora la pregunta es ¿cómo se define el mínimo común múltiplo de este de dos enteros?

## [00:40:20]

este muy bien, ¿cómo lo definirían ustedes? ya definimos que ya mostramos que es lo que hay que hacer entonces ahora Cómo describo Usando lógica Esto Bueno, a mí se me ocurrió esta forma Yo creería que es algo como Lo que habías denotado Como MCM Bueno, que tiene que existir un K Tal que El MCM Es igual a SK Por Lo que estaría a la par Que sería el MCD Que no me acuerdo cuál es Como lo denotaste La D, D mayúscula Ajá, D mayúscula y el A por B No, el A por B nomás, creo, yo creo Sí, claro que sí Por ahí es Ah, bueno, sí, pero ese sí lo podemos operar Digamos como Sí, como una función, podemos hacerlo directamente, sí Ok, sí, algo así, digamos Algo así Algo así A mí se me ocurrió esto A mí se me ocurrió esto Este Voy a llevarme esto Porque hay muchos símbolos que hay aquí cuáles son mis definiciones entonces ahora tengo que definir utilizando cálculo de predicados de primer orden

## [00:42:07]

¿qué es esto? ¿verdad? porque aquí no dice ¿qué es? no, solo dice este es un predicado ok, ahora me pregunto, bueno, ¿cómo se define ese predicado? ¿cómo hago yo para en cierta forma operacionalizar pero de una manera lógica ese predicado? ah, ok, bueno entonces podríamos decir que para todo A y para todo B ahí vamos a ver qué les parece esto para todo A y para todo B existe un X o sea, es verdad que si para todo A y para todo B existe un X así que esto es un tío del Zoom y existe un Y, ya les digo para qué tengo que poner que existe un Y voy a quitar esto porque me está confundiendo ok, en primer lugar existe un Y tal que ese Y es el máximo común divisor de A y B o sea, si existe un Y tal que ese Y es el máximo común divisor de A y B entonces este eso es un existencial entonces aquí tengo que hacer una conversión de mis notas uy uy uy uy existe este y y este ahora otro de estos y x

## [00:44:48]

es igual aquí estoy usando el predicado de igualdad aquí voy a usar las funciones x es a por b entre Y yo no puedo poner D de Y perdón es esto no puedo ponerlo aquí debajo porque esto no es una función es un predicado entonces tengo que decir que Y es el elemento que hace que este predicado sea verdadero respecto A y B y entonces ese mismo y lo utilizo aquí entonces si es cierto que existe si existe un x tal que si existe un y tal que ese y es el este el máximo común divisor de a y b y este x es igual a a por b entre y vamos a ver 1, 2, aquí está el existencial déjenme contar paréntesis Yo los he sacado, este es por acá, este es acá, este es aquí. Ok, si todo es excierto, ¿dónde es el para todo B? Debería ser aquí, sí.

## [00:46:52]

Eso implica que justamente, este, ah no, mentira, no puede estar ahí porque está fuera del ámbito, es esta X de aquí. entonces eso tengo que decirlo aquí, eso implica que ese x precisamente el x al que se refiere este existencial es el máximo común, el mínimo común múltiplo perdón, de a y de b esto no es sencillo de hecho prolog no fue hecho, no fue pensado para hacer cálculos aunque Por ejemplo, este maravilloso libro, Artificial Intelligence Techniques in Prologue, de Joab Shoham, es de la editorial Double Day, de San Francisco. la biblioteca del tecnológico tiene un ejemplar de este libro extraordinario aquí uno encuentra por ejemplo frutas mínimas cofre el algoritmo hay una versión del algoritmo a estrella en prolog entonces pues cosas así si se ven, a decir verdad si hay que hacerlas no es la parte más gruesa digámoslo así de inteligencia artificial logicista pero sí hay que hacerlo

## [00:48:54]

este es un libro que les recomiendo abiertamente si tienen un interés más que casual en lenguajes para en lenguajes lógicos es un libro muy recomendable bueno y por supuesto si están pensando en el punto de vista logicista de inteligencia artificial a mí es el que más me cae que mejor me cae y hasta cierto punto disculpen por presumir de esta forma lo que se está viendo hasta cierto punto con las empresas de inteligencia artificial en este momento me da una gran satisfacción porque precisamente una de las cosas que a mí siempre me han disgustado de la inteligencia artificial conexionista es la falta de accountability de estas inteligencias o sea yo no sé qué hay ahí el conocimiento es almacenado como un conjunto monstruosamente grande de números de punto flotante entonces no hay manera de saber qué conocimiento está ahí este

## [00:50:18]

Que se yo, por ejemplo, según parece, no quiero ofender a nadie, no es mi intención, solamente para mostrar a lo que me refiero. Según parece, a esta inteligencia artificial GROK se le mostró una imagen de diferentes, compuesta a su vez de imágenes de representaciones gráficas o visuales de diferentes divinidades de religiones. bueno y también personas que no son divinidades pero que tienen un alto peso religioso, entonces había una imagen del Buda una imagen, diferentes imágenes de dioses hindúes como de Ganesh, Shiva por supuesto había una imagen como la imaginación popular usualmente imagina a Jesús de Nazaret entonces había diferentes imágenes religiosas y este y la persona que le puso la imagen dijo, le puso la tarea a Grock de elimine todos los dioses que son falsos ok, entonces si esto fue verdadero porque yo solo vi los resultados no me consta que efectivamente fue una

## [00:51:59]

tarea que se le encargará a Grock pero si si lo fue resulta que Grock respondió con una imagen completamente en blanco excepto la figura de Jesús de Nazaret este y donde se le preguntó por qué dejó solamente esa figura dijo porque ese es el único que no era falso ok esa es la posición de las personas cristianas muy respetable ok está bien lo que pasa es que si usted es judío o si usted es musulmán o si usted es hindú no creo que esté muy de acuerdo con que esa sea una respuesta apropiada, o sea quiero decir que tienen sesgos pero como de antemano no sé yo cuáles son los sesgos en este caso, bueno, tiene este este, no voy a obviamente a juzgar si es correcto es incorrecto pero en política por ejemplo este grok es famosa por ejemplo por decir frases elogiosas de líderes autoritarios como adolfo hitler como benito mussolini francisco franco o sea tiene sesgos políticos muy fuertes

## [00:53:27]

pero si yo examino el conocimiento de esta inteligencia artificial que vería números solo números solo números de punto flotante decenas de miles de millones de números de punto flotante ese es el conocimiento de cualquier inteligencia artificial conexionista no es auditable en cambio la inteligencia artificial logicista simbólica si lo es porque su conocimiento está consignado por ejemplo en sentencias de algo que se parece a cálculo de predicados entonces yo si puedo interpretar como ser humano que hay ahí y que conexiones hay entre el conocimiento o sea puedo crear programas que me digan que relación hay entre las diferentes sentencias o sea si es auditable en realidad la inteligencia artificial está pegando con pared en este momento por precisamente por su falta de auditabilidad no saben que hay ahí no saben que o sea lo único que parece es que cuando sale una sentencia muy rara

## [00:54:47]

la gente misma le dice oiga eso no puede ser cierto por esto y esto a veces la inteligencia se pone en modo de aprendizaje y se corrige a veces no es demasiado el conocimiento humano los mismos creadores de estas inteligencias y que le dan mantenimiento ellos mismos no tienen control de qué más está aprendiendo entonces creo que se están topando con el problema de que hay mucho conocimiento falso y además de que se está alimentando de su propio conocimiento falso y eso va a darle lugar a disparates Entonces ellos mismos vean que un capitalista tan agresivo como Elon Musk admitiera que tenemos que poner en pausa esto, pero eso sí tenemos que hacerlo todos, que él mismo admitiera eso significa, maestro, esto está muy mal. aquí no es un asunto ético sabemos que Elon Musk no tiene ninguna ética más que la de ganar todo el dinero que sea posible para él

## [00:56:09]

entonces que él mismo estuviera de acuerdo con que un toquecito estuvo de acuerdo con el madre de Anthropic y Sam Altman no, no, vamos a poner el freno humano un toquecito aquí porque se nos está saliendo de control es por esa carencia de auditabilidad entonces la verdad me he sentido muy satisfecho por eso ok bueno entonces continuamos con esto como ven entonces ya esto me dice cuando ya yo puedo decir que este x es el mínimo como múltiplo si satisface esto porque aquí Y yo puedo manejar el predicado de igualdad diciendo, ok, lo único que tengo que hacer, como se ve, es ahora sí aplicar estas funciones y ya esto me da el valor que yo necesito y ese es el x que ya necesito, que estoy necesitando encontrar. que bien, ah bueno, ok, pura vida ok, como entonces ahora lo que tengo que hacer es, y como se demuestra esto, como se demuestra que existe un ye que cumple esto

## [00:57:33]

ok, ya vemos que tiene que ser algo parecido, o sea tiene que definirse como una implicación y como un existencial verdad, o sea este es el existencial y esta es la implicación Ah, ok, bueno, eso ya nos da Una especie de machote Para ver cómo definimos Esto, este es más interesante Cómo creen que se pueda Definir eso Ese sí lleva más trabajo, por supuesto Ah, y ustedes saben que necesito Un predicado más Ahora me estaba fijando Voy a apuntarlo porque Si no, se me olvida Vas a definir el de la aritmética modular, ¿no?

## [00:58:44]

Perdón, Enrique, decías Vas a definir el del módulo Exactamente No había definido el módulo No puedo usar la m Porque ya la estoy usando para Mínimo común múltiplo O puedo decir que R es y módulo z Es que le pongo la r Por residuo Entonces x es el residuo De y y z Ok Bueno y ahora si Ya tenemos todos los elementos Para definir el máximo común divisor como ven esto es más difícil todavía porque tiene dos casos ok estos paréntesis que ustedes están viendo aquí se ponen para ser muy formales y describir cuál es el ámbito de el cuantificador por eso es que esta implicación yo la tengo que poner aquí adentro porque estoy dentro del ámbito de este cuantificador o en lógica se le suele decir el alcance el alcance es el término más técnico ese es el alcance de este cuantificador existencial entonces si yo lo pongo afuera ya no se sabría quien es x tengo que ponerlo aquí para que

## [01:01:48]

quede en el alcance del existencial entonces para eso es que ya poniéndonos más serios hay que poner todos estos paréntesis ok entonces vamos a empezar este voy a empezar por así decirlo por acá que el máximo común divisor de A y B es B si A módulo B es o sea lo vamos a hacer así el máximo común divisor de A y B es o B o el máximo común divisor de B y A módulo B es uno o el otro claro, son excluyentes porque esta condición no puede ser simultánea con esta, pero no necesito especificarlo tanto si pongo un O el hecho de que uno sea la negación del otro digámoslo así, me da gratis el asunto de que si no se cumple uno entonces se tiene que cumplir el otro no necesito ser tan estricto para poner un O exclusivo ok, entonces este podríamos tal vez decir esto, para todo A y para todo B ok, mejor me voy a perder todo y eso no me sería así ¡Ay, no! Zoom sí que me da problemas con eso.

## [01:04:22]

Para todo A,

## [01:04:27]

sí vamos a usar los paréntesis con alcance. Y para todo B,

## [01:04:46]

¡Ay, no! ¡Ajá, perfecto!

## [01:04:57]

Para todo A y para todo B,

## [01:05:03]

¿Ok? ¿Cómo digo esto?

## [01:05:14]

Si A módulo B es igual a cero, entonces B es el máximo común divisor de A y B. como lo digo con cálculo de predicados esta es la parte fácil ¿y cómo verá lo que B ha que describir? es esto si B es el o sea, si A módulo B es igual a cero entonces B es el máximo común divisor de A y B entonces yo diría que va a dar la idea general que utilizando el R, X, Y, Z Ajá Si X es igual a cero Entonces de Y Y corresponde al módulo Sí, entonces ¿qué te parece si lo escribo así?

## [01:06:35]

Si cero es el residuo de A y B Ajá, sí ¿Verdad?

## [01:06:41]

Entonces si cero es el residuo de A y B Y ahí estás metiendo incluso el concepto de constante por decirlo así sí, sí, sí, ahí estoy metiendo la constante cero, que es legítimo entonces si eso es cierto esto implica que B es el máximo común divisor de A y B ¿verdad? sencillo ok puede que nuestro lenguaje de programación contenga residuo como una función, de hecho en el caso de prologue eso es totalmente cierto así que no necesitamos definir que es el residuo aunque si tuviéramos que definirlo no habría ningún problema pero vamos a suponer que efectivamente si tenemos algún operador de residuo alguna función que nos dé el residuo entonces para todo A, para todo B listo si Ebre de 0 si Ebre de si cero es el residuo de A y B entonces B es el máximo común divisor de A y B o y ahí podrían negarlo exactamente ahí lo puedo negar

## [01:09:03]

si esto no es cierto entonces vamos a ver cómo definimos lo otro eso implica que Ahora lo interesante es Cómo vamos a describir Esto otro de aquí El otro caso Ya lo pusimos Cómo definimos esto Cómo hacemos la definición recursiva De el Máximo común divisor No sé si se puede volver a poner La condición inicial Solo que modificando el x y el y Parece que hay que hacerlo ¿Verdad?

## [01:10:53]

Ok, puede que tengamos que modificar un poco esto más adelante.

## [01:11:12]

Tengo libres la Y y el X.

## [01:11:18]

Hagámoslo así, a ver, ¿cómo nos va? entonces si existe un Y tal que ese Y es el residuo de A y B ya yo sé que el residuo no es cero ¿verdad? porque ya pasé por aquí entonces si existe el residuo, ya yo sé que no es cero pero por así decirlo es como si no supieras y entonces si existe algún otro sé que existen entonces eso no me estresa Si existe un Y tal que Y es el residuo de A y B y recordemos que los existenciales exigen un Y en lugar de una implicación. entonces si existe esto y otra vez existe un x tal que ese x es justamente el mínimo común múltiplo de b y y ok esto está en el alcance de esto entonces si existe ¿Cómo es ahí? Y es, Y se convierte en el, ya en el resultado del módulo A, módulo B, ¿verdad? No. No. No. Entonces ahí, pero ahí no estás como volviendo a evaluar la condición del, de que no es cero, digamos.

## [01:14:14]

Tengo que hacerlo después, efectivamente, por esto, por esta parte de aquí. Pero es que toma en cuenta que aquí ya yo estoy Con Ah bueno suponiendo que ya es cero O sea que no es cero Sí Estoy suponiendo que no es cero Sí entonces si del otro lado ya uno sabe Que existe otro que no Sí Y vamos a ver X es el Mínimo común Múltiplo de perdón, el máximo común divisor un toquecito este ok se cierra ahí perdón por lo que voy a hacer más paréntesis todavía pero es para separar bien esta situación de esta otra entonces esto implica que si existe un Y ahora sí, listo si existe un Y este o sea si F0 si 0 no es el este mínimo perdón el residuo de A y B esto implica que si existe un X tal que satisfaga esto tal que Y es el residuo de A y B y existe un X que es el mínimo común múltiplo perdón el máximo común divisor de b y y si se cumple todo esto de acá entonces

## [01:16:29]

mentira, mentira, ese no puede estar ahí tiene que estar en aquí, porque ese es este x justamente si existe un x tal que ese x es el máximo común divisor de b y y, tiene que estar aquí porque para que ese x se refiera a él ese X es justamente el perdón aquí es esto debería ser un Y porque es un existencial y ese X es justamente o sea es verdad que ese X es o sea si existe un X que hace esto y ese X entonces es también el máximo común divisor de A y B No, profe, más bien ahí El símbolo es el lote ¿Qué es esto, verdad?

## [01:17:57]

¿Perdón? Que ahí más bien fue que pusiste El símbolo O Entonces más bien Tienes razón, tienes razón Es al revés Gracias ¿Qué es en el fondo lo que estoy diciendo aquí? Y ahora sí, ya queda ¿Verdad? El mismo máximo común divisor de A y B es el máximo común divisor de B y a módulo B eso es esto que estoy diciendo aquí ok entonces bueno ven, sí, sí se puede sí se puede describir con lógica un cálculo ok, sí, se ve enredadísimo pero es que obviamente estos lenguajes de este paradigma no están enfocados a esto aunque pueden hacerlo como ustedes ven ¿tienen alguna pregunta?

## [01:19:39]

no, no verlo es muy fácil digamos, hacerlo es más complicado sí sí, se lleva un ratillo llegar a esto, sí bueno, a mí me llegó me llevó un ratillo llegar acá obviamente este no, verdad ok ok, el siguiente punto en el cual tenemos que pensar es bueno, ok y ese es un punto muy importante en el paradigma lógico y es el siguiente ¿cómo hago yo para demostrar? ¿por qué punto aquí es que es la computadora la que tiene que sacar hacer la demostración ok, esto parece ser una cosa un poco contradictoria ¿verdad? ¿por qué?

## [01:21:01]

porque parece ser como un poco extraño que yo diga que la computadora tiene que hacer la demostración sí, porque al final es incompleta, es un sistema cerrado no puede hacer la demostración directamente no puede hacer la verificación total o sea, no existe un algoritmo para hacer demostraciones y no puede haber un algoritmo para hacer demostraciones, ¿verdad? Eso violaría precisamente el descubrimiento de Turing, ¿verdad? De que existe siempre un algoritmo para construir la demostración de cualquier sentencia que sea verdadera. lo que se hace aquí es por así decirlo atacar, o sea la estrategia que se usa en estas máquinas de inferencia es atacar el problema por fuerza bruta y este lo que hacemos es que cuando escribimos los programas facilitamos esa fuerza bruta por ejemplo poniendo las sentencias en un orden diferente apelamos a ciertos tipos de trucos

## [01:22:28]

que permiten decir no no más si usted ya llegó aquí y esto es falso ya no siga por acá para limitar esa fuerza bruta y tratar de demostrar lo que se quiere mostrar es que además hay un detalle que no se dice con la máquina de Turing y es esta, de que cuando yo hago una demostración yo como ser humano me digo ok, bueno, yo quiero demostrar esto y parto de este y este y estos supuestos, tengo estas premisas y llega un momento en que me pego con pared pucha, no puedo de aquí lo he intentado, no puedo seguir ¿qué me falta? puede ser y eso es lo que a nosotros nos pasa cuando deshacemos demostraciones puede ser que una de dos puede ser que me falten premisas bueno no, más bien podría ser esa es la causa casi siempre, me faltan premisas o sea yo suponía que esas premisas son verdaderas y si son verdaderas pero hasta cierto punto no puedo pasar porque una de dos o hay otro resultado previo

## [01:23:52]

que yo debía haber demostrado y no lo he demostrado para que me aporten una premisa adicional o y eso es lo que a mí me pasaba con mucha frecuencia y me sigue pasando hay algo más que yo debía haber sabido o sea que era materia pasada, digámoslo así y no me acordaba yo no me acordaba si tal cosa sí es cierta si yo agrego esto aquí lo puedo usar eso toda la vida me ha pasado con mucha frecuencia entonces por eso es que en general esas situaciones también están cubiertas en el en el teorema este de Turing, o sea puede ser que haya cosas previas que debieron haber sido verdaderas antes y no las tengo en este momento Y entonces el algoritmo no puede tapar, no puede cumplir con, bueno, ¿cómo identifico qué es aquello que me falta? Ya no hay un algoritmo que me diga qué es lo que me falta para poder completar una demostración. entonces no es tan incoherente que yo quiera hacer una máquina

## [01:25:18]

de demostrar lo que en el fondo estamos construyendo es una máquina que demuestra con las premisas que se le dan pero hasta ahí puede llegar o sea no puede identificar que me está faltando en caso de que no pueda completar la demostración que eso si es en lo que estaba pensando David Hilbert cuando dijo que sería interesante ver si existe un algoritmo que incluso me identifique qué es lo que me falta por demostrar y por lo tanto pueda meterse en un proceso recursivo de identificar qué es lo que me hace falta demostrarlo y entonces volver a la demostración original entonces eso es lo que aclara por qué estas máquinas de inferencia que he dicho sea de paso trabajan con una variante digamos de fuerza bruta ¿Cómo es que funcionan?

## [01:26:25]

Ok, entonces, antes de meternos más profundamente en eso tal vez ustedes no se habían dado cuenta pero hay dos maneras de demostrar voy a ponerlo aquí supondría que una de esas, eso entiendo yo por fuerza bruta es ir y mandarse la tabla de verdad y empezar a probar con todo de ahí sí y entonces yo lo que hago en mis programas es que a sabiendas de que eso puede pasar acomodo las cosas de tal forma que digámoslo así aquellas vertientes que con mi experiencia o con la experiencia de otros yo creo que por estas es por donde se va más a hacer la demostración donde funciona mejor es donde explora primero para, digámoslo así, tener una especie de, lo que en criptografía yo uso este término que es fuerza bruta acotada, o sea, tratar de hacer fuerza bruta, o sea que no se me estalle, a menos que de ahí, ni modo, lo que era más probable según yo, no lo encontró ahí de ahí, ni modo, jálese

## [01:27:53]

no crean, las inteligencias artificiales de conexionistas, en realidad hacen la misma estrategia de fuerza bruta ¿por qué creen que son tan grandes los centros de datos para estas inteligencias artificiales? no es solamente para atender millones de consultas simultáneamente, sí eso sí es cierto, pero también es porque se necesita una cantidad exagerada de poder computacional para acomodar estas cosas en un tiempo razonable este ok, entonces, volviendo a nuestro punto hay dos maneras de resonar si si queremos mostrar que voy a usar vocabulario de un poco más técnico supongamos que tengo un conjunto de premisas delta y yo necesito vamos a ver si está aquí quiero mostrar que una sentencia fi es demostrable a partir de delta ser demostrable significa o se deriva a partir de delta, también se se denomina así este símbolo es que existe una demostración, o sea, existe una cadena de sentencias

## [01:30:20]

este a partir de acá tal que el último elemento de la sucesión es fi o sea, yo lo que necesito hacer, debemos encontrar, yo creo que me cambié el tipo de letra lo siguiente tengo que encontrar una sucesión de sentencias bueno, perdón, voy a poner estas bastantes de estas ahí no ahí lo que estás tratando de definir entonces es como que todas esas líneas de la demostración son como cadenas de símbolos por decirlo así, el lenguaje que leería reconocería la máquina tal que, digamos, de la derivación del primero, yo empiezo a derivar los siguientes y llego a que la última derivación que yo le agregué fue fi, que era el resultado bueno, esa es una manera estoy tratando, más bien estoy haciéndolo un poco más general, digámoslo así de qué es una demostración ¿verdad?

## [01:32:56]

es un conjunto de, es una sucesión de sentencias donde cada una se deriva lógicamente de la anterior o de las anteriores y la última es FI, ¿verdad? Es que lo que quiero mostrarles es que hay dos formas de construir esta sentencia, esta cadena. Hay dos maneras.

## [01:33:37]

Entonces, esta sucesión de sentencias se puede construir de las siguientes formas.

## [01:34:04]

La primera es decir, bueno, ok, necesito FI.

## [01:34:28]

Entonces, Trato de demostrar inmediatamente antes que debería ser verdadero para que phi sea verdadero.

## [01:35:05]

¿Me lo tengo bien? Sí.

## [01:35:14]

Y entonces, bueno, yo digo, bueno, si S sub n es verdadero, phi sería verdadero. Ok, entonces ahora, ¿qué necesito para que S sub n sea verdadero? este y este continuar hasta que pueda encontrar, o sea, pueda llegar a las sentencias que son mis premisas o sea, voy para atrás, para atrás, para atrás o sea, más bien, desde el último, sí para atrás, para atrás, para atrás hasta que llego a que ese sub 1 es una premisa ay, como es una premisa esta es verdadera, entonces si esta es verdadera la que la seguí es verdadera y así sucesivamente y ya fi es verdadero entonces voy construyendo la demostración de atrás perdón, de adelante para atrás esto se llama precisamente por eso porque empiezo desde la última hasta la primera Backward Chaining Prolog es un lenguaje que hace demostraciones con Backward Chaining o sea, la máquina de inferencia de Prolog

## [01:36:55]

trabaja con Backward Chaining, o sea, yo empiezo con lo que quiero demostrar, entonces me pregunto ok, bueno, para que esto sea verdadero, ¿qué debería ser verdadero antes?

## [01:37:09]

y así voy hasta llegar a mis premisas un principio similar de lo que utiliza la inteligencia artificial esta, por redes neuronales de convolución, pero cuando tiene que hacer un ajuste, que hace un que hace un backpropagation, obviamente lo hace con derivadas parciales y otras cosas, pero lo que hace No, no, no, no, no. La back propagation es un ajuste de pesos. Ah, ok. Es un, es simplemente que ya sea que tiene un conjunto de, este, de aprendizaje o que tiene algún criterio para saber si, este, si está cerca de la respuesta correcta. ¿Verdad? O, más bien, lo que hacen estas inteligencias, la táctica más usual que tienen es la de, más bien, aprendizaje por refuerzo, donde una vez que empiezan a trabajar y tienen muchos casos, y esos casos son ya sea exitosos o, o sea, tienen un criterio de éxito, si no son exitosos entonces corrige sus pesos dependiendo de qué tan mal lo están haciendo

## [01:38:30]

¿verdad? entonces los pesos simulan por así decirlo las conexiones neuronales la fuerza de la conexión de una neurona artificial con sus vecinas entonces aumenta o disminuye sus pesos puesto que son números de punto flotante de acuerdo con ese parámetro ok, si es un método de corrección del mercado exactamente entonces la siguiente, la otra estrategia es inicio con las premisas y este avanzo avanzo digámoslo así, saco consecuencias empiezo a generar Con mi conocimiento empiezo a generar derivaciones lógicas hasta que en algún momento llego a fin.

## [01:40:13]

Ok, yo sé lo que están pensando. Eso parece tener terribles problemas de tipo combinatorio, ¿verdad? Bueno, podría tenerlos si usted no es cuidadoso. esto se llama como ustedes pueden suponer forward chaining y por ejemplo clips funciona con forward chaining aquí esto le falta una tilde y aquí que le pasó no hay sugerencias pero me dice que no le gusta bueno ok, entonces ¿cómo ven? a eso es a lo que me refería cuando les decía que no es un paradigma que esté así totalmente tan consolidado como los otros anteriores porque hay dos estrategias diferentes para construir las demostraciones y justamente estas estrategias configuran muy críticamente la manera en que se escriben los lenguajes y la manera en que a partir de aquí yo trato de diseñar mi solución a partir de las sentencias que yo tenga que describir mi problema.

## [01:42:06]

Entonces, primero vamos a trabajar, ya que sabemos esto, entonces vamos a trabajar con Prolog. para eso nos hace falta otro requisito teórico que es el proceso de conversión a cláusulas pero bueno, obviamente ya eso se va lo vamos a ver, de hecho ya me pasé por 5 minutos disculpen, eso ya lo vamos a ver en la próxima clase ok, entonces vamos a dejarlo acá gracias por haber asistido a esta sesión y poner atención y que tengan muy buena tarde, muy buen fin de semana también, entonces ¿será que se puede pasar ese documento antes de que nos desconectemos? el que acabo de hacer sí, claro por supuesto, con mucho gusto con mucho gusto, claro sí, el 13 no hay ninguna el martes 13 qué mala suerte tiene el martes 13 no tenemos nada nada en especial que yo sepa porque resulta que el 29 de octubre cayó jueves ¿verdad? y es feriado, en Cartago

## [01:43:30]

es uno de los feriados más pasiones que hay, es un feriado local ok, pero eso es hasta el 29, ok, por lo pronto entonces que tengan muy buena tarde, muy buen fin de semana y nos estamos viendo, hasta luego
