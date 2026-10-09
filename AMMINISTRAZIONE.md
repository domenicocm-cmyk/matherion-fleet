# Amministrazione

Sei sottosezioni, nel gruppo **Amministrazione** del menu:

| Sezione | A cosa serve |
|---|---|
| Fatture passive | Le fatture ricevute dai fornitori, con il riepilogo IVA per aliquota |
| Prima nota | Le scritture contabili, che nascono dalle fatture |
| Bolli e tasse | Le tasse automobilistiche, veicolo per veicolo |
| Liquidazione IVA | Il saldo IVA di ogni periodo |
| F24 | I modelli da versare, con i tributi riga per riga |
| Previsionale F24 | Che cosa si pagherà nel mese e da dove viene ogni importo |

Tutto finisce nei fogli del registro Excel come gli altri moduli: sette fogli
nuovi (`Fatture passive`, `Fatture passive IVA`, `Prima nota`, `Bolli`,
`Liquidazione IVA`, `F24`, `F24 tributi`). Non c'è niente da salvare a parte.

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

Viene **proposto** (controllalo):

- la **categoria di costo**, dedotta dalle descrizioni delle righe;
- la **targa**, solo se in fattura compare una targa già in anagrafica — così non
  si inventano accostamenti;
- il **conto di costo**, dalla categoria;
- la **detraibilità IVA al 100%**: giusta per i veicoli strumentali e per quelli
  dati a noleggio. Sulle autovetture a uso promiscuo va messa al **40%**.

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
  acquisti, pensati per essere passati a chi tiene la contabilità.
