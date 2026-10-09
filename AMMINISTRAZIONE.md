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
abbia espressamente. Oggi ce l'hanno due ruoli:

- **Master** — vede e fa tutto, come sempre.
- **Amministrazione** — il ruolo nuovo. Vede e modifica le sei sezioni, più
  fatturazione e proforma, documenti e calendario; vede senza modificare mezzi,
  contratti e anagrafiche; **non** entra in Parametri né in Utenti.

**Filiale**, **Officina** e **Sola lettura** non vedono il gruppo nel menu e non
possono aprirne le pagine neanche conoscendone l'indirizzo. La sola lettura, che
vede tutto il resto del registro, qui si ferma. Le scadenze fiscali nel cruscotto
seguono la stessa regola: una filiale non le vede.

Si assegna il ruolo in **Anagrafiche → Utenti e accessi**, campo *Ruolo*.

> Il passo successivo, che resta da fare, è il permesso **per singolo utente e
> per singolo modulo**: oggi la grana è il ruolo, non la persona.

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
- **non è una contabilità generale**: è una prima nota che quadra e un registro
  acquisti e vendite, pensati per essere passati a chi tiene la contabilità;
- **non ripartisce da solo i costi di una fattura su più veicoli**: attribuisce
  quello che le righe dicono, e quello che le righe non dicono resta un costo
  della flotta. Se una fattura cumulativa va divisa, la divisione si fa a mano
  nelle righe;
- **non indovina sempre il periodo o il contratto**: quando li ricava dalla
  descrizione invece che dai campi del tracciato, lo scrive nelle note.
