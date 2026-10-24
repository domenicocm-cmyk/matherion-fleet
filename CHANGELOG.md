# Versioni pubblicate
- **2026.10.01c** — pubblicata il 02/10/2026
- **2026.10.02** — pubblicata il 02/10/2026
- **2026.10.03** — pubblicata il 02/10/2026
- **2026.10.04** — pubblicata il 02/10/2026
- **2026.10.05** — pubblicata il 04/10/2026
- **2026.10.05b** — pubblicata il 05/10/2026 — fatturazione: la società
  emittente non nasconde più i clienti delle altre società, e i contratti
  senza società locataria o noleggiante vengono dichiarati invece di sparire.
- **2026.10.05c** — pubblicata il 05/10/2026 — collegamento con la
  piattaforma dei turni: il piano diventa giornaliere aperte, il registro
  pubblica mezzi e autisti. Vedi TURNI.md.
- **2026.10.05d** — pubblicata il 05/10/2026 — sistema visivo Matherion
  Fleet: palette blu petrolio, tipografia e spaziature di `fleet-ui.css`,
  in tema chiaro e scuro. Nessun cambiamento di comportamento.
- **2026.10.05e** — pubblicata il 05/10/2026 — fatturazione: l’avviso dei
  canoni già in proforma si apre e dice quali contratti, per quale cliente e
  in quale proforma; i numeri di contratto ripetuti vengono dichiarati.
- **2026.10.05f** — pubblicata il 05/10/2026 — i mezzi fermi dichiarano dove
  si trovano e su quale centro di costo maturano; la proforma stampata resta
  allegata alla proforma; nuova sezione Documenti, creati e mancanti.
- **2026.10.05g** — pubblicata il 05/10/2026 — confronto fra le foto di
  consegna e di riconsegna: affiancate, sovrapponibili con una tendina, e con
  le zone cambiate evidenziate sulla foto di rientro.
- **2026.10.05h** — pubblicata il 05/10/2026 — il registro si aggiorna da solo
  quando salva un'altra postazione, senza chiudere la sessione; gerarchie di
  accesso con le protezioni contro il restare chiusi fuori.
- **2026.10.06** — pubblicata il 06/10/2026 — il contratto generato resta
  allegato alla riga del noleggio, dalla stampa massiva o dal pulsante sulla
  singola riga; la copia generata resta distinta da quella firmata.
- **2026.10.07** — pubblicata il 07/10/2026 — la targa del libretto si scrive
  a mano quando la lettura ottica non la trova; il libretto si legge dalla
  scheda di un mezzo preciso; gli allegati si vedono nell’elenco mezzi; nei
  documenti mancanti c’è «Gestita».
- **2026.10.07b** — pubblicata il 07/10/2026 — i contratti di leasing e
  noleggio si duplicano: «Duplica» ricopia fornitore, date, canone, servizi e
  franchigie e lascia vuoto il numero. Si fa una copia sola, e si apre subito
  la scheda, oppure più copie in un colpo, numerate di seguito.
- **2026.10.09** — pubblicata il 09/10/2026 — nuovo modulo **Amministrazione**
  con sei sottosezioni: fatture passive, prima nota, bolli e tasse,
  liquidazione IVA, F24 e previsionale F24. Le fatture entrano dagli XML
  dello SDI (anche firmati .p7m) o da Excel e il file resta allegato alla
  riga; escono in Excel, XML e PDF. Il modulo si vede solo con ruolo Master
  o con il nuovo ruolo **Amministrazione**. Vedi AMMINISTRAZIONE.md.
- **2026.10.09b** — pubblicata il 09/10/2026 — dalla fattura passiva si
  leggono anche causale, contratto di locazione, targa, canone e periodo di
  riferimento, presi dai campi del tracciato o, se il fornitore non li
  compila, dalla descrizione; le righe della fattura vengono conservate, così
  una fattura di leasing su dieci veicoli attribuisce il costo a ciascuno.
  Nuova sezione **Fatture attive**, gemella delle passive. Nuova vista
  **Margini per veicolo** e **scheda economica** del singolo mezzo, dalla
  lista mezzi e dal cruscotto: costi, ricavi e margine di una targa, con la
  fonte di ogni numero e le fonti che rischiano il doppio conteggio spente
  e dichiarate.
- **2026.10.10** — pubblicata il 09/10/2026 — due nuovi ruoli, **Ufficio flotta**
  (tutta la parte operativa, senza amministrazione né margini) e **Operativo**
  (giornaliere, assegnazioni, manutenzioni, dotazioni); in **Utenti e accessi**
  il pulsante **Permessi** assegna a ogni persona, area per area, nessun
  accesso, sola lettura o modifica, come eccezione al ruolo; **Guarda come lui**
  mostra il gestionale com'è per quella persona. Utenti e Parametri restano
  solo del Master e l'ultimo Master non si può togliere. Vedi ACCESSI.md.
- **2026.10.10** — pubblicata il 09/10/2026
- **2026.10.10b** — pubblicata il 09/10/2026 — contratti con più targhe: il
  canone può essere **per veicolo**, oppure un **totale da ripartire** in parti
  uguali o per importi indicati targa per targa (i centesimi non si perdono);
  la scheda economica del mezzo prende la sua quota. Le righe di fattura
  passiva senza targa che citano un contratto con più veicoli si dividono fra
  le targhe del contratto, all'importazione o con il pulsante «Ripartisci»; la
  riga originale resta scritta nella quota. Vedi AMMINISTRAZIONE.md.
- **2026.10.10b** — pubblicata il 09/10/2026
- **2026.10.10c** — pubblicata il 09/10/2026 — in **Utenti e accessi** il
  pulsante **Invita** prepara il messaggio per la persona: link al gestionale,
  account Microsoft da usare, profilo, che cosa fare se non entra. Si apre
  nella posta o si copia; il gestionale non spedisce niente da solo.
- **2026.10.10c** — pubblicata il 09/10/2026
- **2026.10.12** — pubblicata il 12/10/2026 — **mese commerciale**: il canone
  si divide sempre per 30, in ogni mese. Un mese intero vale il canone per
  intero (anche ottobre di 31 giorni e febbraio di 28); un mese parziale vale i
  giorni di utilizzo effettivi su 30, mai più di 30. Vale per il canone del
  mese di riferimento nel registro (colonna Da fatturare e formula del foglio),
  per le proforma, per la scheda economica del mezzo e per i margini; prima
  si divideva per i giorni del mese di calendario, e nei margini per 30,44.
- **2026.10.12** — pubblicata il 12/10/2026
- **2026.10.12b** — pubblicata il 12/10/2026 — i contratti si generano dal
  **modello Word che sta nella cartella del registro** (su SharePoint o
  sincronizzata), non da quello incluso nel programma: cerca
  `Modello_Contratto_Noleggio_Furgoni.docx` e `Modello_Contratto_Quadro_Multiplo.docx`
  nella cartella «Modelli» (o in quella indicata in Parametri), poi in
  «Contratti» e nella cartella principale. Si rilegge a ogni generazione; un
  modello con un errore di segnaposto non blocca la stampa e viene segnalato.
  Il modello caricato a mano dalla pagina Stampa resta prioritario.
- **2026.10.12b** — pubblicata il 12/10/2026
- **2026.10.13** — pubblicata il 13/10/2026 — fatture: le **note di credito**
  si leggono con importi negativi e in rosso (passive e attive), con filtro
  Documento; i **bolli di fattura** hanno colonna, filtro, controllo «dovuto
  non indicato» e riepilogo trimestrale con codici F24 2521–2524; nuova
  sezione **Banca e carte** (conti, carte, cassa, saldi, estratto conto,
  giroconti e addebito carta, riconciliazione) con scelta del conto nei
  pagamenti e negli incassi; nuova sezione **Note spese** dei dipendenti con
  approvazione, prima nota, rimborso e costo per veicolo. Vedi AMMINISTRAZIONE.md.
- **2026.10.13** — pubblicata il 13/10/2026
- **2026.10.16** — pubblicata il 16/10/2026 — l'**Ufficio flotta** genera e
  stampa i contratti di noleggio; nuova sezione **Mancati pedaggi** sotto i
  Verbali (pratiche con le targhe e gli importi per targa) e riaddebito in
  fatturazione alla società che aveva il mezzo, più 20 € di gestione pratica
  per pratica e società (parametro); per ogni verbale si sceglie la voce
  **Rinotifica** o **Gestione amministrativa**, anche dal riepilogo; **riaddebito
  carburante** con prima il costo e poi l'importo da addebitare. Vedi RIADDEBITI.md.
- **2026.10.16** — pubblicata il 16/10/2026
- **2026.10.17** — pubblicata il 16/10/2026 — **Note spese**: l'importo si salva a
  ogni battuta e il totale si aggiorna subito (prima si perdeva chiudendo con Esc
  o cliccando «Fatto» appena scritto); il riepilogo «da rimborsare» conta anche
  le note presentate. Nuova pagina **Grafici e analisi** con grafici interattivi
  (flotta, scadenze, occupazione dei mezzi, fatturato, ricavi e costi, verbali,
  mancati pedaggi, note spese). Vedi GRAFICI.md.
- **2026.10.17** — pubblicata il 16/10/2026
- **2026.10.18** — pubblicata il 17/10/2026 — **Note spese dal telefono**: l'app
  dei telefoni (versione 1.1.0) registra una spesa con importo, tipo, pagamento e
  foto dello scontrino; il gestionale la ritira alla prima apertura nella nota del
  mese del dipendente («Spese da app», in bozza) con lo scontrino negli allegati.
  Nessun doppione. Vedi APP.md.
- **2026.10.18** — pubblicata il 17/10/2026
- **2026.10.19** — pubblicata il 17/10/2026 — verbali: importo riaddebitabile
  al cliente anche se pagato dalla società; gestione/rinotifica sotto il
  verbale con casella; gestione sinistro da 20 € con casella e parametro.
  Vedi RIADDEBITI.md.
- **2026.10.19** — pubblicata il 17/10/2026
- **2026.10.20** — pubblicata il 19/10/2026 — **Contratti: operazioni massive**.
  Caselle di selezione nella lista, generazione Word e/o PDF per contratto, per
  società o tutto insieme, esportazione dell'elenco in Excel (anche un foglio per
  società) e CSV, e degli allegati in ZIP. Vedi CONTRATTI_MASSIVI.md.
- **2026.10.20** — pubblicata il 19/10/2026
- **2026.10.21** — pubblicata il 19/10/2026 — **Centri di costo e costi
  dell'appalto**. Il centro di costo del contratto arriva nel menu e abbina il
  mezzo; «Nuovo centro di costo» nel contratto; costi per centro e per mese
  (Fast Rent e le altre società) con Excel; il centro di costo nel riepilogo e
  nei movimenti di Telepass e carte. Vedi CENTRI_DI_COSTO.md.
- **2026.10.22** — pubblicata il 19/10/2026 — **Carte e movimenti per centro di
  costo, storico del mezzo**. Centro di costo su carte e Telepass e sui
  movimenti (anche in blocco), ricerca per numero carta, costi sul centro del
  movimento e non sul contratto, «Storico mezzi» con tutte le modifiche nella
  scheda economica. Vedi CENTRI_DI_COSTO.md.
- **2026.10.22** — pubblicata il 19/10/2026
- **2026.10.23** — pubblicata il 19/10/2026 — **Grafica Studio e canoni per
  targa**. Tema «Studio» di index.html su tutte le pagine; il canone si
  allinea da solo fra contratto di noleggio, scheda del mezzo e noleggi non
  scaduti (stessa targa), con i costi del contratto fornitore accanto e le
  modifiche nello storico. Vedi CANONI.md.
- **2026.10.24** — pubblicata il 20/10/2026 — **Documenti dei mezzi in blocco**.
  Dall'elenco mezzi si esportano in ZIP i documenti scelti per targa e per
  tipo (libretti, polizze…), anche quelli collegati alla stessa targa, con
  indice Excel e documenti mancanti. Vedi DOCUMENTI_MEZZI.md.
- **2026.10.24** — pubblicata il 20/10/2026
- **2026.10.25** — pubblicata il 20/10/2026 — **Guida**. Un assistente nel
  gestionale: si scrive la domanda («come carico un sinistro?», «dove trovo i
  costi del centro di costo Amazon?») e la Guida risponde ed evidenzia sullo
  schermo i passaggi. Vedi GUIDA.md.
- **2026.10.26** — pubblicata il 21/10/2026 — **Rimessa Diretta**. Con termine
  di pagamento 0 (Parametri) i contratti e le proforma riportano «Rimessa
  Diretta» al posto di «a 0 giorni data fattura»; lo 0 non torna più a 30.
- **2026.10.27** — pubblicata il 22/10/2026 — **Franchigie senza IVA**. Nelle
  proforma la franchigia/danni del sinistro è addebitata senza IVA (natura N2.2,
  risarcimento); restano con IVA canoni, spese di gestione e gestione sinistro.
- **2026.10.28** — pubblicata il 22/10/2026 — **Verbali: solo Global One non si
  rinotifica**. I verbali dei mezzi a noleggio si rinotificano tutti al cliente;
  quelli dei clienti indicati in Parametri (riga 38, predefinito «Global One»)
  restano alla società: «Da pagare», pagati dalla società, fuori dalle Rinotifiche.
- **2026.10.29** — pubblicata il 23/10/2026 — **Importa polizze**. Da Mezzi si
  sceglie il PDF/le scansioni delle polizze: il gestionale legge targa, polizza,
  scadenze e premi, raggruppa per mezzo, mostra l'anteprima e alla conferma
  aggiorna la scheda e allega la copia con le sole pagine di quel mezzo.
  Vedi POLIZZE.md.
- **2026.10.30** — pubblicata il 23/10/2026 — **Rimborso accise gasolio**
  (Amministrazione). Calcolo trimestrale per i veicoli da 7,5 t Euro 5+, con
  l'accisa del giorno di ogni rifornimento, quadri, limite 1 l/km, esclusioni
  motivate, tabella aliquote modificabile ed export Excel. Vedi ACCISE.md.
- **2026.10.31** — pubblicata il 24/10/2026 — **Tachigrafo** (Amministrazione).
  Scadenzario degli scarichi (carte 28 giorni, unità di bordo 90), archivio dei
  file .ddd con conservazione di 12 mesi, controlli e formazione, fascicolo
  Excel. Nuovo campo «Tachigrafo installato» in Mezzi. Vedi TACHIGRAFO.md.
