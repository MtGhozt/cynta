---
clase: "Clase 5"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1327675611.m4a
modelo: large-v3
idioma: es
duration_sec: 6418.7
---

## [00:00:02]

Ok, les había dicho que en el paradigma lógico tenemos que demostrar cosas, pero no nosotros.

## [00:00:15]

Mediante software estamos dotando a la computadora de una verdadera máquina de inferencia. En otras palabras, un tipo de manejo simbólico que le permita codificar sentencias lógicas y mediante mecanismos también lógicos, lógicos en sentido estricto, en sentido de la disciplina, pueda llegar a concluir, ya sea a conclusiones verdaderas o a admitir que no pudo llegar a demostrar la conclusión que nosotros queríamos que, que encontrara, que demostrara. Y permítame agregar que esto último puede ocurrir por dos razones. Una, porque no tenemos suficiente conocimiento para poder llegar a la conclusión que queríamos. O sea, la conclusión es verdadera, si existe una demostración, sólo que hay algunas premisas que necesitamos y que no tenemos en nuestro conocimiento en este momento esa es la primera razón, la segunda es simple, llanamente pues que la sentencia es falsa

## [00:01:47]

y entonces de la misma forma no podemos construir una demostración para esta para esta sentencia hay una discusión aquí entre profesores de la escuela para tratar de adaptar el plan de la carrera a las nuevas realidades de la construcción o fabricación de software ok entonces perdón por la distracción decía entonces tenemos que hacer que la computadora construya demostraciones ¿cómo nos escapamos de la contradicción, digámoslo así, o si quieren llamarla así, la paradoja de Turing, llamémosla de esa forma, aunque Turing nunca habló de eso, de que cómo estamos haciendo programas que demuestren cosas, cuando Turing demostró que tal programa no puede existir. Bueno, el asunto está así. Lo que Turing demostró Es que en general no puede existir un programa determinístico que pueda demostrar cosas.

## [00:04:21]

O sea, que pueda siempre encontrar la demostración de alguna sentencia. entonces de que por qué seguimos insistiendo en los lenguajes lógicos bueno, en primer lugar si revisamos con cuidado el sistema de de Robinson de Prolog vemos una cosa y es que justamente Prolog es teoría incompleto pero teoría incompleto precisamente significa que solamente puede hacer lo mismo que una máquina de Turing y viceversa y precisamente Turing demostró que la máquina de Turing no puede demostrarlo todo, en primer lugar en segundo lugar en realidad el sistema Prologue se basa en una versión restringida del cálculo de predicados porque lo único que admite son cláusulas de Horn no admite todo tipo de cláusulas, precisamente para eludir la segunda parte del problema de Turing a saber que en el fondo lo que Turing demostró es que no existe un algoritmo determinístico ¿qué quiere decir eso? de que si admitimos

## [00:05:53]

backtracking y le damos al sistema todo el conocimiento que necesita eventualmente tal vez en uno o dos millones de años para los teoremas más difíciles pueda encontrar la demostración pero de nuevo vean vean la la sutileza de ese punto de si le damos toda la información que necesita recuerden lo que dijo Erdős sobre el teorema de bueno sobre el problema de de Collatz él dijo, la matemática no está suficientemente madura para responder esta pregunta is not ripe enough o sea que en caso de que sea cierta todavía no sabemos todo lo que hay que saber para poderlo demostrar como les decía por ejemplo también otro caso muy famoso el último teorema de Fermat que no era tal teorema era una conjetura el que dice que si yo tengo x a la n más y a la n igual a z a la n para n entero por supuesto para n mayor que 2 no existen tres números reales tales que satisfagan la ecuación para n mayor que 2

## [00:07:38]

para n igual a 2 y para n igual a 1 la respuesta es obvia de hecho para n igual a 2 es lo que se llaman las ternas pitagóricas pero para n igual a 3 y ahí en adelante 3, 4, 5 la suposición de de Fermat era que no existían tres números que satisfacieran eso perdón, para A, B y C enteros para A, B y C enteros y N o sea, para todo el mundo entero entonces parecía que era verdadero pero fue hasta 1996 en que Andrew Wiles un matemático inglés basado en el trabajo en unos casos especiales de otro matemático japonés de apellido Taniyama fue que pudo demostrarlo y aún así fue cuando la primera vez que él enunció la demostración bueno primero duró cinco días explicándola así de larga es o sea, pidió a la universidad donde él trabajaba, no sé si fue Cambridge que le dieran permiso de hacer un seminario de cinco días sobre unos cuantos resultados en teoría de números

## [00:09:35]

bien, típico de esas universidades por supuesto que le dieron el permiso pero él no dijo que era lo que quería hacer, no que dijo que era lo que quería demostrar fue ya cuando llevan como por el tercer o el cuarto día que la gente sí se dio cuenta de que era lo que en el fondo iba quería demostrar y entonces el auditorio donde estaba dando la conferencia se llenó, pero aún así cuando él terminó y digamos creo que fueron como 15 días en que otros matemáticos ya examinaron con todo cuidado la demostración, se dieron cuenta de que había tres huecos en su demostración, había tres cosas donde decía bueno, si tenemos esto podemos concluir tal cosa no, yo no veo por qué usted pega este brinco de aquí a acá sea más detallado y entonces se tardaron como un par de meses más en cubrir esos tres huecos en la demostración porque faltaba información verdad, este o sea, el teorema de Turing

## [00:10:46]

tiene que ver inclusive con el hecho de que tengamos, de que no sabemos si tenemos toda la información a mano No sabemos si tenemos toda la información necesaria disponible. Así que por eso estos programas o estas máquinas de razonamiento no violan el principio de Turing porque puede que no puedan encontrar una demostración que sí exista y ellas tampoco puedan. Ok, entonces, habiendo aclarado ese punto teórico que es muy importante, vimos que, al contrario de los otros paradigmas, aquí se crea un abismo en la forma de construir estos programas o estas máquinas de demostración, básicamente, porque hay dos formas de demostrar. a saber de construir una demostración mentalmente a saber backward reasoning y forward reasoning backward reasoning es cuando yo empiezo con la conclusión y voy para atrás eso es prologue y ya vimos un ejemplo en clase aplicado a un teorema geométrico

## [00:12:10]

como podríamos tal vez construir esa demostración de de atrás para adelante perdón, de adelante para atrás, o sea empezando desde el final preguntándonos, bueno, si para que esto sea verdadero, ¿qué necesito previamente que sea verdadero?

## [00:12:30]

este y la construcción hacia adelante es la de partir de las premisas y ver si de alguna manera puedo llegar a la conclusión y este otra clase de lenguajes como ven entonces tienen una máquina una máquina de demostración muy diferente y además bueno tienen elementos en su máquina virtual que Prolog no necesita o los lenguajes parecidos a Prolog más o menos está claro esto tienen alguna pregunta les gustaría que ahondara más en algún aspecto que no te haya quedado claro yo creo que todo está perfecto profe, al menos por mi parte muchas gracias Matías todo claro muchas gracias muy amables ok, entonces y Andrés no vimos otras características de Prolog en los Guillermo, gracias este, o sea, Prolog puede manejar listas Prolog no tiene vectores ni tiene matrices o sea, cualquier estructura de datos compuesta que quiera crearse debe ser implementada mediante listas una virtud

## [00:14:18]

de las listas de Prolog es que los elementos de la lista pueden ser de cualquier tipo que usted quiera O sea, usted puede construir una lista de listas, si usted quiere, y usted puede mezclar flotantes con enteros, como usted lo necesite, en una misma lista. O sea, puede tener un nodo que tiene un entero, y ese nodo que tiene un entero tiene a la par otro nodo que tiene un número de puntos flotantes. inclusive, usted puede tener una lista donde algunos de los elementos de la lista no están determinados todavía, o sea, no están instanciados eso es perfectamente legítimo al contrario, por ejemplo, recuerden en el paradigma funcional las listas de Haskell donde todos los elementos de la lista debían ser del mismo tipo Prolog no, Prolog no necesita eso por razones de tiempo no podemos ahondar demasiado en prologue, pero porque tenemos que ver este otro paradigma.

## [00:15:39]

Bueno, esta versión del paradigma, la de forward reasoning. Recuerden que el problema que nos preocupa no es que ya tengamos la demostración lista. O sea, como los libros de matemática, que uno ve tal cosa, demostración, y la demostración que aparece en los libros de matemática siempre parece ser forward reasoning o sea, siempre es forward reasoning porque empezamos con las premisas y con todos los teoremas anteriores que ya se han demostrado y se procede de ahí hasta que al fin ¡pum! de una manera maravillosa aparece la demostración pero aquí no se trata de eso exactamente se trata de el proceso de cómo alguien encontró esa demostración o sea es muy posible que especialmente en demostraciones complejas en demostraciones grandes la demostración se haya construido por pedazos y algunos pedazos se construyeron forward y otros pedazos se construyeron backward y después se ensambló

## [00:16:53]

todo y parece que qué talento el de este matemático sí, muy talentoso pero nada menos fue un desorden terrible mental para poder llegar a la demostración y aquí necesitamos una máquina que sea capaz de por así decirlo imitar el modelo mental humano de construir una demostración hasta cierto punto Vean que yo no estoy incluyendo a la hora de considerar demostraciones, no estoy incluyendo a las redes neuronales o a los sistemas de inteligencia artificial generativa que utilizan redes de convolución para considerar una demostración ¿Por qué? ¿Por qué yo no considero eso dentro de sistemas de demostración? A pesar de que, de vez en cuando, con bombos y platillos, alguno que otro, compañía, dicen que gracias a la inteligencia artificial ya demostramos tal cosa.

## [00:18:15]

Hay que ser críticos, no acepten eso de buenas a primeras. vean creo que fue alrededor de los años 30, aunque no estoy muy claro con la fecha no sé si fue en los 30 o fue 20 años después de los 50 pero un filósofo inglés llamado Bertrand Russell dijo lo siguiente si yo cuento con un tiempo suficientemente largo y lleno una habitación con chimpancés y a cada chimpancé le doy una máquina de escribir recuerden eran los 30 o incluso los 50 y yo entreno al chimpancé para que oprima teclas al azar de la máquina de escribir y les damos una cantidad suficientemente grande de papel entonces si tenemos si exponemos un tiempo suficientemente largo pues podremos producir ahí la Ilíada o Hamlet porque desde cierto punto de vista estas obras no son más que la combinación de caracteres de escritura y si yo puedo disponer de un tiempo suficientemente grande para no decir infinito

## [00:20:07]

de un dispositivo mecánico en este caso los chimpancés que puedan generar hileras al azar pues eventualmente se toparán con la ilíada ¿verdad? yo no sé por qué nadie ha señalado que la inteligencia artificial generativa es precisamente este grupo de chimpancés solo que en lugar de oprimir teclas al azar lo que están haciendo es juntando pedacitos de palabras donde mediante algún mecanismo de recompensa hay algunos pedacitos que les gustan más que otros y simplemente juntan los pedacitos dependiendo de eso dependiendo de de que tan atractivo es dar un pedacito poner otro a la par ok entonces como es que las computadoras de estas inteligencias demuestran cosas entre comillas bueno es que ni siquiera están demostrando nada primero han sido entrenadas estrictamente con los teoremas o sea con los textos de los teoremas que un grupo de matemáticos consideraron que es lo relevante para este

## [00:21:39]

campo de conocimiento en el cual quieren demostrar algo y después de entrenarlos con este grupo de textos específico por más grande que sea el conjunto de textos lo único que saben hacer partirlo en pedacitos y decir bueno esta está a la par con una probabilidad tanto, esa está a la par de este otro con una probabilidad de tanto, e inclusive ni siquiera calculan las probabilidades las redes neuronales lo que hacen es simplemente mediante entrenamiento saber que, entre comillas que es dado este it's more likely que este otro esté a la par eso y entonces agarre usted unos 200 o 300 mil procesadores con sus correspondientes tarjetas de este de gráficos y déjelos cobrer, qué sé yo, un par de semanas a ver si acaso generan algo que tenga sentido a ver si acaso así como todos nosotros le preguntamos cosas y sale a veces como una burrada que de padre señor mío

## [00:23:02]

pues estas otras a la hora de mostrar cosas también muy posiblemente los matemáticos que estaban en eso tuvieron que remendar partes del texto producido así que esa es la razón de que yo ni siquiera me detengo a considerar esto como sistemas de demostración como tales en cambio estos otros dos sí ¿prejuicio? tal vez no lo no lo descarto pero esa es mi justificación ok Ok, entonces quiero darles un ejemplo de más o menos cómo funcionaría un sistema de encadenamiento hacia adelante para producir una demostración.

## [00:23:52]

Ustedes dirían, bueno, ¿y para qué se molesta si eso se parece a cómo están las demostraciones en matemática? No exactamente, porque recuerden que lo que nos interesa es el proceso de construir la demostración. Y ahí entonces hay una sutileza que quiero que conozcan.

## [00:24:25]

Entonces quería plantearles una vez más un caso basado en geometría euclidia básica que yo tengo la esperanza humilde de que los sistemas de educación secundaria de Costa Rica no esté tan pero tan pero tan mal ya en este momento que ya ni siquiera le dan geometría en los cinco años que están en la secundaria espero por favor corrijanme si estoy equivocado, si vieron ustedes geometría en la secundaria si no lo vieron no fue culpa de ustedes ¿verdad? no sé, ¿alguien que me quiera contestar?

## [00:25:25]

lo básico, profe, no sé ya, bueno, pero si vieron algo por lo menos ok ok, gracias bueno, espero que entre lo básico esté lo que vamos a hablar yo me imagino que sí, porque este es uno de los sermones más básicos, básicos, básicos de geometría euclidia de nuevo no, no, no estoy hablando de la demostración sino de cómo encontramos con encadenamiento hacia adelante la demostración de que la suma de los ángulos internos de un triángulo es un ángulo llano o sea la suma de dos ángulos rectos bueno, ¿cuáles serían nuestras premisas? ¿con qué contamos desde el inicio? bueno primero con el quinto postulado el quinto postulado si se acuerdan Es aquel que dice que dadas dos líneas rectas paralelas, perdón, dada una línea recta, disculpen, dada una línea recta y un punto exterior a esa línea recta, existe una sola línea recta que pasa por el punto dado y es paralela a la recta original. Una sola.

## [00:26:57]

Este es el fundamento de la geometría Euclidia. Gracias a ese postulado se demuestra que si hay una transversal entre dos paralelas,

## [00:27:15]

entonces los ángulos correspondientes entre paralelas son iguales. O sea, el ángulo que está marcado aquí en rojo de la recta B y la transversal tiene la misma medida que el ángulo que se forma entre la misma transversal y la recta paralela A. Estos ángulos se llaman correspondientes y basado en el quinto postulado se puede demostrar que tienen la misma medida. otra premisa con la que contamos es la igualdad de la medida de ángulos internos, perdón, de ángulos alternos internos o sea, dadas las dos rectas este y la transversal el ángulo beta y el ángulo alfa, que son alternos internos tienen también la misma medida permítanme un momentito nada más porque también podemos demostrar otra cosa que es importante acá que necesitamos perdón, momentito por favor que les comparto lo que estoy haciendo y es otra cosa con la que contamos es con la igualdad de medida de ángulos

## [00:30:11]

opuestos por el vértice entre dos rectas uy, también contamos con eso en otras palabras dada esta recta y la otra que tenemos acá entonces este ángulo tiene la misma medida que este otro y este ángulo tiene la misma medida que este otro o sea contamos con que eso es cierto ya de previo son nuestras premisas ok entonces cómo construiríamos la demostración de que la suma de los ángulos internos de un triángulo cualquiera, este, da dos ángulos rectos. O sea, el ángulo, lo que se llama un ángulo llano. Este, ok. Entonces, tengamos un triángulo cualquiera. ¿Cómo construimos la demostración? bueno hagamos esto tomemos uno de los lados como un lado digamoslo así, un lado base entonces prolonguemos ese segmento porque es un segmento de recta prolonguemoslo en ambos en ambas direcciones y tracemos una línea recta

## [00:32:28]

paralela a ese lado ok entonces ahora hagamos esto otro dado este otro segmento de recta o sea eso nos define aquí tenemos tres ángulos llamémoslos hay un ángulo a lo normal es usar letras griegas pero este para no quitarnos tiempo de eso voy a dejarlos con letras latinas hay un ángulo B y hay un ángulo C ok bueno, entonces yo puedo agarrar este lado y prolongarlo también puesto que es un segmento de recta puedo prolongarlo digamos para considerar la recta que lo contiene ok, ahora yo sé que aquí yo tengo se me está definiendo un ángulo que voy a llamar B' primo. Recuerden, estamos tratando de construir la demostración. O sea, lo que nos interesa es el conjunto de pasos para construir la demostración, no el conjunto de pasos de la demostración en sí. Entonces, por este camino yo digo, bueno, ok, pura vida, entonces tengo este ángulo B y B primo, y yo sé que B y B

## [00:34:34]

primo tienen la misma medida. Ajá. Sí, yo sé que la medida... voy a hacer, esta notación está muy fea pero es por cuestiones de tiempo perdón que no soy suficientemente preciso con la notación matemática la medida del ángulo B es igual a la medida del ángulo B' ok entonces digo yo, bueno voy a tomar el mismo camino con el otro lado y prolongo entonces la recta en cuyo segmento que pertenece el otro lado y yo digo, bueno, ok, entonces eso me permite encontrar un ángulo, perdón, A' cuya medida es igual que la de A ok ahora yo tengo aquí un ángulo C para que todo funcione, yo tengo aquí otro ángulo que yo podría llamar C' primo y si c primo fuera igual a c listo porque si esto es igual a esto y esto es igual a esto y esto es igual a esto es obvio que la suma de los tres ángulos a primo b primo y c primo es un

## [00:36:36]

ángulo llano o sea son dos ángulos rectos y listo porque me topo con pared ahí porque ahí pucha ¡pum! de pronto yo no puedo decir eso porque decirlo sería cometer una falacia que se llama saltar hacia la conclusión díganme, ¿qué me garantiza que el llamado ángulo C' es igual a C?

## [00:37:32]

¡Nada! ¡Nada me lo garantiza! ¡Yo no puedo decir eso! ¡Ah carajo! ¿Entonces qué tengo que hacer? ¡Me devuelvo!

## [00:37:44]

Entonces me devuelvo un paso para decir bueno, ok, eso no funcionó, ¿ahora qué? ¿Cuál otra premisa me podría servir?

## [00:37:54]

Y entonces me topo con una premisa que me dice que los ángulos opuestos por el vértice son iguales. Entonces, A. Ok. Entonces, me fijo en quién es el ángulo opuesto por el vértice a B'. Y lo llamo B''. Ah, ok. Sí, hay otra sentencia que me garantiza. hay otro postulado, perdón, postulado no hay un teoremita anterior que me garantiza que B' es igual a B' o sea, noten lo que acabamos de hacer acabamos de hacer backtrack o sea, pum, de pronto me topé con una pared siempre que uno está demostrando las demostraciones casi nunca salen así de directas bueno, hablo por mi propia experiencia personal de pronto oiga, un momento, ¿sabe? ¿y cómo garantizo que esto es verdad? y entonces me doy cuenta de que no sé si hay algo que me garantiza que eso sea verdad, y en este caso por ejemplo yo no puedo afirmar que C y C' fueran iguales pero entonces digo, bueno, ok, B' es igual a B'

## [00:39:32]

doble primo y de la misma forma puedo decir que a doble primo es igual a a, o sea tienen la misma medida, lo que quiero que se den cuenta de esto, lo que yo tuve que hacer, tuve que devolverme tuve que hacer backtracking haciendo backtracking yo quiero ver hacia donde me dirige eso bueno yo digo ok entonces a primo es igual a A doble primo ¡Ah! Esto es diferente porque entonces si A doble primo es igual a A primo y A primo es igual a A entonces A doble primo es igual a A ya tienen la misma medida por la misma razón B doble primo es igual a B tienen la misma medida ¡Ah! Ahora sí puedo sumar a doble primo o sea yo ahora si puedo decir que voy a usar esto ahora si yo puedo decir que a doble primo más c más b doble primo es igual a ahora si porque a a doble primo es igual a primo, y A primo es igual a A entonces yo aquí puedo poner A dejo a C y ahora yo puedo decir, bueno, B doble primo

## [00:41:31]

es igual a B primo, y B primo es igual a B y ahora sí, ya dado una recta, esta recta que está ahora puesta a mi lado base eso es una recta, o sea, entre los tres están construyendo la recta y por lo tanto yo sí puedo afirmar que esto da la medida perdón, eso es la medida de un ángulo llano aquí creo que sí vale la pena si me disculpan en algunos libros de geometría por ejemplo en el de Barilli de esta forma se denota la medida de un ángulo llano o sea de este ángulo de aquí y el ángulo recto, la medida del ángulo recto se lo denota con pi medios ok, entonces lo que me interesa aquí es este asunto de la, de que tuve que devolverme no pude avanzar directo hacia la conclusión sino que mi sistema de razonamiento va a tener que ser capaz de ir hacia atrás o sea, no es un algoritmo determinístico ¿tienen alguna pregunta? ¿se entendió bien que es lo que quise decir? ok, muchas gracias

## [00:43:36]

sí, sí, yo creo que sí ok cualquier duda ahí me decís con muchísimo gusto yo estoy para esto ok, muchas gracias Sebastián ok, entonces quiero hablarles ahora de un representante de esta de esta categoría de programas lógicos que se llama CLIPS esto significa si el nombre es un poco un poco nos pierde un poco porque dice C-Language Interface for Production Systems la razón de que tenga ese nombre es que la máquina de razonamiento fue construida fue escrita en C pero el lenguaje no tiene absolutamente nada que ver con C en absoluto ok Clips nace en el contexto de un tipo de programas en inteligencia artificial simbólica conocidos como sistemas expertos basados en reglas la idea es esta

## [00:46:04]

Un sistema experto era un... yo creo que ya se dejaron de usar este tipo de sistemas por la inteligencia artificial generativa, pero durante varias décadas los sistemas expertos y especialmente los basados en reglas eran el tipo más exitoso de sistema de inteligencia artificial que se usaba en el mundo real. real. O sea, sí, sí, sí hubo sistemas basados en inteligencia artificial que sí funcionaron en el mundo real. Entonces, un sistema experto era un conjunto de software que de alguna manera codificaba conocimiento experto. O sea, es irónico, pero, por ejemplo, un mecánico cuando está diagnosticando un motor digamos de combustión interna digamos el auto nueva franca una cosa que se descubrió en la investigación en inteligencia artificial es que las personas que son expertas en algún área de conocimiento a la hora que aplican su conocimiento lo hacen de una manera muy estructurada

## [00:47:54]

¿por qué? porque la cantidad de causas posibles que hacen que por ejemplo que una persona esté enferma o que un motor no funcione o que yo pueda declarar que un deudor es bueno o no es bueno o es riesgoso la cantidad de circunstancias que pueden concurrir ahí es muy grande, pero los expertos a lo largo de muchísima experiencia saben guiarse por indicios de este, qué cosas deben verificar primero para poder guiarse entre la maraña de cosas que puede tener mal un auto, por ejemplo, digamos que un auto de combustión interna, de los que usan gasolina, este tipo de automóvil, digamos que no arranca. Ese es el problema que tiene. Ok. Uno cuando dice que alguien está bateando, precisamente el batear, ese verbo que nosotros usamos en castellano de Costa Rica, significa que se nota que la persona no es suficientemente experta porque está empezando a probar alternativas

## [00:49:33]

prácticamente al azar. No está siendo guiado por un proceso de razonamiento basado en conocimiento. Por ejemplo, un auto no arranca. ¿Qué dirían ustedes si la persona que se supone es un experto en automóviles de lo que primero que se pone a hacer es verificar cuál es la presión de aire en las llantas o se pone a chequear si las marchas pasan bien o no pasan bien o se pone a verificar si el pedal de freno está muy flojo, aún cuando uno no sabe muy poco de mecánica automotriz uno sabe que eso no podría ser la primera en la que uno tiene que fijarse uno diría, bueno revise este, dele vuelta a la la llave de ignición y ponga atención oiga ok este, entonces se oye el arrancador, el motor del arrancador no se oye si si se oye, ah ok eso le sirve al si se oye y se oye fuerte entonces ya el mecánico de una vez descarta un problema eléctrico, ya sabe que no es la batería no es no es el

## [00:51:26]

el motor del arrancador por lo menos ya descarta eso entonces tal vez lo siguiente que se fije es, ¿y tiene suficiente gasolina? ven O sea, el experto basado en su conocimiento de cómo funciona un motor y de los datos específicos de este automóvil y un proceso de razonamiento que le permite precisamente tomar los indicios y aplicarle a teoría, dados los indicios, entonces él puede ir hasta llegar a cuál es la causa de que el motor no arranque o de que el auto no arranque.

## [00:52:14]

Entonces, las reglas de, revise esto primero, ponga atención a esto, ¿se encienden las luces o no se encienden? Esas reglas así, explícitas, son puestas en el sistema experto, son decodificadas utilizando el lenguaje propio del lenguaje del sistema experto. de manera tal que yo sí veo las reglas o sea, alguien que sabe leer en ese lenguaje sí sabe cómo interpretar si hay alguna regla que es incorrecta o hay alguna regla que falte entonces el conocimiento tal vez es importante decir esto es de manera explícita, por ejemplo otro ejemplo, como hago yo para en un sistema experto yo quiero poner un sistema experto para saber si un cliente de un préstamo es buen cliente o no es buen cliente o sea dar un préstamo siempre es un riesgo de que no me lo paguen en algún momento para el banco es un riesgo porque además préstamos como los préstamos hipotecarios que son a 20 años de plazo, por ejemplo

## [00:53:56]

en los Estados Unidos, eso es lo mismo que pasa con los préstamos para hacer una carrera universitaria una carrera universitaria en los Estados Unidos, cuesta entre, dependiendo de si usted quiere llegar solo al bachillerato o quiere llegar al doctorado, puede costar entre 40 y 100 mil dólares ok, entonces usted hace un préstamo educativo y termina pagándolo toda su vida son préstamos a 30 años de plazo esa es la maravilla del sistema educativo de los Estados Unidos para hacer una carrera universitaria en Estados Unidos o sea, si usted no es un atleta que le llame la atención a alguna universidad para que le den una beca deportiva este de ahí usted tiene que tener un préstamo usted tiene que conseguir un préstamo este de este tipo ok entonces desde el punto de vista del banco o de la entidad que va a hacer el préstamo del fondo del fondo de becas de ahí

## [00:55:28]

la posición de ellos es bueno de ahí yo voy a prestarle plata a alguien por 30 años que me garantiza que voy a recuperar ese dinero completo, eso y los intereses verdad perdón por la propaganda discúlpenme, no tienen que compartir mi opinión por supuesto pero precisamente este es el tipo de educación universitaria que hay gente interesada en desmantelar en este momento en el país y que quieren entonces que ustedes hagan préstamos de este tipo ok como les digo no necesariamente tienen que compartir mi opinión pero si les hago eso porque como funcionario de la educación pública la defiendo eso es lo que queremos mantener todavía bien entonces, ¿cómo hace usted para saber si un deudor es bueno o no?

## [00:56:39]

se le está jugando, ¿verdad? entonces siempre es un azar ok, entonces usted dice, bueno voy a chequear este si hay algún sistema por ejemplo en Costa Rica si lo tenemos, de que si esta persona tiene otras deudas, ¿qué tan buen deudor es?

## [00:57:02]

toda persona que haya hecho una deuda en Costa Rica de cualquier tipo, está ha ingresado en un sistema de deudas de me parece que es la SUGUEF, la Superintendencia General de Entidades Financieras. Entonces, si usted ha sido un mal deudor, está su su su historial de que es un mal deudor ahí. No está detallado, porque eso es información privada, pero sí está alguien marcado como no, este deudor es de clase B, no no paga tiempo ha entrado en morosidad varias veces ok, entonces primero verifica con la SUGREF este, si todo sale bien entonces usted pregunta bueno este ¿usted tiene empleo o no tiene empleo? no, yo no tengo empleo, ah ok, entonces ahora vamos a hacerle preguntas sobre sus papás ¿en qué trabajan? este, más o menos ¿cuánto es el ingreso de su casa? hace muchísimos años la Universidad de Costa Rica por ejemplo, para darle a usted una beca le pedí, yo no sé el tec en este momento

## [00:58:11]

no lo sé yo hablo de la Universidad de Costa Rica cuando yo fui estudiante le pedían a uno que aportara una copia de los recibos de servicios públicos electricidad agua, teléfono en aquellos años para ver más o menos cuánto era el monto total que usted pagaba por servicios públicos o sea, era todo para saber si su capacidad de pago era buena o no bueno, en el caso de las becas era para saber si usted se la merecía o no, ¿verdad? en fin entonces, este conjunto de reglas son las que se utilizaban para determinar si un si un deudor podía ser bueno o no. Dicho sea de paso, de nuevo, como ustedes pueden ver, yo no soy muy fanático de las redes neuronales de convolución. Una red de convolución, en este momento, ya trabajaría de una manera diferente, porque se le diría, bueno, este cliente que tiene estos y estos y estos y estos parámetros, es un mal cliente. entonces le doy una lista

## [00:59:33]

completa de clientes malos y ciertos parámetros que yo considero relevantes este y lo entreno con eso y por el otro lado le digo bueno estos son clientes buenos y en los parámetros tienen estas características ok usted lo entrena la red neuronal establece sus pesos y ahora entonces usted cuando va a pedir un préstamo nada más llena los parámetros suyos y la red neuronal determinará si usted calza en el patrón de los buenos deudores o de los malos deudores la diferencia del sistema viejo con el sistema nuevo es el siguiente que los sistemas expertos basados en reglas ellos pueden este justificar su conclusión o sea ellos pueden decir bueno este no pasó por este criterio porque hay una regla que dice que si usted es un deudor de clase C en la SUGUEF entonces no es un mal deudor y no califica y esta persona cuando se revisó en la SUGUEF efectivamente dio que es de clase C

## [01:01:01]

el sistema puede decirlo puede ponerlo en la pantalla oiga, es así porque yo tengo esta regla incluso las reglas pueden tener excepciones pero dice, no, porque usted no califica para una excepción ok, entonces ya yo sé por qué en este momento usted va a pedir un préstamo y le dicen, no, no se lo podemos dar ¿por qué? porque la computadora dice que no ok y por qué la computadora dice que no porque dice que no por eso nada más no hay explicación no hay manera de pedir una explicación simplemente le dan con la con la puerta en las narices por eso es que a mí no me gustan tanto estos sistemas por más ventajas que tienen y si las tienen por supuesto yo las uso Yo uso este tipo de sistemas para encontrar información. Para mí es un auxiliar bibliográfico, ese tipo de sistemas.

## [01:02:12]

Pero de ninguna manera le pido que razone por mí, porque yo sé cómo funciona. En fin, los sistemas expertos de antes tenían este conjunto de reglas. permítanme un momentito y a ver si les encuentro algún conjunto de reglas que les pueda mostrar ok, bueno no encontré ninguno apropiado en este momento ok, otra cosa que debo decir es que debido a la forma de codificar su conocimiento resulta que el lógico estadounidense Emil Post había creado en los años 30 un de hecho Post fue estudiante de Church había creado un sistema de codificar información, de codificar información lógica mediante algo que él llamó reglas de producción entonces debido a que se utilizó el formalismo de post para la creación de muchos de estos sistemas expertos no de todos había otros sistemas como Dendral como Prospector que utilizaban un sistema diferente este pero estos en particular usaban

## [01:05:17]

las reglas de producción de post y por lo tanto fueron llamados sistemas de producción ok, eso es lo que explica que esto se llama C-Language for Production Systems son clips, es un lenguaje hecho explícita y exclusivamente para crear sistemas de producción o sea sistemas expertos basados en reglas de sistemas de producción perdón por querer hacerle propaganda a la inteligencia artificial de la vieja escuela pero díganme por favor, ¿alguno de ustedes vio alguna vez un capítulo de una serie de televisión que se llamaba CSI que era de investigadores forenses la conozco pero nunca la he visto yo al menos pero si la conozco si ok entonces Entonces, ok, sí, para aquellos que la conocen, ustedes los que la conocen probablemente hayan visto alguna escena donde tienen una muestra, inclusive una muestra biológica en un hisopito y cortan el hisopito. se ve, siempre

## [01:06:57]

eran muy detallados para mostrar esto, yo no sé por qué, lo ponían en un vial muy simpático, una forma de conito lo centrifugaban y luego lo metían en un tomaban la muestra y la metían en un espectrómetro de masas ok, pero la parte interesante era que después de pasar por el espectrómetro y después de estar un rato con los brazos cruzados una impresora láser generaba una página diciendo ah ok no esta la muestra lo que es es ácido clorhídrico ok nadie lo dijo nunca pero el espectrómetro de masas lo único que hace es decirme la proporción de ciertos pedazos de cierto peso en la muestra entonces con sólo esa información un sistema experto llamado Dendral era capaz de deducir cuál es la sustancia que tenía ese espectro Este fue un éxito rotundo de inteligencia artificial y nunca nadie se lo reconoció. Pero ya había sido un logro de inteligencia artificial. tal vez por agregar el primer

## [01:08:56]

malogrado sistema experto basado en reglas fue Meissen creo que Meissen es de 1974 y es Fagenbaum Fagenbaum ese sistema experto lo que hacía era diagnosticar enfermedades debidas a infecciones bacterianas. Era muy bueno. Era bastante, bastante bueno. Fue un trabajo excepcionalmente bueno. Fue la tesis doctoral, por cierto, de Feigenbaum en MIT en sistemas, bueno, en la Secretaría de Inteligencia Artificial. Pero como trataba de cosas médicas, de diagnóstico médico, al establishment de los médicos les dio mucho miedo utilizarlo porque ellos fueron los primeros que se toparon con el problema en que estamos hoy en día a saber de que si usted le da un sistema que parece ser inteligente a la gente la gente va a tener la tendencia desgraciadamente va a tener la tentación de dejar que la máquina piense por usted y entonces creer solamente en lo que la máquina le está diciendo y si la máquina

## [01:11:00]

está diciendo algo incorrecto usted está no es que usted no pueda saberlo es que usted simplemente decidió dejarle ese asunto a la máquina y como estamos hablando de vidas humanas y a veces de tratamientos que tienen que aplicarse en cuestión de minutos hay bacterias por ejemplo que pueden atacar el organismo de una manera rapidísima o sea se reproducen a una velocidad exponencial y usted tiene que tiene nada más si acaso a veces 12 horas para decir que le doy a esta persona para ralentizar el crecimiento bacteriano y permitir que el cuerpo empiece a generar sus propias defensas como les digo hay infecciones bacterianas tan agresivas por ejemplo hay una cepa de me parece de estafilococcus que es inmune a la penicilina es estafilococcus aureus hay una cepa de estafilococcus aureus no, Escherichia coli de Escherichia coli hay una cepa de Escherichia coli que es resistente a la penicilina

## [01:12:27]

a la pucha y lo puede matar usted en cuestión de 24 horas y la Escherichia coli es una es una bacteria que se encuentra en el suelo o sea en este momento donde usted esté tiene sus pies encima de una cantidad de un océano de Escherichia coli ok entonces nadie quiso usarlo perdón aquí yo creo que me equivoqué esto es así más bien ok entonces el asunto es que bueno entonces pero este es un sistema para cosas muy específicas pues en realidad no Porque dada la variedad de ambientes diferentes a los que se aplicó la técnica de sistemas expertos, los lenguajes para desarrollarlos, O sea, los lenguajes específicos se volvieron, digámoslo así,

## [01:14:11]

during completos.

## [01:14:21]

Y estos lenguajes implementan...

## [01:14:26]

Uy, qué torpe estoy con el teclado.

## [01:14:36]

Forward chaining. Ok, entonces, ¿cuál es la arquitectura de estos sistemas? Porque también noten que son sistemas que razonan, o sea, son sistemas que construyen demostraciones. Por ejemplo, en el caso de los deudores, son sistemas que tienen que demostrar que un deudor es apropiado para que se le dé un préstamo, o que un deudor dado no es apropiado para que se les dé un préstamo. Profe, disculpa, ¿puedes devolverte un segundo la diapositiva anterior que no puedo notar algo? naturalmente, con mucho gusto permíteme por favor la anterior, claro esa es esa misma, muchas gracias con mucho gusto listo perfecto ok, permítame un momentito quiero mostrarles entonces la arquitectura de este tipo de sistemas porque esto explica entonces como se ve las cosas en el caso de Eclipse en particular.

## [01:17:08]

En general, los sistemas expertos basados en reglas o de razonamiento hacia adelante en este caso tienen esta estructura.

## [01:17:36]

Mediante el lenguaje yo codifico las reglas. esto que ustedes ven que son reglas IF-THEN se basa en esto a principios del siglo XX se demostró que era posible tener un sistema, o sea, de que se podía reducir todo el conjunto de reglas de inferencia a sólo una se podía trabajar únicamente con modus ponens claro, las demostraciones se hacen imposiblemente largas ¿verdad?

## [01:18:26]

como todos ustedes saben por ejemplo que por analogía, les voy a hacer una analogía a este respecto que yo tengo tres compuertas booleanas tengo AND bueno, incluso puedo decir que tengo cuatro tengo AND, tengo OR tengo NOT y tengo XOR pero yo puedo reducir todas a sólo una yo puedo trabajar solamente con Nant o puedo trabajar solamente con Nora claro, como les digo las sentencias lógicas se vuelven imposibles de leer porque de pronto se hacen así larguísimas y con montones de paréntesis por todas partes pero de que se puede se puede entonces de la misma forma demostraron que era posible por ejemplo Hilbert y Ackerman por un lado este Roser por otro por ejemplo el libro de lógica simbólica de Coppi en la segunda parte examina todo el sistema de Roser con todo detalle o sea, primero demuestra que con solo modus ponens yo puedo tener cálculo proposicional y luego, basado en eso

## [01:20:02]

demuestra que el sistema de Roser puede extenderse a cálculo de predicados con una sola regla de inferencia con modus ponens ok, entonces, el asunto de que tenga solamente reglas if-then es que estoy usando modus ponens nada más entonces mi base, la que aquí es llamada mi base de conocimientos es precisamente todo mi conocimiento lógico, general expresado mediante modus ponens o sea, solamente reglas del tipo si esto, entonces esto si p, por consiguiente q si every, por consiguiente s lo que aquí se llama la base de datos son los hechos que puedo yo dar por cierto entonces por ejemplo yo arranco con este con los datos del por ejemplo en el caso de un préstamo con los datos del cliente con los datos básicos del usuario aunque como ustedes ven en los sistemas más complejos yo puedo también usar datos que se encuentren en fuentes externas externas. Esta base

## [01:21:31]

de datos que se llama aquí es lo que internamente el sistema da por cierto pero los sistemas más complejos pueden ser usados incluso para que tenga este acceso a bases de datos fuera del programa ok la máquina de inferencia trabaja mediante Moose Ponings o sea, dado un hecho de aquí me fijo cuál de las reglas de acá lo tiene como antecedente o sea, por ejemplo, yo tengo como un hecho P y entonces busco aquí cuáles reglas dicen P por consiguiente Q P por consiguiente R P por consiguiente T o sea, puede haber varias reglas que tengan a P como antecedente por eso es que este sistema no es determinístico puede haber vías que me dan hacia callejones sin salida y por eso entonces tengo que hacer backtrack lo único que vale aquí es que una vez que yo usé una regla ya no la puedo volver a usar esa sí es una restricción que hay aquí ya una regla solo puede usarse una vez

## [01:22:59]

y si ya la usé y no funcionó listo, ya la desecho entonces la regla perdón, el inference engine el motor de inferencia trabaja con modus ponens o sea, se fijan los hechos en las reglas para ver cuál este es disparada eso es lo que se llama cuál regla es triggered es como apretar el gatillo de un revolver triggered, cuál es disparada claro, al disparar una regla, lo que va a provocar es que haya nuevos hechos, o sea, cosas que ya puedo dar por ciertas, que se agregan a la base de datos y esos nuevos hechos, sumados a los hechos que ya yo sé me pueden servir para disparar más reglas así, hasta que llego a la conclusión que se me pide que llegue, o sea, que este razonamiento termina aquí por ejemplo con la conclusión de que si ya una vez que yo ya llegué a determinar, o sea si esto y esto y esto y esto entonces este es un mal deudor y ya le digo deténgase ya llegamos a la conclusión

## [01:24:31]

a una de las conclusiones posibles y usted llegó a esa ya terminamos ahí entonces en la base de conocimiento tiene que entregársele el conocimiento adicional de ok yo quiero que usted llegue hasta ahí todo gira alrededor de estas tres cosas como ven de la base de conocimiento la base de datos o sea la base de hechos y mis reglas de inferencia o sea perdón mi módulo de inferencia porque como ven la base de datos externa para lo que me sirve es simplemente para decir ok este aquí tengo más hechos si es que hay alguna regla que me dice busque más hechos en la base externa lo del programa externo es por esto porque la máquina de inferencia de lo que se encarga es de este simplemente seguir usando el modus ponens de ninguna manera la máquina de inferencia por ejemplo tiene capacidades no se supone que tenga capacidades para por ejemplo mostrar un ambiente gráfico usar el mouse

## [01:25:53]

si tiene que localizar esas bases de datos están en internet entonces manejar la dirección IP abrir puertos ver si el otro puerto está habilitado o no, ese tipo de carajadas, filtrar información que viene de la red no tiene por qué ser parte de la máquina de inferencia, entonces el programa externo me sirve para eso, para encargarse de todas las carajadas que no tienen que ver con razonamiento por ejemplo, interfase con el usuario hacer una interfase con el usuario agradable cuando yo voy disparando las reglas como ven las reglas están ahí la regla número uno está, la regla número dos está, entonces yo puedo llevar una bitácora de cuál regla disparé, en qué momento entonces cuando la bitácora ya dice, o sea cuando yo ya llego al final, en la bitácora está todas las reglas que yo visité y el orden en que yo las visité entonces ya la bitácora es una explicación oiga

## [01:27:19]

y porque usted me negó mi préstamo a por esto usted ingresó este dato hay una regla que me dice con este dato verifique tal cosa ok yo verifique tal cosa hay una regla que me dice que si este número es menor que 18.4 entonces dispare tal otra regla o sea, se disparó tal otra regla que dice, bueno, entonces hay que investigar tal otra característica y por lo tanto después de como unos 10 pasos dije, bueno, entonces con este dato y este y este, basado en estas reglas el banco, la política del banco es negarle el préstamo le puede explicar por qué lo hizo por qué llegó a esa conclusión bueno, aquí la base la interfaz de usuario está por aparte, pero como les digo puede ser también el programa externo bueno la interfaz para el desarrollador es precisamente digámoslo así la máquina virtual que cobre la máquina de inferencia entonces por lo tanto el así llamado ingeniero en conocimiento

## [01:28:41]

ese título llegó a existir y el experto del mundo real utilizan la interfaz de desarrollador para precisamente crear todo el sistema las facilidades de explicación también le llegan al desarrollador, eso es lo que quiere decir en este caso para hacer depuración conjuntamente el ingeniero en conocimiento y el experto esta es más o menos la anatomía de todos estos sistemas, CLIPS en particular tiene esta anatomía ok ¿tienen alguna pregunta? muy bien muchas gracias muchas gracias Matías muchas gracias hay una cosa que se puede decir más de la máquina de inferencia y y es que me perdí Sonoperson Sonoperson en el mio computer Hay unas cuantas cosas que ustedes tienen que saber De esta maquina de inferencia La primera es que Las reglas Son del tipo Este Este Este no me permite dibujar Dios mio que ya que estaba en Word Son del tipo P Por consiguiente Q no me lo tiene aquí

## [01:31:20]

ahí está, son de ese tipo P por consiguiente lo que pasa es que P puede ser una fórmula bien formada y eso es una virtud enorme que a uno le puede encontrar estos sistemas, usted puede decir bueno, si esto y esto o esto y no esto entonces esto implica que tal cosa ok, entonces y además o sea, yo puedo tener una cosa como este, me llevo esto bueno de la forma de, por ejemplo P, donde estos son predicados más puedo ponerlo así son predicados que admiten variables entonces podría tener una cosa de la forma P o Q y necesito una negación digamos no R por consiguiente ese es el tipo de fórmulas bien formadas que se me permite, se me da permiso de tener en esos sistemas, por ejemplo Eclipse entonces noten que el antecedente puede tener o es ah, perdón, aquí no puse un no, perdón sorry, sorry, sorry este disculpen el antecedente puede tener o es el consecuente no el consecuente solo tiene is

## [01:34:45]

este, ahora bien como estas reglas a usted le quito esto eso a usted si se lo pongo ay no Como estas reglas Por lo general Son de Si esto y esto y esto y esto Entonces Ponga esto como que tal cosa es cierta Pregúntele Al usuario tal cosa Porque se permite que una de estas Sea entrada o salida Elimine tal cosa De lo que usted creía cierto Entonces estas se llaman reglas también de este este de condición acción vean que en este dibujo las teníamos como reglas if then si, se pueden ver así, if esto, then esto otro, pero en el mundillo digámoslo así, de los sistemas expertos, a eso se le tenía mejor este nombre este

## [01:36:14]

Ahora, hay otros detalles que yo necesito darles de la máquina de inferencia. Vamos a ver, tiene una característica que quiero que ustedes vean. Entonces, quiero ver si tengo ya hecho un esquema ya suficientemente detallado. Permítanme, por favor. No, no hay ninguno, entonces voy a tener que hacerlo yo mismo. No hay problema. Uy, profe, nuevamente la diapositiva anterior que si la puedo poner en un segundo pura vida, pura vida, muchas gracias está buenísimo lo que usted necesita entonces, ¿cuáles son los componentes de este de la máquina de inferencia?

## [01:38:37]

ok la cosa está así se cuenta con una estructura de datos que se llama bueno, tiene varios nombres algunos autores lo llaman el contexto otros autores lo llaman el ambiente environment ¿por qué pasa esto? los hechos de los que estamos viendo aquí son los hechos con los que arranca el sistema pero el sistema yo lo puedo hacer para que interactúe con el usuario y entonces le pida más cosas particulares es que usualmente esos hechos que están ahí son los hechos más generales las cosas que son absolutamente ciertas por ejemplo que un puede ser que yo clasifique a los deudores en A, B, o sea, aquellos a los que les pueda dar un crédito aún así también los clasifique el A, B, C, D y lo que pongo ahí es el techo de cuánto puedo prestarles ¿a qué? y entonces yo digo bueno, los deudores tipo A tienen de techo hasta unos 100 millones de colones los de tipo B tienen como techo unos

## [01:40:50]

20 millones de colones y los de tipo C estos apenas son un par de millones es lo que puedo prestarles y agarro mucho o sea, esos son hechos generales del sistema tengo estos techos para este deudor, el techo es tal para este otro, el techo es tal pero precisamente, si yo llego por ejemplo al banco, llego ahí con los papelitos de ver, ustedes me pidieron esto estos son los datos que yo puedo darle esos son datos contingentes que me pertenecen a mí, ¿verdad? No son hechos generales del sistema de conocimiento. Entonces, en ese caso, se va creando esta estructura de datos que se llama el contexto o ambiente, donde están los datos particulares de este caso sobre el cual se está razonando ok como ustedes ven puede que en el ambiente en un momento dado esté no R pero puede que también esté Q pero no esté P ok entonces esa regla el antecedente se satisface pero parcialmente porque le falta algo

## [01:42:36]

puede que haya otra regla que diga Q y no R o S y S si se encuentra en el en mi ambiente en ese momento ah ok, entonces las dos reglas, esta que están viendo y la otra que les he quedado de decir ambas son factibles para ser disparadas o sea yo no puedo desechar una de a priori sino que tengo que decir a ok suave en este momento yo podría disparar esta o disparar esta otra entonces en un momento dado el asunto funciona así dado el contexto existe otro componente que se llama la agenda la agenda la agenda es la lista de las reglas que podrían ser disparadas en este momento entonces el sistema de inferencia lo que hacen en realidad es dado los hechos y el contexto actual revisa, o sea, crea la agenda o sea, busca en la base de conocimiento las reglas que podrían ser disparadas dado el contexto actual y los ponen a todas en la agenda y de ahí necesita cobrar un algoritmo para este

## [01:44:49]

decidir cuál dispara primero, ven por eso es que esto puede dar lugar a backtracking o sea yo puedo seguir una cierta línea pero digo había un momento en que ya no tengo ninguna regla para seguir no he llegado al final y por lo tanto tengo que descartar la aplicación de la última regla que hice y entonces tengo que eliminar los hechos que esa puso en el contexto y entonces ver con los hechos con la nueva lista de hechos y con la agenda tal y como quedó, que podría yo disparar en este momento, es como si hubiera dado un paso hacia atrás y trato de ver con las reglas que ya tengo ahora a donde puedo continuar cual había otra que fuera factible dispararla en este momento y que no la disparé porque había antes otra que yo creía que era mejor y no me funcionó, entonces voy a trabajar con la siguiente para eso es que se lleva la agenda esa es la idea de la agenda y de el del contexto este

## [01:46:09]

ok, bueno este en la próxima clase, el próximo vamos a ver, el martes 3 el jueves 5 vamos a ver un ejemplo ya de codificación con clips y cerraríamos en ese día ya el paradigma lógico y entraríamos a orientación a objetos ok así que bueno ya se me acabó el tiempo hace rato dicho sea de paso y vamos a dejar entonces nuestra sesión acá y nos vemos virtualmente también el próximo jueves entonces así que muchas gracias por haber llegado a esta sesión y nos vemos, hasta luego
