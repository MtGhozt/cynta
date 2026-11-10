---
clase: "Clase 2"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1880428214.m4a
modelo: large-v3
idioma: es
duration_sec: 5820.8
---

## [00:00:02]

Gracias, les decía, como toda función es describible usando cálculo de predicados de primer orden, entonces, pues, en vista de que todo proceso computacional puede ser reducido a funciones, a la evaluación de funciones parcialmente computables, por consiguiente, cualquier proceso computacional debería poder ser descrito mediante cálculo de predicados del primer orden ese es el razonamiento que nos lleva a este modelo digamos que lo justifica desde el punto de vista teórico este modelo nace porque hubo bueno, en realidad Hay una corriente en inteligencia artificial que sostiene que cualquier actividad cognitiva, esto es meramente una tesis, o sea, no existe una demostración de esto, es simplemente un supuesto. es una tesis en el sentido de que es algo que se propone o sea, estamos hablando de tesis en el mismo sentido que hablamos de la tesis de Church es un supuesto metodológico

## [00:01:42]

no ha sido demostrado pero tampoco ha sido refutado y este sostiene que cualquier actividad cognitiva humana memoria razonamiento abstracto o sea manejo de símbolos formales interpretación de imágenes manejo de imágenes mentales manejo de mapas mentales lenguaje todos estos actividades cognitivas pueden ser reducidas o explicadas o más bien descritas mediante el lenguaje de la lógica formal entonces este supuesto que hacen hacer lo que se llama el punto de vista logicista en inteligencia artificial es el que estuvo detrás de la del desarrollo de un todo un marco teórico de investigación en lógica lógica por un lado es lógica por el otro lado es psicología cognitiva y por el otro inteligencia artificial que entre otras cosas este marco metodológico involucró la creación de lenguajes lógicos, por supuesto donde el Prolog no fue el primero hubo otros intentos muy interesantes

## [00:03:31]

Hubo, por ejemplo, para la tesis doctoral de Jeffrey Winograd, el famoso proyecto SHR de MLU, SHR de MLU. Para ese proyecto usó un lenguaje llamado Microplanner, que trataba de hacer algunas cosas muy similares a las que hacemos hoy con Prologue. entonces Prologue no es el único lenguaje lógico pero si es el más conspicuo es el que sobresale más se ha trabajado mucho más en él hay muchas más líneas de código en él pero no es el único nosotros vamos a ver dos además de Prologue vamos a ver Clips no sé si tienen alguna pregunta alguna duda hasta este momento Por mi parte todo perfecto profe, muchas gracias Al contrario, gracias a usted Muchas gracias por el feedback Y a Ian también, muchas gracias Ok, entonces Para poder ver Obviamente De una manera provechosa El paradigma lógico Necesitamos Repasar un poco lo que se supone ustedes debieron haber visto sobre lógica en el curso de

## [00:05:22]

matemática discreta ok, en ese curso debieron haber visto primero el lenguaje de la lógica simbólica el conjunto de símbolos que es muy reducido muy chiquitito que utilizamos para simbolizar y luego la simbolización en sí ¿Qué es cómo pasar del lenguaje ordinario, del lenguaje natural, al lenguaje de la lógica?

## [00:06:08]

Primera cosa que tenemos que señalar es la siguiente. Hay algo que destaca de una manera muy patente la lengua castellana que nosotros hablamos. Y es que cuando uno ve la conjugación verbal completa, que es algo que se ve en la secundaria, No sé si ustedes recuerdan que los verbos tienen cuatro modos, modo imperativo, modo subjuntivo, modo imperativo y modo potencial. Cada uno de esos modos describe una manera particular de las situaciones en el mundo Y hay que señalar que de esos cuatro modos O sea, cada uno de esos modos verbales se utiliza para indicar cosas particulares sobre las oraciones O sea, por ejemplo, el indicativo se utiliza para señalar cosas o situaciones del mundo que o son verdaderas o yo creo que son verdaderas en algún momento puede ser en el futuro pasado o en el momento actual el imperativo ni siquiera es eso el imperativo es una manera de dar órdenes el subjuntivo

## [00:07:54]

y el potencial se refieren a dos maneras sutilmente diferentes de indicar digamos lo así alternativas o situaciones posibles no situaciones actuales entonces digo todo esto para señalar que a la lógica al cálculo predicado de primer orden solamente le interesa lo que en castellano se codificaría con el modo indicativo ok entonces primer requisito una oración debería estar en modo indicativo para poder ser simbolizada vamos a ver este veamos estos ejercicios de simbolización sea necio veamos este primero los ácidos y las bases son compuestos químicos el binario es un ácido por lo tanto el binario es un compuesto químico esto es muy sencillo de hecho es un una una este es un argumento y inclusive el autor de este argumento nos hace una sugerencia de simbolización bueno no de simbolización de interpretación o sea la interpretación es una función que relaciona situaciones del mundo real

## [00:10:42]

con ya sea símbolos de constantes o símbolos de bueno símbolos de constantes de objeto o símbolos de constantes de predicado para poder utilizarlos en la en la simbolización del argumento entonces dice los ácidos y las bases son compuestos químicos uno tiene que suponer que entonces adx significa X es un ácido B de X, X es una base Q de X X es un compuesto químico el vinagre es un ácido, entonces podemos suponer que V de X significa X es vinagre, muy bien entonces este es muy sencillo indíquenme, ¿cómo lo simbolizarían ustedes?

## [00:11:44]

yo lo haría como AX el conector lógico Y, BX No sé, podría ser Implica, QX Para el otro lo haría Después de eso conectado con un Y ¿Cuál era vinagre? VX V de X V de X Implica A de X Y todo eso en general El resultado de todo eso implica Que V de X y también implica Q de X ok ok, muchas gracias muchas gracias bueno, también se puede hacer como por inferencias lógicas digamos como con eso es porque está escrito así, ¿verdad? pero no lo puede escribir como como ¿cómo se llama esto? como con hipótesis, por decirlo así y dar la conclusión tipo con inferencias lógicas, digamos no solo con reglas de la parte bueno, no sé, con reglas de simplificación y esas cosas decía yo también, es otra forma ok te agradezco mucho tu intervención de hecho más bien por favor toma lo que te voy a decir como refrescamiento de la parte de lógica pero realmente te agradezco que hayas intervenido entonces

## [00:13:34]

de esa, digamos de una manera que quiero que se entienda como didáctica te digo que cometiste ciertos errores en tu primer planteamiento pero de nuevo no es no es mi intención no es desestimar la desestimar la participación tuya me quiero más bien darle sin miedo para tener un mejor conocimiento entonces, ¿qué te faltó? te faltaron unas cuantas cosas, primero si yo estoy diciendo permíteme ver porque yo mismo tapé esa esa imagen, si estamos diciendo los ácidos de la base son compuestos químicos y estamos diciendo ADX simboliza el primer elemento eso significa que estamos hablando de cálculo de predicados y este puede ser que este fuera el énfasis más bien que se dieran en matemática discreta vos estás tratando de meter en la oración como si fuera cálculo proposicional, pero esto es otra cosa, es cálculo de predicados correcto, correcto, si nunca lo evalúen

## [00:15:18]

en el razón, entonces ¿qué te faltó? en primer lugar un cuantificador o sea, los ácidos y las bases son compuestos químicos, eso quiere decir que cualquier cosa que sea un ácido o una base no nos engañemos ahí con el I porque no hay nada que sea al mismo tiempo una base y un ácido obviamente el pH justamente divide eso en dos categorías totalmente inconexas si el pH es inferior a 7 es un ácido si es superior a 7 es una base o al revés en este momento no lo tengo claro para ser honesto, pero en todo caso no hay nada que sea al mismo tiempo un ácido y una base entonces ese I que dice ahí es un O lógico entonces para todo X se cumple lo siguiente este los ácidos y las bases son compuestos químicos, eso significa que si X es un ácido O a ver dónde está el O lógico aquí no está el O tal vez son operadores operadores relacionales operadores binarios, aquí está entonces, si X es un ácido O

## [00:17:05]

X es una base voy a ser un poquito más claro entonces aquí si X es un ácido, O es una base entonces son compuestos químicos pues dice, los ácidos y las bases o compuestos químicos, o sea, toda cosa que sea un ácido o que sea una base, entonces ese X que es un ácido o una base es un compuesto químico espero que no se me confundan demasiado, pero así fue como yo aprendí lógica este símbolo en lógica en lógica simbólica, es una implicación la flechita es la que se usa en matemática para indicar implicación entonces cuando yo hago matemática utilizo la flechita pero cuando hago lógica utilizo la herradura así lo llaman los lógicos en confianza, digámoslo así ok, entonces la primera sentencia que dice los ácidos y las bases son compuestos químicos, se simbolizaría así, para todo x si x es una base o x es una perdón es un ácido o X es una base entonces ese X es un compuesto químico

## [00:18:41]

y esa es una sentencia de hecho está separado por un punto gráficamente en la en la oración misma ahora el vinagre es un ácido, aquí hay una cosa interesante y es que como no lo proponen dice V de X ok, eso significa que nos están sugiriendo simbolizar esto como cualquier cosa que sea vinagre entonces esa cosa será un ácido, eso es lo que nos propone simbolizar, entonces les decimos nosotros, Juanis si usted quiere que yo haga eso, eso es perfectamente razonable, o sea uno podría decir V de X es cualquier cantidad de una sustancia que sea binaria entonces para todo X porque no es un binario en particular todo binario o sea todo líquido que sea binario es un es un ácido lo cual es correcto sin importar si es binario de guineo o binario de manzana o ácido acético puro pues todo eso es binario entonces para todo X el alcance, eso es algo que se acostumbra mucho el alcance del cuantificador

## [00:20:27]

se pone, algunos autores, la mayoría lo ponen con paréntesis redondos para limitar el número de símbolos en la lógica alguna otra gente usa paréntesis cuadrados de vez en cuando como Irving Copie, entonces cualquier cosa que sea vinagre es un ácido lo correcto es esto son dos sentencias aparte ahora viene una expresión muy usual por lo tanto a ok o sea se me está se me está proponiendo que esto es un argumento entonces esto es un razonamiento y tiene una conclusión hay premisas y hay una conclusión bueno so far, so good así que alguna gente permítanme aquí vamos a ver voy a usar esto se supone que esto debería ser una línea continua pero ustedes, espero que me tengan paciencia con las carencias del medio ok entonces ahora tengo que decir por lo tanto muy bien también muchos autores en lógica el por lo tanto vamos a ver dónde está debería estar acá saber matemáticas básicas ahí está por

## [00:22:44]

lo tanto se suele escribir así muchos autores lo usen así, no todos por lo tanto el vinagre es un compuesto químico o sea cualquier cosa que sea binaria entonces es un compuesto químico así que nuevamente voy a llevar todo esto para todo x si x es binaria entonces es un compuesto químico ok entonces esta sería la simbolización en cálculo de predicados de primer orden de la expresión los ácidos y las bases son compuestos son compuestos químicos el vinagre es un ácido y por lo tanto el vinagre es un compuesto químico vamos un poco más allá ¿cómo lo demostrarían? O sea, hagamos una demostración bien formal. ¿Cómo demostrarían esto? ¿Cuál sería la demostración? Porque parece que es un argumento correcto, ¿verdad? O sea, efectivamente, a partir de las premisas yo llego a la conclusión. Y en el mundo real la conclusión es correcta, dicho sea de paso.

## [00:24:51]

yo considero que se podría utilizar algún tipo como el silogismo hipotético porque partir de V de X llegas a X esa parte no sé seguro cómo simplificarla pero de ahí podrías pasar de AX a Q de X y ya tendrías esa condición directa digamos por ahí diría por ahí diría exactamente, por ahí diría este permítame mostrarles me falta una ok, este Vamos a ver. Voy a arriesgarme. ¿Cómo la demostraría yo? Vean un detalle. Tenemos que familiarizarnos una vez más con el proceso de demostración por una razón. En el paradigma imperativo, yo ejecuto instrucciones. En el paradigma funcional yo evalúo funciones. En el paradigma lógico yo demuestro sentencias. Entonces, la máquina virtual de cualquier lenguaje del paradigma lógico es un motor de inferencia. de alguna manera es una máquina para razonar, ok eso significa que debo volver a familiarizarme con la manera en que se demuestran cosas entonces, ok

## [00:28:03]

lo primero que voy a hacer es esto, ¿qué es esto?

## [00:28:23]

ok, esto es una premisa ¿y qué es esto? eso es otra premisa es más, ya saben que ya que se me había olvidado este comportamiento tan vacilón de de Word entonces en cualquier demostración lógica incluso en matemática debería ser así solo que como los argumentos en matemática son tan grandes nunca se hace pero se podría hacer perfectamente o sea, uno y dos son premisas ok, ¿cuál sería el siguiente paso de mi demostración?

## [00:29:55]

ok yo, yo haría esto yo diría esto, ¿qué estoy haciendo ahí?

## [00:30:29]

yo no sé si a ustedes les enseñaron a demostrar en lógica pero, este, usted toma el libro de Coppi o el libro de Don Luis Camacho o cualquier otro libro decente de lógica, el de Benson Mates por ejemplo también y se toparía esto primero que tengo que decir en cualquier línea de una demostración lógica, yo tengo que decir de dónde saqué eso entonces esta línea 3 de dónde vino y yo digo, ok, eso vino de la línea 2 lo siguiente que tengo que decir es ¿por qué? ¿por qué la línea 3 viene de la línea 2?

## [00:31:22]

¿qué regla lógica estoy aplicando? O, visto así, ¿qué regla lógica me da permiso de escribir la línea 3 apoyándome la línea 2?

## [00:31:44]

¿Ok? La ley que me permite hacer eso es ejemplificación existencial.

## [00:32:00]

La regla de ejemplificación existencial.

## [00:32:05]

¿Ok?

## [00:32:07]

Entonces, claramente yo haría... Así ahí está. por lo menos está esa mi línea cuatro sería voy a echar a Ernesto disculpa, una consulta claro, adelante ahí nada más, no sería como ejemplificación universal existencial tienes razón, tienes toda la razón completamente gracias ciertamente ese fue un error muy grave muchas gracias que torpeza la mía gracias, gracias ok, en vista de que es un universal yo puedo usar la misma variable que usé en la ejemplificación anterior, porque esto aplica para todo x entonces no tengo necesidad de introducir una variable nueva de hecho a mi me conviene que sea esa, así que dejo esa porque es un universal entonces 4 de dónde viene 4 viene de 1 por la misma razón ejemplificación universal ¿y qué es eso?

## [00:34:07]

ok entonces este mi pregunta es aquí ¿hacia dónde voy?

## [00:34:41]

¿cómo hago para llegar a mi conclusión?

## [00:34:56]

bueno este es un poco más difícil ahora que lo estoy viendo es un poco más difícil de demostrar me disculpo con ustedes es un poquito más difícil de demostrar este va a implicar va a necesitar una un elemento o una como una técnica de demostración que yo estoy seguro que ustedes no conocen entonces me disculpo por eso porque ya a partir de aquí ustedes pegarían con pared no por falta de capacidad de ustedes sino porque hay algo que está faltando aquí que ustedes no conocen este y eso que ustedes no conocen es esto ese sería el paso 5 lo que ustedes no saben que se puede hacer es esto y es una cosa que se llama un argumento hipotético pero no creo que ustedes les hayan dado esto en este no creo que les hayan dicho de esto en su curso de matemática discreta, y es que un argumento hipotético funciona así, y digamos tiene mucho sentido, supongamos que yo tuviera V de X este

## [00:37:21]

entonces a partir de ahí ¿qué? supongamos que tengo V de X si yo tuviera V de X entonces ¿qué tendría? por modus ponens correcto sí, sí Sebastián, correcto tienes también la razón yo tendría A, B, X este entonces 6 sí, tendría A, B, X y ese A, B, X vendría de, perdón, este 6 vendría de de 3 y de 5 por Modus Ponens porque Modus Ponens necesita dos dos antecedentes entonces ya tengo tengo que esto es cierto tengo esto, entonces puedo concluir esto ok y a partir de aquí que?

## [00:39:35]

que más? a partir de ahí para donde Gabro? Sí, yo haría lo que dijo Sebastián, más bien utilizo AX y le hago con adición le pongo BX Correcto, y Sebastián también está en lo correcto con eso uso adición si tengo ADX, entonces puedo decir ADX o BX más aquí lo tengo ok, entonces 7 vendría de 6 por adición Ah, ok, entonces, perfecto Entonces Línea 8 Ya yo puedo concluir con Q de X ¿Verdad? Un montón de espacios en blanco ahí Ok, ¿de dónde viene 8? 8 viene de 7 Y de 4 Como los ponen también Entonces Vamos a ver Cómo se los pongo Cómo lo dibujo de dónde están las formas aquí están resulta que en lógica yo quería otra línea en lógica puedo hacer esto ok entonces mi línea 9 es v x implicaría q de x y así se valdría bien una forma que se me acaba de ocurrir sí, después de, bueno es una forma que se me ocurrió digamos si nosotros no hubiéramos conocido hipótesis por ejemplo si uno de tres utiliza

## [00:45:01]

aplicación de disyusión para digamos negar v de x y ponerle un o a x entonces tiene no v de x o a x a eso le hace una adición de BX y después ese digamos lo que uno hace es con poner los paréntesis entre BX y AX y el log que te quedó entre no VX lo vuelves a pasar a implicación y ya te queda VX implica AX o BX y ya puedes llegar directamente No sé si eso también Sí, sí, sí, siguió de otra forma, muy bien Sí, sin usar Sin usar argumento hipotético Haciendo una adición de BX Sí, pasamos, digamos, de la implicación de UX A una negación de UX Y con un O De AX, que esa sería la implicación de discusión Sí, claro A eso le adicionas el BX devolves a la, bueno ahí lo tenés que obviamente hacer pero con el primero es que se me olvidó, ¿cuál es esta propiedad? que uno puede, si tiene la misma operación hacer una primero o la otra que no es conmutación asociatividad asociatividad entre AX, BX

## [00:46:37]

y ya devolves ahora sí a a la implicación, entonces ya te queda VX implica AX OX y como eso implica QX por cirugismo hipotético creo que es o ya llega directamente no, no, no, no llego directamente porque necesito la hipótesis de VX, supongamos si no, no puedo dispararla ah bueno, si, si no, no puedo empezar ok, correcto, si siempre se ocupa si, si siempre se ocupa ok, ok este lo que esta línea 9 dice simplemente es, bueno, en caso de que V de X, entonces Q de X ¿verdad? lo cual coincide con la hipótesis, o sea, yo no estoy afirmando de que exista nada que se llame el vinagre yo digo en caso de que existiera vinagre entonces sería una sustancia química no hay ningún tipo de sentencia existencial acá este eso es algo así como si yo dijera este si usted es alguien de la casa Targaryen y dice la palabra Dracarys, entonces un dragón puede matar gente escupiendo fuego ok, sí

## [00:48:23]

por eso no implica ni que existan dragones ni que el alto valirio sea un idioma, verdad, sea un idioma que haya hablado alguien alguna vez ok, entonces el último paso sería justamente este entonces ahora si que ya yo tengo V de X implica Q de X entonces si puedo decir paso 10 que este 10 viene de 9 por este generalización universal entonces si no solamente lo pudimos simbolizar sino que lo pudimos demostrar Aunque bueno, requirió un argumento hipotético. Entonces vean cómo, vean el proceso de demostración en acción. De alguna manera yo me sé las reglas de inferencia y de sustitución y yo no, y es algo que Andrés tampoco hizo, ni Sebastián. no empezamos a hit the bush como se dice en inglés a probar a lo loco con las reglas con cual le podía ocupar, sino que más o menos teníamos una idea de por dónde podía esto cómo podíamos construir la demostración porque somos personas

## [00:50:54]

las personas sabemos hacer eso nadie sabe cómo, dicho sea de paso, todavía no tenemos la menor idea de cómo los seres humanos hacemos eso como generamos heurísticos para empezar a crear demostraciones la inteligencia artificial todavía tampoco tiene eso entonces pero ustedes me van a decir pero ya hay matemáticos usando como inteligencias artificiales para que los ayuden a hacer demostraciones así lo que pasa es primero los matemáticos seleccionan cuidadosamente los textos que les dan a estas inteligencias generativas para que hagan búsquedas ahí, porque en el fondo eso es una búsqueda guiada por criterios estocásticos, en primer lugar. En segundo lugar las computadoras no usan heurísticos usan fuerza bruta lo que pasa es que si usted tiene una cantidad de procesadores tan grande como con la que cuenta este tipo de instalaciones entonces la fuerza bruta al cabo de una semana

## [00:52:27]

pues ha probado una cantidad tan escandalosamente alta de combinaciones posibles para hacer la demostración de que al final como les he dicho en alguna otra ocasión no sé si a ustedes es como si un huracán entrara en una en una bodega con partes de un avión y si el huracán dura mil millones de años pues al final arma el avión solo probar una y otra y otra cosas haciendo las pruebas a velocidad de nanosegundos verdad entonces no en el fondo estas no están demostrando nada y también yo les digo con qué criterio ya tienen que detenerse verdad entonces no demostrar no no demuestren ahora que ya se asentó el polvo porque Sam Altman salió a los medios proclamando oigan nuestra inteligencia ya demostró uno de los problemas del milenio una una tesis muy importante con respecto a ciertos casos de de las leyes de Navier y Stokes que mecánica de fluidos pero ya que cuando lo examinaron con cuidado

## [00:54:02]

qué fue lo que hizo, a qué conclusión llegó se dieron cuenta que no no resolvió el problema o sea resolvió un caso particular con ciertos supuestos muy fuertes del teorema, eso sí lo hizo pero lo que el teorema la hipótesis que se quiere demostrar, no, esa no ha sido demostrada, y dicho sea de paso gastaron el equivalente en tokens de más de 10 millones de dólares para poder hacer eso, ok, entonces de esto es en el fondo de lo que trata el paradigma lógico. Primero tener simbolización y luego demostración utilizando las sentencias ya cuantificadas.

## [00:55:07]

Un momentito.

## [00:55:39]

No, me equivoqué.

## [00:55:42]

¿Los maestros son entusiastas o carecen de éxito?

## [00:55:47]

No todos los maestros carecen de éxito. Por lo tanto, hay maestros entusiastas que Este, podemos suponer que M de X significa que X es entusiasta, bueno, perdón, X es maestro, disculpen, M de X es que X es maestro, E de X que X es entusiasta, y C de X es carece de éxito, ok, ¿cómo simbolizaríamos esto? ahora sí, ya viéndolo mejor entonces podría ser igual vamos a hacer un intento para todo x entonces ahora sí ya tenemos el cuantificador sería m de x implica e de x o c de x así, juntos la otra sentencia podría ser ¿cómo dijiste con la primera? ok, para todo x cumple que m de x implica e de x o c de x ajá, sí, sí, estoy de acuerdo la otra creo que podría ser más bien con existencial existe x tal que esto es lo más sorprendente tal que m de x bueno, ahí habría que negar el x no todo lo más hay que poner como que existe un X en el cual es maestro y no tiene X

## [00:57:53]

entonces creo que lo haría E de X tal que M de X y no E de X por ejemplo ahí habría que mejorar eso y por lo tanto entonces sería existe X tal que M de X implica C de X perdón E de X ok, ok y solo la segunda, ¿verdad? que tal vez está para terminar sí, sí, sí pero eso estuvo muy bien eso estuvo bastante bien nuevamente sí te haría una observación pero eso eso estuvo muy bien vamos a ver vamos a precisar ahí estoy compartir voy a traerme vamos a ver, la primera sentencia dice los maestros son entusiastas o carecen de éxito y yo estoy completamente de acuerdo con la simbolización que hiciste, voy a traerme esta de aquí, solo para no copiar demasiados símbolos, entonces para todo X este si X es un maestro entonces Entonces, no es ahí, es aquí. Entonces, o es entusiasta o carece de éxito.

## [01:00:37]

Ahora, la otra fue interesante. Te fuiste, Andrés, directamente al existencial.

## [01:00:51]

En mi caso particular, una de las cosas que a mí todavía hoy en día me da terribles problemas cuando hago demostraciones o inclusive cuando hago cálculos es que siempre se me queda perdido algo, siempre un signo, un punto algún factor es espantoso entonces llegué a la conclusión de que yo no puedo saltarme pasos yo mi inteligencia no da para tanto yo no tengo una inteligencia rápida no tengo una inteligencia este de gran alcance, no si yo salto pasos, dejo algo perdido así que no voy a volver a saltar pasos, así que yo lo haría más despacito esto, yo en particular entonces dice, no todos los maestros carecen de de éxito ok, entonces yo digo, no para todo X, o sea, no todos los maestros, no para todo de que si X es un maestro, entonces carece de éxito, yo no me tenía la existencia todavía, yo este entonces la conclusión que esto nos trata de decir es entonces este, por lo tanto

## [01:03:00]

hay maestros entusiastas si, no está diciendo que todos los maestros sean entusiastas dice que existen algunos Hay algunos. Yo interpretaría que ahora sí la conclusión sí me está pidiendo un existencial. Entonces, aparentemente, aquí me está diciendo existe un X que es un maestro. Y aquí sí te tengo que señalar una cosa. Los existenciales usan el Y. Entonces, existen X que son maestros y son entusiastas. Ahí no diría una implicación. Esto es interesante demostrarlo, ¿verdad? lo último es por el hecho de que no siempre se va a cumplir digamos dependiendo del X por eso es que hacemos el Y no, este, porque más bien si hay un X o sea, si existe un individuo que dice es maestro y es entusiasta hay maestros entusiastas o sea, no es hipotético tienen ambas cualidades es que la implicación siempre es hipotética ok, ok entonces yo mismo me pregunto, ¿será demostrable esto? Esto sería uno sería

## [01:05:13]

a esa área donde quiero llegar entonces esto es una premisa esto también entonces, ¿qué haría yo?

## [01:05:48]

bueno como te decía yo prefiero andar despacito aquí entonces por eso pondría esto la negación de el, o sea ahora aplicaría la regla de negación de el del cuantificador si no para todo x algo entonces existe un x tal que no algo entonces la negación del cuantificador sería existe un x tal que no es cierto que m de x implica c de x no era una copia era un cut ok entonces 3 viene de 2 por negación del cuantificador existencial como te digo eso es porque yo carezco por completo de la destreza de saltar pasos cada vez que lo hago meto la pata en algún lado ok, entonces mi paso 4 sería ok, no tenía necesidad de esto o sí sí, sí la tenía ahora hago esto que es una sugerencia que ya habías hecho antes que lo tenías muy claro Andrés eso es la definición de implicación material entonces 4 viene de 3 por este definición de implicación material ok 5 sería de Morgan ¿verdad? si aplico aquí

## [01:09:30]

de Morgan entonces voy a tener MDX y perdón aquí es si es un O, esto es I CDX ¿verdad? entonces 5 viene de 4 por de Morgan ok supuestamente debería poder llegar aquí, si el argumento fuera válido, verdad ok, parece que sí, verdad, parece que sí se puede porque, cuál sería a partir de aquí nuestra estrategia yo diría que podríamos hacer ejemplificación existencial, ahora sí entonces puedo hacer simplificación y quedarme con solo el MDX si me quedo con el MDX entonces aplicaría luego ejemplificación universal sobre esta y podría tener EDX o CDX ok pero yo necesito llegar solo a CDX ya lo tenés porque también de 5 puedes simplificar no cdx y por si lo mismo es de un tivo quitar la c y ya te quedas con x correcto, correcto también podría aplicarse este modus tollens también lo puedes negar porque tengo edx o cdx y esto equivale a que este edx vamos a ver implica no c de x y tengo no c de x

## [01:12:27]

entonces puedo sacar e de x bueno, perdón, podría hacerlo al revés ¿verdad? que c de x implica no e de x perdón, no c de x implica e de x y ya tengo no c de x y tendría el e de x y ya tendría el de acá ¿verdad?

## [01:13:04]

ese es 6 tendría puedo usar la misma variable ah, un momentito tengo que ser cuidadoso con eso tengo que ser muy cuidadoso con eso eso es otra cosa este 6 sería voy a hacerlo así introduzco una variable nueva porque esta variable está siendo introducida por un existencial hay que tener mucho cuidado con las variables nuevas que se introducen cuando usted ejemplifica porque no queremos cometer una falacia de generalización entonces hay que ser muy cuidadoso con las variables m de y y no c de y esta viene de 5 por ejemplificación existencial ok entonces ahora si uso esta 7 este es un para todo o sea en particular se aplicaría a y puesto que es un para todo entonces 7 viene de 1 por ejemplificación universal copy en lugar de poner restricciones sobre las variables copy lo que hace es usar un argumento hipotético para hacer la ejemplificación existencial esa es otra forma de ver esto ok

## [01:16:05]

entonces por simplificación yo puedo tener m de y por simplificación en 6 esto viene de 6 por simplificación muy bien entonces ya yo tengo esto bueno también está bien hay varios órdenes en los cuales se puede hacer pero no alteran el resultado entonces 9 viene de 7 y de 8 por modus ponens o k entonces seamos muy estrictos si aplicamos las reglas como se debe porque esto es un proceso formal aquí podríamos habernos saltado un paso pero podemos hacer esto no, eso no eso es una estupidez esto tiene más sentido no ahí eso claramente viene de nueve por este conmutatividad que es una de las reglas de sustitución de Irving Copie ok entonces si C, Y, O E de Y entonces no C de Y implica E de Y esto viene de 10 por la definición de implicación material bueno, en realidad estoy aplicando dos reglas definición de implicación material y doble negación para ser así bien bien bien formales entonces 12

## [01:20:15]

no C de Y también por simplificación simplificación en 6 ok, entonces ya tengo E de Y eso es 13 y tengo 13 por 11 y 12 por modus ponens ok, entonces ¿a dónde quiero llegar? a M de X y E de X ya tengo E de Y tengo M de Y entonces precisamente ya tengo 14 M de Y y E de Y esto viene de 8 y 13 por conjunción ok, ya tengo el M y ya tengo esto entonces, véanlo aquí Y fue introducida por una ejemplificación existencial entonces, eso me da permiso de que en esta sentencia yo pueda hacer una generalización existencial porque estoy refiriéndome a ese Y sé que existe por lo menos un individuo así porque eso vino desde acá, entonces este Y que yo no sé quién sea pero sé que existe sé que existe porque eso vino de acá, entonces es a ese Y al que me estoy refiriendo Entonces, eso me permite Mira, yo no esperaba que fuera demostrable Y sí, sí lo es Eso me permite decir que existe un X Tal que MDX y EDX

## [01:24:19]

Entonces, podríamos recalcar el hecho De que esa Y fue introducida por un operador existencial Haciendo alusión precisamente a la línea 6 entonces eso viene de 6 y de 14 por generalización existencial y voilà, si, si era cierto si pudimos llegar acá fácil o no, verdad mucho más larga esta demostración, verdad y eso que aquí me salte un paso, verdad, porque lo que había que decir era no, no sé de para poder llegar aquí con la definición estricta de implicación material ok opiniones como lo ven ok tomen en cuenta que si el clima nos lo permite en el segundo parcial puede que se topen con un ejercicio de estos así que afilen un poquitito sus destrezas en simbolización y en demostración porque son implícitas del paradigma lógico ok, como ustedes vieron, aquí yo tengo una lista de 17 no, mentira, de 19 de 19 ejercicios de demostración en grado creciente de complejidad son válidos

## [01:26:55]

no me he fijado en esta parte y todos son válidos bueno, válido habría que tener el contraejemplo para para digamos decir que no es válido para ser formal no, no, es que la demostración de que es válido es encontrando la demostración precisamente no, digo, si fuera el caso en que aquí todos los ejercicios son válidos, pero si fuera el caso que por ejemplo hubiese uno que no es válido, habría que presentar el contraejemplo si es posible encontrar alguno si yo les indicaría si existe algún contraejemplo ok, ok es que no ser demostrable es que como demuestras que algo no es demostrable, verdad es por eso esa es la precisamente el el lío en que nos metió GEDDEL, verdad no puedes demostrar que algo no es demostrable, aunque sabemos que existen cosas que son verdaderas y no son demostrables, ¿verdad?

## [01:28:22]

Y claro, si algo, si un argumento es falso, o sea, si un argumento es incorrecto, o sea, una conclusión no se extrae de las premisas de no podría ser un argumento o construirse un argumento válido alrededor.

## [01:28:42]

O sea, no debería haber si las premisas son verdaderas no debería haber ninguna manera válida de llegar a una conclusión falsa verdad porque de hecho eso no puede pasar porque las reglas de inferencia son precisamente tautologías o sea esa es la belleza la belleza que tiene el argumento los argumentos de la lógica el hermoso no sólo la belleza el enorme poder que tiene la lógica simbólica. Este, si me permiten, por favor, disculpen que me extiendo un poquitito en esto, pero hay una película que muestra o trata de mostrar, digamos, cómo fue la hazaña de devolver a la Tierra a los astronautas del Apolo 13. el Apolo 13 era la tercera perdón, la segunda la tercera misión que iba hacia la luna sí, sí fuimos a la luna y le estalló por alguna razón no sé si la investigación llegó a concluir por qué es que estalló un tanque de oxígeno cuando iban de camino

## [01:30:31]

y eso puso en peligro la vida de los astronautas ya no podían, no había suficiente combustible para que completaran la misión y pudieran regresar entonces lo que se vieron forzados a hacer fue lo que se llama un slingshot gravitacional en la luna y aprovechar ese slingshot y el poco combustible que les quedaba para regresar a la Tierra les comento esta película porque hay una escena que desde la primera vez que la vi me impactó profundamente yo no sé si habrá sido así en la realidad o no pero aunque fuera ficticio sería hermoso en que el capitán, el comandante de la misión que por cierto Tom Hanks es el que el actor que encarna al comandante de la misión cuando ya Dave simplemente dan el slingshot y aprovechando eso ya se vienen dirigiendo hacia la Tierra y necesitan ahorrar combustible entonces simplemente cortan el suministro se usaron los motores solamente para realinear la órbita del

## [01:32:06]

del módulo de comando y con eso dispararse salirse de la empujoncito para salir de la órbita lunar y de esa forma aprovechar la ese slingshot yo no sé si esto sea cierto o no pero es tan hermoso porque el comandante dice en ese momento bueno Houston informó que en este momento la nave está siendo piloteada por Sir Isaac Newton es bellísimo es el poder de la ciencia el poder de la razón el poder del razonamiento Newton jamás hubiera imaginado una situación como esta pero las reglas que Newton dedujo utilizando lógica fueron, gracias a que usó lógica, fueron correctas y aún en esta otra situación que Newton jamás hubiera previsto y que a velocidades con las que andábamos no era necesario ni grandes masas, no era necesario utilizar mecánica relativista no, no, la misma vieja mecánica, bueno la misma mecánica, las reglas de la mecánica en la física del siglo XVIII podían aplicarse

## [01:33:43]

y funcionaron esto es hermoso, realmente es el poder de la razón humana y ese poder de la razón humana descansa en esto que están viendo en sus pantallas en este momento en el poder de la lógica ok, entonces yo les voy a subir estos ejercicios de lógica y entonces la pregunta que nos queda es, bueno ok, esto es el paradigma lógico Tenemos que poder simbolizar nuestros algoritmos como si fueran sentencias lógicas. Y tenemos entonces que reducir cualquier tipo de ejecución de un algoritmo, lo que sería la ejecución de un algoritmo, un paradigma imperativo, a la demostración de algo, de alguna manera. que se puede, se puede o sea, el paradigma lógico es teoría en completo pero como ven cuesta un poquitillo más adaptarse a esta otra forma de demostrar a esta otra forma de concebir los algoritmos ok, no sé si tienen alguna pregunta está bien, excelente pura vida, muchas gracias Andrés

## [01:35:29]

Sí, profe, por el momento no Ya a la hora de la verdad empezar Ahí veremos, pero por el momento no Sí, voy a empezar Otra vez más Una vez más, disculpen ¿Cómo se ve el máximo común divisor Descrito en lógica?

## [01:35:49]

Perdón, el mínimo común múltiplo Que ese ha sido el ejemplito Chiquitito que he estado exhibiendo Una y otra vez en todos los paradigmas Este Para ejemplificar estas ideas porque, que es bonito este mínimo como un múltiplo, tan humilde que se ve y tiene de todo entonces, ¿cómo se vería mínimo como un múltiplo de paradigma lógico? ¿cómo describo el algoritmo como un conjunto de sentencias lógicas? bueno, vamos a ver eso en la próxima clase, que va a ser el, ok, hoy estamos, vamos a ver 6 de octubre, pucha ya vino octubre ya estamos en octubre ahorita se acaba este semestre nos queda de octubre y noviembre y nos vemos el próximo jueves 8 el jueves 8 de octubre ok voy a terminar la grabación acá
