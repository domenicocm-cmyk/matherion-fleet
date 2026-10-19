# Contratti: selezione, generazione ed esportazione massive

Dalla versione 2026.10.20 la lista **Contratti di noleggio** ha una casella su
ogni riga, la casella nell'intestazione (seleziona tutti i visibili) e, sopra la
tabella, la barra della selezione.

## La selezione

- «Seleziona i N visibili» rispetta i filtri attivi: filtra per società,
  centro di costo o stato e poi seleziona.
- «Deseleziona tutto» svuota la selezione.
- La selezione della lista è separata da quella di *Stampa contratti*.

## Genera contratti…

| Scelta | Opzioni |
|---|---|
| Tipo | contratti singoli, oppure contratto multiplo (quadro) |
| Formato | Word, PDF, oppure tutti e due |
| Un file per | ogni contratto · ogni società (locataria o noleggiante) · tutto insieme |
| Documento | data del contratto; allega la copia Word alla riga di ogni contratto |

La finestra mostra in anteprima quanti file escono e come si chiamano. Se i file
sono più d'uno escono in un archivio ZIP; nella modalità «cartella di lavoro»
vengono scritti in `Contratti/<nome>_<data>_<ora>/`.

- **Per società**: tutti i contratti della società vengono uno dopo l'altro nello
  stesso documento. Nel PDF ogni contratto riparte da pagina 1.
- Ai contratti senza numero il numero viene assegnato alla generazione (serve un
  ruolo che possa scrivere nei noleggi). Nel contratto multiplo si assegna anche
  il numero del quadro.
- Se il modello personalizzato non contiene il blocco `{#contratti}…{/contratti}`
  il Word esce comunque, ma un file per contratto, in una cartella per società.

Dalla pagina **Stampa contratti** il pulsante «Word e PDF, per società…» apre la
stessa finestra con i contratti spuntati lì.

## Esporta…

- **Elenco in Excel**: tutti i dati del contratto (società, centro di costo,
  date, canone, franchigie, deposito) più giorni del mese e importo da fatturare.
  Con «un foglio per ogni società» si ottiene anche il foglio *Riepilogo*. Le
  date sono vere date, gli importi veri numeri, i totali sono formule.
- **Elenco in CSV**: separato da punto e virgola, con la virgola decimale.
- **Documenti allegati (ZIP)**: gli allegati dei contratti selezionati, una
  cartella per contratto (e, se si vuole, per società).

## Come nasce il PDF

Il gestionale gira nel browser e non ha un convertitore Word → PDF: il PDF si
disegna direttamente dal contratto Word già compilato (paragrafi, tabelle,
grassetti, colori, bordi, sfondi, piè di pagina con il numero di pagina). La
struttura e i dati sono quelli del Word; il carattere è Helvetica invece di
Calibri. Con i modelli di base le pagine coincidono con quelle del Word.

Non vengono resi: immagini e loghi, tabelle dentro tabelle, intestazioni di
pagina, e negli elenchi puntati o numerati il numero diventa un punto. Se il
modello personalizzato li usa, il PDF li perde; il Word resta intatto, e per un
PDF identico basta «Salva come PDF» da Word.

La libreria PDF (`pdf-lib`) è dentro il file offline; nel file online si scarica
da jsDelivr alla prima generazione.
