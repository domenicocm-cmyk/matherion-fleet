# Riaddebiti ai clienti: mancati pedaggi, verbali, carburante

## Mancati pedaggi (sotto Verbali)

Quando il concessionario autostradale scrive per un pedaggio non pagato apri
**Mancati pedaggi › Nuova pratica** e registra numero di pratica, ente, date,
importo della pratica, scadenza, protocollo e pagamento. Gli allegati (la
lettera, la ricevuta) si caricano dalla scheda.

Il cuore è **Targhe e importi**: una riga per ogni veicolo della pratica, con la
data del transito (o il periodo), la tratta e **l'importo di quella targa**.
Accanto a ogni riga compare la società a cui si addebita: è quella che in quella
data aveva il mezzo a noleggio, ricavata dai contratti. Se nessuna società aveva
il mezzo, o ce n'è più d'una nel periodo, il gestionale lo dice e la società si
sceglie a mano: non indovina. Se l'importo della pratica differisce dal totale
delle targhe, lo segnala (spese e sanzioni non attribuite a una targa restano a
nostro carico).

Una pratica che resta a nostro carico si segna togliendo «Da riaddebitare»; una
pratica «Contestata» o «Annullata» non si riaddebita.

### Alla preparazione della fatturazione

In **Fatturazione e proforma** la fonte «Mancati pedaggi» (accesa di default)
aggiunge, per ogni società:

- una riga **Mancato pedaggio** per ogni targa/importo, senza IVA (anticipazione,
  natura N1, art. 15 DPR 633/72);
- **una sola** riga «Gestione pratica mancati pedaggi autostradali» da **20 €**
  più IVA, per ogni pratica e per ogni società interessata. Se la stessa pratica
  torna in un mese dopo per la stessa società, la gestione non si ripete; se la
  proforma viene annullata o cancellata, pedaggi e gestione tornano da
  fatturare.

L'importo della gestione si cambia in **Parametri › Gestione pratica mancati
pedaggi** (riga 36 del foglio).

## Verbali: «Rinotifica» o «Gestione amministrativa»

Nella scheda del verbale il campo **Voce da addebitare al cliente** sceglie come
si chiama la spesa in fattura. Si può cambiare anche nel riepilogo della
fatturazione, riga per riga, e la scelta resta sul verbale. L'importo è sempre
quello di «Spese di gestione da addebitare».

## Riaddebito carburante

Si indica **prima quanto paghiamo, poi quanto si addebita**.

- Su un movimento «Rifornimento» segnato «Da riaddebitare»: l'importo del
  movimento è il costo; il campo **Importo da addebitare** è quello da fatturare
  (vuoto = il costo senza IVA). Nel riepilogo della fatturazione la riga mostra
  il costo nostro e un campo per l'addebito.
- In una proforma in bozza: pulsante **Riaddebito carburante**, che chiede data,
  targa, litri, costo (IVA esclusa) e importo da addebitare.

Il **costo sostenuto** resta scritto sulla riga della proforma, così il margine
sul carburante si legge. Nella scheda economica del mezzo, il riaddebito non
ancora fatturato usa l'importo di addebito.

## Ufficio flotta

L'Ufficio flotta può **generare e stampare i contratti di noleggio** (da Stampa
contratti e dal pulsante sulla riga) e gestisce le pratiche di mancato pedaggio.
Non apre la fatturazione.

## Verbali e sinistri: addebiti selezionabili (2026.10.19)

**Importo del verbale al cliente, anche se pagato dalla società.** Sul verbale
il campo «Importo da riaddebitare al cliente» (No/Sì) fa entrare in
fatturazione l'importo pagato anche quando ha pagato la società. La riga è
«Riaddebito verbale», senza IVA (N1). Se l'importo pagato manca, il verbale
finisce nel pannello «da sistemare».

**Gestione amministrativa / rinotifica sotto il verbale.** Compare nel
riepilogo subito sotto il verbale (riga rientrata «↳») con una casella per
selezionarla o deselezionarla. Una riga deselezionata è barrata, non entra nei
totali né nella proforma e resta da fatturare: riappare da sola il mese dopo.

**Gestione sinistro (20 €).** Per ogni sinistro addebitato a un cliente compare
sotto la franchigia la riga «Gestione sinistro», con casella. L'importo è nei
parametri (riga «Gestione sinistro»); sul singolo sinistro il campo «Addebita
la gestione sinistro» (Sì/No) la esclude.

Ogni riga ha il suo segno «già fatturato»: annullando una proforma si liberano
solo le sue righe.

## Che cosa non fa

- non riconosce da solo la società se più clienti hanno avuto il mezzo nel
  periodo: serve la scelta a mano;
- la natura IVA dei pedaggi (N1) e l'IVA sulla gestione sono proposte: conferma
  il trattamento con l'amministrazione;
- non ripartisce una pratica tra società in proporzione ai giorni: ogni importo
  è attribuito per targa e data.
- l'IVA (N1, fuori campo) sull'importo del verbale riaddebitato è una proposta:
  confermala con il commercialista.
