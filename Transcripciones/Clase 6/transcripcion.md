---
clase: "Clase 6"
curso: "Lenguajes de programación"
temas: ["paradigma lógico", "orientado a objetos"]
fuente: audio1902695593.m4a
modelo: large-v3
idioma: es
duration_sec: 5721.3
---

## [00:00:01]

Bueno, entonces, para que quede en el vídeo, la semana entrante, que es la semana del 19 al 23, por solicitud de la Vicerrectoría de Docencia y de la Federación de Estudiantes, tal y como yo lo entiendo, vamos entonces a hacer actividades asincrónicas en lugar de nuestras clases virtuales sincrónicas bueno ok, entonces estamos con que para hacer programación lógica una estrategia que sea que se adoptó es el de tratar de tener un lenguaje lógico mucho más simple pero que sea equipotente con el cálculo de predicados de primer orden o sea que pueda ser lo mismo ok, entonces una propuesta de eso es la que planteó el lógico estadounidense John Robinson en los años 60 del siglo pasado que se llama regla de resolución

## [00:01:30]

Y en lo que consiste, bueno, según el planteamiento de Robinson, es eliminar todas las conectivas, exceptuando la negación que en cierta forma no es ninguna conectiva porque no conecta ni siquiera dos entidades, solamente modifica una, un predicado. y eliminar las veintitantas reglas de inferencia del sistema de copy y reemplazarlo por una sola regla, la regla de resolución. Claro, con el requisito previo de haber transformado todas nuestras sentencias del cálculo de predicados a cláusulas. entonces habíamos quedado que la regla de resolución tal y como la plantea Robinson se vería de esta forma que si C1 es una cláusula puesto que ahora se van a ver así las cláusulas donde lambda p y q son predicados con la aridad que sea necesario decíamos que c1 entonces puede verse como el conjunto que contiene a lambda unión el conjunto que contiene todo lo demás y si tenemos una segunda cláusula

## [00:03:27]

que contiene al inverso de lambda o la negación de lambda con otro conjunto de predicados A, B, los que sean entonces C2 se puede ver como lambda negado o sea, el conjunto que contiene lambda negado, unión el resto o sea, A, B, etc. están metidos en M entonces se ve como la unión de dos conjuntos entonces resolución sería así se dice que se resuelven C1 y C2 de la siguiente forma si yo tengo lambda el conjunto que contiene lambda, unión K y el conjunto que no contiene a lambda perdón, que disculpe, que contiene el el not de lambda o no lambda el negativo de lambda, digámoslo así unión M entonces esto resuelve creando una nueva cláusula que es la unión de K y M ok permítanme voy a compartirles las viejas reglas de inferencia del sistema de copy y yo les decía, traten de traten de demostrar utilizando resolución Modus ponens, modus tollens el silogismo hipotético y el dilema constructivo

## [00:05:46]

no sé si alguno de ustedes hizo la el intento de de demostrarlos voy a suponer no, no, bueno ok Andrés, muchas gracias por tu, por mencionarlo bueno, hagámoslo hagámoslo para que ustedes vean cómo se, cómo funciona esto ok, modus ponens perdón, voy a compartir no estoy compartiendo, perdón este modus ponens se ve como si P implica Q no es muy listo esta inteligencia artificial y tengo P bueno, voy a insertar esto si P implica Q y tengo P de ahí puedo inferir ese es el famoso modus ponens y debo decir el importantísimo modus ponens ok ¿cómo se vería esto bajo el esquema de resolución? bueno P implica Q equivale a no P o Q y listo Ya esto nos queda de una forma En una forma De cláusula Es inmediato, ¿no? Porque ya como tiene el no P y el P Entonces se van y queda Q, ¿no? Correcto Qué desastre es esto No me entendió nada, no me entendió ni papa Este En resolución Tendría

## [00:08:52]

¿De qué se me hizo? Aquí está Aquí tendría No P coma bueno, por lo menos acertó con la Q la otra cláusula contiene sola P entonces Andrés correctamente no señala que aquí tengo o sea, esta yo la puedo ver, hagámoslo despacio esto se me transforma en vamos a poner otro aquí haciéndolo despacito despacito y con buena letra en no P unión Q y la otra sentencia ¿en qué se me transforma?

## [00:10:26]

P porque resolución exige que yo tenga lambda unión algo y no lambda unión otra cosa entonces yo necesito una unión aquí ¿unión con quién? ¿y con la Q? no con el vacío ah sí, porque es el otro ajá, es esta esta es la que es no P unión Q y esta es P unión vacío sobre esto aquí sí puedo aplicar resolución y este por cierto P en este caso se llama el átomo resuelto o sea, Robinson propone que cada uno de los elementos de la cláusula se llamen átomos entonces este es el átomo resuelto y el resolvente que es el resultado del proceso va a ser ¿quién?

## [00:11:44]

va a ser este o sea, estoy haciéndolo bien bien bien formal para tratar de entenderlo mejor entonces el resolvente va a ser Q unión vacío que es precisamente Q y justamente esto es esto ok entonces bueno digamos que es una cosa muy bonita que modus ponens se transforma que es una axioma es una regla del cálculo de predicados es en regla de resolución es un teorema, ok ya podemos proceder un poquito más rápido, Modus Tollens Modus Tollens dice algo parecido a esto dice si P implica Q y aquí en realidad lo que tengo es no Q si no me equivoco sale directo si exactamente entonces debería tener en un peor da entonces con resolución esto se va a ver otra vez como voy a llevarme esto no peor que esté aquí solo que aquí en cambio voy a tener este no q así que si en cambio o sea ésta la puedo ver como Q coma no P y aquí tengo no Q y entonces esto resuelve en este no P puesto que Q

## [00:14:30]

y no Q desaparecen este es el resolvente con eso si está probado que toda sentencia bueno toda demostración con cálculo de primer orden también se puede realizar con con regla de resolución o solo bajo ciertas condiciones ok digámoslo así poniéndome este poniéndome muy quisquilloso si me disculpas por favor creo que lo que quisiste decir es más bien que si todo lo que es demostrable en cálculo de predicados de primer orden es demostrable en resolución más bien Ya, porque la demostración obviamente son diferentísimas, ¿verdad? Pero lo importante es que lo que sea demostrable en uno sea demostrable en el otro. Y viceversa. Esa es una característica que es una pregunta sumamente importante. Lo que estaremos preguntando ahí es si la regla de resolución es completa.

## [00:15:56]

Porque nuestro conjunto de referencias siempre es el cálculo de predicados de primer orden. entonces sí, la gran pregunta es si cualquier cosa que sea demostrable en cálculo de predicados del primer orden va a ser demostrable usando resolución digamos la pregunta es, ¿será regla de resolución completa?

## [00:16:21]

muy bien, eso es una muy buena pregunta vamos a contestarla dentro de un momento, pero sí esa es la pregunta siguiente que tenemos que hacernos listo, listo, perfecto claro, mucho gusto este, ok, entonces para completar acá es muy claro a la hora de resolver estos dos es obvio que quien desaparece es no P, verdad perdón, es Q disculpen entonces quien me queda nada más es no P, que es exactamente lo que yo quería que quedara ok, entonces yo les mencionaba que podían probar con el silogismo hipotético P implica Q, Q implica R por lo tanto Q implica R como ven este nombre es muy viejo porque esa regla no es un silogismo de ninguna manera pero se le quedó ese nombre, pero no es un silogismo más adelante vamos a hablar de los silogismos vamos a ver si podemos hacer alguna cosita bonita con programación lógica y silogismos, entonces lo que estamos diciendo también es que yo no ayudo porque

## [00:18:20]

yo si que dibujo feo decimos P por consiguiente Q Q por consiguiente R y de aquí queremos concluir G P implica R good lord jesus christ mejor borro esto porque se puso la cosa muy fea yo no sé ahí donde había una sumatoria verdad que sí está bien yo dibujo muy feo porque no es para tanto entonces voy a hacerlo aquí por lo tanto este P implica R R ok, en resolución esto se vería como no P o Q nuestro viejo amigo no P o Q no Q o R y aquí ya también queda muy directo aplicando resolución de que tengo aquí el Q y aquí el no Q entonces el átomo resuelto es Q así que me va a quedar no P unión R y eso es exactamente esto está bonito está bonito por ahora digámoslo así va bien este por ahora decimos que el otro es este es más elaborado el dilema constructivo P implica Q y R implica S P o R y entonces Q o S este se ve más interesante ¿verdad? entonces este es el dilema constructivo si está bien

## [00:22:02]

entonces es P implica Q y siempre se me pierden es que no están aquí, deberían ¿verdad? porque si está en el universal y el existencial deberían estar ahí P implica Q Y R implica S Además Tengo P O R Y de aquí queremos Concluir Q o S Mejor me llevo a la siguiente página para que no sea tan feo Ok, este se ve un poquitito Más interesante, ¿verdad?

## [00:24:07]

Ok, usando resolución Tenemos que transformar esto a cláusulas Entonces esto se me transforma en dos cláusulas ¿verdad? y esta es una tercera o sea usando resolución aquí yo voy a tener no P o Q por este no R o S como cláusulas aparte y además voy a tener P o R ok entonces resolviendo Esta Resuelve con esta ¿Verdad?

## [00:25:48]

Es más, voy a hacer esto A esta la voy a poner 1 para poder identificarla Porque ya tengo varias Entonces Esta es 2 y esta es 3 Entonces resolviendo Resolviendo 1 Con 3 Obtengo Q O R ¿Verdad? porque entonces hago la unión de esto con la unión de esto entonces esto me da una sentencia que puedo llamar 4 bueno, una cláusula que yo llamaría 4, yo no sé por qué se puso eso así, ok entonces ahora puedo resolver 4, vamos a ver no, sí, sí, mentira, 2 con 4 si resuelvo 2 con 4, ¿qué voy a obtener? 5, ¿verdad? ¿y 5 es quién? si resuelvo 2 con 4 el átomo resuelto es R entonces me va a quedar Q unión S y voilà esa es a donde queríamos llegar ok ¿alguna pregunta?

## [00:27:58]

bien, bien, todavía no, claro, sí bien, así es como se demostraba lo que quería que ustedes hicieran este digamos como ejercicio ok este ahora entonces tratemos de responder la pregunta que nos hizo Andrés ¿cómo puedo yo hacer para demostrar que cualquier cosa demostrable en el cálculo de predicados es demostrable en resolución ok este parece que la cosa es relativamente sencilla desde este punto de vista cómo hago yo para demostrar cosas en cálculo de predicados respuesta uso las reglas de inferencia si yo usara algo que no es una de las reglas de inferencia entonces listo eso invalida mi demostración ahora si se dan cuenta las reglas del cuantificador lo que hacen es que agregan el cuantificador o quitan el cuantificador o sea las reglas de manejo del cuantificador no me cambian mis sentencias en el

## [00:30:09]

sentido de que el mismo conjunto de símbolos, la misma fórmula bien formada que está en el alcance del cuantificador, no se altera. Lo único que se altera es una sustitución de variables por otras variables o tal vez variables por constantes. Pero las fórmulas bien formadas no cambian. Si se dan cuenta, las reglas de inferencia, voy a ponérselas acá, las reglas de inferencia, en cambio, o sea, las nueve reglas de inferencia como tales, y las diez reglas de sustitución, sí me, ya sea agregan, bueno, de hecho agregan a mi conjunto original delta de sentencias otras fórmulas bien formadas que son diferentes de las fórmulas originales entonces estas si me agregan este me cambian por ejemplo conectivas este eliminan predicados o sea estas si transforman las fórmulas bien formadas así que la cosa es así si cualquiera de las reglas de inferencia y de reemplazo puede ser expresada en el cálculo

## [00:31:58]

de resolución entonces el cálculo de resolución sería completo así que tenemos que preguntarnos si alguna de las reglas de inferencia no es posible demostrarla usando resolución ok, ya vimos que Mousponens Mousponens, silogismo hipotético dilema constructivo, sí el silogismo disyuntivo es obvio que también, pero ¿qué pasa con la conjunción?

## [00:32:51]

algo más trivial cuando son impotentes De ahí no hay negado Por ejemplo No, porque Al seguir Decir vos la doble negación No, digamos que si uno tiene P o P, entonces da P Pero es que eso no es una regla de inferencia Pero es de simplificación No cuenta Ah, ok, ok, que está aquí decir vos Ajá, desde abajito Ajá Concentrémonos en la conjunción Ok, ok, ok Ok en la conjunción si yo tengo P y tengo Q ¿con quién resuelvo?

## [00:33:47]

no hay átomo resuelto tengo una sentencia, perdón, una cláusula que dice P y otra cláusula que dice Q no tengo ninguna manera de resolver para poder obtener al final P y Q peor, simplificación bueno, simplificación se transforma igual porque tengo P, tengo Q no, esta sí, porque si tengo P y tengo Q tengo P, eso sí se puede ver bien adición adición sí es un lío porque como de P puedo obtener P o Q, mediante resolución, no hay manera o sea resolución así como la estamos viendo no es completa ok, entonces eso quiere decir que hasta aquí llegamos bueno No, obviamente no. Digo obviamente porque si le estamos utilizando y exponiendo y dándonos tanto trabajo es porque Robinson encontró una forma de salir de la toalladera y eso es lo que vamos a ver a continuación. Vean una cosa Este Yo les pregunto ¿Qué les parece Esta Esta sentencia es muy simple Pero es muy famosa Y es muy importante

## [00:35:51]

¿Qué les parece que yo tenga Esto Eso tiene un valor de verdad ¿Cierto?

## [00:36:21]

Siempre es falso Ese tipo de sentencias tienen un nombre, lógica son contradicciones no, es una contradicción una falacia es otra cosa una falacia es una sentencia que está mal demostrada o sea que la conclusión no se extrae de las premisas con la demostración que usted me ha dado usted tiene sus premisas y quiere decirme y de estas premisas se obtiene esta conclusión pero la demostración que usted hace es incorrecta eso es una falacia entonces hay falacias formales y hay falacias no formales en una falacia formal efectivamente se así se trabaja con una demostración como hemos visto pero en algún punto yo estoy invocando mal alguna regla de inferencia o me Estoy inventando una regla de inferencia.

## [00:37:41]

Por ejemplo, la falacia del antecedente. Es una falacia formal.

## [00:37:51]

Si yo digo, por ejemplo, si llueve y no ando paraguas, entonces voy a quedar mojado. ok digamos que yo quedo por alguna razón completamente mojado y entonces digo ah ok eso significa que llovió y usted no andaba para aguas verdad no no no eso no funciona así ya P implica Q pero si tengo Q eso no significa que P eso solo pasa si P es equivalente a Q. Pero si solamente P implica Q, pues eso no significa que Q implica P. Si P implica Q, no Q implica no P. ¿Verdad? Puede ser, por ejemplo, que yo estuviera pasando por un jardín donde hay aspersores y cuando yo estaba pasando, los aspersores empezaron a tirar agua o puede que yo estuviera en la parada del autobús y había un hueco en la parada del autobús y llegó un automóvil pegó en el hueco y con eso me mojó ven esa es una falacia formal las falacias informales son este son muchas veces juegos con el lenguaje que que en realidad

## [00:39:39]

no están demostrando nada a mí me realmente me me decepcionan bueno hay gente que no me decepciona porque es imposible que me decepcionen porque yo nunca creía en ellos desde el principio, en ningún momento pero si es horrible que en cosas que son muy importantes que deciden el destino de millones de personas se trate de justificar alguna conclusión con una evidente falacia y las falacias me preocupan mucho porque nosotros los que pasamos por una educación de alto nivel una educación universitaria deberíamos estar muy atentos y nosotros más que ninguna otra persona deberíamos ser capaces de detectar las falacias y si es el caso inclusive si tiene la importancia denunciar que se nos quiere hacer creer en algunas cosas usando falacias les voy a dar dos ejemplos el primero es este benjamín netanyahu primer ministro de israel se acaba de presentar en la asamblea general de las naciones

## [00:41:15]

unidas ok alguno de ustedes sabe cómo contestó Netanyahu a la acusación de que el gobierno israelí está cometiendo un genocidio contra el pueblo palestino o sea, eso puede ser cierto o puede ser falso ¿verdad? estamos aquí viéndolo desde un punto de vista lógico ok, entonces Netanyahu está en el podio y quiere demostrar que esa acusación contra el gobierno de Israel es falsa tiene todo el derecho del mundo de defenderse y presentar sus alegatos de por qué esa sentencia es falsa no sé si alguno de ustedes se dio cuenta qué fue lo que dijo para decir para justificar que su gobierno no podía ser acusado de genocidio yo no personal no tengo idea bueno Bueno, Benjamín Netanyahu dijo, Inglaterra y Francia nos están acusando de comportarnos como una potencia colonialista y masacrar a la población palestina.

## [00:42:41]

Pero, ¿qué autoridad tienen Inglaterra y Francia de acusarnos de ser un país colonial y de hacer masacre sobre otras personas, si ellos fueron potencias coloniales que masacraron a las poblaciones donde se establecieron? ese fue el argumento de Netanyahu ok, a ustedes que les parece es una falacia o no es una falacia o sea, está realmente demostrado que con ese argumento yo no puedo acusar al gobierno israelí de comportarse de una manera colonialista y acusarlo de las masacres y es que es decir como, y tú más no se quita simplemente acusa al otro de lo mismo ok, sí y se llama así esa falacia tiene nombre y se llama tiene un nombre en latín porque es una falacia viejísima ya en la edad media los monjes de la edad media se habían dado cuenta de que eso no es correcto se llama la falacia del tú cuocue o sea la falacia del tú también si usted incurrió en el mismo comportamiento, entonces

## [00:44:16]

no puede decirme que si yo que es incorrecto que yo me comporte de como me comporto, no, no es cierto no es cierto eso no es lo que dice Netanyahu es verdad o sea, Francia y el Reino Unido establecieron sistemas coloniales donde masacraron a la población Francia por ejemplo en Argelia Bélgica, en el Congo el Reino Unido bueno, el Reino Unido o Inglaterra cuando llegó a los Estados Unidos empezó a desplazar y a empujar a las poblaciones nativas indígenas y en la India cometió atroces masacres contra la población eso es totalmente cierto pero eso no significa que no lo puedan criticar o que no que eso no significa que Israel no se esté comportando igual ok, entonces es atroz que ante una cosa tan seria, pues un jefe de estado se defienda con una falacia ok otro caso que yo les quería plantear fue bueno ustedes estaban como muy jovencitos en esa época y tal vez no le pusieron cuando

## [00:45:43]

Donald Trump perdió las elecciones contra Biden hace seis años y no mentira sí, hace seis años y para ganar para tratar de ganar en el estado de Georgia le hicieron falta 1300 votos Ok, Trump llama personalmente al oficial de votación, que es republicano, dicho sea de paso, y lo llama personalmente y le dice al funcionario, el jefe, el encargado del sistema electoral de Georgia, republicano, y le dice mira tú sabes que yo gané en Georgia entonces esos 1300 votos tienen que aparecer porque si aparecen entonces demostramos que sí yo gané en Georgia pero tienen que aparecer porque yo efectivamente gané en Georgia what ¿qué tipo de falacia es esa?

## [00:47:17]

suena como una falacia cíclica digamos sí, así se lo llama, argumento circular también se lo llama los filósofos le llaman petición de principio este es es obvio que alguien como Donald Trump no puede darse cuenta de que es una falacia porque es demasiado imbécil para siquiera detectar ni una sola falacia por más sencilla que sea pero que cosa más atroz que una cosa como un proceso electoral tan importante alguien trate de defenderlo con una falacia tan obvia entonces me he extendido en esto, me disculpan por favor porque las falacias me provocan demasiada preocupación este tomemos en cuenta que por ejemplo si las inteligencias artificiales generativas lo único que hacen es la imagen que viene a mi mente es pesca de arrastre o sea, tiran sus redes y ahí recogen todo lo que haya y después tratan de encontrarle algún sentido este usando sus pesos en sus redes neuronales entonces

## [00:48:41]

esa es la forma en que uno puede por ejemplo sesgar a una a una inteligencia artificial de estas aliméntela con suficientes falacias y como es incapaz absolutamente de discriminar desde un punto de vista lógico entonces estas inteligencias artificiales simplemente van a escupir falacias es uno de los riesgos de ese tipo de de mecanismo de recuperación de información yo no sé incluso yo me resisto a llamarlas inteligencia artificial porque para mí tiene más que ver con bases de datos que con inteligencia artificial de verdad este, entonces volvamos a lo que, a lo que, en donde estamos eso es nacido a través de digamos, lo tomé como excusa por la la este lo que me dijo Andrés sobre sobre sobre falacias entonces esto no es una falacia es una contradicción porque es falsa lo que distingue una falacia de una falsedad es que la falsedad es falsa en cambio una falacia es un argumento que

## [00:50:16]

la demostración que se me hace para esa conclusión a partir de ciertas premisas es incorrecta la demostración está mal incluso, no sé si ustedes saben, pero existe una falacia que se llama la falacia de la falacia en inglés tiene un nombre muy simpático porque en inglés se llama fallacy fallacy y consiste en decir precisamente que si una sentencia es falaz o sea que ha sido mal demostrada entonces es falsa no, tampoco se puede decir eso lo que yo puedo decir es que yo no estoy seguro de que algo de que lo que usted me está diciendo es verdad porque lo demostró mal entonces yo no puedo afirmar que sea verdadero pero tampoco puedo afirmar que sea falso decirlo si sería encubrir en la falacia de la falacia en mi opinión pero es sólo mi opinión usted no tiene que compartirla ese es uno de los defectos en los que en mi opinión de nuevo incurre este muchos pensadores ateos o sea es cierto que

## [00:52:01]

Porque ninguna de las demostraciones que se han planteado a lo largo de la historia del pensamiento, en muchas culturas, de la demostración de Dios, ninguna demostración es correcta. todas ellas tienen problemas por eso digamos la gente más eminente, los pensadores cristianos por ejemplo, más eminentes sostienen que la existencia de Dios es algo a lo que se llega por fe no por la razón o sea incluso ellos están de acuerdo no hay una demostración bien construida lógicamente correcta de la existencia de Dios pero la falacia de la falacia en la que algunos pensadores ateos es decir, ok si no se puede demostrar que Dios existe entonces tiene que ser falso que Dios existe ah, no, no eso no es cierto no, no, eso sería incumplir en la falacia de la falacia y sería incorrecto también ok, entonces, pero ¿cuál es el punto en el cual voy? ¿por qué me extendí tanto en esto?

## [00:53:40]

bueno, porque precisamente P, no P y Q es una es una contradicción o sea, esto es siempre falso ok, ahora o sea, no P y P ¿Cómo se ve esto en resolución?

## [00:54:15]

¿Cómo se ve?

## [00:54:32]

Bueno, no P Se vería así, ¿verdad?

## [00:54:38]

O sea, serían dos cláusulas Esta sería la primera Y este Qué curioso es Ah, es por esto Y esta sería la segunda Entonces noten una cosa muy curiosa Pueden resolver Esto pueden resolver con esto ¿Y cuál sería el resultado?

## [00:55:23]

Vacío, vacío. Exactamente, el vacío. Ok, muchas gracias por mencionarlo. Eso me da vacío, el conjunto vacío. Ok, eso significa que en el sistema de Robinson, el conjunto vacío es ni más ni menos la forma en que se manifiesta la contradicción. Ok, entonces Ustedes saben Bien que es la demostración por Contradicción, ¿verdad?

## [00:56:42]

Dice, parte de una premisa y si Partiendo de eso se da una contradicción Significa que di algún paso Que hizo no es válido, que algo es Imposible, partió de algo que dice Contradice, ¿no? Más o menos Más o menos Creo que uno agarra, tiene que Combinar, tiene que como suponer Que algo es falso y combinarlo con la premisa y lograr llegar a que es contradictorio y así se demuestra. ¿Qué es lo que supongo que es falso?

## [00:57:13]

La conclusión. Aquello a lo cual yo quiero llegar. Entonces, la idea es, yo tengo un conjunto delta de premisas y tengo una conclusión, o sea, técnicamente hablando, si lo vemos en lógica,

## [00:57:29]

digamos que delta es un conjunto de premisas y yo de aquí quiero concluir ay no, eso está peor este eso, así se hace quiero llegar a una sentencia o sea, quiero decir que phi es deducible a partir de delta, donde delta es mi conjunto de premisas entonces la este, eso es lo que quiero, se quiere demostrar ay, perdón, ya yo no sé ni escribir castellano, que terrible, ¿verdad?

## [00:58:31]

Perdón, disculpen, disculpen. ¡Ah, demonios! Se quiere demostrar que pi es deducible a partir de delta. O sea, eso significa que existe una demostración, o sea, de que con las, con las premisas que hay en delta, efectivamente, o sea, lo que se quiere hacer es esto. digamos, poniéndonos ya así muy técnicos en lógica, lo que queremos es decir que sí es deducible a partir de delta, pero usando más bien este esto, vamos a ver dónde está debería tenerlo esta cosa es que tengo este pero no, no es este el que me sirve ah, es este que cualquier modelo bajo el cual las sentencias de delta son verdaderas entonces bajo esos modelos phi también es verdadera esto es lo que yo quiero probar mi intención es en realidad ver si esto es verdadero entonces como ustedes dicen lo que se hace es crear un un conjunto delta primo que es igual a delta agregándole fi o más bien disculpen disculpen

## [01:01:50]

no, lo que le agrego es no fi o sea, aquello que yo ¿qué es lo que significa la doble producción? ese símbolo esto ok Ok, significa que así como está bajo cualquier interpretación de las sentencias que están en delta y que hagan verdaderas a las sentencias de delta, entonces esa misma asignación hace verdadero o sea, fi es verdadera con esa misma asignación con esa misma interpretación esto tiene que ver con ser verdadero esto tiene que ver con ser demostrable o sea, que vean que la demostración por contradicción como que tiene una peligrosa goza relación aquí porque tiene una pata en el asunto de la demostración pero tiene otra pata en el asunto de los modelos, el teoría de modelos en realidad ¿verdad?

## [01:03:18]

entonces lo que yo hago es incluir el inverso de phi junto con delta y se llega a una contradicción y de ahí se parte de que si esto agregado aquí transforma a esto en falso, entonces es que el asunto es así. Yo supongo que las cosas que hay en delta, las sentencias que hay en delta son verdaderas.

## [01:04:03]

Pero, si delta unión con no fi hace que el conjunto delta primo se vuelva contradictorio, ¿quién es el culpable?

## [01:04:18]

Delta fi. es lo que se supuso falso exactamente, o sea, no fi por consiguiente como es una lógica binaria o sea, fi o es verdadero o es falso entonces si no fi me da, me provoca que todo este conjunto se vuelva contradictorio el culpable tiene que ser no fi y eso significa entonces que fi debería ser verdadero esa es la justificación de la demostración por contradicción entonces eso debe ser porque esto es falso y entonces uy, esto debería ser verdadero una demostración muy linda por lo sencilla que es, pero también por lo importante que es es la demostración de que raíz de dos no puede ser un número racional este no sé si ustedes recuerdan esa demostración ¿Cómo se demuestra que la raíz cuadrada de 2 no es racional? Era que siempre quedaba un número Digamos, épsilon Que tenía que ser computable en algún momento Tenía que resolver, o sea, que no se podía Determinar su valor exacto

## [01:06:22]

No, no, no, es más sencillo Es mucho más sencillo Este La demostración va así Yo digo, bueno ¿Cómo demuestro que la raíz de 2 No es racional? Bueno, voy a suponer que sí es racional. Y entonces, si sí es racional, se le aplican todas, o sea, son verdaderas todas las sentencias que yo conozco sobre los números racionales. Entonces, si en raíz de dos sí es racional, entonces deben existir dos números enteros A y B tales que A sobre B es igual a la raíz de 2 y además A y B, este, A módulo B es igual a 0.

## [01:07:45]

O sea, no tienen factores en común, son relativamente primos. O, como se dice también, forman una fracción irreducible. para todo número racional existen dos números enteros A y B tales que A y B no tienen factores primos en común ¿verdad? entonces supongamos que A y B son los números que son A sobre B es raíz de 2 y además A y B no tienen factores en común ¿ok? eso significa que raíz cuadrada de 2 es igual a entre b pero eso significa que 2 va a ser igual a a al cuadrado dividido entre b al cuadrado ¿verdad?

## [01:08:52]

¿pero eso qué significa?

## [01:08:57]

eso significa que a al cuadrado es par ¿verdad?

## [01:09:24]

porque a al cuadrado es este 2 por b al cuadrado ok, ahora si yo multiplico un número par por otro número par el resultado es par ¿verdad? 6 por 6, 36 2 por 2, 4 este 4 por 4, 8 o sea, si bueno, es más, bueno, si lo quieren ver de otra forma 2 por 6 es 12 o sea la multiplicación de dos números pares es par ahora 3 por 5 es 15 3 por 7 es 21 7 por 5 es 35 la multiplicación de dos números impares es un impar ahora si a al cuadrado es par a al cuadrado es igual que a por a eso significa que a es par si a es par Entonces A tiene que ser el resultado de 2 multiplicado por alguien más Llamémoslo A' ¿Verdad?

## [01:11:00]

Ok, ahora volvamos acá 2 es igual que A al cuadrado entre B al cuadrado Veámoslo así, perdón 2 por B al cuadrado es igual que A al cuadrado Entonces, 2 por b al cuadrado es igual que 2 por a' al cuadrado, ¿verdad? O sea, 2 por b al cuadrado, voy a llevarme todo esto, 2 por b al cuadrado es igual que 2 al cuadrado, o sea, 2 por 2, por a por a', ¿verdad? O sea, A' por A'. O sea, es 2 al cuadrado por A' al cuadrado. Pero entonces, de ahí, aquí tengo un 2, aquí tengo otro 2. Eso significa que B al cuadrado es igual que 2 por A' por A'. ¿Qué se concluye de ahí entonces?

## [01:13:55]

Que B también es par. Correcto. Entonces B al cuadrado es par. Si, digamos, haciéndolo despacito B al cuadrado es par Así que B es par Luego, eso significa entonces que B Es igual que 2 multiplicado Por algún número B' Ok, entonces volvamos aquí Por consiguiente A entre B Es igual que qué? Que 2 multiplicado por A' dividido entre 2 multiplicado por B'. ¿Dónde está la contradicción?

## [01:15:19]

¿Con quién? ¿Con cuál sentencia estoy así llegando a una contradicción ahí?

## [01:15:31]

Ahí le estaría quedando como que A entre B es igual que A' entre B, ¿no?

## [01:15:39]

Es que la contradicción es esta. yo estaba suponiendo que A y B no tenían factores en común pero viéndolo así si tenían un factor en común ambos son pares entonces tienen por lo menos el 2 exactamente entonces si yo había supuesto que no tenían factores en común y ahora digo si, si tienen factores en común usted dijo P y ahora me está diciendo no P entonces P y no P contradicción Por lo tanto, lo que usted introdujo, que era suponer que raíz de 2 era racional, tiene que ser falso.

## [01:16:32]

Porque eso fue lo que usted coló de pronto en el conjunto, en todo el conjunto delta de las axiomas y teoremas del conjunto de los racionales. entonces de esa forma de esa forma funciona la demostración por contradicción entonces ¿a dónde llegó Robinson? Robinson dijo bueno, ¿y qué tal si las demostraciones las hacemos todas por contradicción?

## [01:17:19]

vamos a ver empecemos a ver si ya sabemos que modus ponens sí se demuestra con resolución ahora, ¿qué pasa si metemos modus ponens y la tratamos de demostrar por contradicción?

## [01:17:48]

ok, entonces yo tendría lo siguiente, devolvámonos a donde estaba modus ponens aquí, voy a llevarme todo esto si, está bien este, este es modus ponens original, y yo quiero llegar a concluir esto ok, entonces, usando esto en en el cálculo de de Robinson se llama así resolución con refutación ok, eso se vería de esta forma tengo esto tengo esto y entonces agrego esto perdón, voy a llevarme más bien el de aquí agrego lo contrario de lo que yo quiero demostrar y agrego esto como una premisa ok, entonces ¿qué va a pasar? lo que va a pasar es esto esto, voy a hacerlo de esta forma un poco más compacta, digamos resuelve en o sea, esto aquí y esto acá va a resolver aquí en cubo, ¿verdad?

## [01:20:18]

pero vean tengo esto y tengo esto entonces, si yo tengo, acabo de agregar esto a mi conocimiento y ahora le estoy agregando esto o sea, lo estoy resolviendo con esto, entonces esto ¿a dónde me llega? esto vacío o sea, llegué a una contradicción por lo tanto al haber agregado esto y llegar a una contradicción entonces eso demuestra por contradicción que lo contrario de esto es lo correcto ok, entonces así podría demostrar modus ponens con refutación ok, ahora sí vamos a ver si podemos hacer lo mismo con este con conjunción conjunción dice así yo tengo P perdón, voy a hacerlo voy a probármelo de aquí conjunción dice, si tengo P y tengo Q puedo concluir P y Q ok, ahora vamos a ver si podemos demostrar esto con este con resolución, con refutación en resolución, con refutación yo tengo lo siguiente tengo P, tengo Q y ¿qué más tengo? ¿cómo se ve la negación de P y Q? no P o no Q correcto

## [01:24:03]

por mero no P o no Q y es muy obvio que esto da una contradicción mediante resolución es obvio porque al resolver perdón sería así es obvio porque este este resuelve con este y me deja no Q y entonces esto resolviendo con no Q me da vacío entonces conjunción si se puede demostrar con refutación este entonces este resulta que el cálculo el cálculo de la regla de resolución con refutación si es completo no sé si tienen alguna pregunta o sea eso responde a tu pregunta Andrés resolución es equivalente al cálculo de predicados si, si incluimos refutación y cuando uno incluye digamos refutación es que funciona como técnica adicional o es su fuerza que absolutamente todo lo que se tenga que demostrar siempre sea por contradicción exactamente que todo tiene que ser por contradicción bueno, en realidad también teníamos que demostrar una cosa adicional y es que la regla de resolución

## [01:26:35]

es una regla de inferencia sound o sea que es tautológica pero bueno, obviemos eso, pero sí, les garantizo que sí es una regla tautológica no es difícil demostrarlo pero ya no tenemos tanto tiempo permítanme a ver si lo tengo por aquí sí en el mismo documento donde les ponía el proceso de conversión a cláusulas ya se los muestro ok, permítanme un momentito es que el zoom es medio mañoso aquí está

## [01:28:04]

No, no es ese. Ah, sí, sí es este.

## [01:28:09]

Ok, en este mismo documento habíamos llegado que desde nuestra sentencia inicial de que si todos los caballos son animales, entonces la cabeza de un caballo es la cabeza de un animal, que sí es demostrable usando cálculo de predicados, por supuesto. entonces por eso es que dado esto introdujimos esto para hacer una demostración por contradicción en lo que yo estaba pensando cuando redacté esto es precisamente en la resolución con refutación entonces agregamos esto que ven en la negación de mi conclusión y quiero llegar a un conjunto de cláusulas a este conjunto de cláusulas final.

## [01:29:19]

Tomen en cuenta que aquí ya está incluida la negación de la conclusión, ¿verdad?

## [01:29:32]

Entonces, ¿qué pasa si aplicamos resolución a esto?

## [01:29:42]

En notación de Robinson,

## [01:29:45]

eso se escribiría de esta forma.

## [01:29:50]

Y la numeré. ok si estas no son nuestras premisas veamos lo que podemos hacer aquí hay una cosa que no les he mencionado que también hay que tomar en cuenta que se llama unificación la unificación consiste en lo siguiente si yo tengo una variable en una en una cláusula yo puedo generar otra cláusula Ya sea reemplazando esa, o sea, toda aparición de esa variable en la misma cláusula con otra variable. Todas, ¿verdad? Todas las apariciones. O puedo reemplazar toda aparición de esa variable con una constante a lo largo de toda la cláusula. Entonces, vean que en 1 yo voy a hacer eso, voy a unificar X con Z, bueno perdón, dice, perdón, X con F de A, disculpen, X con F de A dice en 1. Y sí, entonces eso me produce no C de F de A o A de F de A. Y entonces puedo resolver eso con 2 y obtengo A de F de A.

## [01:31:50]

Si yo unifico Z con F de A en 4, entonces eso me da no A de F de A y no K de A F de A en 4. fabrico una sentencia más una cláusula más y entonces si yo resuelvo esto con esto entonces produzco fabrico esto y finalmente yo resuelvo esto con tres y obtengo vacío entonces de esta forma con regla de resolución si es posible demostrar que si un caballo es un animal entonces la cabeza de un caballo es la cabeza de un animal con unificación y refutación ok todo esto para ver si podemos llegar a el primero de nuestros lenguajes lógicos que se llama Prologue Prologue es un lenguaje lógico que utiliza podemos decirlo desde el punto de vista técnico está utilizando cláusulas utilizando resolución con refutación y unificación y trabajando en una manera de backward chaining eso es Prolog ok, entonces bueno, ya solo me queda un minuto vamos a ver el lenguaje prolog ok, vamos a bueno, perdón

## [01:33:50]

hoy es jueves entonces voy a dejarles unos cuantos ejercicios más de de esto de simbolización de este de paso a cláusulas de resolución para toda la semana entrante entonces la siguiente semana que es presencial, dicho sea de paso vamos a terminar ya con meter prolog y quiero entonces también ver el otro lenguaje lógico que quería mostrarles que es este clips ok, entonces este ya se me venció el tiempo vamos a quedar aquí por hoy y esa es nuestra agenda para la semana entrante y recuerden vamos a pasarnos entonces a modo asincrónico para este tratar de de quedarle bien a Dios y al diablo de acatar la resolución de la vicerrectoría de docencia por supuesto y de cooperar con la organización de la de la federación de estudiantes de la FEITEC ok, entonces voy a tener
