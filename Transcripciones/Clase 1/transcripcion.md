---
clase: "Clase 1"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1199039163.m4a
modelo: large-v3
idioma: es
duration_sec: 5880.0
---

## [00:00:00]

Sí, muchas gracias. Quería empezar hoy con el paradigma funcional. Ya van a ver por qué lo dejé de tercero. Perdón, el paradigma lógico, disculpen. ¿Cuál es lo que podríamos llamar el fundamento teórico profundo del paradigma lógico? Bueno, vamos a ver, desde un punto de vista muy general, muy muy general, pues si uno tiene que definir la lógica, a mí me gusta mucho la definición de Irving Coppe, que dice que la lógica es la disciplina cuyo objetivo son los métodos, o sea, lo que investiga son los métodos para distinguir un argumento bueno o correcto de un argumento malo o incorrecto. Entonces, desde ese punto de vista, el propósito de la lógica es muy técnico. Son los métodos para distinguir argumentos bien construidos de los argumentos que no están bien construidos, donde un argumento es una justificación de una sentencia.

## [00:02:01]

entonces el propósito original de la lógica era como muy general si bien todos queremos decir y todos queremos pensar y todos queremos creer en sentencias que son verdaderas porque una sentencia verdadera es una sentencia que describe correctamente una situación de algún mundo puede ser un mundo imaginario puede ser un mundo este mundo real donde vivimos a pesar de que siempre de hecho es una cuestión hasta de supervivencia creer en cosas que sean verdaderas cuando ya las necesidades intelectuales se ponen muy sofisticadas, entonces se vuelve mucho más difícil distinguir qué es verdadero de qué es falso. Así que ha sido una gran preocupación en realidad siempre el distinguirlo, pero cuando tenemos que tratar con cosas como la ciencia, la matemática u otros tipos de pensamiento, entonces es cuando el saber si algo es verdadero o falso se vuelve muy complicado. Entonces, tal vez

## [00:04:03]

la primera persona que distinguió esto con suficiente claridad fue Sócrates, cuando de una manera muy majadera y que le costó la vida andaba por las calles de Atenas enfrentando a las personas con sus propias creencias y demostrándoles que aquello que ellos creían que era correcto pues tal vez no era correcto estaba mal fundamentado Sócrates no lo hizo de una manera sistemática su discípulo principal Platón tampoco pero Aristóteles sí Aristóteles lo hizo de una forma mucho más sistemática. Bueno, pero como ven, entonces la lógica lo que trata es de cosas como muy generales. Que es, ¿cómo puedo distinguir un buen argumento de un mal argumento?

## [00:05:16]

Los matemáticos creían estar a salvo de eso hasta finales del siglo XIX. Cuando, por ejemplo, el concepto de espacio entró en crisis. cuando surgieron las geometrías diferentes de la geometría Euclidia y mucho peor cuando Cantor demostró que había infinitos más grandes que otros lo cual es algo totalmente contraintuitivo bueno entonces el resultado de eso fue que de una manera mucho más estricta de lo que jamás había sido, la matemática se volvió lógica, o sea, hubo una especie de convergencia, por un lado, estos problemas tan duros que tenía la matemática que enfrentó, digamos así, la forma en que los matemáticos pensaban su propia disciplina, o descubrían cosas dentro de su propia disciplina, en primer lugar,

## [00:06:30]

Y en otra, un intento muy interesante, fracasado, pero fue muy interesante, que inició un par de matemáticos ingleses, George Boole y Augustus de Morgan, para tratar de reducir la lógica al álgebra. Las famosas álgebras booleanas son una especie remanente de ese intento de reducir la lógica al álgebra ¿Por qué fracasó? Bueno, porque Boole y De Morgan eran pioneros en esto no se habían dado cuenta de que el manejo de lo que ahora llamaríamos de los universales y de los existenciales complicaba las cosas profundamente.

## [00:07:37]

En fin, el caso es que por lo menos nos dejaron unos rudimentos de algo que ahora se llama lógica simbólica. La convergencia de la búsqueda de solidez en la matemática con este desarrollo de la lógica convergió a la versión moderna del cálculo de predicados de primer y segundo orden. ¿y qué con eso? digan ustedes bueno es lo primero que quiero mostrarles en la pantalla y es que el cálculo de predicados de primer orden es un lenguaje capaz de describir cualquier sentencia en matemática o sea cualquier cosa que yo diga en matemática si me pongo así bien estricto siempre voy a ser capaz de describirlo usando el cálculo de predicados de primer orden de hecho les puedo decir algo muy importante esto que acabo de escribir es un elemento fundamental en en la demostración del teorema de incompletitud de Gödel el teorema de incompletitud de Gödel

## [00:09:52]

que dice que en la matemática siempre hay sentencias que son verdaderas pero no son demostrables.

## [00:10:07]

Bueno, ¿y qué tiene eso que ver con programación de computadoras? Ok, a eso vamos.

## [00:10:20]

Vean, si el cálculo de predicados puede describir cualquier sentencia en matemática, Entonces, eso significa que la descripción de cualquier función, o sea, las funciones son elementos matemáticos y se declaran mediante sentencias. qué sé yo, por ejemplo decir que puedo escribir la función cuadrática como de que el elemento que y que corresponde con un x dado es justamente el y que resulta de multiplicar x por sí mismo es una sentencia y es una sentencia que describe una función las funciones son descritas mediante sentencias entonces cualquier función ay perdón puede ser descrita mediante el cálculo de predicados en particular las funciones parcialmente computables ahora sí, entonces conclusión si cualquier algoritmo puede ser descrito con una función parcialmente computable entonces cualquier algoritmo puede ser descrito usando cálculo de predicados voilà y este es el nacimiento de el

## [00:13:58]

paradigma lógico ¿hay alguna duda o pregunta con lo que acabo de mencionar?

## [00:14:15]

de mi parte todavía no muchas gracias Andrés ok, entonces si tenemos un lenguaje que simultáneamente con ser equivalente al lenguaje del cálculo de predicados de primer orden o sea que es completo con respecto al cálculo de predicados de primer orden que tiene una gramática fácilmente reconocible por un compilador que cuente con un algoritmo de ejecución similar a un proceso de demostración lógica del cálculo de predicados de primer orden entonces estamos implementando el paradigma lógico o sea que no es tan sencillo porque está bien el cálculo de predicados de primer orden funciona lo que pasa es que el cálculo de predicados de primer orden es muy difícil de manejar computacionalmente es demostrable que una demostración o encontrar una demostración solo mediante cálculo de predicados de primer orden da lugar a algoritmos NP o sea, que se puede se puede, lo que pasa es que este

## [00:15:45]

requiere una cantidad enorme de esfuerzo computacional este aún con este aún con la así llamada inteligencia artificial actual en el fondo estas inteligencias vamos a ver cuando usted le pide una demostración de algún tipo de digamos de sentencia de resultado matemático muy conocido entonces de mediante la técnica de armado de rompecabezas que tiene estos algoritmos le construyen una demostración basada en que existan demostraciones similares en la red o de que ya la demostración está en la red y que haya sido entrenada adecuadamente con eso entonces, lo que yo siempre he dicho, estos algoritmos no demuestran en ese caso no está demostrando nada está recuperando esa información de este montón de información que está consignada de una manera no estructurada entonces es el equivalente a una búsqueda de una base de datos. O sea, ahí no está haciendo ningún esfuerzo de demostración.

## [00:17:43]

Recientemente, los esfuerzos de demostración de por ejemplo, hace poco hay una polémica muy fea porque la inteligencia artificial de OpenAI encontró una demostración de una de una sentencia de un problema relacionado con las ecuaciones de Navier-Stokes que tiene que ver en física con movimiento turbulento de fluidos entonces un caso particular y muy importante de las ecuaciones de Navier-Stokes con ciertos parámetros daba lugar a un problema que era muy importante de resolver y que todavía no se había resuelto entonces esta gente salió con bumbos y platillos diciendo nuestra inteligencia artificial demostró que cierta sentencia respecto a este aspecto particular de Navy Stokes es verdadera ok el pequeño detalle era que aparentemente dos investigadores de la misma OpenAI habían estado trabajando en ese problema y estaban trabajando en ese momento y partes de la demostración de OpenAI

## [00:19:15]

se parecían extraordinariamente al trabajo que esta gente había estado ya haciendo o sea, no solo la entrenaron específicamente para tratar de encontrar la demostración de Navier Stock sino que la alimentaron con el mismo trabajo de estos investigadores que no lo habían publicado oficialmente o sea, les robó las ideas simplemente parte de lo crucial de de la demostración que en realidad era de dos seres humanos que habían gastado mucho de su talento en encontrar ciertas vías alternas para resolver este problema y además se dejó ver que el esfuerzo que OpenAI había puesto había gastado tantos tokens creo que era el equivalente de más de de 20 millones de dólares en tokens o sea fue simplemente un esfuerzo de combinación de fuerza bruta así que por lo que legítimamente no podemos decir que que lo haya resuelto no sé si han oído hablar de un argumento muy simpático que hay en contra de la

## [00:21:06]

teoría de la evolución de Darwin que dice que la teoría de la evolución de Darwin funciona como si en un hangar lleno de piezas de avión pero desordenadas y puestas por todas partes se desataron huracán dentro del hangar y cuando ya el huracán termina hay un 747 totalmente armado eso para digamos supuestamente poner en ridículo la evolución, bueno pues así funcionan estas inteligencias es un esfuerzo de fuerza bruta tan colosal que al final medio resulta armada una demostración y entonces los seres humanos intervienen este y puede que este las partes que están mal hechas se puedan arreglar pero aquí estamos hablando de otra cosa aquí estamos no estamos hablando de esa forma de, dizque, construir demostraciones, sino que estamos hablando de construir demostraciones de una manera cognitiva similar a como lo hacemos los seres humanos. O sea, partimos de un conjunto de

## [00:22:37]

sentencias y nosotros sí tratamos de aplicar las reglas de inferencia de una manera válida en una secuencia válida con el objetivo de tratar de llegar a la conclusión a la que queremos llegar entonces es ese otro camino el que se trata de seguir en el paradigma lógico no sé, di un rodeo bastante grande para describir lo que no es demostrar en este paradigma para distinguirlo de lo que sí es demostrar yo espero que ustedes cuando llevaron el curso de matemática discreta hayan llevado una haya sido bastante completo o haya sido completa la enseñanza que tuvieron con respecto a lógica simbólica porque eso es lo que vamos a estar ocupando en esta parte del curso entonces no sé, di un rodeo demasiado grande con muchísimas con muchísimos elementos no sé si alguien se me quedó perdido porque hablé demasiado si hay algo que no quedó claro o que les gustaría que aclarara de una forma

## [00:24:20]

más comprensiva o más sintética no sé si me di a entender todo bien profe bueno, muchas gracias Luis Guillermo entonces a eso es a lo que nos referimos demostrar utilizando cálculo de predicados al que uno está acostumbrado en los cursos de lógica no es computacionalmente factible, eso está demostrado también así que primero tenemos que disponer de un lenguaje equivalente al cálculo de predicados de primer orden, no podríamos usar directamente el mismo lenguaje pero además esa aritmética tiene que ser fácilmente reconocible por un compilador, o sea tiene que ser descrita con este con una aritmética Bacchus Naur ustedes saben que esa es una pregunta interesante nunca me la había hecho ¿Qué falta de agudeza la mía?

## [00:26:00]

¿Se puede escribir el cálculo de predicados de primer orden con una gramática de Bacchus Naur? O sea, obviamente sí. ¿Y cómo sería?

## [00:26:29]

Con una BNF.

## [00:26:42]

En cualquier libro de lógica serio, usted encuentra las reglas que definen una fórmula bien formada.

## [00:26:52]

Bueno, entonces lo que habría que hacer es traducir las reglas de una fórmula bien formada a Bacchus-Naur ok este es más, aquí tengo que decir una cosa interesante y es que necesitamos lenguajes que además de estas tres condiciones este último tenemos que poner un requisito más fuerte al final que contar con un algoritmo de ejecución similar a un procedimiento de demostración lógica del cálculo de pregrados de primer orden pero que sea este de tiempo polinomial eso es un requisito computacional fuerte, este para no tener esperando tanto tiempo a Emanuel este, de puedo ponerlo por escrito tal vez ahora que termina la sesión y lo pongo en el tech digital el temario del examen para no dejar al pobre Manuel esperando tanto tiempo que me hace rato que me preguntó si puedo pasar el temario del examen ok entonces ahora habíamos dicho que en el paradigma este en el paradigma imperativo

## [00:28:59]

los algoritmos son conjuntos de instrucciones que se ejecutan en el paradigma funcional un algoritmo es un conjunto de funciones que se evalúan entonces en el paradigma lógico lo que tenemos es que todo algoritmo es un conjunto de sentencias donde yo tengo que demostrar cosas O sea, mi algoritmo se tiene que ver como una descripción lógica de un, digamos, lo ha sido un conjunto de sentencias y luego yo le pregunto, dada esa descripción, si alguna sentencia es verdadera. Entonces, tengo que demostrar que esa sentencia es verdadera. En eso consiste el paradigma lógico. En sentencias que se demuestran. No son funciones que se evalúan, ni instrucciones que se ejecutan. ejecutan. O sea, aquí no tengo instrucciones. Este, ¿cómo están hablando aquí de la escuela?

## [00:30:34]

Profe, ¿cómo fue eso último? Que son, no son instrucciones, son sentencias evaluadas, ¿es? No, sentencias que se demuestran. Ah, ok. Porque eso es todo lo que yo hago en lógica, demostrar cosas.

## [00:31:09]

Y entonces tengo también términos lógicos, o sea, predicados. O sea, son sentencias basadas en cálculo de predicados y este suponiendo que de que cierta que ciertas sentencias que tengo ciertos hechos que yo describo con este lenguaje del cálculo de predicados entonces se le plantea al sistema de creencias algo una sentencia más y esa sentencia entonces hay que demostrar que es verdadera puede que no puede que una de dos o la sentencia legítimamente falsa y por lo tanto no se puede demostrar porque es falsa o dos tal vez yo no le di suficiente información al sistema y por lo tanto no puede demostrarla porque con cierta cantidad de conocimiento no es posible demostrarla pero este entonces en ese caso tal vez lo que me hace falta es aumentar la cantidad de conocimiento de el este del sistema entonces otro detalle interesante es que el concepto de variable que tenemos en en este

## [00:32:49]

paradigma es el que impere lógica o sea, la pertenencia a un conjunto del valor de una variable es posterior a la existencia de esta variable o sea, primero existe la variable y después determino qué cosa es entonces, una cosa interesantísima aquí es que si bien existen los tipos una variable no está amarrada necesariamente a un tipo una variable puede ser del tipo que sea en diferentes momentos de el este de la demostración, o sea, obviamente cuando una variable se amarra con un valor entonces yo digo, ok ya esta variable en este momento, al ser de tal valor, como tal valor es de cierto tipo, entonces la variable es de cierto tipo pero una cosa interesantísima en este esquema es que es factible que la variable se desligue de ese valor y quede indeterminada y pueda tomar un valor diferente de un tipo diferente, en este paradigma eso es perfectamente factible, entonces

## [00:34:25]

como ven el concepto de variables como más laxo en el paradigma lógico porque corresponde con el concepto de variable en lógica y es el hecho de que son los individuos de que para los cuales un cierto predicado es verdadero pero pueden ser de conjuntos muy dispares los los individuos para los cuales ese predicado puede ser verdadero entonces aquí lo tenía con una comparación entre el paradigma imperativo procedimental y el paradigma lógico en el paradigma procedimental tenemos instrucciones en el paradigma lógico tenemos sentencias fórmulas bien formadas eso es lo que significa este FBF fórmulas bien formadas well formed formulas WFF en inglés vean que no pongo que necesariamente son del cálculo de predicados porque de hecho la computadora no va a trabajar con cálculo de predicados directamente en el mismo lenguaje sino con uno que sea equivalente en el paradigma

## [00:35:58]

preparativo yo ejecuto instrucciones en el paradigma lógico yo hago una evaluación veritativa o sea tengo que demostrar cosas o sea son sentencias que se demuestran no son instrucciones que se ejecutan es totalmente incorrecto hablar de instrucciones en en prologue puede que la gente lo use porque perdón por insistir en esto El paradigma imperativo fue como los dinosaurios en el periodo Cretácico y Jurásico. Fueron el grupo dominante. Así que, o sea, si había una criatura importante en estos dos periodos geológicos, fueron los dinosaurios. así que digamos que los dinosaurios de los años 60, 70 e inclusive los 80 durante 30 años las especies que dominaron la tierra de la programación fueron los lenguajes imperativos entonces la gente se acostumbró a decir que los lenguajes tienen instrucciones y que uno coger un programa es ejecutar una secuencia de instrucciones

## [00:37:25]

y que también un algoritmo es un conjunto de instrucciones no, mentira eso es verdadero solamente para los imperativos el asteroide que les cayó encima en los años 90 fue programación orientada a objetos ese fue el asteroide que mató a bueno, todavía sobreviven algunos ¿verdad?

## [00:37:55]

C es tal vez el único, el último de los dinosaurios que sobrevive y un poquito de Pascal entonces, lo que es los datos en el paradigma imperativo procedimental son espacios medidos en bytes, en RAM en cambio en el paradigma lógico equivalen a variables en el sentido lógico ok ¿alguna pregunta?

## [00:38:31]

está bien ok, pura vida vamos a ver que esta presentación tiene más cosas tal vez de las que tiene demasiado de historia este entonces, ¿qué puedo decirles? este voy a ver por donde continúo bueno Bueno, ¿qué puedo decirles? ¿Qué es lo que para uno puede ser más difícil del paradigma lógico? Bueno, en mi opinión, en primer lugar, la primera dificultad que tiene uno es que uno tiene que ser bueno simbolizando. después de todo el paradigma lógico los lenguajes del paradigma lógico son una versión del cálculo de predicados aquí vamos a ver dos lenguajes lógicos vamos a ver Prolog y vamos a ver Clips voy a ver si un momentito Prolog es muy famoso fue desarrollado específicamente para trabajar en inteligencia artificial hay un punto de vista particular en inteligencia artificial que no tiene nada que ver con redes neuronales y no quiere tener nada que ver con redes neuronales dicho sea

## [00:41:08]

de paso qué es él lo llaman este vamos a ver cuál era el término que utilizaba don Claudio Gutiérrez para inteligencia artificial simbólica redes neuronales era llamado inteligencia artificial conexionista o inteligencia artificial subsimbólica digamos en la jerga de todos la gente que trabaja en esto entonces Entonces dentro del ámbito ya tenemos una gran parte de grandes divisiones en una gran división, disculpen, en el cálculo de la inteligencia artificial. Por un lado lógica simbólica y por el otro lado lógica subsimbólica o conexionista. esto que ha causado tanto boom y que todavía está causando tanto ese tanto hype en parte por razones comerciales o en gran parte por razones comerciales más bien es inteligencia artificial conexionista entonces estos otros lenguajes son para la otra parte para la inteligencia artificial simbólica ahora dentro de la inteligencia artificial simbólica

## [00:42:53]

hay un grupo de gente muy testaroda que son los que más me simpatizan a mí son con los que yo más me identifico es decir no sé si hay una palabra preciosa en inglés para ser así tremendamente bueno, testarudo en inglés se dice stubborn pero hay una palabra en inglés para la gente que es más que testarudo ¿verdad? que es ya recalcitrante y a mí me fascina esa palabra es die hard bueno, la gente que está en este eso lo llaman el punto de vista logicista de la inteligencia artificial son realmente diehards de corazón son los que mejor me caen y yo simpatizo tremendamente con ellos de hecho son tan son tan testarudos este que este vamos a ver si se los pongo aquí que publicaron hace cuatro años lo siguiente, ya se los muestro Die Hard es duro de matar igual que las películas publicaron esto que todavía me callaron mejor en el Journal of Applied Logic el manifiesto el manifiesto logicista

## [00:45:27]

que dice al final dejemos que la inteligencia artificial basada en lógica sea un campo en sí mismo o sea, algo ya, separémonos de las redes neuronales, no queremos saber nada de eso este incluso otras técnicas más algorítmicas de inteligencia artificial veámoslo como como algo subsidiario y como una consulta bueno yo había ido a la charla de Carlos Araya el trabajo de él creo que es algo similar a esto porque está basado principalmente en lógica simbólica en inteligencia artificial simbólica porque me acuerdo que no tenía mucho que ver con, o sea se despegaba un poco aparte de datos de recuperación de información y iba más como para ese lado sí, correcto correcto

## [00:46:37]

este, él tenía que ver más con, bueno, de lo que yo sé, de lo que yo más me enteré del trabajo que le dio muchísimos créditos, es gramáticas formales, encontrar una descripción lógica de gramáticas formales de tal forma que se pudieran aplicar transformaciones, sí, que tenían mucho desde el punto de vista lógico, aunque también muchísimo de álgebra es que, permítame decirle, hay una a nivel profundo sigue habiendo una relación muy muy densa entre ciertas ciertos tipos de álgebras y lógica simbólica y eso se puede manifestar perfectamente en lenguajes formales entonces es una mezcla de lógica con álgebra lo sé porque un un señor que fue mi jefe cuando yo trabajé en en caja de ande don carlos loría después se pasó a trabajar en este en este ámbito precisamente en la empresa de carlos araya en arpinsoft así que tuve un cierto contacto con lo que ellos estaban haciendo

## [00:48:11]

ya un poquito más hacia adentro entonces, por un lado es lógica pero por otro lado también es álgebra ciertos tipos de álgebras muy particulares ok, ok pero sí, sí, tiene usted razón este entonces vean que interesante este este paper está disponible a pesar de ser del severe usted lo puede bajar este paper es un argumento sostenido para la visión de que una lógica una inteligencia artificial basada en lógica debe llegar a ser, debe convertirse en un campo autocontenido totalmente divorciado de los paradigmas que todavía incluyen que se incluyen bajo el paraguas de ahí, o sea, ahí resultó ser un paraguas demasiado grande como el conexionismo y el punto de vista de sistemas continuos basado por ejemplo en lógicas lógicas difusas este paper incluye un sumario autocontenido de la inteligencia artificial basada en lógica también como el rechazo a un cierto número de objeciones

## [00:49:37]

que inevitablemente van a traerse contra la declaración de independencia que aquí se que aquí se expresa ese a mí me encanta este punto de vista se los confirmo, yo tengo un sesgo a favor de esta gente, me encanta su punto de vista entonces este fue digamos la motivación de la creación de un lenguaje como Prolog bueno, del lenguaje Prolog el lenguaje Eclipse nació de lo que podríamos llamar una manera subsidiaria porque los sistemas expertos basados en reglas digamos que se estandarizaron de ciertas formas tales que se volvió más bien apropiado diseñar un lenguaje específico para diseñar, valga la redundancia, sistemas expertos basados en reglas. lo que pasa es que estos lenguajes y específicamente Clips crecieron lo suficiente como para, o sea, crecieron en poder expresivo hasta convertirse en lenguajes Turing completos específicamente Clips y este, quiero que lo

## [00:51:32]

conozcamos porque representa un punto de vista también interesante sobre este como implementar el proceso de demostración permítanme ver por dónde andaba yo un momento por favor ok entonces vamos a ver qué problema tiene el paradigma lógico bueno, el problema más grave que tiene el paradigma lógico es el siguiente aquí se trata de demostrar sentencias entonces tenemos primero dos problemas uno como encontramos un lenguaje que por un lado sea equivalente al cálculo de predicados de primer orden pero por el otro este sea el proceso de demostración sea computacionalmente factible o sea aquí pasó una cosa Y es que el lenguaje que conocemos del cálculo de predicados de primera orden, descubrimos que estaba muy íntimamente ligado a las reglas de demostración. Y tal vez lo mejor sea cambiar las reglas de demostración, pero eso nos obliga a cambiar el lenguaje. vamos a ver

## [00:53:37]

permítanme insistir en esto en el paradigma lógico yo escribo sentencias que tienen que ser de alguna manera equivalentes al cálculo de predicados de primer orden que por un lado y por otro que me permitan demostrar si una sentencia es verdadera ok entonces yo me pregunto cómo se demuestra empecemos con el corazón de esto que es en la demostración cómo es que yo demuestro bueno parece muy sencillo y es que a partir de un conjunto de premisas que se asumen verdaderas se aplican las reglas de inferencia hasta que se pueda llegar a la conclusión eso es demostrar sin saltarse pasos sin abusar del lenguaje siguiendo formalmente las reglas de inferencia debo decir eso me creo en la obligación de decirles esto a ustedes porque yo no me canso me van a disculpar por favor pero si hay algo de lo que yo no me canso es de hacer propaganda en contra de las falacias empezando porque las personas

## [00:55:33]

tienen una una confusión realmente curiosa entre lo que es una falacia o sea lo que es una sentencia falsa y una sentencia falaz este voy a decir cosas que son como muy obvias téngame paciencia por favor pero lo que yo quiero marcar con cuidado una sentencia falsa es una sentencia que no es verdadera, esto es mucho más que una que una que algo obvio o sea, si algo no es verdadero es que no corresponde con el mundo discúlpenme voy a decir cosas que son como muy infantiles pero es que quiero probar mi punto por ejemplo decir que las vacas vuelan por sí mismas verdad no montadas en un avión no las vacas no vuelan en este universo en este mundo en esta en este en el mundo en que nos movemos las vacas no vuelan. Entonces, una sentencia falsa es la que diga que las vacas vuelan, o de que las avestruces vuelan, o de que los chompipes vuelan. No, estos animales

## [00:57:17]

no vuelan. Entonces, esta sentencia, decir por ejemplo, que las avestruces vuelan, es falsa. Y es imposible que vuelen, pesan demasiado realmente para, para, y con las alas ridículas que tienen, es imposible hacer que un avistruz duele. Entonces una sentencia es falsa cuando no corresponde con la realidad de algún mundo. Ustedes me han escuchado mencionar el asunto de algún mundo y ustedes pueden decir, bueno, es que este sujeto debe ser un muy fanático de los multiversos. No, no, no es tanto así, este, si yo digo, este, por ejemplo, que, este, Don Quijote montaba en un caballo llamado Babieca, esa sentencia es falsa, no porque alguna vez haya existido Don Quijote, y que fuera un Hidalgo del siglo XVIII en la antigua región de la Mancha. No, nunca existió una persona llamada así en España, pero dentro del universo planteado por la novela El Ingenioso Hidalgo, Don Quijote

## [00:58:48]

de la Mancha, dentro de ese mundo, la sentencia, Don Quijote montaba un caballo llamado Babieca es falsa el caballo de Don Quijote se llamaba Rocinante Babieca era el caballo del Cid entonces a eso es lo que más prefiero con algún mundo las obras de literatura nos plantean cada una de ellas un mundo un mundo el autor nos dice bueno imaginemos que tal cosa fuera verdadera, o sea imaginemos un mundo donde esto pasa entonces a eso es a lo que me refiero con sentencias que son verdaderas en algún mundo entonces en cambio una sentencia falaz también llamada falacia es una sentencia demostrada incorrectamente o sea es una sentencia que yo no puedo comprobar directamente con el mundo y que no sea demostrado formalmente por ejemplo afirmar que Donald Trump es una persona muy apta para gobernar a los Estados Unidos basado en el criterio de que en su momento mucha gente lo creyó así

## [01:00:48]

si usted me dice que Donald Trump era la mejor persona para poner en ese sitio tan importante solo porque mucha gente lo creyó en su momento es una falacia es la famosa falacia de apelación a la multitud solo porque mucha gente haya creído que eso es cierto no hace que algo sea cierto todo lo contrario la realidad está demostrando que es brutalmente falsa semejante sentencia pero bueno en todo caso una sentencia puede ser verdadera pero estar mal demostrada entonces este yo no puedo creer en esa sentencia debido precisamente que está mal demostrada demuéstrele bien primero para que yo pueda creer en ella especialmente en estos tiempos de totalitarismos este lo que ocurre es lo siguiente hay un término y si me disculpan que esté ingresando con cosas de la realidad en lugar de solamente ver cosas de de lenguajes lógicos tomando como excusa el hecho de que del proceso de demostración

## [01:02:21]

pero eso se debe a que vivimos tiempos muy convulsos yo no esperaba a estas alturas de mi vida estar viendo tiempos tan revueltos y con tanto con tantas cosas desafortunadas que creíamos haber dejado en un pasado muy remoto y verlas volver a surgir cosas que incluso yo yo no vi de una manera tan directa que ocurrieron en la década de los treintas y los cuarentas del siglo pasado que yo ni siquiera vi yo nací en los sesentas este Entonces, si me disculpan por eso, debo extenderme, creo que es mi obligación extenderme en esto, porque hay una palabra, o sea, creo que es mi obligación como profesor universitario. Hay una palabra que los sociólogos empezaron a usar pero que luego adoptaron los filósofos Y me parece una palabra que describe muy bien algo que se hace en política Esa palabra es narrativa ¿Cuál es la narrativa? ¿Quién domina la narrativa? ¿Qué es una narrativa?

## [01:03:55]

una narrativa es un cuento una narrativa es como un cuento infantil una narrativa es una cierta visión de la realidad que arma algún grupo político, religioso económico y que nos tratan de vender las cosas son de esta forma por ejemplo en este momento estamos inmersos en la narrativa este economicista liberal el mercado es Dios el mercado siempre sabe que es lo mejor para la gente el mercado decide ¿por qué? bueno porque el mercado decide que se produce para quién cómo lo distribuyo y cuánto vale entonces el mercado decide por ejemplo qué es lo que hay que fabricar y si alguien no compra algo entonces hay que dejar de fabricar eso y el mercado decide también entonces en cuánto se va a vender y esa es la narrativa esa es la narrativa básica el mercado es Dios hágale caso al mercado, ir en contra del mercado es pecado, es deformar la realidad esa es la narrativa

## [01:05:42]

entonces todo se orienta así este, tener compasión por los demás no, no, ¿cómo se le ocurre? no, no, precisamente los pobres son pobres porque quieren este, si los pobres quisieran dejar de ser pobres estudiarían trabajarían más duro tienen el descaro de decirnos eso este actuarían más inteligentemente entonces y de esa forma dejarían de ser pobres pero si son pobres es porque no han hecho esto y no han hecho eso porque no quieren esa es la narrativa entonces toda narrativa tarde o temprano se fundamenta en un cierto conjunto de falacias entonces hay algunas cosas que sí son verdaderas del discurso de la narrativa pero hay otras que quieren hacernos comprar que este que deberíamos poner en duda y decir no, no, un momento eso no está bien demostrado o las consecuencias de eso son contradictorias lo que pasa en estos tiempos es que se nos está justamente el carácter

## [01:07:18]

de un régimen autoritario es imponernos una narrativa o sea usted debe creer esto durante los tiempos de la colonia hubo una identificación pero súper súper cercana entre el poder del rey y la religión católica bueno La versión católica del cristianismo, para ser más exactos. La versión católica del cristianismo justificaba el poder del rey y por lo tanto legitimaba el poder del rey sobre todos los dominios del continente americano. En consecuencia también la corona española imponía entonces el catolicismo como única religión verdadera. Y así lo decían. Eso es lo que decía. Todavía yo no sé si se sigue diciendo, pero el catolicismo es la única religión verdadera. creo que el credo católico todavía lo dice esa parte no me acuerdo del credo tuve que aprendérmelo de memoria para la primera comunión pero últimamente no lo recuerdo es la imposición de una narrativa y ahora quieren

## [01:08:54]

imponernos la narrativa neoliberal o sea que exista el neoliberalismo pues no está mal está bien que haya libros, por ejemplo permítame mostrarles qué casualidad, está bien que existan libros como este perfecto o sea, la gente que realmente cree que el capitalismo lo mejor que se haya podido inventar es maravilloso, está bien que exista gente así es más, pero esperen para que vean qué interesante aquí tengo otro libro de Milton Friedman que este este libro Free to Choose esta este libro fue la biblia de el gobierno de este Ronald Reagan y de George Bush padre este y vean qué interesante lo que dice este libro dice que Milton Friedman para Milton Friedman la libertad económica es un requisito esencial para la libertad política esta es la tesis central de este libro pero oigan que interesante una de las consecuencias que Friedman pretende demostrar, dice al permitir

## [01:10:48]

a los individuos cooperar voluntariamente el sistema de libre mercado ejerce del límite al poder coactivo del estado ok eso está bien pero vean la segunda parte dice y actúa como una fuerza dispersora que impide grandes concentraciones de riqueza en unas pocas manos yo no sabía que este tipo era comediante cuando yo vi esto pero qué es eso pero no pero parece que para ser economista hay que llevar un curso sobre stand up comedy de veras con gente como Elon Musk como Mark Zuckerberg por el amor del cielo de que demonios está hablando parece que como que no está funcionando el sistema verdad algunas cosas se inventaran pero está bien está bien que está bien que publiquen esto, que lo traduzcan que la gente tenga el derecho de leerlo sí, sí, sí, claro es más, los invito a que lo lean y resulta que sacando ese libro salió este otro que fue casualidad

## [01:12:25]

o sea, también tiene que haber permiso de leer esto, ¿verdad? y juzgarlo críticamente también ver en qué cosas pudo haber tenido Marx razón y en qué cosas se equivocó pero no estamos viviendo esos tiempos estamos viviendo tiempos en los cuales esto se nos quiere imponer ya no se trata de que usted puede leer esto usted tiene que creer esto hasta ahí no qué tiene eso que ver con todo lo que les he hablado que tenemos que ser muy críticos porque nos están imponiendo narrativas y la forma de ser críticos es justamente desenmascarar las falacias y desenmascarar las contradicciones del sistema discutir abiertamente entre nosotros cosas como por ejemplo hasta dónde una persona tiene permiso de hacerse daño a sí mismo especialmente cuando por ejemplo con el caso de las drogas llega un momento en que pierde la capacidad de juzgar y de evaluar que se está haciendo daño a sí mismo

## [01:14:02]

porque la necesidad de la droga es mayor que su capacidad de evaluarse y de auto evaluarse y de ser consciente de sí mismo digo eso porque esta gente creyendo en el libre mercado dicen bueno de ahí las drogas psicotrópicas hay un mercado para ellas y si hay un mercado entonces como el mercado es Dios tiene que haber todo el derecho de de de de que se pueda comprar y vender puesto que hay un mercado y es la libertad de las personas, si una persona quiere hacerse daño a sí mismo, debe tener libertad de hacerlo toquecito, siempre y cuando, siempre esté en capacidad de este, juzgar sobre su propia situación hay un punto a partir del cual los adictos ya no pueden juzgar esto y son los adictos los que sostienen el mercado ven, este Entonces, hay que reconocer estas falacias, hay que verlas, hay que darnos cuenta de que estas narrativas contienen montones de falacias.

## [01:15:30]

Así que yo no quiero que me impongan algo que obviamente o es del todo falso o me lo están haciendo pasar gato por liebre. O sea, como que es verdadero sin habermelo demostrado propiamente. entonces me disculpan por haber quemado tanto tiempo de la clase en estos temas que son más del ámbito de lo que estamos viviendo en este momento y que me guindé de esto precisamente con un tema de lógica pero insisto como universitarios que ustedes y yo somos eso es lo que nos tiene que distinguir ser más capaces de ser críticos yo no le estoy diciendo quiero recalcar esto severamente y fuertemente y que quede en la grabación yo no le estoy diciendo que usted debe creer en esto ni le estoy diciendo que debe rechazarlo no le estoy tampoco diciendo que no debe creer en esto de ninguna forma la universidad también pierde su carácter cuando desde un desde una cátedra un docente quiere imponer a su

## [01:16:58]

vez sus ideas sobre sus estudiantes eso está mal eso no debe hacerse y ustedes no ustedes como estudiantes no deben permitirlo entonces insisto yo no les estoy diciendo deben creer en esto o deben creer en esto no, yo les estoy diciendo sean críticos con ambos eso sí y como universitarios ustedes y yo estamos en mejor posición de ser críticos por eso es que la gente que está metida hasta las orejas en la narrativa, dicen que en las universidades nosotros los profesores los cuál es el término, le lavamos el cerebro a ustedes, porque el estudiante universitario está menos dispuesto a creer en comulgar con ruedas de molino, como se dice en un delicioso proverbio español, en creer la primera idiotez que un politiquillo de al dos por cuarto quiere hacernos creer el estudiante universitario está menos inclinado a eso, entonces dicen, es que las universidades le lavan el cerebro no, no, no

## [01:18:16]

No, no, en las universidades queremos enseñarles a ser críticos y claro, cuando sale con cualquier cantidad de falacias, los universitarios somos más capaces de darnos cuenta, pero en fin, insisto, les pido disculpas por haberme extendido tantísimo sobre esto, Pero también es que yo estoy harto de, en lo personal, de que se me trate de imponer una narrativa en la que definitivamente no creo y no tengo por qué creer. Pero insisto también, cada estudiante y cada persona es libre de pensar lo que crea más conveniente. entonces y es que el tema central aquí es este cómo demostramos cómo evitamos las falacias bueno, evitamos las falacias construyendo buenas demostraciones ok, bien, vale cómo obtenemos buenas demostraciones la la intención original de Bull y de Morgan era, bueno

## [01:19:42]

Si podemos reducir la lógica al álgebra, entonces sería usando cálculo, cálculo, pero cierto tipo de cálculo, cálculo algebraico. Nosotros estamos más que familiarizados con eso. Son álgebras booleanas. entonces tenemos un operador or, un operador and un operador not este usamos distributividad y un montón de cosas puramente algebraicas no funcionó se quedaba algo como medio camino lo que si desarrollamos fue algunos sistemas de demostrar bueno el sistema más conocido y más extendido en las universidades es el sistema que fue desarrollado para sus cursos de lógica por el profesor estadounidense Irving Coppe escribió un libro que como todo libro universitario de lógica para los cursos iniciales se llama introducción a la lógica. En él Coppi enunció un conjunto de reglas y dijo ok estas son las reglas de inferencia y en realidad los lógicos estuvieron de acuerdo. Sí, es un conjunto

## [01:21:30]

de reglas de inferencia. Entonces, ¿cómo demostramos. La idea es que a partir de un conjunto de premisas que se asumen verdaderas, se aplican las reglas de inferencia hasta que se pueda llegar a la conclusión. Vean este detalle. Este detalle es importantísimo. Que se asumen verdaderas. O sea, perfectamente podría darse el caso de que yo aplique correctamente las reglas de inferencia y aún así llegue a una conclusión falsa eso es perfectamente posible permítame darles un ejemplo que fue una una para mí fue una divertida anécdota este algunos de ustedes se llevarán a las manos a la cabeza pero bueno esto me pasó ya les muestro disculpen un momentito de esta anécdota es para ilustrar esto que acabo de mencionarles permítanme mostrarles un momento por favor ya casi casi el hablar resulta que en un momento dado estaba en un en un acuario un acorde muy grande muy muy grande y vi esto ok

## [01:24:54]

vi un animal enorme por lo menos unos 3 metros de largo con una cola plana aletas gruesas un morro ojos a los costados y que respiraba por un agujero en su cabeza en la parte de arriba de la cabeza ok la única peculiaridad rara que yo veía es que no tenía aleta dorsal o K entonces aleta de atrás plana que mide 3 metros o menos que tiene un hocico largo dientes de forma cónica aletas gruesas y respira por un agujero en la en la nuca yo me acerqué a una de las personas que estaban cuidando, digámoslo así en el acuario y me acerqué y con toda la inocencia del mundo le pregunté, oiga, disculpe ¿qué clase de delfín es ese? porque el hecho de no tener aleta dorsal me pareció raro ¿por qué yo hice esa pregunta? porque en mi base de conocimiento las características que yo les he dicho identifican a un delfín bueno, la señora de una manera muy muy poco amable me indicó, me regañó más bien

## [01:26:58]

diciéndome, oiga, eso no es un delfín es una ballena beluga Oh, ok. ¿Qué fue lo que pasó ahí? ¿Cuál fue mi error? Bueno, todas mis sentencias eran verdaderas, ¿verdad? Excepto que la parte, que precisamente la parte que faltaba era justamente parte indispensable de la definición de delfín, tener aleta dorsal. supongo que debe haber otras más profundas para los biólogos pero yo pensaba que si ese conjunto si esto, esto y esto son verdaderos y con solo ver al animal yo me daba cuenta de que son verdaderas, entonces el animal es un delfín lo que yo no sabía era qué tipo de delfín pero me sacaron del error, no, no, momento lo que usted está diciendo es verdadero pero le falta información por lo tanto su conclusión es falsa o sea yo razoné bien pero hubo un hecho que me faltó y es si no tiene aleta dorsal no es un delfín eso es un ejemplo de algo que en lógica se llama cálculo no monotónico

## [01:28:35]

es un problema interesantísimo precisamente en inteligencia artificial del punto de vista logicista como hago yo para trabajar con cálculo lógico no monotónico este entonces que es lo que quería decirles con todo esto aparte de mostrarles que soy un perfecto ignorante en mamíferos acuáticos este bueno que no basta con que todas mis premisas sean verdaderas puede que me hagan falta premisas o puede ser que mi razonamiento sea verdadero pero alguna premisa sea falsa en mi caso, mi premisa falsa era aunque el animal no tenga aleta dorsal es un delfín o sea, la premisa falsa que yo estaba que estaba ahí encubierta y de que yo no me había dado cuenta es que yo creía que puede hay, o sea que existen delfines sin aleta dorsal esa fue mi premisa falsa yo no sabía que tenía esa premisa falsa pero sí, sí la tenía entonces se está escondida puede ser que una de mis premisas sea falsa

## [01:30:07]

y aunque mi razonamiento sea correcto, mi sentencia mi conclusión puede ser falsa precisamente por eso entonces, todo es importante Mis premisas deben ser verificablemente verdaderas y mi razonamiento debe ser correcto. Ok, entonces el conjunto de reglas que ustedes probablemente conocieron, espero que hayan conocido, en el curso de matemática discreta, es el llamado sistema de copia. que consiste de esto nueve reglas de inferencia diez reglas de sustitución cuatro reglas de cuantificación dos reglas de negación del cuantificador y opcionalmente uno ve cuatro reglas de manejo de la igualdad recuerdan las reglas de inferencia modus ponens, modus tollens silogismo disyuntivo, silogismo constructivo este adición ahí llevo cinco, me faltan cuatro este hay otra en la cual yo puedo separar unas sentencias y yo digo P y Q es verdadero, por lo tanto P este este es una gran simplificación creo

## [01:31:56]

sí, es simplificación, tienes razón, gracias hay otro que creo que se llama silogismo disyuntivo aunque no es un silogismo del todo si P implica Q y Q implica F, entonces P implica R bueno esas nuevas reglas de inferencia las 10 reglas de sustitución ¿transitividad no es ese?

## [01:32:25]

yo no lo conozco como transitividad sino con el nombre de algún tipo de silogismo, aunque no son silogismos del todo, dicho sea de paso las diez reglas de sustitución por ejemplo, conmutación asociatividad distributividad las reglas de De Morgan la definición de implicación material, definición de equivalencia material doble negación ok, todas esas son el conjunto de reglas de sustitución las cuatro reglas de cuantificación cómo elimino el cuantificador cómo introduzco el cuantificador ya sea el universal o el existencial sí Andrés, creo que es el silogismo hipotético tienes razón que insisto, no es un silogismo del todo entonces les decía las reglas de manejo del cuantificador son la ejemplificación existencial, ejemplificación universal generalización existencial, generalización universal las dos reglas de negación del cuantificador no para todo X p de x equivale a que

## [01:34:08]

existe un x tal que no p de x que no existe un x tal que phi de x equivale a que para todo x no phi de x y hay cuatro reglas adicionales de manejo de igualdad porque igualdad es un predicado muy peculiar es muy peculiar de hecho en matemática nosotros manejamos cuatro definiciones diferentes para el mismo simbolito de las estas líneas las líneas las líneas horizontales paralelas tiene cuatro significados diferentes en matemática es increíble eso lo que es más increíble es que después de tantísimos siglos de estar haciendo matemática fue la matemática alemán Gottlob Frege a principios del siglo XX el primero que se dio cuenta de que la igualdad ese símbolo se usaba con cuatro significados diferentes entonces esas cuatro reglas del manejo de la igualdad se utilizan cuando igualdad significa que efectivamente el predicado afirma que dos entidades en realidad son la misma ok, el caso es este

## [01:35:43]

el sistema de copy es muy poco práctico para una computadora porque en términos computacionales los algoritmos de demostración utilizando el sistema de copy son NP vean esto este la forma en que se demuestran, en que los seres humanos demostramos cosas, por así decirlo, vean, cabe aquí, cabe en mil quinientos centímetros cúbicos, para que una computadora, bueno, un sistema de computadoras, sea capaz de hacer lo que para demostrar nosotros, bueno, es más, ni siquiera lo hacen, ningún sistema, este, de estos, de inteligencia artificial, demuestra como demostramos nosotros, esos sistemas lo que hacen es armar un rompecabezas y necesitan una cantidad enorme de energía para hacer eso y nosotros trabajamos simplemente con una cantidad de recursos infinitamente más restringida este bueno, este asunto de cómo crear una demostración un sistema que demuestre en este ambiente es algo

## [01:37:34]

que se lleva su tiempo vamos a dejar la clase acá para retomarlo en la sesión que tenemos el próximo viernes no mentira, jueves jueves 24 de cómo encontrar un sistema de demostración que nos pueda servir para para que lo pueda manejar una computadora entonces voy a
