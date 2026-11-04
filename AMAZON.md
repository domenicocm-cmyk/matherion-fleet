# Amazon DLO3

**Amministrazione › Amazon DLO3.** Porta nel gestionale il «Portale DLO3»
(cartella FAST_RENT_PORTALE) e lo incrocia con i dati della flotta.

**Sincronizza dal portale** (cartella o ZIP, ripetibile quando vuoi): legge il
fatturato settimanale (quantità × tariffe, gasolio = km × coefficiente, MFN
178 €), i costi mensili e il TFR, le fatture Amazon (PDF letto: numero, periodo,
imponibile, righe giornaliere; stato approvata/pagata/contestata dal portale), le
pre-fatture, le scorecard (punteggio, livello, classifica) e i file Forecast e
FASR. Si aggiorna per data, settimana e numero di fattura: nessun doppione,
nessuna cancellazione, i valori già compilati non si svuotano. I PDF restano
allegati ai documenti.

Schede: **Panoramica** (fatturato, costi, margine, informazioni mancanti),
**Settimane** (calcolato contro fattura Amazon, stato fattura, pre-fattura,
scorecard), **Costi e margini**, **Fabbisogno mezzi**, **Documenti**.

**Informazioni completate dal gestionale**
- Carburante e costi della flotta del mese: dal centro di costo Amazon (movimenti
  delle carte, canoni, fatture passive, verbali) quando il portale non li ha.
  «Salva nel registro i costi completati» li rende definitivi. I valori del
  portale hanno sempre la precedenza.
- Fabbisogno: rotte previste (FASR, forecast) + scorta (Parametri riga 47, 10%)
  contro i mezzi del centro di costo Amazon; ricavo previsto.
- Quando una fattura è approvata il suo imponibile prevale sul calcolato,
  ripartito sui giorni come nel portale.

Parametri (righe 45–48): nome del centro di costo, tariffa rotta, scorta,
ultima sincronizzazione. Nei Dipendenti c'è il campo «ID autista Amazon» per
collegare gli autisti della scorecard.
