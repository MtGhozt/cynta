---
clase: "Clase 4"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1093639621.m4a
modelo: large-v3
idioma: es
duration_sec: 5810.4
---

## [00:00:03]

Estamos con el tema de la programación lógica. La programación lógica consiste en ver cómo hago para que la computadora lleve a cabo un proceso formal de razonamiento. Entendiendo como proceso formal de razonamiento puede llegar a una conclusión a partir de ciertas premisas utilizando reglas de razonamiento el término en lógica el término que se usa en lógica es sound rules o sea, reglas fuertes sound, en este caso se está utilizando con el significado de profundo una regla de razonamiento es sound si está autológica lo cual es muy razonable porque uno espera que si algo es si algo es una regla de inferencia lo que tiene que hacer es que si las premisas son verdaderas entonces no hay manera en que la regla de falso

## [00:01:49]

Las premisas son verdaderas, pero las premisas son sentencias, donde esas sentencias pueden estar compuestas con una combinación de predicados unidos por I, por O, o con algunas cosas están negadas, o hay implicaciones, o hay equivalencias. entonces una premisa es una sentencia entonces la idea es que sin importar cuál es el valor de verdad de de los predicados que son parte de el de la sentencia de las sentencias que son las premisas la regla aún así me da un valor siempre verdadero la regla completa entonces una regla de inferencia si es una una regla sound una regla estable o regla fuerte y ese es el tipo de reglas de razonamiento que estamos admitiendo en el cálculo en cálculo de predicados ok entonces ya sabemos que usamos lógica simbólica que entonces eso tenemos que saber simbolizar ya vimos que el truco para adaptar esto a programación es que si queremos hacer un cálculo

## [00:03:36]

lo que digamos el sustrato formal de esto es que yo estoy preguntando por un existencial o sea demuéstreme formalmente que existe un X tal que satisface ciertas propiedades y el digamos lo que uno tiene que hacer es que a la hora de definir las propiedades uno las define de una manera que sea operacionalizable o sea que sea algo que lleve a verificar algo concreto de manera que las demostraciones existenciales son constructivas siempre como me demuestra que existe un individuo que hace esto o esto tal o cual cosa Ah, véalo, aquí está. Ese es el tipo de demostraciones que se hacen acá para darnos cálculos. Y así de esa forma, entonces, adaptamos nuestros algoritmos a un lenguaje lógico. Por supuesto, los lenguajes lógicos son más apropiados para la descripción formal de conocimiento que pueda ser manipulable usando lógica. entonces no es que para cálculos concretamente

## [00:05:31]

puede ser que los lenguajes funcionales sean mucho mejores pero bien que mal los lenguajes lógicos son lenguajes incompletos así que esta parte de la ciencias de la computación, pues tiene que incluirlos. Ok, entonces ya sabemos que tenemos que simbolizar nuestros algoritmos y que la mayor parte de ellos van a simbolizarse mediante alguna demostración de tipo existencial. Bueno, ahora nos tenemos que preguntar dos cosas. Una, si es posible crear un lenguaje de programación que se parezca bueno primero si será posible utilizar el cálculo de predicados como tal así como lo vimos para para programar si sí, ah bueno que dije ya lo tenemos si no entonces cómo construimos un lenguaje que sea tan poderoso como el cálculo de predicados de primer orden pero que al mismo tiempo sea más fácil de manejar por una computadora ok bueno como ustedes pueden

## [00:07:10]

suponer la respuesta a la primera pregunta es no el cálculo de predicados de primer orden tal y como está la computación en este momento da lugar a problemas o a algoritmos que son de tipo NP. O sea, que se puede, se puede. Lo que pasa es que la cantidad de energía de recursos computacionales que habría que usar son excesivamente altos.

## [00:07:53]

Entonces no resultan prácticos. Bueno, en este momento de la computación le han metido tantísimo dinero a los recursos computacionales que este la verdad es triste que fuerza bruta sea el la norma más bien en este momento pero bueno todavía nos interesa tener un poquito de de eficiencia computacional y les decía otro segundo problema es si tenemos que decidirnos a cómo razonar, o sea, cómo construimos nuestra máquina virtual de razonamiento. Esto va a tener una influencia muy poderosa sobre el lenguaje que diseñemos. Vamos a utilizar backward chaining o forward chaining. Esto es tan importante que precisamente esto divide los tipos de lenguajes lógicos, o sea los hay que usan backward chaining y los otros que usan forward chaining no sé si tienen algún aporte o alguna pregunta o alguna observación que les gustaría hacer profe bueno yo tal vez no es como del tema pero

## [00:09:24]

es que la semana pasada te había pedido que si podías subir el ejercicio que habíamos hecho en el world Ah, ok Era como para recordarle eso, si podía subirlo Claro, claro, muchas gracias por más bien ustedes por recordármelo Pura vida, pura vida Aquí tengo los papelitos Sí, muchas gracias, voy a anotarlo El de mínimo común múltiplo Sí, correcto ese Claro Ok, este... Ok, el tema que vamos a tocar hoy es... el de digamos los lenguajes backward chaining o sea los lenguajes que empiezan por la conclusión y entonces yo la idea es que yo me pregunte bueno para que esto sea verdadero que debería ser verdadero previamente ok yo digo bueno la conclusión se deduce fácilmente y esto, esto y estos son verdaderos. Ah, ok. Bueno, muy bien. Entonces, ahora, ¿cómo hago para probar las tres precondiciones de mi conclusión? Ah, ok. Para que la primera precondición sea verdadera,

## [00:11:34]

deberíamos de primero haber demostrado esto, esto y esto. Para que la segunda precondición sea verdadera, deberíamos haber demostrado antes esta otra cosa. Ven, va a ir más bien de la conclusión hacia hacia atrás por eso se dice backward y la idea es llegar hasta las premisas y llega un momento en que yo, ok, pero para que esto sea cierto estas dos cosas deberían ser verdaderas ah mira, pero estas dos cosas son las premisas están entre mis premisas, ah ok, que he dicho entonces ya, esto es verdadero y ahí para adelante ok, les decía que este Vean cuál es la dificultad de tratar de hacer una demostración con cálculo de predicados.

## [00:12:58]

Estas son las reglas de inferencia. Bueno, esas son las reglas de inferencia y de reemplazo en cálculo, me sirven tanto para cálculo proposicional como para cálculo de predicados. A eso hay que agregar las reglas de cuantificación, que por cierto, esta regla que ustedes están viendo en este momento, están un poco incompletas porque yo puedo hacer la generalización universal solo si el C sobre el cual estoy tratando de hacer el universal, esta variable esta variable ha sido introducida por una ejemplificación universal entonces si eso es así yo si puedo hacer eventualmente una generalización universal porque si no podría cometer la falacia del existencial y es que consiste en esto que yo haga una ejemplificación universal haga ciertos razonamientos y ya con eso diga que existe un elemento que satisface esto y eso es eso es inválido eso es una falacia de hecho podríamos llamarla

## [00:14:57]

la falacia del existencial déjenme darles un ejemplo yo digo, tengo una sentencia universal que dice todos los unicornios son blancos y entonces instancio la universalmente decir bueno X es un unicornio por consiguiente X es blanco y hago una hipótesis de que hay un unicornio que se llama Rodolfo y entonces este Rodolfo es un unicornio y todos los unicornios son blancos y si un X es un unicornio entonces X es blanco, entonces Rodolfo es blanco ok entonces llego a la conclusión de que Rodolfo es blanco pero puedo llegar también a la conclusión de que ahí tengo a Rodolfo y entonces o sea, tengo una cosa que se llama Rodolfo y tengo una cosa que es blanca o sea, que Rodolfo es blanco

## [00:16:12]

Ah, ok, entonces de ahí puedo generalizar existencialmente, dado que Rodolfo es un unicornio, que existen los unicornios, porque yo no puse ninguna restricción aquí, tal y como está en este cuadrito, no estoy poniendo ninguna restricción para generalizar existencialmente sobre una variable, o sobre una constante. entonces, pero todo está basado en un universal y los universales son hipotéticos, o sea si hubieran si hubieran si hubiera unicornios serían blancos para hacer eso más patente de una manera espero que no me consideren demasiado blasfemo y conste que lo que estoy haciendo es una cita el filósofo estadounidense Raymond Smulian publicó hace muchos años un artículo muy lindo en el cual él especula sobre la naturaleza del libre albedrío Raymond Smulian fue un importante lógico estadounidense del siglo pasado y que además tiene unos unos libros, publicó muchos libros muy interesantes

## [00:17:40]

de acertijos lógicos entonces él enseña lógica pero mediante acertijos y son maravillosos disculpen que hable tanto de Smulian pero es que yo conocí la obra de Smulian en mis cursos de lógica con Don Luis Camacho y le agradezco muchísimo eso a Don Luis porque son maravillosos esos libros Raymond Smulian le fascinaba la temática de las paradojas de las sentencias autorreferenciales entonces uno de los primeros libros de acertijos lógicos que él tiene se llama el nombre el libro se llama, ¿cómo se llama este libro?

## [00:18:38]

lo cual de nuevo es autorreferencial ok, bueno, les menciono todo esto perdón porque bueno, estamos con los problemas del existencial, ¿verdad? estamos, que no queremos hacer ese tipo de ese tipo de falacias entonces tiene ese pequeño defecto ese cuadro, pero tomemos eso en cuenta ok, ¿a dónde es que quiero llegar? ¿a qué es que esto estalla exponencialmente si queremos hacer un algoritmo que demuestre utilizando estas reglas porque no hay ningún criterio formal para decidirse por una regla o por otra las computadoras son pésimas pero terriblemente malas haciendo eso cualquiera de ustedes pueda argumentar pero ya hay computadoras haciendo demostraciones, o sea la inteligencia artificial de ahora hace demostraciones sí y no la mayor parte de las veces si yo le pregunto cosas relativamente bien conocidas de matemática, me dará alguna demostración que ya está almacenada

## [00:20:28]

en algún lado, que ya alguien hizo entonces eso es lo que me dice o sea, por así decirlo se aprendió de memoria alguna de las demostraciones que están ahí y esa es la que me va a dar ya sea que se la aprendió bien o se la aprendió mal no importa y cuando se está utilizando para hacer matemática ya un poco más creativa en realidad esas son los mismos algoritmos de esta inteligencia artificial pero han partido de cero o sea las han entrenado específicamente con el área de la matemática o las áreas de la matemática o de la física donde se quiere demostrar algo y a la hora de entrenarla las personas que están entrenándola los supervisores ya les dan ciertas indicaciones de vea esto es preferible que esto otro esto tiene más importancia que esto otro para guiar en causar y aún así esas máquinas pueden tardar una semana sea con ese enorme poder computacional y quemando miles de tokens

## [00:21:54]

tardan un rato enorme en encontrar una solución y que incluso encuentran una y no es buena entonces hay que decirle, bueno, empieza de nuevo y excluya tal o cual cosa o sea que aún con la tecnología de hoy en día con el enorme poder de cómputo que hay para correr estos algoritmos Aún así sigue siendo cierto que las computadoras son pésimas cuando tienen que buscar en un espacio donde no tienen criterios acertados de búsqueda, donde no hay buenos heurísticos para escoger entre diferentes opciones para construir una solución. eso es un problema que se ve mucho en inteligencia artificial simbólica que es el problema de encontrar una ruta cuando el espacio de búsqueda es excesivamente grande las computadoras siguen siendo malas en esto cuando no hay un buen heurístico entonces ese es el problema que tenemos en lógica en principio si tenemos 23 reglas de inferencia pues pues hay

## [00:23:34]

23 caminos diferentes abiertos y cada uno de ellos da lugar a otros 23 o sea esto es exponencial en términos de 23 a la n bueno 24 tomando en cuenta las reglas 25 tomando en cuenta las reglas de negación del cuantificador hay caminos que se descartan más rápido que otros, cierto pero siempre hay 25 caminos abiertos no es un buen panorama entonces especialmente en una de las vertientes de la lógica perdón, de la programación lógica para resolver este problema se propuso lo siguiente especialmente a inicios del siglo XX en las décadas de los 20 y los 30 y 40 lo que se pudo en los 40 fueron especialmente ricas en producción lógica fueron especialmente enormes grandes resultados formidables resultados se produjeron en esta época no solamente el trabajo de Turing y de Gödel sino también teoría de modelos el teorema por ejemplo de Lohenheim y Scholem son de los grandecitos de esta

## [00:25:24]

de estas décadas el cálculo lambda de Church entonces entre otras cosas los lógicos por ejemplo para ver si podían llegar a ciertos resultados con más facilidad se orientaron en algunos casos a resultados minimalistas resultados en los cuales se veía si era posible reducir la cantidad de opciones de la lógica para tener un cálculo más potente con el cual se podría hacer demostraciones más directas así por ejemplo se dieron cuenta de que en lugar de 3, de tener 3 operadores el i, el o y la negación, se puede tener solo uno bueno algunos algunos podemos resolver todo con and y or perdón, con and y not o con or y not o sea, en el siglo II pero y ellos no lo sabían porque no le estaban dando nombre en ese momento se toparon también con la curiosa circunstancia que podemos recibir a solo uno Anand o Anor, lo llamaríamos ahora usando los términos que se usan en electrónica fue en esta época

## [00:27:02]

que se descubrió que se podía tener un solo operador lo cual en este momento se está aprovechando para construcción más eficiente de computadoras porque es más fácil construir un AND que un AND usando transistores el AND tiene un transistor más para poder hacer la negación entonces se ha desarrollado técnicas de diseño en electrónica utilizando solo NAND o solo NOR bueno, pero les decía que entre otras cosas se buscó cómo reducir inclusive las reglas de inferencia ok, fue hasta los años 60 que basado en el trabajo de otra gente un lógico estadounidense logró imponiendo ciertas restricciones logró demostrar que el cálculo de predicados de primer orden podía reducirse a tener una sola regla de inferencia y además bueno en su cálculo lógico él elimina del todo las bueno él elimina las conectivas y deja solo el NOT o sea, quita el AND, quita el OR aparentemente, en realidad no es cierto

## [00:28:53]

pero aparentemente quita el AND quita el OR y deja solo el NOT y con una sola regla de diferencia este sujeto de apellido Robinson creó este cálculo y le dio el nombre de regla de resolución lo vamos a ver porque digamos que la regla de resolución es el puente que nos permite pasar de el cálculo de predicados de primer orden a una versión más simplificada del cálculo de predicados entonces la regla de resolución tiene dos partes porque esta es otra restricción la regla de resolución no trabaja sobre las sentencias de cálculo de predicados de primer orden sino que trabaja sobre algo que se llaman cláusulas una cláusula es una sentencia lógica que no tiene cuantificadores y los predicados pueden estar negados o pueden estar sin negar permítanme mostrarles un ejemplo unidos todos como es algunas negadas, otras no negadas aquí P, Q, etc son predicados o sea que pueden tener a su vez

## [00:31:27]

variables o pueden tener constantes y variables una mezcla de constantes y variables y esto es una cláusula entonces el cálculo de predicados perdón, la regla de resolución trabaja sobre cláusulas ok, entonces el primer problema que hay es cómo pasar de cálculo de predicados a cláusulas, a un conjunto de cláusulas y eso es parte de lo que vamos a ver hoy ok, ¿alguna pregunta? ¿los he perdido un poco?

## [00:32:23]

jamás que al final igual entonces si necesita usar los and y los or digamos no es barra que solo que solo dejó el not digamos si se ocupa vieras que es que el truco que él hace es el siguiente la idea de él es que mete todos los predicados en un conjunto y entonces muestra esos predicados como una lista entonces por así decirlo lo que hace desde el punto de vista formal es que elimina los OS y los reemplaza por comas entonces dicen se desapareció la conectiva en serio algo así en el fondo es eso en el fondo es eso pero digámoslo así ya no nos tenemos que preocupar de la conectiva en tanto su tabla de verdad eso desaparece, ya yo no lo considero entonces por eso es que la conectiva como tal desapareció ok y hasta cierto punto tiene sentido porque los elementos en un conjunto yo los puedo poner en el orden que yo quiera entonces la computatividad se va en la colada este ok, hace años

## [00:33:58]

Yo había preparado este documento, te lo voy a compartir también en el Tech Digital, sobre el proceso de Robinson para pasar fórmulas del cálculo de predicados de primer orden a cláusulas. pero hay un temita pequeño que necesito mostrarles que es un detalle que Scholem introdujo en la demostración del teorema de Lovenheim y Scholem que entonces es un primer concepto que tengo que mencionarles que se llama la función de Scholem como les digo aquí Scholem fue un lógico noruego muy importante muy muy importante una anécdota es que nosotros no solamente admiramos el el resultado que obtuvo GEDEL mostrando que en matemáticas siempre existirán sentencias que son verdaderas pero no son demostrables muchas de las cosas que admiramos de este teorema es la manera en que lo demostró Gödel lo que hizo fue decir bueno voy a trabajar con las reglas y los axiomas de la aritmética

## [00:35:44]

eso fue un golpe de genio porque el conjunto de reglas que había establecido Russell y Whitehead para la aritmética valían para cualquier área de la matemática entonces si usted demuestra que hay en la aritmética sentencias que no son demostrables eso vale para en general para cualquier área de la matemática en cualquier parte en geometría en topología este en análisis funcional siempre habrá alguna sentencia que se escapa que no puede es verdadero y no es demostrable Entonces, lo que hizo Gödel fue primero Trabajar con Ok, con la aritmética La aritmética tiene que ver O sea, en realidad es teoría de números, ¿verdad? Tiene que ver con los enteros Y cierto conjunto de axiomas Para los enteros Ok, entonces, él hizo esto, bueno Voy a usar las sentencias lógicas Que hablan De los enteros Y se le ocurrió hacer esto a cada sentencia lógica voy a poder asignarle un único número entero

## [00:37:02]

el número de Gödel y por supuesto en la demostración Gödel muestra cómo encontrar el número de Gödel de cualquier sentencia lógica y él demuestra que esos números son únicos para toda sentencia ok, entonces una demostración es una sucesión de números de Gödel pero son números enteros entonces él demuestra que cualquier sentencia y cualquier sentencia fuera que es verdadera tuviera una demostración entonces esas sucesiones de números deberían tener cierta característica de acuerdo con las leyes de la aritmética pero él demuestra entonces que es imposible que exista ninguna sucesión que de acuerdo con las leyes de la aritmética de números de Gödel pueda encontrarse siempre para cualquier número de GEDL o sea, utilizó la aritmética para demostrar que la aritmética no siempre es demostrable eso es bellísimo eso es bellísimo por eso a Shmulian le encantaba porque todo es autoreferencial ahí

## [00:38:22]

lo divertido es que La única persona en el planeta Tierra que no quedó impresionado con la enorme belleza de esta demostración fue Goethe el mismo. Y en alguna ocasión se le oyó decir, yo no sé por qué la gente habla tanto de mi demostración, porque después me di cuenta que yo hubiera podido obtener el mismo resultado simplemente como un corolario de un teorema de Scholem así que yo no sé, más bien me enredé mucho es demasiado larga le podría haber hecho más corta o sea eso nos muestra primero la enorme importancia de Scholem ¿Verdad? Cuyo Geddel mismo admiraba la obra de Scholem y lo interesante de la propia apreciación de su trabajo de parte de Geddel.

## [00:39:37]

El caso es que Scholem propuso una visión alternativa de la ejemplificación existencial. es el asunto es así cuando yo hago un razonamiento el uso de la generalización existencial está condicionada como les decía a ciertas restricciones para evitar caer en la falacia existencial de la cual ya les hablé por ejemplo copy pone en la ejemplificación existencial la restricción por ejemplo en algunos sistemas lógicos la generalización existencial está condicionada que sólo se puede hacer sobre una variable o constante que se haya introducido con una ejemplificación existencial o sea cuando usted restringe alguno de los dos ya sea el universal o el existencial o sea puede restringir alguno de los dos pero tiene que restringir alguno en el sistema de COPI, como les digo, la restricción se pone sobre la ejemplificación existencial porque sólo puede hacerse dentro de un supuesto.

## [00:40:56]

COPI más bien hace un supuesto como la... Ustedes recuerdan que nosotros hicimos una demostración utilizando una característica hipotética. Ya supongamos que tengo S de X.

## [00:41:18]

Eso se llama un supuesto. o sea, un argumento hipotético agregando que la variable de la ejemplificación no puede ocurrir libre ni en la conclusión del argumento hipotético ni en ningún renglón de la demostración que preceda al argumento hipotético o sea, es una cosa como muy bien alambrada a la demostración misma pero eso aquí no nos sirve porque como les digo, todo eso solicita un control sobre el origen de las variables libres que aparezcan en un razonamiento. Dicho sea de paso, una variable libre es una variable que no está ligada a ningún cuantificador.

## [00:42:15]

Scholem se preguntó si habría alguna mejor manera de manejar las variables que surgen de una ejemplificación existencial y lo razonó de esta manera. En una expresión de la forma existe un x que, tal que, p sub 1 de x y p sub 2 de x se está asegurando que es cierto que existe al menos un X que tiene las propiedades P1 y P2 así que la ejemplificación existencial se puede hacer con constantes es interesante porque se puede utilizar algún tipo de, si me permiten el término, constante anónima inclusive por ejemplo habemos 22 participantes en esta sesión yo sé que alguno de todos nosotros debe tener la fecha de nacimiento si suponemos que el primero de enero es la fecha más digamoslo así más temprana y decimos que el 31 de diciembre es la fecha más tardía entonces yo estoy seguro de que alguno de nosotros no voy a ser yo nací en septiembre pero alguno de nosotros

## [00:44:12]

ha nacido en una fecha que es la más temprana de todo el grupo puede que haya alguien haya nacido en que se yo un 12 de enero o sea alguno de nosotros nació en una fecha que es más temprana que la de cualquier otro ¿quién? yo que sé pero hay alguno alguno de todos es el que nació en la fecha más temprana entonces sabemos que existe aunque yo no puedo identificarlo entonces en los lenguajes naturales es interesante como este ya sea hay nombres, hay sustantivos que se refieren a esas variables anónimas en otros idiomas no son sustantivos sino que son expresiones en castellano por ejemplo usamos fulano sutano perencejo en inglés se utiliza por ejemplo who knows who o John Dow para preferirse a alguien que existe por ahí, pero yo no sé quién es entonces, yo podría utilizar ese tipo de constantes con el existencial entonces, si yo tengo una sentencia de la forma existe un X tal que P1 de X

## [00:45:54]

y P2 de X yo puedo reemplazar la X por alguna constante particular y yo digo bueno, es este ¿qué pasa con una fórmula bien formada como esta otra? para todo x existe un y tal que p de xy y q de xy implica r de xy ¿qué pasa en ese caso? bueno veámoslo así, o sea, ¿qué pasa cuando el existencial está de segundo? si el existencial estuviera de primero se podría trabajar como este caso pero si el universal está de segundo el asunto es un poco diferente, porque en este caso se está diciendo que dado un X cualquiera le corresponde de alguna forma un Y específico tal que lo que se predica de ambos es cierto, o sea ese Y depende del X de alguna manera o sea, formalmente estamos diciendo que existe una función que relaciona a y con x entonces es correcto reescribir la fórmula bien formada que teníamos acá de esta manera es decir, para todo x bueno p de x y p de x y f de x x f de x

## [00:47:44]

para ellos es verdadero P y para XF de X es verdadero Q y eso implica que es verdadero que R de X y F de X o sea la Y se me desapareció y está siendo reemplazada por, digámoslo así un seudónimo o sea el elemento que le corresponde a Y el elemento que le corresponde a X ¿Qué? Como esto es un existencial Sabemos que sí existe ¿O K? Mucho sentido, porque igualmente si uno encuentra el Y Va a depender de X Lo puede desplazar como función Exactamente, sí Correcto Puede ser reemplazado por la constante específica Que le corresponde a ese X en particular Cuando yo ya hago La ejemplificación universal Por ejemplo Entonces F es la función que le asigne Y a X y esa función se la llama la función de Scholem y me permite eliminar el entre comillas el cuantificador existencial reemplazando, o sea, sin tener sin poner ninguna restricción ese es el problema es que vean esto, perdón disculpen la

## [00:49:20]

el titubeo aquí disculpen Es que vean esto. Vean las reglas de cuantificación. O sea, una manera de poder ver las reglas de cuantificación es la siguiente. Las ejemplificaciones tienen el efecto de hacer desaparecer el cuantificador. dada la primera expresión que tenía el cuantificador de ahí concluyo otra sentencia que ya no tiene cuantificador o sea una manera de verlo Benson Mates por ejemplo a él le gusta mucho esta forma de verlo hace desaparecer el cuantificador las instancias o las ejemplificaciones las llamo ejemplificaciones porque así era como las llamaba don Luis Camacho ok permítanme un momentito aquí estoy es difícil hacer aparecer lo que quería mostrarles, es que quiero mostrarles esto, volvamos a las reglas de inferencia vean que interesante este que interesante como se puede ver la simplificación yo puedo ver la simplificación

## [00:51:31]

como diciendo, ok, la simplificación me permite desaparecer la conjunción.

## [00:51:46]

Vean cómo las reglas de definición de la implicación material me hacen desaparecer la implicación.

## [00:52:07]

O sea, porque si P implica Q equivale a no P o Q, entonces el operador implicación desapareció obviamente no desapareció está siendo reemplazado por otra combinación de de operadores pero como tal ya no aparece noten que implicación también puede hacerse desaparecer donde yo digo que P implica Q se define como implica que P y Q o no P y no Q ok, entonces las reglas 16 y 17 hacen desaparecer el operador Benzomates dice, hay reglas que hacen aparecer los operadores y otras que las hacen desaparecer vean que la doble negación permite desaparecer a la negación este en cierta forma si tengo P o Q y tengo no P desaparece el O ok, tomando en cuenta todo eso es que Robinson nos deja este proceso para pasar de sentencias a cláusulas y lo hago mediante un caso o sea, pongo los pasos que son nueve pasos pero quiero que vean a través de un ejemplo la idea es esta

## [00:54:06]

yo tengo el cálculo de predicados para que no nos perdamos Yo tengo el cálculo de las sentencias en cálculo de predicados, pero como estas son difíciles de manejar a nivel computacional, se quiere crear un cálculo lógico basado en cláusulas y no en sentencias de cálculo de predicados, porque con algunos tipos de cláusulas es más fácil trabajar. esa es la meta a la cual vamos lo digo otra vez porque es un camino muy largo y nos podríamos perder de que para qué diablos estamos haciendo todo esto bueno, ese es el objetivo ok, entonces examinemos este argumento si todos los caballos son animales entonces la cabeza de un caballo es la cabeza de un animal primero, tendremos que simbolizarlo para simbolizarlo primero nos damos una interpretación usemos esta interpretación C de X significa X es un caballo A de X, X es un animal K de XY, X es la cabeza de Y

## [00:55:25]

ok, entonces el argumento podríamos simbolizarlo de esta forma para todo X, si X es un caballo entonces es un animal y de ahí puedo concluir o debería poder concluir que para todo x si existe un y tal que ese y es un caballo y x es la cabeza de y si es que noten que la segunda parte de la sentencia habla de cabezas la cabeza de un caballo es la cabeza de un animal entonces por eso el universal es para todo x que sea una cabeza entonces si ese Y es una cabeza y además es la cabeza de un caballo eso implica que existe un Z tal que Z es un animal y X es también la cabeza de Z ok entonces este es el argumento ya simbolizado vamos a llevar este argumento a cláusulas dicho sea de paso, es demostrable esa sentencia se puede, ese argumento se puede demostrar no lo vamos a hacer acá porque no tenemos tanto tiempo pero podría ser un ejercicio bonito para ustedes vean que

## [00:56:59]

introducimos un existencial aquí y acá y tiene que haber una implicación acá entonces y este existencial está ligado con con un predicado de algo que sea una cabeza parece que eso se puede hacer por un argumento hipotético yo le recomendaría usar un argumento hipotético porque de todas maneras hay que introducir el predicado de que supongamos que existe un x que sea una cabeza de algo bueno la idea es que creemos este por razones que todavía no les he dicho pero que les voy a decir más adelante necesitamos demostrar esto por contradicción o sea negar la conclusión y mostrar que la negación de la conclusión con las premisas me da lugar a una contradicción ok eso es un argumento por contradicción así que vamos a utilizar ese tipo de argumento así que entonces deberíamos asumir que nuestra premisa es consistente para mostrar la contradicción

## [00:58:26]

entonces la premisa es consistente con nuestro conocimiento sobre animales es esta, o sea que los caballos son animales pertenecen a ese grupo zoológico bueno, a ese grupo taxonómico para hablar de una forma más apropiada y debemos negar la conclusión para ver si podemos llegar a una contradicción así que más bien entonces nuestras premisas van a ser estas se recuerden que en contradicción uno niega la conclusión y la introduce como una premisa y empieza a razonar a partir de ahí a ver hasta donde llega ok, esto es lo que yo quiero pasar a clausulas entonces John Robinson propuso este procedimiento de nueve pasos para entre comillas transformar cualquier conjunto de fórmulas bien formadas del cálculo de predicados de primer orden en un conjunto de cláusulas en realidad ese proceso es la aplicación una y otra y otra vez de las reglas de inferencia porque si no, no daría lugar a nada

## [00:59:49]

que sea lógicamente válido, ¿verdad? entonces por eso es que transformar está entre comillas porque en el fondo voy a usar otra vez cálculo de predicados y por así decirlo voy a llegar a una conclusión Permítanme solo un momento, por favor. Es que la escuela está enviando información, la dirección de la escuela.

## [01:00:38]

Por cierto, nos dijeron que, no sé si ustedes ya saben, que les avisamos que la semana entrante es la semana del FESTEC. Entonces, la semana entrante, los docentes no tienen permitido ni hacer giras, ni hacer evaluaciones, cuises, exámenes, ni tampoco revisar proyectos para la semana entrante. Entonces, tómenlo en cuenta. Ya es una resolución de la rectoría.

## [01:01:29]

En la semana del 19 al 24 de octubre.

## [01:01:38]

Ah, bueno. Entonces, continuamos con lo nuestro.

## [01:01:45]

El proceso es el siguiente. Primero, el primer paso, eliminar, insisto, entre comillas, las implicaciones y las equivalencias. En realidad, no las estamos eliminando. Se trata de aplicar las reglas de definición de implicación material y de la equivalencia material. Vean que en este caso vamos a usar esas reglas para eliminar la implicación. Entonces, en lugar de tener que para todo x c de x implica a de x, tendríamos para todo x no c de x o a de x. y aquí entonces vean que es esta parte de adentro la que tiene la implicación entonces, y eso está negado dejemos la negación por ahora y negamos lo de adentro entonces no existe un Y tal que C de Y y K de XY o existe un Z tal que A de Z y K de XZ ok, entonces ese es el primer paso eliminar las implicaciones y equivalencias segundo paso, reducir el ámbito de las negaciones, o sea, después del paso dos, lo único que puede

## [01:03:03]

quedar negado son predicados ¿ok? entonces aplicamos de Morgan las reglas de negación del cuantificador y la regla de la doble negación para hacer eso, bueno en la primera ya, ya estaba ya lo único negado es el CDX entonces se queda así, pero en la otra ok, al negar el existencial se me, perdón el universal se me transforma en un existencial negando lo que está adentro ok, ya por si esta negación de este existencial la transformó en un universal y ahora voy a tener que negar aquí tengo que aplicar de Morgan todo esto, o sea, tengo que negar este O perdón se fue por Whatsapp por hacer click en una parte equivocada perdón perdón, ¿dónde estaba? perdón, ya, ahí llegué este ok, entonces lo ahora aplico esto y este I se me transforma en un O pero entonces tengo que volver a negar este universal y se me convierte en un existencial pero tengo que negar lo que está aquí adentro

## [01:05:15]

y utilizando otra vez de Morgan se me convierte en esto si ustedes ven algún error en la aplicación de las reglas, me avisan se lo agradecería mucho y esto también hay que negarlo porque esta negación está negando a esto y a esto entonces el O se me transforma en un I y al negar que existe un z tal que a de z y k de z es para todo x no a de z o no k de x z aplicando de Morgan y negación del cuantificador.

## [01:06:00]

Ok, entonces como ven, ya aquí lo único que está negado son los predicados.

## [01:06:15]

Tercer paso, renombrar variables. de manera que en cada fórmula bien formada cada cuantificador tenga ligada una variable única en cada fórmula bien formada entonces aquí ya y si solo hay una cuantificada que es la x y ya y si aquí yo tengo x tengo y y tengo z entonces si cada cuantificador está ligado con una variable diferente que es única en toda la sentencia en cada sentencia, en cada fórmula bien formada y entonces, nuestro ejemplo cumple con eso ok, ahora aplicamos la función de Scholem como una alternativa a la ejemplificación existencial o sea, el nombre oficial de este paso es eliminar los cuantificadores existenciales ok, la primera no tiene, pero la segunda sí, entonces este x se transforma en una a en esta A A reemplaza X F de A reemplaza Y aquí este, el slash se utiliza mucho en lógica para decir reemplaza A o sustituye A entonces A sustituye a X, F de A sustituye a Y aquí

## [01:07:57]

ese es el único existencial que nos quedó acá este el primero está reemplazado por una constante y el segundo es reemplazado por una función de Scholem aquí X es reemplazado por A porque está en el ámbito de este cuantificador pero Z es un universal así que Z puede quedarse como está paso quinto, poner las fórmulas bien formadas en forma normal prenexa la forma normal prenexa es la que tiene todos los cuantificadores al frente bueno, en el caso de los universales no hay problema, yo siempre me los puedo traer al frente entonces este de aquí puede pasar al frente hacia acá, porque de todas maneras como ven, esta primera parte de aquí ni siquiera menciona a Z y esta ya estaba en forma normal prenexa ok todo bien ahora eliminamos los cuantificadores universales pero en realidad lo que estamos haciendo es ejemplificación universal entonces nuestras sentencias ahora quedan de esta forma

## [01:09:32]

ahora hay que pasar a algo que se llama forma normal conjuntiva la idea de la forma normal conjuntiva es que yo tenga como en este caso los oes no se mezclan con los is sino que tengo esto y esto y esto y esto, pero si alguna cosa es algo compuesto, entonces es un conjunto entre paréntesis predicados relacionados solo con o entonces como aquí, esto es algo que está en una forma sencilla, puede quedarse así este también se puede quedar así y aquí tengo esto o esto, ok se puede quedar junto como ven, es esto o sea, son oes o listas de oes unidas mediante is ok, eso es lo que se llama forma normal conjuntiva ahora, renombrar otra vez las variables de forma que cada fórmula bien formada tenga variables únicas o sea, ahora es sobre el conjunto completo pero bueno por dicha, eso ya lo teníamos, vean que el x solo aparece aquí Z solo aparece acá ahora nos pide que separemos conjunciones

## [01:11:28]

y eso podemos hacerlo aplicando la regla de simplificación o sea esto y esto y esto si esto es cierto entonces esto es cierto por eso aparece este aquí pero también si esto es cierto esto puedo ponerlo por aparte si lo pongo aquí entonces si esto es cierto entonces lo puedo poner por aparte sí entonces vean a lo que llegamos a que en cada línea solamente quedaron cosas separadas con oís esa es la idea, aquí a este paso nueve era donde queríamos llegar y ya estos son cláusulas como ven, entonces este conjunto de nueve pasos me permite terminar en cláusulas perdóname Una consultita. Claro, dime. Cuando dice que tenga variables únicas, ¿a qué hace referencia? A que si aquí hubiera una Y, bueno, si aquí hubiera una Z, como esta Z de esta línea es diferente de la Z de esta otra línea, entonces diga, bueno, y reemplace la Z que está aquí por una W. ¿Ves? Entonces queda una sola

## [01:13:10]

las variables de cada línea son únicas ok, ok, perfecto obviamente eso solo aplica para variables porque las constantes si no pueden ser reemplazadas, verdad, las constantes denotan individuos específicos entonces ellas no se reemplazan ok ok este, entonces ya con esto como ven voy a usar esto más adelante para ver de que me sirve esto ya pude a partir de aquí llegar perdón llegar acá ok ahora permítanme un momentito quiero hacer esto de una forma más directa digamos permítanme un momento lo que hace Robinson es que yo trataba de explicarle a Andrés lo que hace Robinson es una cosa así ya les pongo ya comparto lo que hace Robinson es esto este él dice bueno yo voy a tener este no aquí no estaba yo voy a tener esto y entonces él dice bueno yo lo voy a escribir de otra forma es más vean él dice voy a tener esto y también voy a tener otra cláusula de la siguiente forma, etcétera

## [01:16:45]

y voy a tener todas mis cláusulas ahí entonces lo que propone Robinson es lo siguiente yo voy a ver yo voy a tener todo mi conjunto de cláusulas y entonces qué raro, esto no me está funcionando perdón voy a ver si esto me funciona entonces dice en mi conjunto yo voy a tener esto y voy a tener este otro, ya te voy a tener esta con esta misma, pero todo esto forma parte de un mismo conjunto voy a ver si es verdad que funcione si, funcionó ok, vean que mi conjunto de cláusulas contiene esta y esta entonces eso significa que esta coma de aquí en realidad significa un I pero vean que sujeto me ha jugado, lo que hace ahora él dice, no, en realidad yo quiero ver eso así que es lo que le explicaba creo que conversaba con Andrés hace un rato ven, es como el guasón en la película clásica de Christopher Nolan de Batman Que desaparece Desaparece un lápiz En la reunión con

## [01:19:31]

Donde dice que va a hacer un truco Sí, sí, sí Voy a desaparecer este lápiz Es la cosa más obvible Ok, bueno, ven Es como el mal desapareció el lápiz Dice, no, ven Ya no tengo No tengo Conectivos Desaparecieron esta coma de aquí es un O y esta otra de aquí es un I detalles detalles verdad pero no crean lo que él va a decir a continuación de cómo se hace cálculo de cuantificación asume esta forma o sea es un conjunto que contiene conjuntos esta es realmente la forma de las sentencias lógicas en el cálculo de la regla de resolución de Robinson o sea en el fondo lo que él dice es vamos a llevar a nuestras sentencias del cálculo de predicadas del primer orden a esta forma entonces aquí tiene sentido hablar de unión y de intersección porque son conjuntos y a eso es a lo que se refiere lo siguiente que vamos a ver en el documento cuando les digo que en notación de Robinson esto se puede

## [01:21:10]

escribir de esta forma vean, esto lo hago yo yo no lo he visto en ningún libro pero a mi se me ocurrió que tal vez podía ser un poquito más claro, si le ponemos un número a cada una de las cláusulas entonces este resultado va a poder, si lo escribimos en la notación de Robinson de esta forma con cuatro cláusulas ok, ¿alguna pregunta? después de todo esto bueno, otra vez nada más para no confundirme, ya te entendí lo de la sustitución de la variable única en el último, en el 8 pero entonces ahora me enredé con la del 3, creo que era que era lo mismo pero con los cuantificadores ahí es porque la x del para todo porque en el nombramiento X lo primero que era no era una cabeza y después iba a ser una cabeza, ¿es por eso que no se así lo cumple? ¿o es porque la X está en un para todo y en el otro más bien está en un existencial?

## [01:22:37]

Es que vemos aquí esto yo pude haberlo perfectamente escrito de esta forma para todo X existe un Y tal que C de Y y K de XY y eso implica que existe un Y tal que para todo Y para todo, sí, para todo, perdón existe un Y tal que A de Y y K de XY y el Y de aquí sería diferente del Y de acá porque está en el ámbito de un cuantificador diferente o sea, si yo perfectamente pudiera escribir Y aquí este y como ves es para hacer la importancia del paréntesis para decirme cuál es el ámbito de este cuantificador ¿verdad? entonces a eso es a lo que se refiere, pude yo haber duplicado los nombres de las de las variables porque estaban bajo el ámbito de cuantificadores diferentes entonces aquí me dicen no ma no hay enredos, o sea eso se pueden en general, sí es cierto, pero aquí me conviene que cada vara sea diferente y por lo tanto entonces renombro variables para evitar eso y eso es pero a nivel

## [01:24:00]

de cada, digamos de cada línea el X, el de arriba no importa con el de abajo, entonces así es, ok perfecto, sí, sí, a ver si yo pude haber yo pude haber puesto X Ah bueno, no, no, míralo aquí Yo tengo un X aquí y tengo un X aquí Y eso no es problema Cada línea puede quedar con sus propias variables En este caso Repetí el X Después se me desapareció por asuntos no existenciales ¿Verdad? Pero cada línea pudo haber quedado con un X Porque se entiende que son Xs diferentes Pero al llegar al paso 9 Digo, ya no hagamos eso Si usted le puso X a la primera póngale otro nombre a la segunda esto es como un doble filtro primero inicialmente para los existenciales y los buenos cuantificadores y ya después limpieza total exactamente, eso es eso es exactamente este ok, entonces ya llegamos a la posibilidad de hablar de la famosa regla de resolución la regla de resolución es la regla de inferencia

## [01:25:24]

que nos propone Robinson, y es divertido la forma en que Robinson la denuncia, ya les estoy compartiendo ¿no? Sí porque la regla de resolución se escribe así este sean un poquitito este ya les digo digamos que que Zoom sí que ese menú que tiene Zoom es muy inoportuno a veces digamos que C1 y este bueno me dejó en cambio el mate está bien C1 y C2 son cláusulas pero ahora van a ver C1 y C2 son cláusulas que contienen algo supongamos que C1 es usando la anotación de Robinson este Aquí hay una sentencia, se acostumbra usar lambda, entonces esta lambda está, digamos que hay un P, hay un Q, etc. hay otros predicados ahí y esto además lo voy a escribir de esta forma como el conjunto que contiene A lambda unión K, o sea K es el conjunto que contiene a P a Q y a todos los demás predicados que están en C1 y con C2 hago lo mismo solo que con una pequeña variante ya van a ver C2 es igual a

## [01:30:38]

la negación de lambda con algunos otros predicados que si yo de nuevo voy a usar estos más por falta de imaginación que otra cosa entonces esto se va a ver así como el conjunto que contiene A no lambda unión otro conjunto llamémoslo M Entonces, supongamos que tenemos una cláusula C1 y esa cláusula C2 que tienen esta forma. Entonces, la regla de resolución se ve de la siguiente manera.

## [01:31:58]

Yo voy a decir que se resuelven C1 y C2 de la siguiente manera. ¿Quién es C1? C1 es lambda unión K ¿Quién es C2? C2 es menos negación de lambda son sentencias unión M ¿Ok? Entonces esto resuelve en necesito un por tanto que está aquí por lo tanto K unión M ¿Ok? Esta es la regla de resolución. Esta es mi regla de inferencia nueva. O sea, yo puedo agregar K unión M a mi conjunto de sentencias ya creadas. Vamos a trabajar unos cuantos ejemplos para ver que esto realmente funciona una cosa muy divertida del cálculo de Robinson es que las reglas de inferencia de la lógica normal se vuelven teoremas en este en el cálculo de Robinson ok se me acabó el tiempo y ustedes seguramente están diciendo ir a almorzar

## [01:35:19]

Les propongo esto. Traten de demostrar, veanlo aquí, recordemos, ahí están. Vean, el dilema constructivo, modus tollens, modus ponens y el silogismo hipotético. Traten de demostrar estas cuatro usando la regla de resolución de Robinson. Mos Ponens, Mos Tollens Silogismo Hipotético y el Dilema Constructivo ¿Qué les parece?

## [01:36:18]

Y lo vemos el próximo jueves Sí, no hay nada No hay nada extraño El próximo jueves Recuerden que el jueves 29 de octubre, o sea Este jueves en 15 Es feriado en Cartago Entonces ese día no vamos a tener clase Pero eso está, el jueves en 15 Bueno, entonces Ya voy a terminar la grabación acá Gracias.
