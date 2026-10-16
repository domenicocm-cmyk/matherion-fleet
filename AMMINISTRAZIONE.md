# Amministrazione

Sei sottosezioni, nel gruppo **Amministrazione** del menu:

| Sezione | A cosa serve |
|---|---|
| Fatture passive | Le fatture ricevute dai fornitori, con riepilogo IVA e righe |
| Fatture attive | Le fatture emesse ai clienti, lette dallo stesso tracciato |
| Prima nota | Le scritture contabili, che nascono dalle fatture |
| Bolli e tasse | Le tasse automobilistiche, veicolo per veicolo |
| Liquidazione IVA | Il saldo IVA di ogni periodo |
| F24 | I modelli da versare, con i tributi riga per riga |
| Previsionale F24 | Che cosa si pagherà nel mese e da dove viene ogni importo |
| Margini per veicolo | Costi, ricavi e margine di ogni mezzo |

Tutto finisce nei fogli del registro Excel come gli altri moduli: undici fogli
nuovi (`Fatture passive`, `Fatture passive IVA`, `Fatture passive righe`,
`Fatture attive`, `Fatture attive IVA`, `Fatture attive righe`, `Prima nota`,
`Bolli`, `Liquidazione IVA`, `F24`, `F24 tributi`). Non c'è niente da salvare
a parte.

---

## Chi ci può entrare

Il modulo **non si vede per esclusione ma per permesso**: serve un ruolo che lo
abbia espressamente. Di partenza ce l'hanno due ruoli:

- **Master** — vede e fa tutto, come sempre.
- **Amministrazione** — il ruolo nuovo. Vede e modifica le sei sezioni, più
  fatturazione e proforma, documenti e calendario; vede senza modificare mezzi,
  contratti e anagrafiche; **non** entra in Parametri né in Utenti.

**Ufficio flotta**, **Operativo**, **Filiale**, **Officina** e **Sola lettura** non vedono il gruppo nel menu e non
possono aprirne le pagine neanche conoscendone l'indirizzo. La sola lettura, che
vede tutto il resto del registro, qui si ferma. Le scadenze fiscali nel cruscotto
seguono la stessa regola: una filiale non le vede.

Si assegna il ruolo in **Anagrafiche → Utenti e accessi**, campo *Ruolo*.

Oltre al ruolo, il Master può dare o togliere l'area *Amministrazione* (e quella
dei *Margini*) a una singola persona: vedi ACCESSI.md, «Permessi per singola
persona». Ufficio flotta e Operativo non hanno l'amministrazione di partenza.

---

## Fatture passive

### Come entrano

**Da XML.** «Importa fatture» → trascina i file, anche tutti insieme. Vanno bene:

- i `.xml` del tracciato FatturaPA;
- i `.xml.p7m` firmati: la fattura viene estratta dalla busta. **La firma non
  viene verificata** — senza una libreria di crittografia non si può, e il
  gestionale lo dichiara invece di far finta.

Da ogni file nasce una riga per ogni fattura contenuta (un file può contenerne
più d'una) e **il file resta allegato alla riga**: la fattura si riapre dalla
piattaforma, senza andare sul server.

Viene letto: numero, data, tipo documento, fornitore con partita IVA e codice
fiscale, la tua società intestataria, imponibile e IVA per aliquota e natura,
totale documento, bollo, ritenuta d'acconto con la causale, modalità e scadenza
di pagamento, IBAN.

Vengono inoltre letti, quando ci sono, **causale**, **contratto di locazione**,
**canone** e **periodo di riferimento**. Il tracciato ha i campi apposta
(`DatiContratto`, `DataInizioPeriodo`, `DataFinePeriodo`, `Causale`) ma molti
fornitori non li compilano e scrivono tutto nella descrizione: allora il
gestionale legge la descrizione e riconosce

- `dal 01/03/2026 al 31/03/2026`, `01/03/26 - 31/03/26`
- `marzo 2026`, `periodo: 03/2026`, `2° trimestre 2026`
- `contratto n. MAN/2026/77`, `rif. contratto di locazione: NLT-2025-0001`

Quello che viene dalla descrizione e non dai campi è segnato nelle note della
fattura, perché è una lettura, non un dato certificato. Una data o un importo
non vengono mai scambiati per un numero di contratto.

Viene **proposto** (controllalo):

- la **categoria di costo**, decisa dalla riga che pesa di più — non dalla prima
  parola che combacia, se no una fattura di noleggio da 2.000 € con 120 € di km
  eccedenti finirebbe classificata «km eccedenti»;
- la **targa**: prima quelle già in anagrafica, che sono certe; poi, se non ce
  ne sono, quelle col formato di una targa italiana, segnalate come da
  verificare;
- il **conto di costo**, dalla categoria;
- la **detraibilità IVA al 100%**: giusta per i veicoli strumentali e per quelli
  dati a noleggio. Sulle autovetture a uso promiscuo va messa al **40%**.

### Le righe della fattura

Una fattura di leasing copre dieci veicoli con dieci righe. Le righe vengono
conservate, e il pulsante **«Righe»** le apre: targa, contratto, periodo,
canone, imponibile e categoria, riga per riga, correggibili. C'è anche
«assegna una targa a tutte le righe» per le fatture a veicolo unico.

È da qui che la **scheda economica del mezzo** prende i costi: senza le righe,
una fattura su dieci veicoli non si saprebbe come ripartire. **Una riga senza
targa resta un costo della flotta, non del veicolo**: il gestionale non inventa
una ripartizione.

I fornitori che non sono in anagrafica vengono creati con denominazione e partita
IVA presi dalla fattura (si può disattivare), da completare poi.

Reimportare lo stesso file non crea doppioni: stesso numero, stessa data e stessa
partita IVA vengono riconosciuti e saltati.

**Da Excel o CSV.** Le colonne si abbinano a mano come negli altri moduli, e il
file importato resta allegato a tutte le righe che ha creato.

### Come escono

Pulsante «Estrai», quattro formati:

- **Excel** — una riga per fattura;
- **XML** — un `RegistroFatturePassive` con il riepilogo IVA per aliquota dentro,
  per il programma di contabilità. Non è un FatturaPA: quello è il documento del
  fornitore e sta fra gli allegati;
- **PDF** — il registro stampabile, con i totali in fondo;
- **i file originali** — gli XML e i PDF ricevuti, presi dagli allegati.

I file finiscono in `Amministrazione/Estrazioni` nella cartella del registro.

### Controlli automatici

- **Quadratura**: se imponibile + IVA + bollo + arrotondamento non fa il totale
  del documento, la riga lo dice con lo scarto.
- **Note di credito**: una TD04 **sottrae**, nei totali di periodo e nella
  liquidazione IVA. Nel tracciato gli importi sono positivi e il segno sta nel
  tipo di documento; se non si guardasse, gli storni gonfierebbero l'IVA a credito.
- **Inversione contabile**: le righe a natura N6 vengono marcate, e l'IVA si
  ricava dall'imponibile per l'aliquota. In liquidazione va sia a debito sia a
  credito.

---

## Fatture attive

Le fatture emesse ai clienti, lette dallo **stesso tracciato FatturaPA**: qui il
cedente sei tu e il cessionario è il cliente. Entrano da XML (anche `.p7m`) o da
Excel, portano riepilogo IVA e righe come le passive, e il file resta allegato.

Se il cedente di un file non è una tua società, il gestionale lo dice: è
probabilmente una fattura ricevuta, che va fra le passive.

Riconosce la **scissione dei pagamenti** (esigibilità `S`): l'IVA la versa il
cliente, e non entra fra l'IVA a debito della liquidazione.

**Le proforma restano dove sono.** «Fatturazione e proforma» serve a preparare
la fatturazione; qui ci sono le fatture vere. Quando il numero di una fattura
importata coincide con il «numero fattura SDI» di una proforma, le due cose si
collegano da sole. In liquidazione IVA vale la fattura: una proforma viene
contata solo se non esiste la fattura corrispondente, così lo stesso ricavo non
finisce due volte nel calcolo.

«Porta in prima nota» scrive credito verso il cliente in dare, ricavo e IVA in
avere. «Incassata» registra l'incasso: banca in dare, credito in avere.

---

## Prima nota

Non si scrive a mano: si porta una fattura (o più) in prima nota e **nasce la
scrittura**. Costo e IVA in dare, debito verso il fornitore in avere. Sulle note
di credito i due lati si scambiano.

Ogni scrittura **quadra**. Se per qualche ragione non quadrasse, la riga si
colora e un pannello in fondo elenca le scritture sbilanciate con lo scarto: il
gestionale lo dichiara invece di nasconderlo in un arrotondamento silenzioso.

«Segna pagate» chiede data, mezzo e conto, e può registrare anche il pagamento:
debito verso il fornitore in dare, banca in avere per il netto, **Erario
c/ritenute** in avere per la ritenuta d'acconto trattenuta.

«Annulla la registrazione» toglie tutte le righe della scrittura e rimette la
fattura fra quelle da registrare.

Il piano dei conti è un elenco di suggerimenti, non una gabbia: i conti si
scrivono liberamente e quelli che usi entrano nei suggerimenti.

---

## Bolli e tasse

«Genera dalla flotta» crea una posizione per ogni veicolo in flotta che non ce
l'ha ancora per quell'anno: potenza, massa e classe ambientale dal libretto,
scadenza dal campo *Bollo* del mezzo. Dove esiste il bollo dell'anno prima,
importo, tariffa e regione vengono ripresi.

«Rinnova» sposta la scadenza al periodo successivo tenendo lo stesso importo.

**L'importo è una proposta, non un calcolo autorevole.** Il gestionale fa
`tariffa × base` (kW, oppure quintali di massa complessiva per gli autocarri) e
lo mostra accanto all'importo dovuto quando i due divergono. La tariffa dipende
dalla tabella della tua regione e la metti tu — in Parametri c'è un valore
predefinito. Le tabelle regionali non sono dentro il gestionale, e non sarebbe
onesto far finta di sì.

I bolli non si pagano con l'F24: nel previsionale compaiono in un riquadro a
parte, perché pesano sulla stessa cassa.

---

## Liquidazione IVA

Il pannello in alto calcola un periodo: società, anno, periodicità, periodo →
«Calcola».

```
debito  = IVA sulle vendite + IVA da inversione contabile
credito = IVA detraibile sugli acquisti (compresa la quota detraibile
          dell'inversione contabile)
saldo   = debito - credito - credito del periodo precedente
          - acconto + interessi + altre variazioni
```

L'IVA sugli **acquisti** viene dalle fatture passive del periodo, al netto delle
note di credito e ridotta dalla percentuale di detraibilità di ciascuna. L'IVA
indetraibile è mostrata a parte: non entra nel calcolo, è un costo.

L'IVA sulle **vendite** viene dalle fatture emesse registrate nel gestionale
(proforma passate a «Fattura emessa SDI» o «Pagata»). Se fatturi anche altrove,
il pannello lo dice e il numero si scrive a mano.

Il dettaglio è apribile: le fatture che compongono il totale, una per una, con la
loro quota detraibile. Si controlla, non si deve credere sulla parola.

**Scadenze e codici proposti:**

| Periodicità | Scadenza | Codice tributo |
|---|---|---|
| Mensile, mese *n* | 16 del mese successivo | 6001–6012 |
| Trimestrale, 1º trim. | 16 maggio | 6031 |
| Trimestrale, 2º trim. | 20 agosto | 6032 |
| Trimestrale, 3º trim. | 16 novembre | 6033 |
| Trimestrale, 4º trim. | col saldo annuale | 6099 |

Gli interessi dell'1% sono proposti ai trimestrali, non sull'ultimo periodo. Una
scadenza che cade di sabato o domenica slitta al lunedì; **le festività no**,
quelle vanno controllate.

---

## F24

I modelli, con i tributi riga per riga (sezione, codice, anno, debito, credito).
Scrivendo un codice tributo noto la descrizione e la sezione si compilano da sé.

L'elenco dei codici suggeriti contiene solo quelli di uso corrente e di cui si è
certi: IVA mensile e trimestrale, acconto e saldo annuale, ritenute 1001/1012/
1040/1038, IRES, IRPEF, IRAP, addizionali, interessi 1668, sanzioni, causali INPS.
**Il campo resta libero**: qualunque altro codice si scrive a mano.

«Riepilogo PDF» produce un foglio leggibile per chi paga e per chi controlla.
**Non è il modello ministeriale** e non si presenta in banca al posto dell'F24.

«Registra in prima nota» mette i tributi in dare e la banca in avere.

---

## Previsionale F24

Scegli società e mese: la tabella dice che cosa si pagherà, quanto, e **da dove
viene ogni importo**. Ogni riga porta un'etichetta:

- **in un F24** — il tributo è già scritto in un modello;
- **già versato** — pagato;
- **calcolato ora** — il periodo non è ancora stato liquidato e il previsionale
  lo ha calcolato da sé. Va confermato.

Cosa raccoglie:

- l'**IVA** delle liquidazioni che scadono nel mese; se un periodo non è ancora
  stato calcolato, lo calcola;
- le **ritenute d'acconto** delle fatture passive pagate o in scadenza il mese
  precedente, al 16 del mese, raggruppate per codice;
- i **tributi già messi in un F24** con quella scadenza;
- i **bolli** in scadenza, in un riquadro a parte perché non vanno in F24.

Lo stesso tributo non viene mai contato due volte: se una liquidazione è già
finita in un F24, vale la riga dell'F24 — è quella che si versa.

«Crea i modelli F24» genera un modello per società e per scadenza, in stato
**Previsionale**: gli importi vanno confermati prima di versare.

---

## Il canone rapportato ai giorni: il mese commerciale

Il canone di noleggio si calcola sui **giorni di utilizzo**, ma il mese vale
sempre **30 giorni**, qualunque sia il mese di calendario:

- un mese intero vale il canone per intero (ottobre di 31 giorni, febbraio di 28);
- un mese parziale vale `canone ÷ 30 × giorni di utilizzo`, e mai più di un canone;
- un contratto su più mesi si calcola mese per mese: dal 15 ottobre al 10
  dicembre sono 17/30 di ottobre, novembre intero e 10/30 di dicembre.

Esempio con canone 900 €: 15–31 ottobre = 17 giorni = 510 €; 1–15 ottobre = 15
giorni = 450 €; 10–28 febbraio = 19 giorni = 570 €; 2–31 ottobre = 30 giorni =
900 €. La regola è la stessa nel registro, nelle proforma, nel foglio Excel e
nella scheda economica del mezzo, così il margine usa gli stessi numeri della
fattura. Si applica anche ai canoni dei contratti dei fornitori.

## Contratti con più targhe: il costo per mezzo

Per il margine di un veicolo il canone di un contratto che ne copre dieci va
diviso. Nella scheda del contratto (*Condizioni economiche*) si sceglie come
leggere il canone:

- **Per veicolo**: il canone indicato è già quello di ogni targa (come prima).
- **Totale del contratto, da ripartire**: il canone è uno solo per tutte le
  targhe. *In parti uguali* lo divide per il numero di targhe; *Importi per
  targa* usa gli importi scritti nel campo apposito, nella forma
  `GA123BC=450; GB456CD=520,50`. Se gli importi non tornano con il totale, o
  mancano targhe, il contratto non si salva e dice che cosa non torna.

I centesimi che avanzano vanno alle prime targhe: la somma delle quote è sempre
il totale. La scheda economica del mezzo prende la sua quota, e lo dichiara.

**Fatture con una riga sola per tutto il contratto.** Se una riga della fattura
passiva non ha la targa ma cita un contratto che il gestionale conosce, la riga
si divide in una quota per targa, in proporzione alle quote del contratto. Succede
all'importazione; per le righe già entrate c'è il pulsante **Ripartisci sulle
targhe del contratto** nella finestra delle righe. Ogni quota è marcata
«Ripartita» e porta l'importo della riga originale. Se il contratto non c'è, la
riga resta com'è e il gestionale lo dice.

Un limite da conoscere: la riga si divide per intero, anche quando contiene
voci che non sono canoni (km eccedenti, spese). Se vanno attribuite a una targa
sola, si corregge la riga prima di ripartire.

---

## Margini per veicolo

La domanda è semplice — questo mezzo rende o no — e la risposta richiede di
mettere insieme cose che stanno in sei archivi diversi.

**Dalla lista mezzi**, l'azione «Scheda economica» su una riga. **Dal
cruscotto**, il riquadro «Margini per veicolo» con i cinque migliori, i cinque
peggiori e il selettore della targa. **Dalla sezione «Margini per veicolo»**,
tutta la flotta in una tabella ordinabile, con l'export in PDF e in Excel.

La scheda mostra, per il periodo scelto: ricavi e costi voce per voce **con la
fonte di ciascuno**, il margine in euro e in percentuale, i giorni in cui il
mezzo è stato a noleggio, e il costo al giorno.

### Il doppio conteggio, e come viene evitato

Il canone di un contratto di leasing e la fattura che lo addebita sono **lo
stesso costo visto da due parti**. Lo stesso vale per il consuntivo di una
manutenzione e la fattura dell'officina, o per il canone di un contratto di
noleggio e la fattura emessa al cliente.

Perciò le fonti sono separate e si accendono una per una:

| Fonte | Lato | Accesa di default |
|---|---|---|
| Fatture passive (righe intestate al veicolo) | costo | sì |
| Carburante e pedaggi (movimenti carte e Telepass) | costo | sì |
| Bolli e tasse | costo | sì |
| Verbali a nostro carico | costo | sì |
| Canoni di contratto (dai contratti fornitori) | costo | **no** |
| Manutenzioni a consuntivo | costo | **no** |
| Franchigie sinistri | costo | **no** |
| Fatture attive (righe intestate al veicolo) | ricavo | sì |
| Proforma non ancora fatturate | ricavo | sì |
| Riaddebiti ai clienti | ricavo | sì |
| Canoni di noleggio dal registro | ricavo | **no** |

Accese di default sono le **fonti documentali**: i soldi davvero usciti ed
entrati. Le fonti del **registro operativo** sono spente, e in fondo alla pagina
c'è scritto quali: servono a chi non registra le fatture dei fornitori, e
accenderle insieme alle fatture conterebbe lo stesso euro due volte.

Ogni voce della scheda dice da dove viene, e il PDF riporta in testata quali
fonti erano spente: un numero senza la sua provenienza non serve a decidere.

---

## Note di credito e bolli di fattura

**Note di credito.** Nell'elenco delle fatture passive (e delle attive) una
nota di credito (TD04) si riconosce subito: riga evidenziata, etichetta «Nota di
credito», importo, IVA e totale **con il segno meno e in rosso**. I totali in
testata la sottraggono (un'imponibile di 1.000 € e una nota di 200 € fanno
800 €), e il filtro **Documento** separa le fatture dalle note.

**Bolli di fattura.** È l'imposta di 2 € sui documenti con operazioni senza IVA,
cosa diversa dal «bollo auto» di *Bolli e tasse*. L'elenco ha:

- la colonna **Bollo**: l'importo quando c'è, oppure «dovuto, non indicato»;
- il filtro **Bollo** (con bollo / dovuto non indicato / senza bollo);
- nella testata, il totale dei bolli e quanti ne mancano;
- il pulsante **Bolli di fattura**: riepilogo per trimestre.

«Dovuto non indicato» scatta quando le righe con natura N1, N2.x, N3.x o N4
superano **77,47 €** e la fattura non porta nessun bollo. N5, N6 e N7 non
contano. È un controllo, non una certezza: le esclusioni sono più di quelle
che il gestionale conosce, e l'ultima parola è del commercialista.

Dall'XML si legge sia `ImportoBollo` sia il solo `BolloVirtuale=SI` (che vale
2 €). Nelle fatture ricevute il bollo è già dentro il totale e la prima nota lo
registra su «Imposta di bollo». Per le **fatture emesse** il riepilogo dà, per
trimestre, il numero di fatture con bollo, l'importo, il **codice tributo F24**
(2521, 2522, 2523, 2524) e la scadenza (31 maggio, 30 settembre, 30 novembre,
28 febbraio, spostate al primo giorno lavorativo). Se il primo trimestre non
supera 250 € il versamento slitta al secondo; se i primi due non superano 250 €,
al terzo. Il gestionale **non** compila l'F24: prepara i numeri.

---

## Banca e carte

Sezione **Banca e carte**, nel gruppo Amministrazione: l'archivio dei conti
correnti, delle carte di credito e prepagate, dei conti postali e della cassa.
Per ognuno: nome, banca, IBAN, ultime cifre, società, saldo iniziale con data,
fido o plafond e, per le carte, il conto su cui si addebita e il giorno.

**Il nome del conto è il suo identificativo**: è quello che compare nella
colonna «Conto» della prima nota, e per questo non si cambia dopo i primi
movimenti. Ogni conto ha un saldo che segue la prima nota:

- conto corrente e cassa: saldo iniziale + dare − avere;
- carta di credito: è un debito, cresce con le spese e scende con il
  pagamento dell'estratto (iniziale + avere − dare); il disponibile è il fido
  meno il debito.

Quando segni una fattura **pagata** o **incassata**, il campo «Conto» è una
scelta tra i conti censiti (il predefinito per primo): pagare con una carta
mette l'avere sulla carta, non sulla banca. Dalla scheda di ogni conto:

- **Estratto conto** con saldo progressivo, filtro per periodo, PDF ed Excel;
- **Nuovo movimento**: commissioni, interessi, stipendi, prelievi e versamenti
  di contante, o un altro conto a tua scelta (registrazione `MB-aaaa-nnnn`);
- **Giroconto** tra conti e **addebito dell'estratto della carta** (propone
  importo, conto e giorno; registrazione `GC-aaaa-nnnn`);
- **Riconciliazione**: spunta le righe verificate sull'estratto della banca; il
  «saldo riconciliato» deve coincidere con quello che dice la banca.

La prima nota si filtra per conto e per stato di riconciliazione.

**Che cosa non fa.** Non è collegato alla banca: il saldo è contabile, non
quello reale. Non importa gli estratti (CBI, CSV, PSD2) e non abbina i
movimenti da solo: la riconciliazione è manuale. Senza nessun conto censito
tutto funziona come prima, con il conto di Parametri.

---

## Note spese dei dipendenti

Sezione **Note spese**. Il dipendente raccoglie le spese fatte per l'azienda in
una nota, con una riga per scontrino (data, categoria, esercente, importo, IVA,
targa, e **come l'ha pagata**: anticipo suo, carta aziendale, contanti
aziendali) e gli scontrini come allegati della nota.

Percorso: **Bozza → Presentata → Approvata (o Respinta) → Rimborsata**.

- **Chi non fa parte dell'amministrazione** vede e modifica solo le *sue* note,
  e solo in bozza o respinte. Il collegamento è l'email: quella con cui entra
  deve comparire nell'anagrafica del dipendente.
- **Approva** (amministrazione): nasce la scrittura di prima nota
  `NS-aaaa-nnnn`. Costi in dare per categoria (con la targa sulla riga, se c'è),
  IVA a credito solo sulle righe dove hai scelto «IVA detraibile: Sì»; in avere
  *Debiti verso dipendenti* per le spese anticipate, il conto della carta per
  quelle con carta, la *Cassa* per i contanti.
- **Rimborsa**: per le spese anticipate, dal conto scelto (`NS-…/RIM`), in
  contanti, oppure **in busta paga** (in quel caso non si registra nessuna
  uscita e il debito resta aperto finché non lo chiude il cedolino).
- **Annulla le scritture** riporta la nota a «Presentata».
- **Respingi** chiede il motivo, che il dipendente legge nell'elenco.
- La nota si stampa in **PDF** per la firma.

**Costo per veicolo.** Le righe con la targa, nelle note approvate, entrano nella
scheda economica del mezzo (fonte «Note spese», accesa di default) al netto
dell'IVA detraibile.

**Cautele.** L'IVA è detraibile solo se la scegli tu: senza fattura intestata,
nel dubbio lascia «No» e l'IVA entra nel costo. Il gestionale non calcola
rimborsi chilometrici né indennità di trasferta e non verifica massimali o il
trattamento fiscale delle singole spese: è un'organizzazione del lavoro, non un
parere fiscale.

---

## Parametri nuovi

In **Parametri**, righe 31–34 del foglio:

| Parametro | A cosa serve |
|---|---|
| Liquidazione IVA: periodicità | `Mensile` o `Trimestrale`, decide il periodo IVA predefinito delle fatture |
| Conto banca predefinito | Usato nelle scritture di pagamento |
| Regione per il calcolo del bollo | Proposta sui bolli generati dalla flotta |
| Bollo: tariffa unitaria (€ per kW) | Proposta sui bolli generati dalla flotta |

---

## Quello che il gestionale non fa

Vale la pena dirlo chiaramente:

- **non verifica le firme digitali** dei `.p7m`: estrae la fattura, non la valida;
- **non conosce le tabelle del bollo** regione per regione: calcola `tariffa ×
  base` con la tariffa che metti tu;
- **non conosce le festività**: sposta solo sabato e domenica;
- **non certifica codici tributo e scadenze**: li propone, e sono quelli di uso
  corrente. Prima di versare, conferma importi, codici e scadenze con il
  commercialista;
- **non produce il modello F24 ministeriale**: produce un riepilogo leggibile;
- **non è collegato alla banca**: i saldi sono quelli della prima nota, e la
  riconciliazione con l'estratto è manuale;
- **non compila né versa i bolli di fattura**: li riepiloga per trimestre con
  codici e scadenze da confermare;
- **non è una contabilità generale**: è una prima nota che quadra e un registro
  acquisti e vendite, pensati per essere passati a chi tiene la contabilità;
- **non ripartisce da solo i costi di una fattura su più veicoli**: attribuisce
  quello che le righe dicono, e quello che le righe non dicono resta un costo
  della flotta. Se una fattura cumulativa va divisa, la divisione si fa a mano
  nelle righe;
- **non indovina sempre il periodo o il contratto**: quando li ricava dalla
  descrizione invece che dai campi del tracciato, lo scrive nelle note.
