---
clase: "Clase 7"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1077257764.m4a
modelo: large-v3
idioma: es
duration_sec: 5696.4
---

## [00:00:01]

El lenguaje CLIPS lo estamos poniendo como un ejemplo de otro tipo de lenguaje lógico que no es Prolog y que incluso usa una estrategia diferente, la de Forward Chaining, y al igual que Prolog en el fondo, es un sistema lógico que reduce todo a Mouse Phonics. O sea, en cierta forma, las mismas cláusulas que obtenemos del proceso de Robinson nos pueden servir para construir un programa Clips. solo que clips usa modus ponens entonces no es necesario en clips negar la conclusión eso solo se necesita en prolog esto que están viendo es un programa digamoslo así, inicial de principiante de como se vería un programa prolog, perdón, clips Como lo estoy viendo con... disculpen, lo voy a abrir con Word para que se vea mejor, para que podamos verlo con más definición.

## [00:02:32]

Ok, este, el lenguaje Eclipse admite tres tipos diferentes de definiciones, definiciones de reglas, definiciones de plantillas y definiciones de datos. recuerden que en el en el esquema que habíamos hecho de cómo funciona la máquina de inferencia o el ambiente de inferencia de Clips bueno, en general de cualquier sistema orientado a a reglas de producción tenemos por un lado una base de conocimiento y por el otro una base de hechos O sea, los hechos que son, que el sistema puede considerar como absolutamente verdaderos, como algo dado. Y la base de reglas sería el conjunto de implicaciones que resumen el conocimiento en esta área y que se consideran también válidas.

## [00:04:28]

Entonces, y las plantillas se utilizan para crear estructuras de datos.

## [00:04:44]

Ok, veamos esta sentencia de acá, por ejemplo. Este es un sistema muy primitivo, muy tonto, digámoslo así, para identificar animales. O sea, es un verificador taxonómico, podríamos decir. entonces, lo primero que salta a la vista es, lo primero que salta a la vista es que la sintaxis de todo lo que hay en Clips es la sintaxis de Lisp entonces, esto se ve rarísimo porque parece un programa en Skim por ejemplo, o en Lisp porque está usando la misma sintaxis o sea, todo cerrado entre paréntesis redondos y el primer elemento después del paréntesis abierto es el operador de toda la lista y lo que sigue entonces son los parámetros de ese operador entonces ese mismo sintaxis tiene clips veamos esto que está en gris empieza con la palabra def rule eso es una palabra reservada de clips yo les decía que en Clips hay tres cosas nada más que yo tengo que definir reglas hechos y plantillas

## [00:06:27]

entonces existe un dev rule dev fact y este dev template para las plantillas ok, lo que sigue después de dev rule es una es un nombre de la regla Todas las reglas tienen un nombre único. El propósito de esto es precisamente identificar, llevar un control en el momento de una ejecución, que yo quiero verificar que todo esté funcionando bien. o inclusive de que el sistema se explique que me diga por qué llegó a tal conclusión bueno, él dice, bueno, en primer lugar apliqué la regla R1 después apliqué la regla R3 después apliqué la regla R16 y así sucesivamente entonces la regla R1 vean que hay entre comillas un string y esto es nada más es documental es documentación para mi propio sistema ¿qué hace la regla R1? ¿cuál es el propósito de la regla R1? aquí dice que es identificar mamíferos la idea es que en este pequeño sistemita como ven que es la primera que aparece

## [00:08:17]

r1 es para identificar si el animal es un mamífero ok la mayor parte de los mamíferos de las especies de mamíferos tal vez el 99.9 por ciento de todos los mamíferos tienen pelo ok entonces vean lo que después viene de r1 de la identificación de la regla paréntesis la observación tiene pelo interrogación X y cierra el paréntesis ok bueno después sigue este símbolo y luego dice acert mamífero X ok ¿cómo se interpreta esto?

## [00:09:20]

esta regla se dispara si en el environment recuerdan esa estructura de datos el environment aparece un hecho en este momento esto es un identificador de una variable la idea es que yo diga por ejemplo, identifíqueme al espécimen al espécimen 20 entonces, espécimen 20 es un símbolo podría ser el valor de esa variable, si en el ambiente ya existe el hecho de que espécimen 20, o sea tiene pelo espécimen 20, o sea si eso existe entonces la regla R1 se dispara o por lo menos queda en la agenda, este es el antecedente de la regla, vean que eso está eso es impactivamente un implica o sea P implica Q ok, entonces si espécimen 20 tiene pelo, entonces vean lo que aparece, assert mamífero X assert es la manera en que yo pongo hechos nuevos en el environment en el ambiente, entonces si espécimen 20 tiene pelo entonces de una vez ya lo clasifica como un mamífero vean que este otra forma de

## [00:11:22]

identificar mamíferos es si las hembras dan leche en caso de que falle el asunto del pelo es que vean este hay algunos mamíferos como este hay más de si mal no me acuerdo hay como seis especies de un tipo de roedor que se llaman las ratas topo son unos animalones así no sé si exactamente son de la familia de las ratas pero son mamíferos que viven bajo tierra y que nunca nunca salen viven bajo tierra literalmente tienen unos dientes enormes permítame por favor ponerles para que ustedes vean como ven si alguna vez la naturaleza se empeñó en hacer un animal feo son las ratas topo hay de muchas especies como les decía son seis especies diferentes y no están necesariamente relacionadas cercanamente y lo que caracteriza a esto es un topo verdadero esto es un topo verdadero tienen pelo pero las ratas topo no tienen unas cuantas cerdas pero eso no se puede decir que

## [00:13:30]

tengan su piel cubierta de pelo no tienen pelo porque como no salen a la superficie no necesitan proteger su piel algunas tienen una vista muy débil pero hay otras especies de ratas topo que son completamente ciegas me parece que este es un ejemplo de esa especie los dientes frontales se han desarrollado así porque hacen los huecos precisamente con los dientes ok entonces por eso es que hay varios criterios para clasificar mamíferos porque no necesariamente el tener pelo es lo que o sea si un animal tiene pelo es un mamífero Pero no necesariamente si es un mamífero tiene pelo.

## [00:14:45]

Entonces, ¿cómo ven? Vean, por ejemplo, para identificar aves, el hecho de que tenga plumas, bueno, eso es definitivamente una, que yo sepa, no hay ninguna ave que no tenga plumas, o sea, que tengan su piel totalmente expuesta. pero en todo caso hay un par de criterios más y es el hecho de que vuele y que ponga huevos, bueno, ahora no todas las aves vuelan tal vez el de aquella pluma es más adecuado una vez que ya está identificado que espécimen 20 es un mamífero, entonces el hecho, mamífero, espécimen 20 va a aparecer en el environment entonces ahora preguntamos bueno, vemos, verificamos si en el momento actual en que está corriendo, mamífero este, existe ambos hechos, vean el mamífero y come carne el hecho de que estén así estas dos en el antecedente significa que es una y o la otra este si esto es así

## [00:16:11]

Entonces, esto implica que podemos meter en la base de conocimiento que el espécimen 20 es un carnívoro.

## [00:16:28]

Entonces, ahí se pueden clasificar todavía un poco más en ungulados, felinos. vean que no necesariamente ni en el antecedente ni en el consecuente tiene que haber una sola cosa lo que caracteriza esto es que más bien aquí en el antecedente siempre pregunto sobre hechos que están en el ambiente y en el consecuente siempre hay alguna un conjunto de acciones donde las acciones pueden ser como aquí agregue un elemento más en la base de conocimiento que por ejemplo el espécimen 20 es un leopardo, pero vean que también puede haber cosas como entrada y salida hago un printout esto es printout en la consola eso significa la T de la hilera es un leopardo ok vean esto cómo arranca esto cómo empieza ustedes pueden decir bueno todo eso está muy bien pero cómo sabe el sistema por dónde empezar bueno en el caso de Eclipse el ambiente va a estar vacío al inicio cuando esto arranca yo le digo

## [00:18:18]

a la máquina virtual oiga léase este este programa Eclipse este va a ser su conocimiento él lo lee y en el principio el ambiente va a estar vacío excepto por algo que se llama el hecho inicial entonces va a haber un hecho inicial, entonces vean que hay una regla que es el inicio de la identificación y dice, bueno si en el si en la base de conocimiento está el hecho inicial entonces pone esto en la pantalla el animal observado, vean que es una pregunta, el animal observado tiene pelo, sí o no, y vean que hace dos cosas primero lee la respuesta esta es una variable para la respuesta y va a decir, bueno, la respuesta uno fue sí o no ok, si la respuesta uno fue sí entonces es que pregunta Bueno, tiene pelo. Aquí incluso a esta regla le falta algo, ¿verdad? Debe haber un printout al principio que diga, perdón, indique una identificación para el espécimen. y le digo read ahí está ident

## [00:21:06]

y una vez que lo he leído hago un assert de specimen ident para que la identificación me quede me quede en el sistema ok, entonces a partir de aquí vamos a ver si el animal observado tiene pelo si o no, ok, la respuesta 1 si la respuesta 1 fue sí entonces hago un assert de que efectivamente el individuo tiene pelo hay una cosa que, perdón les dije que fue que es incompleta, disculpen clips en realidad tiene cuatro cosas que define O sea, puedo definir hechos, puedo definir reglas, puedo definir plantillas, pero puedo también definir funciones. o sea, en ese sentido Clips tiene un rango de posibilidades un poco más potente que Prolog porque yo sí puedo definir funciones matemáticas en Clips como objetos por aparte, como cosas por aparte entonces, bueno este es un pequeño ejemplo de lo que podría hacer un sistema experto, o sea, ¿cómo haría un experto para clasificar, este, para, por

## [00:23:47]

ejemplo, para clasificar a, si está habiendo un animal, ¿cómo hacemos la clasificación taxonómica del animal? ¿De qué es eso? Identificar la especie. ¿Cómo hago para identificar la especie, dado que estoy viendo un animal, entonces si bien aquí solo hay reglas como les digo también puedo definir plantillas para estructuras de datos puedo definir hechos como por ejemplo el hecho inicial y puedo definir funciones assert me sirve para poner cosas en el ambiente si, si tengo retract para quitar cosas en el ambiente retract y como ven todo tiene una sintaxis muy sencilla todo es en la forma de si P implica Q donde como ven si tengo varias cosas en el P supongo que cada una de ellas está unida por un I así vuela I pone huevos entonces haga esto y esto y esto y esto otro ok, ¿tienen alguna pregunta?

## [00:25:41]

todo claro, Sarita ok, muchas gracias vean que interesante, esto aún así todavía es una forma de una cláusula por la siguiente razón aquí esto ya es Word, así que voy a poner este documento las cláusulas nosotros vimos que son en la forma Por ejemplo P Q Este Un momentito No, no es ese No tampoco Eh, no Permítame un momento Bueno, ahí Qué dibujo más feo de una llave Y lo entendió bien Puedo tener P Puedo tener Q Puedo tener No R y no S esa S si me quedó horrible bueno aquí lo voy a corregir esto es P Q, no R y no S ok, esto como cláusula en la anotación de Robinson, en realidad está equivaliendo a este P o Q o no R o no S pero este o sea porque está en la forma normal este conjuntiva así que eso equivale a esto y entonces este ¿y qué es esto? ah, perdón, perdón ahí, final de semana final de semestre, final de año se me está juntando todo bueno, ustedes deben estar parecido o peor supongo

## [00:30:42]

entonces esto por supuesto que equivale a esto bueno, si bien si es cierto que nos está fallando aquí porque esto equivaldría R R o S a esto R o S la R vibrante siempre, toda la vida me ha dado muchos problemas de que esto implican bueno, está en los operadores yo creo, ahí está de que RIS implica POQ bueno, ahí nos falla un poco el operando pero no es difícil ver que este modificando un poco la forma, el esquema de producir las cláusulas podemos llegar a esta forma que esto, precisamente esto es una regla de Eclipse como ven bueno, Eclipse es un sistema de en cambio, como ven es de razonamiento hacia adelante yo no sé cuál es mi conclusión en este caso entonces voy preguntando bueno esto es una será esto una si tiene esto si tiene pelo entonces ok es un mamífero entonces ya sabiendo que es un mamífero entonces si es un mamífero y tiene gafas entonces es un carnívoro o si

## [00:34:15]

tiene pelo y tiene colmillos grandes, es un carnívoro. Entonces ahora tenemos todos los tipos de carnívoros, puede ser un cánido, puede ser un félido,

## [00:34:32]

podría ser un primate, los primates son también carnívoros, bueno somos también carnívoros obviamente, aunque no tengamos los colmillos así de grandes, los seres humanos. ¿Qué otros animales son carnívoros bueno, en fin eso no es el tema de la clase de hoy ok, esto es Clips y es la, digámoslo así un representante de la segunda variedad de lenguajes lógicos ¿tienen alguna pregunta? ¿alguna duda?

## [00:35:30]

yo no sé que lo hice pero vieran que yo tenía yo tenía un sistema experto para saber qué nudo de la corbata sería bueno sería bueno usar dependiendo de varios factores, pero no sé que lo hice ya estaba buscándolo para mostrárselos pero si bien es cierto que Clips, quiero resaltar eso, Clips nace en el contexto de la producción o de la fabricación de sistemas expertos basados en reglas de producción creció lo suficiente para hacer un lenguaje Turing completo Ok, empecemos con nuestro último paradigma, que es orientación a objetos, que es el paradigma que podemos decir fue el que casi hace desaparecer al paradigma imperativo. el paradigma imperativo solamente subsiste en parte por legacy code de código muy importante que fue escrito en lenguajes imperativos COBOL, FORTRAN, un poco en Pascal, C por supuesto todavía sigue produciéndose muchísimo código en C y código nuevo en C los físicos

## [00:37:42]

siguen trabajando muy duro en Fortran especialmente en Fortran en algunas de sus versiones en paralelo y eso es lo que mantiene vivo digamos al paradigma imperativo pero para lo que es programación comercial está crecido de una manera tan espectacular creando divisiones que hace muchísimo tiempo no existían como front end, back end gente ya habla del middle end desde hace un rato y bueno, programación orientada a objetos es una de las grandes normas en este momento, es el paradigma más usado los lenguajes, o sea cada vez que surge el lenguaje nuevo lo crean de una vez ya con orientación a objetos y si es de algún otro paradigma aún así le meten características de orientación a objetos ok, este volviéndonos muy atrás, yo les digo que Cobol en los años 60 logró, fue Cobol quien logró que la computación se difundiera a gran escala no fue la computadora en sí

## [00:39:06]

por supuesto que la máquina obviamente ayudó mucho, pero fue la aparición y la difusión del lenguaje Cobol lo que podemos decir que creó la industria de la computación se asentó a las bases de la industria de la computación tal y como la conocemos hoy en día porque las grandes corporaciones como digo aquí, empezaron a comprar o alquilar equipo computacional para automatizar sus operaciones y no solamente las grandes corporaciones privadas también los gobiernos oficina del censo los diferentes dependencias en Estados Unidos, por ejemplo el IRS el brazo armado digamoslo así, del departamento del tesoro o sea, el encargado de cobrar los impuestos no es de sorprender que entonces en Costa Rica las primeras entidades que tuvieron computadoras en los 60 fueron los bancos estatales la caja costavicense del seguro social me parece también que la municipalidad de San José la universidad

## [00:40:45]

de Costa Rica y bueno el ICE el ICE más que nadie porque el ICE necesitaba no solamente administración de cuentas sino también proyectos de ingeniería de gran escala que ocupaban muchos cálculos entonces además del ICE el acueducto se ha alcantarillado para cobrar entonces esta oleada como les digo alcanzó a Europa y Latinoamérica en realidad muy pronto, en cuestión de 5 o 6 años ya empezó a difundirse la computadora y la computación en América Latina solo que vean, en Costa Rica las primeras carreras de computación empiezan hasta los años 70 y segunda mitad de los años 70 inclusive en la Universidad de Costa Rica permitieron que se diera un desorden en este sentido la carrera que inició la computación como carrera bueno, fue la escuela de matemática la cabrera de ciencias de la computación era en realidad un asomo de lo que hoy se llamaría una cabrera de matemática aplicada

## [00:42:20]

usando computadoras esa era la intención de esa cabrera entonces, por ejemplo, en esa cabrera era muy rara en el sentido de que era una cabrera de computación pero no había un curso de sistemas operativos no había un curso de compiladores este no había ningún curso de, bueno, comunicaciones estaban en los sesentas y en los ochentas pero en setentas y ochentas estaba apenas empezando, entonces es razonable que no hubiera nada muy profundo en comunicaciones pero no había nada de eso en cambio la gente llevaba una cantidad enorme de cursos de matemática Por otro lado, el centro de informática de la Universidad de Costa Rica necesitaba programadores, pero la mayor parte de los programadores de ahí se hacían en la calle, ya se hacían por sí mismos. Eran que las compañías como IBM, Burroughs, Kit y Ramírez En ese momento en Costa Rica Les daban cursos cuando compraban la máquina

## [00:43:42]

Les daban cursos a unos cuantos empleados Cursos de Cobol y Hale Esos eran los programadores de esos años Ok, entonces el centro de informática de la Universidad de Costa Rica Dio un paso muy audaz y es empezar a dar cursos de computación pero inicialmente para formar programadores para ellos lo mismo que hacían las empresas solo que fuera el centro de informática quien diera los cursos lo mismo que hacían las empresas que vendían software o hardware de ahí yo no sé quién tuvo la peregrina idea en algún momento de crear una carrera completa con eso, con esos cursos no sé cómo habrá llegado a suceder semejante cosa desde entonces había una cosa rarísima como que el DATIC aquí en el TEC diera una carrera y que no tuviera nada que ver con la escuela de computación ni con computadoras, ni con ATI ni con nadie pero el DATIC tiene su carrera sería extraño ¿verdad?

## [00:44:55]

bueno, eso era lo que pasaba en la UCED en esos años y las universidades tardaron hasta la segunda mitad de los años 70 en crear carreras de computación en Costa Rica bueno, pero ok entonces el asunto fue así eso significó que las grandes corporaciones e instituciones públicas ocuparon implementar sistemas de software muy grandes y en muy corto tiempo aquí les pongo otro ejemplo el pentágono en el caso de los Estados Unidos o sea su departamento de defensa el gran reto tanto antes como ahora es implementar estos sistemas en el menor tiempo posible pero asegurando un nivel alto de confiabilidad, usabilidad y mantenibilidad ok, aquí tengo que hacer una una reseña, o sea tengo que detenerme un momento porque precisamente el cambio que está introduciendo inteligencia artificial en este momento en los sistemas basados en redes generativas de todo eso que estamos pidiendo

## [00:46:24]

en el menor tiempo posible con un nivel de autoconfiabilidad usabilidad y mantenibilidad lo único que estamos teniendo de fijo es implementarlos en el menor tiempo posible, eso nos nos ha servido para acelerar montones la implementación pero las otras características que son tan importantes como la primera siguen flaqueando o sea usted no puede suponer que el sistema que le fabrica una inteligencia artificial sea confiable o sea que ha atajado la mayor parte de las pulgas más grandes de que es fácil de usar de cómo vas a verlo si es una máquina que no está creando y que es sencillo darle mantenimiento tengo entendido que cloud está haciendo cosas interesantes en mantenibilidad introduciendo documentación interna en el código hasta donde tengo entendido yo nunca he usado cloud que se están esforzando porque los sistemas los programas que la inteligencia artificial hace, vengan también

## [00:47:45]

con comentarios internos que signifiquen algo para que los seres humanos podamos darles mantenimiento como digo aquí hay un dicho y es que si usted quiere que algo se fabrique rápidamente, barato y de alta calidad, usted siempre puede obtener solo dos de ellas bueno, a nosotros nos exigen las tres siempre ok, este, ¿cuál era el problema lo que estoy tratando de hacer es mostrar cómo surge el concepto de orientación a objetos o sea, orientación a objetos perdón que a veces se me viene un poco la sangre por la nariz perdón este orientación a objetos surge para resolver un problema un problema de desarrollo de software ese digamos es mi punto en esta parte de la presentación entonces quiero aclarar para ustedes cuál fue el problema que había y que resolvió orientación a objetos más o menos bien más o menos y por qué entonces eso se hizo tan popular bueno cuál era el problema

## [00:49:21]

de la programación imperativa en el desarrollo de sistemas grandes de información, nosotros ya habíamos visto esto en el diagrama de flujo de datos que si ustedes se fijan en el diagrama de flujo de datos lo que muestra es justamente los grandes grupos de datos y como fluye la información entre los grandes repositorios de datos y los círculos representan el conjunto de software que se alimenta de esos datos y produce más datos por ejemplo esta burbuja que dice recepción de pedidos recibe pedidos, cualquier cosa que eso sea y este alimenta algún repositorio que se llama pedidos, puede ser una base de datos puede ser un archivo ya pueden ser tablas en una base de datos o puede ser un solo archivo o varios archivos que conjuntamente codifica la información de pedidos pero no hay mayor detalle sobre los datos vean que por ejemplo recepción de pedidos usa pedidos y contabilidad de envío

## [00:50:58]

también usa pedidos o sea podría ser que haya operaciones que se hagan sobre un pedido que fueron definidas aquí en el módulo de recepción de pedidos y en el módulo de contabilidad de envío se podrían haber usado pero cuando se desarrolló este subsistema de contabilidad nadie sabía que esos este que esos procesos ya se habían desarrollado en recepción de pedidos entonces se escriben de nuevo en la vieja escuela a veces los programadores decidían escribir sus propias versiones por ego yo puedo hacerlo mejor a mi eso me parece muy feo yo lo voy a escribir mejor entonces puede ser por ignorancia puede ser simplemente ego o puede ser que efectivamente la primera versión era muy ineficiente ¿qué aprendimos durante estos 20 años de los 60 y los 70? que se tenía una visión de alto nivel para los datos, pero de muy bajo nivel para el proceso, en el sentido de que pensábamos en el

## [00:52:24]

proceso de una manera muy detallada y lo veíamos a los datos como algo que se usaba en el proceso o sea, el énfasis estaba en el proceso aunque Que desde hacía mucho tiempo, en el ambiente académico, se entendía que algoritmos más estructuras de datos es igual a programas. Y como ven, incluso el profesor suizo, Niklaus Wirth, bueno, él era suizo, pero con ese apellido probablemente era de la zona alemana, en cuyo caso esto se debería pronunciar Niklaus Wirth. ok, digamos que el profesor Wirth ya había publicado un libro que es que justamente tenía ese título, algoritmos más estructuras de datos igual, programas o sea, en su mayoría el medio académico de computación entendía esto por una forma muy general, o sea, conocíamos el tipo de datos abstracto pila que tenía necesariamente las operaciones asociadas push

## [00:53:54]

y POP. Pero precisamente por su generalidad, cada vez que se implementaba el tipo de datos en un sistema, se reescribían las operaciones adaptadas a cada caso particular. Por otro lado, también es cierto que desde antes incluso de que hubiera computadoras verdaderas, los programadores, por ejemplo, de Maresco 1, ya habían implementado una forma muy rudimentaria de, digamos, importar rutinas de cálculo en la fotografía está precisamente una de estas personas que fue programador en este caso programadora de la Mark I ella es Grace Murray Hopper y Hopper en una biografía de ella creo que la tengo por aquí, me parece que es este este Y creo recordar en esta bibliografía de ella que ella contaba que cuando alguien salía en esa máquina y le tocaba hacer una pequeña rutina para, por ejemplo, sacar una raíz cuadrada, calcular un logaritmo calcular una función trigonométrica entonces

## [00:55:37]

lo anotaban en una libreta que tenían a mano y esa libreta se volvió una especie de biblioteca de rutinas, entonces cada vez que alguien ocupaba un cálculo pedía prestada la libreta y copiaba lo que la rutina que aparecía en la libreta en su propio programa entonces ok no parece muy muy serio pero bien que mal ya era una forma de importar rutinas de cálculo o sea la gente entendía que desde hacía muchísimo tiempo que yo podía importar rutinas desde afuera y ponerlas en mi código o sea no tenía yo que escribirlas otra vez si alguien las había escrito en algún lado podía usarlas el lenguaje C por ejemplo consagró esto asimismo en el medio académico ya entendíamos que cuando usted crea una estructura de datos hay ciertos algoritmos que se asocian con esa estructura de datos para poderla manejar y este lo ideal lo correcto es usar esa estructura de datos utilizando solamente

## [00:57:16]

esas operaciones estándar que se definen por esa estructura entonces como les digo aquí costó algo de trabajo que la comunidad académica de computación uniera los puntos de todo esto de una manera muy tímida y igual que como les decía que pasó con Clips en el sentido de que querían resolver un problema y terminaron resolviendo otro este par de científicos noruegos estaban diseñando por ejemplo centrales nucleares y se les ocurrió que sería una buena idea que el software se comportara como un Lego O sea, ensamblando elementos ya creados, pero los elementos traían también las rutinas con las cuales se manejaba cada uno de esos elementos. Ese fue el lenguaje Simula. Ok, entonces eso es orientación a objetos. Es una forma muy sofisticada de, primero, pensar desde las etapas más tempranas de diseño en cuáles entidades, o sea, cuáles entidades serán usadas en el sistema.

## [00:58:42]

claro, cada una de esas entidades va a ser modelada utilizando una estructura de datos y qué relaciones tienen entre sí o sea, también podemos pensar en una jerarquización de estas estructuras además como les digo aquí se trata también de detallar desde etapas tempranas del diseño los algoritmos que deben manejar a estas entidades Y lo más importante de todo, escribir una sola vez todo el código relevante para el manejo de esas entidades y que el lenguaje facilite que no se pueda manosear ese código. En el fondo, abstracción y encapsulación son dos de las principales herramientas para eso. Sí, abstracción me sirve para concentrarme en los aspectos más generales del problema, pero la abstracción yo ya la habíamos utilizado mediante procedimientos, ¿cierto? los objetos me sirven para hacer abstracción pero el asunto de la encapsulación es hacer que el contenido de lo que está en el objeto

## [01:00:16]

sea opaco, usted no tiene que necesariamente verlo y eso impide que la gente se ponga creativa por dicha con este código por supuesto también podemos decir que el propósito o sea un un sub producto muy bueno de esto es es mejorar la calidad del software por una razón porque si ya yo tengo código ya ha sido probado ya se sabe que funciona bien le han encontrado en la mayor parte de las pulgas que tiene entonces ese código que es de buena calidad lo puedo compartir y eso puede ayudar entonces contribuye a mejorar la calidad del código nuevo porque hace que estas piezas que son relativamente confiables se puedan usar dentro de mi código ok todos ustedes creo ya llevaron ya llevaron el curso de PO o sea de programación orientada a objetos así que esto me imagino es nada más un mero repaso ok entonces en que consiste

## [01:01:52]

orientación de objetos. Bueno, un objeto que es, bueno, es un elemento de datos que puede ser simple, compuesto, que está dotado de otros elementos de datos que se denominan el estado del objeto. Por ejemplo, en el caso de una pila, hace falta algún dato adicional que diga si la pila está vacía o no y si no lo está qué elemento está en el top de la pila y tal vez si es relevante si la pila crece para arriba o crece para abajo y además en un objeto están metidos los módulos de software que le dan mantenimiento al estado del objeto esos son métodos y que comunican datos del estado a otros objetos esos son mensajes, o sea el objeto define también qué se le puede preguntar qué mensajes me pueden enviar en consecuencia cualquier lenguaje que se diga del paradigma de habitación de objetos consiste en medios para definir los objetos y sus estados secuencias de mensajes entre objetos

## [01:03:17]

y secuencias de métodos que son internos a cada objeto ok, este permítanme un momento ¿tienen alguna pregunta?

## [01:04:07]

¿coincide esto con lo que usted quería? ¿hay algo que me haya faltado? ¿y que a usted le gustaría agregar?

## [01:04:18]

creo que nada más ahí los mensajes son como llamadas a los métodos o son como o sea que sería como más o menos un mensaje en este contexto bueno, sí, por supuesto al mandarle un mensaje a un objeto eso dispara un conjunto de métodos puede que sea solo uno, o puede que sean varios efectivamente ok sí, se mantiene el mismo concepto sí este por supuesto, el asunto es este el Estado está construido también con objetos, o sea, son objetos internos al objeto riandote. Entonces, en vista de que los métodos se refieren a los objetos del Estado, los métodos a su vez son mensajes también, solo que se envían desde adentro del objeto y que están encapsulados en el objeto. Entonces, en el fondo, los métodos también son mensajes. Así que yo podría hablar solamente de los atributos y los mensajes, para ser más preciso.

## [01:05:52]

Ok, perfecto. Con mucho gusto.

## [01:05:59]

Ok, hay varios tipos de mensajes, ¿verdad? Hay mensajes que modifican el estado del objeto.

## [01:06:08]

Hay mensajes que solicitan información de estado. solamente dígame qué característica tiene determinado elemento de su estado me faltó este último de acá este es que hay otros mensajes que son muy interesantes porque son mensajes que solicitan elaboración de información pero no toda la información está en el mismo objeto Entonces se solicita información elaborada con el estado, pero que requiere información de otro objeto. Entonces yo le envío a un objeto determinado, oiga, yo necesito que usted me dé este dato. pero resulta que para obtener ese dato este objeto tiene que comunicarse con otro objeto para que ese otro objeto le mande la información y este entonces termine de elaborar la información que le está siendo solicitada desde otro lado a eso se deben estas rayitas de aquí entonces podríamos decir que estos son los tres tipos de mensajes que existen en el mundo

## [01:08:33]

de orientación a objetos ok, entonces ¿cómo se ve un programa en orientación a objetos? bueno podemos decir legítimamente que un programa orientado a objetos es un ecosistema de objetos si hay un conjunto de objetos que se mandan mensajes entre ellos que elaboran información hay un objeto main que es el que arranca todo el objeto main le pide a algún objeto que, por ejemplo, obtenga información para que se la devuelva a main o main le pide a este objeto, vea modifique su estado para hacer determinada cosa main le puede decir a este otro objeto, oiga ahora necesito que usted haga tal cosa pero este objeto, a su vez el de color negro, necesita para hacer eso, información que ya el primer objeto el del gris tiene entonces un programa orientado a objetos solamente es un objeto bueno, hay un objeto main otros objetos que por supuesto se definen a partir de una clase, cada uno de ellos, y el

## [01:10:24]

programa es la secuencia en un cierto orden de los mensajes que yo puedo mandar a los objetos eso es un programa en orientación a objetos en su forma pura entonces esto ya nos permite comparar todos los paradigmas ¿cómo se ve un algoritmo en orientación a objetos?

## [01:10:56]

bueno ya habíamos visto que este es más aquí debería decir una cosa decíamos, yo les había dicho desde el puro inicio del curso que la definición de algoritmo que vamos a usar es la de una secuencia de tareas que según que se ejecutan

## [01:11:33]

este o que se llevan a cabo más bien aquí podríamos poner incluso la palabra elaboración O sea, tareas que se elaboran en cierta secuencia, donde el conjunto de tareas es finito, el tiempo en que se lleve a cabo esa elaboración es finito también, y utiliza una cantidad finita de recursos. y desde el inicio del curso les ponía el énfasis en que estamos hablando de tareas, ¿por qué? bueno, porque esas tareas en el paradigma imperativo procedimental son instrucciones, entonces lo que tengo yo es una secuencia de instrucciones que se ejecutan, o sea la elaboración de una tarea es ejecutar la instrucción, así que correr un algoritmo en el paradigma imperativo es ejecutar la secuencia de instrucciones. Ya vimos que en el paradigma funcional esto cambia, porque ya no tengo instrucciones, tengo funciones. Estamos hablando de computabilidad de Church.

## [01:13:07]

Incluso podríamos decir que el paradigma imperativo, estamos hablando de computabilidad de Turing tal vez hay un poquitito más si entonces en el paradigma funcional lo único que tengo son funciones entonces cobrar un algoritmo es evaluar funciones, entonces a partir de una función main esa función main se descompone en otras funciones y yo lo que hago es evaluar funciones eso es un mecanismo de evaluación ok, el paradigma lógico que acabamos de dejar todos son sentencias lógicas entonces en el fondo lo que hacemos es una descripción en cálculo de predicados de primer orden del algoritmo entonces la elaboración del algoritmo será demostrar la veracidad de alguna sentencia universal o existencial OOK, orientación a objetos cuáles son las tareas son mensajes o sea, un mensajes o métodos pero en el fondo todos son mensajes como les había dicho como le explicaba Andrés

## [01:15:00]

entonces, ¿cómo se elabora un cada uno de estos mensajes? bueno es el envío del mensaje lo que este consiste la elaboración o el llevar a cabo una tarea. Puesto que la tarea es un mensaje, entonces consiste en ya sea mandar un mensaje de vuelta con la respuesta o modificar el estado de un objeto. Yo sé que suena muy raro lo que voy a decir y es lo siguiente. En ningún lenguaje verdadero de orientación a objetos hay instrucciones lo que debería haber son solamente mensajes ok pero ustedes han pasado toda una vida pensando que Java y Python son lenguajes orientados a objetos y ustedes pueden estarse preguntando oiga, ¿qué está diciendo este sujeto? porque en Python y en Java sí tengo instrucciones y en C++ todavía peor porque C++ es prácticamente C este bueno es prácticamente C aunque C++ es un poquitito más más cuidadoso en la forma de generar código perdón, pero

## [01:16:59]

sí, en Python hay instrucciones y Python es orientado a objetos, ¿no?

## [01:17:06]

sí y no al tener instrucciones tanto Java como C++ como python se ponen en un en una zona gris intermedia entre verdadera orientación objetos el paradigma imperativo ok entonces ustedes pueden a su vez hacerse otra pregunta o hacerme otra pregunta y es ok entonces cuál sería un lenguaje verdaderamente orientado a objetos si usted tuviera razón, podría pensar ustedes, genuinamente ¿verdad? o sea, recuerden, la esencia de la universidad es que usted puede cuestionar cualquier cosa o sea, hacer cuestionamiento válido usted puede pedir, hacer buenas preguntas y exigir que le den buenas respuestas, entonces si alguien me preguntara cuál sería un programa para mí, verdadero de orientación a objetos yo le respondería Smalltalk O Su pariente más cercano Este Que se llama Squeak Esa es verdadera orientación a objetos Esa es de verdad Ok, entonces ustedes se preguntan

## [01:18:56]

Bueno, ahora eso nos lleva a otro problema Y es ¿Por qué Se desarrollan lenguajes Como Java o Python Si no son Verdaderamente orientados a objetos Y hay otra pregunta que surge y es al darles instrucciones podrían arrastrar los vicios del paradigma imperativo bueno la respuesta a la primera pregunta de por qué estos lenguajes tienen instrucciones bueno la respuesta es que hasta ahora es que tenemos programación hecha por computadoras desde hace más de 80 años que habíamos estado haciendo programación hecha por personas y si a ustedes por ejemplo le enseñaron a programar en C y le dicen bueno queremos un lenguaje nuevo que tenga otras ventajas que C no tiene la idea es esta la cantidad de software que se necesita en el mundo es cada vez mayor cada vez más cosas están pasando a la digital piensen en esto este vamos a ver si tengo alguna por aquí no sé si han visto

## [01:20:49]

por ejemplo las moneditas de 500 colones que están circulando desde hace ya unos meses no sé si han notado una característica muy peculiar de esas monedas y es el poco desgaste que tienen ¿por qué les llamo la atención de esto en este contexto en que estoy hablando? bueno, porque yo me pregunto ¿por qué esas monedas no están gastadas? y la razón es que cada vez menos gente usa dinero físico en el bus del TEC por ejemplo es una rareza el estudiante que paga con billetes y monedas lo más común es que la gente use una tarjeta de crédito o hacen una cosa que para mí que soy de la vieja escuela me parece todavía muy peligroso y es de ahí, usa su teléfono a mí esto me parece peligroso porque como programador viejo que soy y como alguien más o menos familiarizado aunque sea un poquitito con seguridad informática, sé que este bicho es muy vulnerable.

## [01:22:39]

Así que darle mi información financiera a este aparato, vieran que a mí me crispa. Es algo que, como les digo, tal vez es maña de la gente vieja, mala maña, pero yo desconfío mucho y yo no tengo ninguna, pero ninguna aplicación bancaria en el celular, ninguna vieran que eso me ha dado algunos problemas porque a veces voy a comprar alguna cosilla en un puestito de alguien, algún emprendedor, por ejemplo, tiene una cosita ahí que está vendiendo y es un producto de buena calidad y bonito y le dice no, no, mándeme un simple ay, qué pena, yo no tengo eso aquí en el teléfono pero, ¿qué quiero decir con esto? Que la cantidad de software, porque todo eso se mueve entonces a través de tecnología digital, entonces la cantidad de software nuevo y además software viejo al cual haya que darle mantenimiento es cada vez más grande. en el fondo lo que la inteligencia artificial está eliminando

## [01:23:59]

es a los programadores pero no a los profesionales en computación los profesionales en computación todavía necesitamos saber de lenguaje de programación aunque alguien más programe por nosotros todavía necesitamos saber cómo funciona una computadora aunque no vayamos a abrir una computadora y con un cautín empezar a atravesar los circuitos entonces, no crean, en el futuro va a seguir habiendo un curso de lenguajes de programación y vamos a seguir enseñándoles a programar y vamos a seguir dándoles arquitectura de computadoras pero ya no para que programen sino para que sean más capaces de someter a testing darle mantenimiento y verificar la correctitud de código generado automáticamente eso no es nuevo yo bueno relacionado a eso no acuerdo de donde leí una frase creo que era de alguien que trabajaba en una empresa ya grande que decía que la programación murió pero la ingeniería

## [01:25:27]

está más viva que nunca bien que eso muchas gracias por tu aporte efectivamente hay mucho de verdad en eso pero yo creo que decir que la programación murió es exagerado porque eso supone que ya hemos encontrado todos los algoritmos posibles que vamos a necesitar para el procesamiento de cualquier tipo de información sí, eso sí, pero di creo que él era como CEO o algo así de una empresa, di, así que tiene que venderlo como sea tienes razón, tienes toda la razón en eso sí es cierto, pero por ejemplo a mí me entristece mucho que la gente o sea que no sea motivada a pensar en algoritmos nuevos o sea muchas veces nosotros pensamos en los algoritmos y uno de los motivos era porque había que programarlos pero este tipo de inteligencias artificiales no diseñan algoritmos nuevos porque esta inteligencia artificial es si ustedes lo quieren ver así la automatización de una biblioteca

## [01:27:02]

eso es lo que es automatizar bibliotecas antes, en los viejos tiempos si usted necesitaba información ¿qué hacía? antes de que hubiera computadores o de que estuvieran tan disponibles más bien de ahí iba a una biblioteca revisaba el fichero este o algunos de los ficheros había tres tipos de ficheros unos ordenados por obra otros ordenados por autor y otros ordenados por palabras clave entonces uno se iba a palabras clave veía cuáles libros o revistas tenían esa misma palabra clave uno mismo se iba a buscar lo de los estantes en el caso de las bibliotecas de las universidades y le hace los libros ok ¿qué ha cambiado? bueno que ahora es una computadora la que contiene a todos los libros y por lo tanto localiza todas las palabras clave y yo entonces simplemente digito con una frase en español pero medio torcida porque yo ya sé que la inteligencia me entiende mejor si yo digo esto

## [01:28:32]

que si yo digo otro si yo le meto muchos sinónimos entonces se confunde entonces me empiezo a acostumbrar como a pedirle cosas ¿verdad?

## [01:28:43]

así que es la misma vara es la misma vara que antes o sea depende de la información que ya exista en la biblioteca no inventa nueva información bueno a veces si la inventa y decimos que alucina ¿verdad? y es cuando empieza a mezclar información sin ton ni son pero inventar algoritmos nuevos esta inteligencia es muy limitada para crear algoritmos nuevos es muy limitada porque T es lo que usa es un poder combinatorio cosas tan maravillosas como por ejemplo el algoritmo Quicksort, yo no esperaría que una inteligencia artificial pudiera crearlos a menos que haya muchos ejemplos que se parezcan y que entonces crea una versión juntando todo de los que ya existen solo en esos casos como dice Andrés es para facilitar la migración de código lega en parte pero en parte también lo que es legacy es la forma de pensar de los programadores que ya se habían acostumbrado al lenguaje del

## [01:30:22]

antiguo tipo. Hay un detalle que se toma en cuenta y es curva de aprendizaje, o sea cuánto tiempo va a tardar usted en dominar por lo menos lo más básico del lenguaje como para ponerse a programar ya.

## [01:30:42]

Si hay algo a lo que son alérgicas las empresas pero muy alérgicas es a entrenar a su personal y si lo hacen lo hacen una sola vez cuando usted empieza y a partir de ahí es puede ser usted solo porque para ellos significa tiempo productivo que usted no va a estar produciendo para la empresa sino que va a estar aprendiendo y que los empleados ganen cosas para ellos y que no produzcan dinero a las empresas no les interesa además o las empresas les parece muy feo pagarle educación a un empleado porque dicen ok yo le pago a este le doy educación a este empleado entonces yo le pago por adquirir educación y resulta que eso hace que este empleado entonces ahora sepa más y con eso puede irse a otra empresa y la otra empresa no pagó por la educación de él se pare yo ese es el tipo de cosas mezquinas en las que los empresarios se fijan entonces hay cierta inercia dependiendo de los seres humanos

## [01:32:14]

sería muy interesante ver si por ejemplo los humanos también tienen que interpretarlo si a largo plazo esto va a lograr que lenguajes de programación tan sofisticados y tan elegantes como Smalltalk empiecen a ganar un poco de momentum, un poco de impulso, ya veremos a mí me encantaría que ya nos podamos olvidar de Python y de Java, pero como muy acertadamente nos dice Andrés por ejemplo en Python la cantidad de bibliotecas que hay para Python, para hacer lo que usted le dé la gana, ¿verdad? Por ejemplo, Python tiene bibliotecas para que usted pueda cobrar el código Prolog. Tiene bibliotecas para que usted pueda cobrar el código Haskell en un programa Python. Tiene bibliotecas como PyTorch o NumPy para poder trabajar con redes neuronales y con aprendizaje mecánico, aprendizaje estadístico. tiene bibliotecas para poder crear ambientes gráficos bien bonitos y así en general

## [01:33:49]

entonces también esto le da una cierta inercia a estos lenguajes ok vamos a seguir hablando entonces un poco más de orientación a objetos y voy a hacerle propaganda a lenguajes Molotov en las próximas clases ok, hoy es jueves 5 así que nuestra próxima clase virtual va a ser la semana entrante el próximo martes 10 de noviembre ok entonces nos vemos en la semana entrante y espero que todo les salga muy bien estamos en final de semestre y espero que todo les salga perfecto en este final de semestre así que feliz fin de semana también y buenas tardes, hasta luego, nos vemos muchísimas gracias profe, igualmente, feliz fin de semana nos vemos
