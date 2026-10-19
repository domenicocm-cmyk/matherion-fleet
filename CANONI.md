# Canoni collegati per targa

Dalla versione 2026.10.23. Il canone compare in più sezioni; il legame è la **targa**.

| Dove | Che cos'è |
|---|---|
| Contratto di noleggio (cliente) | il canone del noleggio, un ricavo |
| Scheda del mezzo › «Canone listino mensile» | il canone proposto per un nuovo noleggio |
| Contratto di leasing o noleggio (fornitore) | un costo, non un ricavo |

Quando un importo cambia, gli altri si allineano da soli:

- **contratto → mezzo**: il canone listino segue il canone del contratto in corso se era vuoto o se coincideva con quello precedente del contratto;
- **mezzo → contratti**: i noleggi non ancora scaduti che avevano il vecchio listino passano al nuovo;
- **mezzo senza canone listino**: lo prende dal suo contratto di noleggio (in corso, altrimenti il prossimo, altrimenti l'ultimo);
- gli importi **voluti diversi** (listino ≠ contratto) non si toccano;
- i noleggi scaduti e le proforma già emesse non cambiano.

Nella scheda del mezzo, sotto «Calcoli», si leggono sempre dal vivo il canone del noleggio (con cliente e numero contratto) e il costo del contratto fornitore per la stessa targa. Ogni allineamento resta nello **storico del mezzo** con la nota del contratto da cui arriva.

Per sistemare i dati già presenti: Mezzi › selezionare › **Allinea canoni ai contratti**. L'allineamento automatico scatta anche al primo salvataggio.

## Grafica

Dalla 2026.10.23 tutte le pagine (sede centrale, Burago, copia per SharePoint) usano il tema «Studio» del file `index.html` consegnato: palette blu petrolio e turchese, icone nel menu, schede KPI, illustrazione della flotta, temi chiaro/scuro. Il foglio di stile è in `app/studio.css`.
