# Consegne e riconsegne (dalla 2026.10.42)

Menu **Flotta → Consegne e riconsegne**. Per ogni mezzo dato a noleggio a un cliente o
affidato a un utilizzatore:

1. **Nuova consegna**: tipo, targa, contratto (o utilizzatore), data, ora, km, carburante,
   chi ritira. Per i noleggi km inclusi al mese e costo del km extra arrivano dal contratto
   (modificabili). Per gli utilizzatori si crea anche l'assegnazione del mezzo.
2. **Foto e danni**: otto lati (anteriore, posteriore, laterale sinistro e destro, tetto,
   interno e cruscotto, vano di carico, contachilometri e carburante). Su telefono il pulsante
   apre la fotocamera. Le foto sono ridimensionate (max 1800 px) e archiviate come allegati
   del verbale. Per ogni lato: **Confronta lo stesso lato** (affiancate e con cursore di
   sovrapposizione) e **Registra danno** (già presente al ritiro oppure nuovo alla
   riconsegna, tipo, gravità, stima).
3. **Registra riconsegna**: data, ora, km, carburante, note. Mostra subito giorni, km
   percorsi, km inclusi, eccedenza e importo.
4. **Stampa verbale**: dati, km, danni e foto, con spazio per le firme (salva PDF dal browser).

## Calcolo dell'eccedenza
- Giorni = dal momento del ritiro al momento della restituzione (data e ora).
- Km inclusi nel periodo = km al mese ÷ (365/12) × giorni.
- Km eccedenti = km percorsi − km inclusi − tolleranza (parametro `cnsTolleranza`, 0 km).
- Importo = km eccedenti × costo km extra. Km del mezzo e assegnazione si aggiornano da soli.
