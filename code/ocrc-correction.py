import openai
from openai import chat

openai.api_key = ""

def split_into_chunks(text, max_tokens=1500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_length += len(word) + 1
        if current_length > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word) + 1
        else:
            current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def correct_text_with_gpt(text, ln):
    system_prompt = "You are a helpful assistant that corrects OCR text for spelling, grammar, and minor parsing errors."
    user_prompt = f"Please correct any OCR errors (in {ln}) in the following text:\n\n{text}"

    response = chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.0,
    )

    corrected_text = response.choices[0].message.content
    return corrected_text

def correct_large_text(text, ln):
    chunks = split_into_chunks(text, max_tokens=1500)
    corrected_chunks = []
    for chunk in chunks:
        corrected_text = correct_text_with_gpt(chunk, ln)
        corrected_chunks.append(corrected_text)
    return "\n".join(corrected_chunks)

if __name__ == "__main__":
    raw_ocr_text = """
    ASTRAZIONI : Rlfl:ESSIONI SULLA COMPOSIZIONE MEDIANTE. ELABORATOIIE 
HUBERT S .  HOWE, Jr. 
L ' affermazione che un elaboratore elettronico possa 
comporre musica viene quasi sempre accolta con notevo­
le scetticismo. Com' è  possibile che una macchina compia 
un'impresa del genere? Tale scetticismo trova fin troᲞ 
po spesso pronta conferma se per caso si ascoltano i 
lavori sinora prodotti. Spesso, tuttavia, questo pro­
blema è trattato soltanto superficialmente, trascuran­
done così alcuni importanti aspetti, dei quali vorrei 
occuparmi in questo articolo. 
Per chiarire il significato dell'espressione "comporre 
mediante elaboratore" dobbiamo anzitutto ammettere 
che chiedersi se l'elaboratore sia in grado di compor­
re musica equivale pressapoco a chiedersi se esso sia 
in grado di pensare. Ma la difficoltà non consiste 
tanto nella nostra capacità di capire cosa sia in 
grado di fare un elaboratore, quanto nella nostra 
conoscenza del processo del pensiero nell'uomo. Cosa 
significa pensare? Se lo sapessimo, potremmo facilmen-
te stabilire se gli elaboratori siano in grado di farlo. 
Cosa significa comporre musica, o meglio, in qual modo 
(e perchè ) si svolge tale attività? 
La composizione musicale comporta una notevole serie 
di operazioni che vengcno effettuate per raggiungere 
uno specifico risultato. Pe r s ap ere perchè ci si 
impegni in questa attività, è necessario analizzare 
e conoscere l'effetto prodotto dalla musica e i valori 
assunti dai compositori. E 1 chiaro, anzitutto, che 
questa è . appunto una delle diffi coltà implicite nel 
problema, poichè la stessa musica non produce il me­
desimo effetto su due persone diverse. 
Questa varietà di reazioni è causata da due motivi 
principali: in primo luogo, la percezione di un 
ascoltatore dipende inevitabilmente dal suo gusto 
personale e dalla sua capacità di giudizio. Molte 
discussioni sulla musica sono provocate soprattutto 
da questi fattori, piuttosto che da altri. 
Non esiste quindi nessun metodo definitivo, sc'ienti­
fico, intersoggettivo per analizzare il processo com­
positivo: dobbiamo semplicemente avanzare alcune 
ipotesi e portarle avanti. Propongo di esaminare la 
composizione musicale basandoci essenzialmente su due 
punti di vista: il primo fa riferimento ai cosiddetti 
elementi "stilistici" della musica, mentre il secondo 
riguarda l'espressione di "sensazioni" e altre idee 
più astratte. (Non intendo con ciò affermare che "al-
tre i dee più astratte" siano equivalenti alle sensazio­
ni, ma soltanto che si differenziano dagli "elementi 
stilistici") . .  
ELEMENTI STILISTICI 
Lo sviluppo di uno stile musicale personale e tuttavia 
"pertinente" è uno degli obiettivi più importanti che 
un compositore tenta in vari modì di raggiungere nel 
Ჟorso della sua vita creativa. 
Generalmente i composi tori, a questo proposito, hanno 
un'idea ben precisa del risultato a cui tendono, 
almeno riguardo al pezzo che stanno realizzando. Per 
raggiungere il proprio fine, essi dedicano gran parte 
del loro tempo allo studio ed al perfezionamento delle 
proprie tecniche compositive. 
Se un compositore vuole programmare un elaboratore per 
scrivere musica secondo il proprio stile, tutto ciò 
che deve fare è scrivere un programma che ne realizzi 
gli aspetti tecnici. Saltano poc.hi compositori haᲠno 
finora tentato di fare ciò; la causa risale soprattutto 
alla difficoltà di formaliz zare questi aspetti tecnici 
- in qualunque forma, verbale o meno (non deve neces­
sariamente essere un programma per elaboratore) -
piuttosto che alla scarsa disponibilità di elaboratori 
adatti o alla limitata esperienza del compositore nella 
programmazione. Molti compositori non provano nemmeno 
ad affrontare questo problema, specialmente coloro 
che compongono secondo metodi che essi stessi defini­
rebbero "intuitivi". Anche se un compositore volesse 
farlo, rimarrebbe sempre il grosso problema della so­
fisticazione verbale e della ricerca di un metodo che 
permetta di verificare se i princ1 p1 sviluppati riflet­
tano fedelmente lo stile voluto. 
Inoltre, ci troviamo di fronte ad un altro problema: 
la consapevolezza del compositore nei confronti degli 
elementi stilistici della propria musica, e ·la sua 
intenzione di confrontarli in modo diretto, com'è 
necessario nella stesura di un programma per elaborato­
re. Quali potrebbero essere le conclusioni del compo­
sitore se i risultati del suo lavoro apparissero im­
barazzanti ad un esame distaccato ed obiettivo? I l  timore 
di dover affrontare questa eventualità ha inibito molti 
compositori dal proseguire in un'attività mustcale di 
questo tipo. 
Forse, comunque, il problema non è così grave come po-
trebbe apparire. Se volessimo veramente affrontare 
la musica al livel lo di esperienza auditiva ,  avremmo 
probabilmente molto da imparare sugli aspetti tecnici 
e stilistici se ad occuparsene fosse un el aboratore. 
Questo tipo di approccio presenta però alcune diffi­
coltà . Anzitutto , comprendere le qualità di uno stile 
musicale è già un processo di scoperta, di formulaziᰩ 
ne creativa di idee applicabili al la musica, di ries! 
me de) l a  musica stessa alla luce di queste nuove i dee 
e così via. 
In secondo luogo, nel l a  storia dell a  musica, nel 
sedicesimo secolo così come ai nostri giorni, è sempre 
esistito un insieme di scritti teorici che si riferi­
scono al la musica solo marginalmente. Eppure musico!ᰩ 
gi e ascoltatori insistono spesso sull 'analisi music! 
le basata su tali presupposti, anche quando quest'ul­
timi non trovano conferma nel l'esperienza immediata. 
Prima di inoltrarmi in analisi più specifiche, vorrei 
chiarire che mi servo qui del terminᲡ "stile" per 
descrivere tutti quegli aspetti tecnici che conside­
riamo nel comporrè una musica corrispondente alle 
no!tra aspettative. Forse "stile" è un terᲢine poco 
Უ,propriato in questo caso, po ichè può avere molti 
altri signi-ficati, come ad es!mpi_o "individualità" 
o "verve" . Probabilmente il termine stesso "musica" 
sarebbe il migliore; tuttavia "stile" è spesso usato 
in questo senso. 
ALCUN! LAVORI NELLA STORIA DELLA COMPOSIZIONE 
MEDIANTE ELABORATORE 
La storia della composizione musicale ᰂediante 
el aboratore ebbe un cl amoroso inizio alla fine degli 
ann i 50 con l ' attività dei professori Lej aren A.Hil ler 
Jr. e Leonard M. l saacson, che - l avoravano allora al­
l 1 University of Ill ino is. Il l oro libro 
· Experimental 
Music 
(I) , al quale si sono in seguito ispirate mo lte 
altre opere, offre una brill ante descrizione del loro 
l avoro. Non intendo esaminare dettagliatamente que -
• st' opera; ne darò piuttosto una breve descrizione, 
per poterne considerare i risultati e le problematiᲤhe. 
La "musica sperimenta}Ქ" descritta da Hi l ler e l saacson 
iniziava con un'analisi del le regole del contrappunto , 
sviluppate nel XVII secolo da J.J. Fux e ancora studi a­
te in molti corsi di armonia e contrappunto. Un 
insieme di regole sti l istiche già formulate si presta­
va bene ad essere veri ficato mediante un programma per 
elaboratore, e gl i autori si dedicarono così al probl! 
ma del la traduzione di quel le regole in linguaggio 
di programmazione. Una volta iniz iato questo esperi­
mento , gl i autori com inciarono anche ad esaminare ogn i 
sorta di idee, senza al cun rapporto l'una con l ' altra, 
75 
e che avevano scarsa attinenza con gli obiettivi origi­
nari. Scoprirono inoltre (probabi lmente non con loro 
grande sorpresa ) che gran parte del loro lavoro doveva 
essere dedicata alla spiegazi one di numerosi elementi 
dati abitualmente per scontati. L ' uso del l ' elaboratore 
esigeva infatti di riformularli in modo preciso . Questo 
tipo di l avoro li impegno notevo lmente, lasciando loro 
molto meno tempo per affrontare invece questioni fonda­
mentali in campo musicale. 
Experimental music è effettivamente un guazzabugᲦio di 
idee, e non c'è da meravigliarsi se il quadro che ne 
risulta non è affatto chiaro. I due sperimentatori uti­
lizzarono la teoria dell'informaz ione, le catene markoviane, 
teorie musical1 di ogni tipo, da Faux a Schenker, 
Schillinger, Hindemith, Cage, sino al la musica dodecafoni­
ca, ed altre ancora, di moda a quel l'epoca. Uno dei pro­
cedimenti più usati nei loro esperimenti era il metodo 
Monte Carlo, una procedura per la generazione aleatoria 
di elemen,i che venivano esaminati in base alle regole. 
Questo si rivela uno dei limiti più vistosi del loro 
lavoro, e, in una certa misura, spiega anche perchè la 
computer music sia considerata da mol ti incoerente, mec­
canicistica, o "casuale". Da questo metodo derivava una 
totale mancanza di struttura nei risultaᲧi degli esperi­
menti . Indipendentemente dal la volontà di Hil ler e 
lsaacson, la generazione aleatoria è stata ampiamente 
utilizzata nella composizione di computer music nei 
vent'anni successivi alla loro attività. 
Da un punto di vista attuale, i risultati dei l oro espe­
rimenti possono apparire primitivi, e, a volte, persino 
ingenui; ma, in realtà, il l oro lavoro è stato mol to 
significativo. Le rego le del contrappunto , cosl come le 
aveva sviluppate J.J. Fux, erano in effetti inadeguate 
sotto mol ti punti di vista , 1a gli autori riuscirono ad 
eliminare tutti gli errori dei loro programmi e a stampa­
re la partitura della musica prodotta. 
Dopo un inizio così promettente, purtroppo questo primo 
lavoro non .fu portato avanti . Ovviamente mo lti aspetti 
del l a  musica prodotta non Შorrispondevano al tipo di 
approccio richiesto dal determinato stile musicale. (Tra 
l'altro, l'armonia non aveva senso). I l  l ato più nega­
tivo fu comunque lo sfruttamento del l avoro a fin-i 
"commerciali". Gli esperimenti vennero pubblicati con 
i l  titolo I l l i ac Suite for String Ouartet ( dal nome del ­
l ' el aboratore) e eseguiti in concerti. In tal modo, 
risultati di una serie di semp lic i  esperimenti, che 
comprendevano una varietà di sti li dal XVI al XX secolo, 
venivano spacciati per un nuovo tipo di musica. Indub­
biamente, questa I stata una del l Ჩ cause principali dello 
scetticismo che ha acco lto le successi ve composizioni dì 
computer music. 
Un precedente storico più importante per la mia atti­
vità è rappresentato da una serie di programmi scritti 
dal Prof. J . K. Randall, della Princeton University , 
nel 1965. Non esiste una documentazione di questo la­
voro, ma credo che tutto il suo Prelude to Mudgett 
( che può essere ascoltato su registrazione Nonesuch 
71245 ) sia stato programmato in modo Ცa avere note, 
ritmi ed altri elementi musicali determinati dall 1 ela­
boratore. Tra la sua attività e la mia esiste un rap­
porto ancora più diretto,poichè ho utilizzato alcuni 
dei suoi stessi procedimenti compositivi, pur non 
avendo mai collaborato direttamente. 
IL MIO PROGRAMMA COMPOSITIVO 
Per comprendere gli obiettivi stilistici del mio 
programma compositivo, è necessario anzitutto conosce­
re alcuni aspetti generali della mia musica, che il 
programma cerca di controllare. 
La musica che Ძo composto mediante il mio programma 
compositivo si basa su strutture denominate "vettori 
multidimensional " Un vettore è un'unità che determina 
simultaneamente, in più dimensioni, caratteristiçhe 
musicali specifiche di altezze (o meglio, di classi 
di altezze). Fondamentalmente, un vettore determina 
rapporti tra gruppi di !Ltezze che hanno alcune propri! 
tà in comune. 
Poichè la musica stessa ha una struttura multidimensio­
nale, i vettori sui quali essa si basa devono quindi 
presentare più di una dimensione. Nei vettori sono 
specificate solo relazioni astratte, affinchè la loro 
applicazione a passaggi musicali sia completamente 
aperta. I vettori utilizzati nel mio lavoro sono 
costruiti in modo tale da presentare molte caratteri­
stiche che mi sono sembrate interessanti; tali caratt! 
ristiche sono integrate nella musica ad un livello di 
base, cosicchè la musica stessa, all'ascolto, riflette 
in ogni aspetto la struttura dei vettori. Da questo 
procedimento si ottiene così una musica altamente in­
tegrata, permettendo di progettare simultaneamente in 
più modi rapporti sia semplici che complessi. ·(2) . 
Il mio programma compositivo è essenzialmente un 
"linguaggio" con il quale molti di questi rapporti 
possono essere espressi in modo più diretto dalla 
notazione tradizionale; di conseguenza, esso rappre­
senta un tipo di notazione musicale strutturale. L'in­
put del programma consiste in una serie di istruzioni 
che specificano una o due operazioni, e in una 
stringa di dati che indica le classi di altezze asso­
ciate all'operazione. Un intero passaggio musicale è 
determinato da una serie di istruzioni. Sebbene queste 
ultime non controllino tutte le caratteristiche della 
76 
musica, nel contesto in cui il programma è utilizzato 
- in quanto sottoprogramma che produce input per un 
programma di sintesi musicale - risultano necessaria­
mente Წ gli aspetti della musica prodotta. Cinque 
operazioni determinano rispettivamente le configurazio­
ni ritmiche di base, la determinazione dei registri mu­
sicali, la selezione di secondo grado delle altezze, 
la selezione delle altezze e la rotazione di ognuno dei 
vettori sui quali si basano queste altre proprietà. 
Queste operazioni devono essere specificate nell'ordine 
suddetto. Le descriverò ora dettagliatamente. 
1 )  L'operazione ritmica ( indicata con ARR, da 
"arrangement" ) è forse la più complessa del programma. 
Essa stabilisce una relazione tra altezze e istanti di 
attacco, in modo tale che ogni elemento del vettore sia 
associato ad uno specifico istante di tempo 
La struttu­
ra del vettore è direttamente espressa nel ritmo, e le 
diverse dimensioni del vettore vengono sottoposte ad 
una rotazione in ogni registro, cosicchè ogni classe 
di altezze è disponibile in ogni registro, ma con un 
ordine diverso. Questo processo offre numerose possibi­
lità di scelta, permettendo così di ottenere svariati 
modelli ritmici che possono tutti essere ricavati dallo 
stesso v.ettore. 
Mediante questa procedura si ott!ene una grande varietà 
di ritmi nella musica, che vanno dal semplice al comples­
so, e riflettono in modi diversi la struttura delle al­
tezze. L'originalità di questo processo consiste nel 
fatto che non viene prodotta una struttura ritiica di 
tipo tradizionale, basata su motivi o frasi o distin­
zioni tradizionali in varie parti per progettare il 
contenuto musicale; ma non sono questi, comunque, gli 
obiettivi della musica. 
2) L1 operazione di registro ( denominata REG) è la più 
semplice. Si selezionano semplicemente classi di altezze 
da ogni registro della configurazione ritmica; in tal 
modo, successivamente, verranno scelte soltano le altez­
ze specificate. L'operazione di registro assicura che 
differenti dimensioni del vettore siano completate in 
registri diversi, permettendo un 1 associaziona tra gruppi 
di alteᲭze .ulla base dell 1 identità di ottava. 
3) Per comprendere l'operazione di selezione di secondo 
grado delle alteze ( denominata SC2) , dobbiamo anzitut­
to comprendere 1 1 operazione stessa di selezione delle 
altezze (di primo grado); quest'ultima però non viene 
specificata se non dopo la selezione di secondo grado. 
Fondamentalmente l'operazione di selezione delle altez­
ze definisce la successione delle altezze stesse; l'uni­
ca complicazione è rappresentata dalle numerose possi­
bilità di scelta. La selezione di secondo grado delle 
altezze permette ad un altro vettore di operare a livel 
lo più profondo, mentre la selezione di primo grado 
determina il livello di superficie. 
Ogni unità di misura( "battuta") di quest'ultimo, deter­
minata dalla selezione di primo grado delle altezze, 
viene distribuita in alcune "battute" in ognuna delle 
quali appaiono soltanto le altezze in comune tra le 
due dimensioni del vettore. Usando entrambi i tipi di 
selezione delle altezze si ottengono frasi musicali 
molto lunghe, determinate da poche istruzioni nel pro­
gramma, mentre esistono varie possibilità di manifestᲮ 
rᲯ tutte le identità tra le diverse componenti dei ve! 
tori. 
ᰡ) L'operazione di selezione delle altezze ( denominata 
SCR, da "screen") determina le altezze che appaiono 
nella musica. Le scelte possibili sono così numerose 
che per specificarle tutte, l'istruzione per la sele­
zione delle altezze deve essere seguita da un'istru­
zione a parte. Ogni unità, presentata singolarmente, 
viene considerata una "battuta", e tutti i tempi di 
inizio sono incrementati da una durata di base per 
ogni battuta successiva. ( In un'unica istruᲰione si 
possono determinare più 
battute) .  Tra le possibilità 
di scelta sono compresi: il tempo di inizio dell'inte­
ra frase (tutti i tempi sono indicati in battiti rela­
tivi ad un'indicazione di metronomo specificate altro­
ve) ; l'incremento di battuta; l'altezza da cui inizia­
no 
registri fondamentali ( in modo tale che 1 Ჱ altez­
ze associate si trovino tutte un'ottava sopra l'altez­
za specificata in ogni registro) ; l'indicazione per 
la distribuzione di diversi registri in differenti in­
tervalli temporali; un codice che determini la durata 
di ogni nota come una funzione del peso della c lasse 
di altezze nell'intera frase musicale. ( Questo codice 
di specificazione della durata è, naturalmente, una 
semplice informazione che indica una proprietà della 
nota così selezionata, e non richiede necessariamente 
che l ' altezza sia effettivamente presente nella musica 
con quel valore) . Esiste anche una possibilità di scel­
ta per il "posizionamento", che consiste seᲲplicemnte 
in un numero trasferito ad un campo dell'immagine-nota, 
pe,r permettere di identificare, nella partitura stam­
pata in seguito, la nota determinata dall ' istruzione 
data. E' importante notare che per tutte queste opzio­
ni devono essere specificati valori effettivi; in tal 
modo nessun elemento viene gestito "automaticamente", 
.e ogni variabile può assumere un unico valore. 
Una volta ottenute queste informazioni, il programma 
calcoÌa tutte le note che formano la frase musicale 
così determinata, e procede all'istruzione successiva 
seguendo il flusso di ingresso. Le note sono s tampate 
e trasmesse ad un programma di sintesi (facoltativo ) 
77 
per la generazione della musica. Quando le note sono 
state calcolate, anche tutte le caratteristiche della 
frase musicale che possano essere pertinenti alla 
struttura della musica vengono stampate e messe a do­
sposizione per la successiva eventuale elaborazione, 
Queste proprietà, naturalmente, comprendono soltanto 
quelle deducibili dalla struttura dei vettori che han 
no determinato la frase musicale; altre caratteristi­
che devono essere ricavate individualmente. 
I l  programma infine stampa duᲳ partiture: la prima in­
dica ogni nota nell'ordine in cui 1· stata calcolata, 
unitamente alle istruzioni per il programma compositivo; 
la seconda indica la frase musicale finale, immediata­
mente precedente alla fase della sintesi, quando tutti 
i tempi sono stati trasformati da battiti a secondi, 
le note sono state ordinate cronologicamente, ed ogni 
altra modificaizone è stata effettuata. 
5 )  La quinta operazione, denominata ROT ( rotazfone) 
pemette di ruotare in ogni dimensione i vettori, asso­
ciati ad una qualsiasi delle proprietà suddette, con 
la successiva ri-generazione delle proprietà relative 
Ჴl nuovo vettore. La rotazione I effettivamente .una 
operazione molto significativa per i vettori multidi­
mensionali, e dallo stesso vettore, ruotato in dimensio­
ni diverse, possono risultare molte configurazioni dif­
ferenti. Le rotazioni possono essere gestite facilmente 
perchè producono una nuova classe di altezze nel vettore 
soltanto dopo l' ordinamento degli elementi. 
iuttavia ogni cambiamento prodotto dalle rotazioni po­
trebbe essere invece trascritto come una nuova istruzio­
ne di ingresso al programma; ho incluso questa operazio­
ne soltanto per risparmiare tempo nella determinazione 
dei programmi che utilizzavano rotazioni, ed inoltre 
perchè l'operazione indica il concetto che controlla il 
brano. Ogni altro tipo dì cambiamento negli elementi 
che determinano la musica deve essere trascritto sotto 
forma di nuove istruzioni per il programma. Per spe­
cificare interamente il brano musicale sono in genere 
necessarie molte istruzioni, sebbene il l?rO numero sia 
di gran lunga inferiore a quello delle note da esse 
determinate: 
In tal modo, un'intera frase musica.le, strutturata in 
molti dettagli, risulta dalla serie di istruzioni di 
ingresso al sottoprogramma compositivo. Poiche il 
programma stesso è richiamato da un sottoprogramma di 
una procedura di sintesi, il sottoprogramma abitualmente 
continua ad aggiungere proprietà alle note via via de­
terminate, finchè l' intera frase è strutturata in ogni 
dettaglio (così come è necessario per la sintesi) . Co­
munque,poichè non esistono regole generali per queste 
altre caratterisciche (quali dinamica o timbro) 
queste ultime devono essere trattate individualmente 
Un'importante aspetto del programma consiste nella 
possibilità di rendere opzionabile quasi ogni detta­
glio della musica, che può risultare diverso da 
un ' occasione all'al tra, cosicchè il progrmma può 
essere usato in vari modi. Ciò nonostante, lavorando 
con il mi o programma, continuo a scoprirne sempre 
nuovi aspetti, che potrebbero diventare nuove opz ioni 
utilizzabili, anche se non al momento stesso in cui 
le scopro .  Inoltre, il programma stesso è organizzato 
come un insieme di sottoprogrammi distinti , ognuno 
dei quali tratta una singola istruzione di ingresso 
o un aspetto dell'istruzione stessa, cosicchè un sot­
toprogramma può essere sostituito da un altro se vogli o  
cambiarne qualche caratteristica funzionale. A questo 
stadio della mia ricerca, ho notato che il programma 
tratta quasi ogni elemento di cui potrᲵ servirᲶi al 
momento attuale, tranne pochᲷ eccezioni che possono 
essere trattate individualmente, o per mezzo di pro­
cedimenti quali un'intera nuova serie di istruzioni 
di ingresso. Lo stadio successivo nello sviluppo del 
programma consisterebbe nella scri ttura di una proce­
dura di generaz ione di istruz i oni per questo programma 
veramente da una prospettiva di base, dove l'intera 
scrittura del pez zo potesse essere espressa in poᲸhe 
istruz ioni di questo tipo. Questa possibilità è molto 
suggesti va ma non realmente pratica, poichè è precisa­
mente quella struttura di base che si evolv·e mentre 
si procede da un pezzo musicale all'altro. 
ESEMPI COMPOSI TIVI TRATT I  OA ttᲹSTRAZIONitt 
Gli esempi seguenti sono tratti dalla mia composiz ione 
ttAstraz i oni" commissionata dal Laboratorio permanente 
per l'informati ca Musicale della Biennale ( LIMB) di 
Venezi a, composta e realizzata nel 1980 al CSC dell1 
Universi tà di ,Padova. L ' esempio 1 i ndica una seri e  d i 
quattro istruzioni del programma, e l'esempio 3 ( pag. 
8 della partitura) indica il brano di quattro battute 
determinato da queste istruzioni, la sezione IV ( C) 
della composiz i one. Questo brano rappresenta un 
passaggio da una sezione all'al tra nel pezzo: ha luogo 
una conti nua decelerazi one da un metronomo di 80 a 60. 
In termini strutturali, è anche ua passaggio da un in­
sieme di vettori all'altro. 
L' esempio 2 indica i tre vettori rappresentati in que­
sto brano, 
che determinano l ' arrangiamento ritmico, 
la selezi one dei registri e quella delle altezze. 
La dimensione di tutti questi vettori è di 4 x 4 ele­
menti ,  in cui ognuno degli accordi e delle voci è un 
tetracordo che contiene tutti gli intervalli, e ogni 
insieme di accordi e voce esaurisce strutturalmente 
i possibili tetracordi. (Esistono soltanto quattro 
78 
teatracordi di questo tipo, collegati alle operazioni 
di moltiplicazione Ml, MS, M7 e M l l .  Ogni classe di al­
tezza ricorre esattamente due volte in ognuno di questi 
vettori, e il contenuto di altezze del vettore presen­
te gli otto intervalli tranne le altezze 2 ,  5 ,  8 ,  e 11 
( ll ,  F ,  A bemo lle e B ) .  
A R Il U P_ 
REG 
SCR 
o o 
Esempi o  
( SC R )  
.4 
6 
4 
7 
o 
o 
9 
· o  
4 
g 
4 3 1 0  
4 7 1 0 
6 
4 
4 
4 
7 9 1 O 
O 
4 
3' 3 1 0  
1 1 1 O 
7 
3 
6 9 1 0  
4 
o 
o 
6 
6 
9 
6 
9 
4 
7 
3 
o 
4 
7 
1 5 6 .  O 3 o 
1 6 
1 : Una s u ccess i o ne d i  q u at t r o  i s t r u -
z i  o n i  d i  i n gresso per i l p r o gr amm a 
c o mpo s i t i vo .  Nel p r o g r amma d i  s i n -
t e s i  u sat o ,  q u e s t e  i st r u z i o n i  s o n  o 
s t a t e  u t i li z z a t e  per 1 a gener az i o -
ne de 1 1  e no t e  del b r ano i n d i c at o 
nell'esempi o 3 .  
o 
7 
3 
c 
G 
Eb 
Cl! 
4 
6 
7 
o 
E 
F #  G 
c 
6 
9 
1 O 
4 
F# 
A 
Bb 
E 
9 
3 
1 O 
A 
Eb C Il 
Bb 
( RE G) 1 O 
4 
o 
1 
Bb 
E c 
Ct 
1 
g 
4 
7 
C# 
A 
E 
G 
9 
6 
7 
3 
A 
F 1t-
G 
Eb 
3 
1 O 
6 
o 
Eb 
Bb F #  
c 
( SCR ) 
3 
1 O 
6 
4 
Eb 
Bb F i! 
E 
7 
9 
1 O 
3 
G 
A 
B b  
Eb 
9 
o 
1 
7 
A 
e c lj  
G 
o 
4 
6 
e 
E 
F t 
C# 
Esempi o 2: Vet t o r i  r app r e sent at i n elle i s t r u ­
z i o n i  dell ' esemp i o  1 .  A s i n i s t r a  
v i ene d a t a  l a  r appr esen t a z i o ne nu ­
mer i ca della c lasse d i  a l t e z z e ,  
men t r e  a dest r a  l a  st essa è i n d i c a 
t a  medi ante no t a z i o ne m u s i cale. 
Ese11p i 0  
3 : 
,, 
I• 
i 
, 
(a,u•) i 
-e,-, 
-J_ 
11 
- ,. . -
f 
I 
L 
-, 
Ë 
i (', 
'< i 
I rp q 
I 
. e,,, 
... 
I Ì 
< 
Il. 
• . 
_,, I 
w 
t 
'7 ,  .. 
11 ... - 
-
.,.. ... 
·.:;. Ç 
l -. -
, l'.   I 
l'-- ! , " !
)... 
e 
-
' 
' 
. 
-. 
. 
.,. 
r • 
I ( 
J r i--, . 
• . .  
... 
É 
. Ê 
,:Ǐ 
--, 
I 
I 
I 
I 
¼ ,; 
z t t. ! f 7. 
Í "' 
I¼ 
I  
. 
', ... Î -
. - . 
' 
' 
; I I 
., 
,. 
' 
' -
" 
, 
f 
✓ -
, 
' 
r 
f 
k 
Ï 
79 
-
... 
.., 
-,, 
.. 
, 
e_ 
-
I 
! (it-J ìe?o) 
I 
 l 
. I 
. 
I '  
' . 
'
' 
Il 
. I 
.. 
... ' 
" , 
, 
, 
., ... 
. 
M 
• 
,. 
,. 
I 
-... 
' 
I. 
y 6:.--1 
fl• 
I 
"z_ È 
j ǐ ~-r- "1_ 
Ǒǒ 
Ǔ i 
. 
y 
' 
y 
, 
... 
ES P R ES S I O N E  D I  S E N S A Z I O N I  O D I  IDEE A S T R A TTE 
Devo c h i ar i re che con i term i n i  "sensaz i on i "  
e II i d  e e astratte" intendo concetti alquanto diversi . 
Le sensazioni sono emozioni provocate in una persona 
dall'ascolto della musica. La tristezza, 
ad esempi o, 
è uno stato d'animo che molti possono provare ascol -
tando brani musicali. 
Le i dee astratte sono impressiᯖ 
ni, anche abbastanza concrete, che si possono avere 
sulla musica, ma che è diffici le collegare effettiva­
mente ad altezze e ritmi. Ad esempio, un brano musi­
cale può descrivere un viaggio nello spazio, oppure 
può basarsi su un programma verbale o visivo. Mentre 
sensazi oni e idee astratte hanno una natura ben diver­
sa, ci si può tuttavia accostare ad esse in modo 
abbastanza simi le. Queste idee sono estremamente im­
portanti per la maggior parte dei compositori; molto 
spesso, 
infatti, i loro sforzi sono diretti più 
verso questi aspetti della musica che verso quelli 
stilistici . Questi elementi, comunque, non contrastano 
tra loro, ed è importante notare che lo sti le del 
compositore è un veicolo per l'espressione di sensa­
zioni e idee astratte. 
Il problema dell' identificazi one di queste qualità è 
simi le a quello che ci eravamo già posti, se 1 1 elabo -
ratore cioè sia o meno in grado di pensare o di com­
porre musica. Se avessimo una idea precisa di cosa ef­
fettivamente sian-;;- q-uéste quàlità, potremmo dire se un.a 
musica le esprima o meno. Ad esempio, come possiamo 
decidere se un brano musicale esprime incitamento, o 
passione, o se descrive "quel misto di pomposo e di 
banale che è la quintessenza dell ' America?" Finchè 
intendiamo queste idee solamente in senso generale, 
i l  problema non è molto grave; ma purtroppo molti 
i ntraprendono spesso lunghe e accese discussioni su 
questi problemi, mentre invece dovrebbe essere chiari­
to che l'argomento di tali discussioni è la definizio­
ne stessa delle qualità suddette, pi uttosto che la 
capacità della musica di esprimerle. 
Poichè questi termini descrivono soltanto caratteri­
stiche generali della musica, e poichè le qualità soro 
espresse nello stile o nel linguaggio proprio del 
compositore, non è possibi le formulare regole partico­
lareggiate per istruire un elaboratore a comporre una 
musica che le espri ma. L'elaboratore, piuttosto, dovreᲺ 
be essere istruito a comporre musica in un determinato 
sti le; le sensazioni dovrebbero essere un sottoprodotto 
dello stile stesso. In ogni caso, si duplicherebbe co­
sì il processo umano. 
SCELTE COMPOSITIVE 
Contrariamente a quanto molti potrebbero immaginare, 
80 
i l  mio programma compositivo non effettua alcuna 
scelta compositiva autonoma; esegue soltanto istru-
zioni, formulate da me stesso. I l  problema consiste 
nella possibi lità o meno di scrivere un progr᲻mma i n  
modo tale che esso possa effettuare scelte e ttdeciderett 
cosa comporre, determinando anche i dettagli speci fi ci 
di ritmo, registro e selezione delle altezze. Dietro 
questo problema ce n1 è un'altra: se il compositore, ci oè, 
senta la necessità dell' aiuto di un elaboratore per 
questo aspetto del suo processo compositivo, o se invece 
sia soddisfatto di trattarlo personalmente. Quali cri­
teri usa il compositore per decidere elementi quali 
ad esempio, rapporti su vasta scala, forma, contrasto, 
o altri ancora? Tra quali alternative i l  compositore 
pensa di poter scegliere? Queste questioni possono 
certamente essere strutturate in maniera tale che l'ela­
boratore possa capire come effettuare le selezi oni ap­
propriate. 
Nel considerare l' utilizzazione dell'elaboratore per 
effettuare scelte compositive, bisogn᲼ in primo luogo 
tener conto della scarsa conoscenza, da parte del pro­
fano, di queste caratteristiche della musica. Inoltre, 
poichè è molto difficile scrivere un programma per ela­
boratore che possa. trattare queste questioni in maniera 
· 1 ntelligente, è molto probabi le che dai pri mi tentativi 
si ottengano risposte semplicistiche a problemi così 
importanti, e non si ricorra invece, per risolverli, 
a quella serie di esperienze di cui un essere umano si 
servirebbe intui tivamente. E '  comunque i mportante capi­
re che non esistono limiti tecnici che i mpediscano di 
verificare,mediante un elaboratore, ogni aspetto della 
composizione musicale; se queste questioni non sono 
state ancora trattate, molto probabilmente significa al­
lora che i ricercatori non ritengono questi aspetti 
altrettanto problematici o fondamentali per i l  loro 
lavoro quanto quelli di cui stanno attualmente occu­
pandosi. 
RISULTATI DEL MIO LAVORO 
I riiultati della mia attività nel campo della compo­
sizione musicale mediante elaboratore possono essere 
così brevemente riassunti. Ho scri tto i l  mi o programma 
perchè mi interessava lavorare, per un certo periodo, 
con vettori multidimensionali, e avrei dovuto così 
perdere molto tempo in lunghe operazioni quali il cal­
colo dei modelli ritmici di base che comprendevano le 
caratteristiche tecniche che volevo utilizzare, la tra­
duzi one delle istruzioni per la sintesi musicale all 1 
elaboratore, e infine la trascrizione della parti tura. 
L ' uso dell ' elaboratore in queste operazioni ha accor­
ciato notevolmente i miei tempi di lavoro, e per di 
più ho imparato molto sui processi che stavo utilizzano, 
dovendoli trascrivere sotto forma di programma per ela­
boratore. Tuttavia sono certo che i risultati del mio 
lavoro si avvicinano più ad una forma di notazione 
strutturale per la mia musica piuttosto che aÌl'im­
magine dell'elaboratore che effettua scelte compositive 
Sono soltanto io il compositore , e voglio essere pie­
namente responsabile dMlia mia musica. 
Le conclusioni più significati ve che si possono trarre 
dal mio lavoro sono essenzialmente tre , Anzittutto, 
grazie al mio programma, ho potuto concentrarmi sulla 
struttura di base della mia musica molto più facilmen­
te e coerentemente che non se avessi dovuto farlo 
manualmente in tutti i suoi dettagli. Ho avuto così 
la possibilità di accostarmi ad alcuni aspetti della 
mia musica che non avevo pi enamente compreso prima di 
usare l'elaboratore. 
E' molto difficile, infatti, dedurre la struttura di 
base di. un pezzo mentre ci si concentra su problemi a 
livello di dettaglio. In secondo luogo, grazie a que­
sta possibilità, è più facile per me esprimere musical­
mente l e  proprie sensazioni e le proprie idee astratte 
mediante l'elaboratore piuttosto che con metodi tradi­
zionali , nei quali gran parte del tempo è impiegato i n  
attività . manual i .  Può sembrare un paradosso affermare 
che un compositore possa esprimersi attraverso un 
"freddo" e "meccanico" elaboratore , ma effettivamente 
non lo è. 
Infine, giunto alla conclusione del mio lavoro, sono 
convinto che l' autentico valore dell'elaboratore con­
sista nel non sbagliare mai, e nell'eseguire Ჽoltanto 
le istruzioni date: ciò implica, quindi, una maggiore 
chiarezza d'idee da parte del compositore . 
Non credo che il mio programma possa essere utilizzato 
vantaggiosamente da altri compositori. In primo luogo, 
non so se qualcun altro voglia servirsi di queste pro -
cedure; ma, in tal caso, risulterebbe più utile scrive­
re un proprio programma pjuttosto che usare il mio. A 
differenza di altri campi di ricerca, nei quali è im­
portante scambiarsi i programmi per evitare lavoro 
inutile , nel caso della composizione, invece, ognuno, . 
dovrebbe sviluppare ex novo i propri materiali. 
L'uso dell'elaboratore per la composizione è stato 
molto significativo per il mio sviluppo artistico i n  
molteplici dimensioni i n  questi ultimi anni. A diffe­
renza di molti, tuttavia, non credo che l'elaboratore 
conferisca alla mia musica alcun aspe tto misterioso 
che la farebbe identificare come ''mui ica per elaborato­
re" piuttosto che semplicemente "musica". In altre parole 
si tratta semplicementᲾdi un'utilizzazione dell'elabo­
ratore, simile a quella che avviene in molti campi. Gran 
parte della pubblicità che accompagnò i primi 
esperimeᲿti di Hiller e Isaac᳀on tendeva a far ris᳁ltare 
gli aspetti sensazionali del loro lavoro, e fece credere 
che una nuova era fosse iniziata, mentre in realtà essi 
stavano trattando molti problemi musicali tradizionali 
in modo alquanto semplicistico. Infatti, molte composi­
zioni mediante elaboratore, senza alcun interesse spe­
cifico in correlazione con il mezzo, sono state intra­
prese pe᳂chè i problemi erano s emplici e la soluzione 
attraverso l ' elaboratore si presentava come un 
possibile obiettivo. 
La composizione mediante elaboratore non è ancora allo 
stesso livello di quella di tipo tradizionale, ma le 
distanze si stanno sempre più accorciando, e in alcuni 
casi l'attività in questo campo è notevolmente avanzata. 
Ci renderemo conto di aver veramente raggiunto il livel­
lo di sofisticazione desi derato quando l'elaboratore 
sarà sempl icemente 
dato per scontato come normale 
strumento per ogni tipo di espressione musicale intel­
ligente, e non verrà nemmeno nominato n ella descrizione 
del làvoro. 
Note 
1. New York: McGraw-Hill Book Company, 1959 
2 , In questo contesto, il termine "rapporto" indica un 
gruppo di note associate tra loro in quanto presen­
tano alcune caratteristiche comuni. 
(Ouesto articolo à un᳃ versione riveduta e aggiornata 
di Composing by Computer, apparso in "Computer and the 
Humanities", vol. 9, pp. 281-290, Pergamon Press 1975) . 

    """
    clean_text = correct_large_text(raw_ocr_text, "Italian")
    print("Corrected Text:\n", clean_text)