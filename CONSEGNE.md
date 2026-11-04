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

## Apertura automatica alla creazione del contratto (2026.10.44)
Quando si salva un nuovo contratto di noleggio, singolo o multiplo (contratto quadro), si apre da solo il verbale «Stato del veicolo alla consegna» per ogni mezzo, uno alla volta («1 di 5»): contratto, cliente, data di inizio, km inclusi e costo km sono già compilati; restano da inserire km al ritiro, carburante e le foto per lato. «Salta questo mezzo» passa al successivo (il verbale si può sempre creare dopo da Flotta → Consegne e riconsegne). I mezzi del contratto che hanno già un verbale vengono saltati. I rinnovi massivi non aprono i verbali (il mezzo è già dal cliente).

## Riconsegna: km e chiusura con proforma (2026.10.45)
- **Correzione km**: la finestra «Registra riconsegna» mostra e consente di correggere i km al ritiro (uscita), i km alla restituzione (rientro), i km inclusi al mese e il costo del km eccedente. Se nel verbale mancavano, vengono ripresi dal contratto collegato (per numero, o per targa e periodo), così l'eccedenza si calcola sempre. I valori restano salvati nel verbale.
- **Chiusura**: subito dopo la riconsegna si apre «Chiusura della riconsegna» con gli addebiti calcolati (km eccedenti e danni nuovi stimati). Tre scelte: *Genera la proforma* (bozza intestata al cliente del contratto, con eventuale importo extra), *Archivia con addebito zero*, *Decido dopo*. Per i mezzi affidati ai dipendenti c'è anche «Addebito al dipendente».
- Si riapre in qualsiasi momento da «Chiusura e proforma» (scheda e elenco). L'elenco segnala le riconsegne con chiusura da definire; il verbale stampato riporta proforma o «addebito 0,00 €».
