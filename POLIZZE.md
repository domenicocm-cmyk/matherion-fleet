# Importazione delle polizze assicurative

**Flotta › Mezzi › Importa polizze.** Si sceglie il PDF della compagnia (anche
un unico file con le polizze di tutta la flotta, come quello Unipol: per ogni
mezzo certificato con carta verde + quietanza, con i versi bianchi in mezzo) o
foto/scansioni.

1. **Lettura.** Testo del PDF se c'è, altrimenti lettura ottica (OCR, la prima
   volta serve internet per scaricare il motore). Le pagine bianche si saltano.
2. **Riconoscimento** per pagina: targa, n. polizza, n. applicazione, decorrenza,
   scadenza, periodo pagato, data pagamento, premio netto/imposte/SSN/lordo
   (controllati con la somma), premio annuo, franchigia, compagnia, proprietario.
3. **Raggruppamento** per targa (certificato + quietanza dello stesso mezzo).
   Le targhe lette male si correggono con quelle in anagrafica (0/O, 8/B…);
   se è dubbia viene segnalata. Il numero di polizza si confronta fra tutte le
   pagine: vince la lettura più frequente.
4. **Anteprima** modificabile (targa, polizza, scadenza). Esiti: *Nuova*,
   *Aggiorna*, *Già presente* (stessa scadenza già allegata), *Più vecchia*
   (non tocca nulla), *Da correggere* (targa non in anagrafica).
5. **Conferma.** Aggiorna la scheda del mezzo (compagnia, polizza, scadenza RCA,
   e i nuovi campi applicazione, decorrenza, premio annuo, ultima rata) e allega
   una copia **con le sole pagine di quel mezzo** (tipo «Polizza assicurativa»,
   con la scadenza). La modifica entra nello storico del mezzo.

Limiti: l'OCR può sbagliare una cifra; per questo l'anteprima va controllata
(il premio annuo letto in modo incoerente con la rata non viene importato).
Il premio non entra ancora nei costi per centro di costo.
