# Centri di costo: contratti, mezzi e costi dell'appalto

Dalla versione 2026.10.21 (carte, movimenti e storico dalla 2026.10.22).

## Dal contratto al menu «Centri di costo»

Quando salvi un contratto di noleggio (singolo o multiplo) con un centro di costo:

- se il centro **non esiste** nel menu Centri di costo, viene creato per la società locataria (e a quella società si attiva «Gestisce centri di costo»);
- il **mezzo** del contratto viene abbinato al centro. Un mezzo che ha già il centro di un'altra società non si tocca; un contratto futuro non toglie al mezzo il centro che ha adesso; un noleggio finito non sposta nulla;
- nel menu i **mezzi** di un centro sono quelli abbinati più quelli con un noleggio in corso o futuro che lo indica.

Nel modulo del contratto:

- **+ Nuovo centro di costo** crea il centro senza lasciare il contratto e lo seleziona;
- scegliendo la targa, il centro del mezzo (se è della società locataria) si propone da solo.

**Allinea mezzi ai contratti** (in Centri di costo › Elenco) rifà lo stesso lavoro su tutti i contratti già inseriti.

## Costi per mese

Centri di costo › **Costi per mese**.

- Si sceglie la società (all'apertura **Fast Rent**), l'anno e, se serve, una voce di costo.
- La matrice mostra, per ogni centro di costo, i dodici mesi e il totale; sotto, lo stesso per voce di costo, con la fonte.
- Clic su un centro (o «Costi dell'appalto» sulla riga dell'elenco): voci per mese, mezzi e collegamento alla scheda economica di ogni mezzo.
- **Esporta Excel**: fogli «Costi per mese», «Per voce», «Per mezzo» e «Note».

### Come si assegna un costo a un centro

Si usano le stesse fonti della scheda economica del mezzo: fatture passive, carburante e pedaggi, bolli, verbali a nostro carico, note spese; più, se accese, canoni di contratto, manutenzioni a consuntivo e franchigie.

1. I giorni in cui il mezzo ha un noleggio vanno al centro di **quel contratto** (o del mezzo, se il contratto non ne indica uno).
2. I giorni senza noleggio vanno al centro del mezzo, se è della società che si guarda; altrimenti restano al proprietario, sotto «Senza centro di costo».
3. Un costo senza targa ma con un centro (fattura, verbale…) va diretto a quel centro.

Le fonti del registro operativo (canoni dei contratti di leasing e noleggio, manutenzioni, franchigie) sono **spente** di partenza, come nella scheda economica: se le fatture del fornitore sono registrate, conterebbero lo stesso costo due volte. Si accendono in fondo alla pagina.

Importi senza IVA. I costi di una società non si sommano a quelli di un'altra.

## Telepass e carte carburante

- **Movimenti**: colonna e filtro «Centro di costo».
- **Riepilogo per targa**: colonna «Centro di costo»; menu «Riepilogo per» per raggruppare per centro; clic su un centro per vederne le targhe.

## Carte, Telepass e movimenti sul centro di costo (2026.10.22)

La carta carburante o il Telepass è abbinato dal gestore a una targa, ma nella pratica si usa su più mezzi e su più filiali. Per questo i costi seguono il **centro di costo**, non il contratto del mezzo.

- **Carta o dispositivo**: nuovo campo «Centro di costo della carta». Si imposta dalla scheda o in blocco (Telepass e carte › Dispositivi e carte › selezionare › «Assegna centro di costo…»), con la possibilità di applicarlo anche ai movimenti già importati da una certa data.
- **Movimento**: all'importazione (o alla creazione) il movimento riceve il centro della carta; se la carta non ne ha uno, quello del mezzo alla data del movimento. Si cambia sul singolo movimento o in blocco («Assegna centro di costo…»). Un centro scritto a mano non viene mai sovrascritto.
- **«Assegna i centri di costo mancanti»** scrive sui movimenti già presenti che non hanno un centro quello della carta o del mezzo. In elenco, un centro non ancora scritto compare come «dalla carta / dal mezzo · non fissato».
- **Costi**: «Costi per mese» e il riepilogo di Telepass e carte contano ogni movimento sul suo centro, anche se il mezzo ha un contratto con un altro centro. Un movimento senza alcun centro segue la targa come prima.
- **Ricerca**: nei Movimenti si cerca anche per **numero della carta o del Telepass** (con o senza trattini e spazi) e per centro di costo.

## Storico del mezzo

Ogni modifica a un mezzo (centro di costo, stato operativo e ogni altro dato), ai suoi noleggi (cliente, date, centro, canone…) e alle sue assegnazioni viene registrata in un foglio **Storico mezzi** del registro, con data e ora, valore prima e dopo, e chi l'ha fatta. Gli abbinamenti automatici dai contratti lasciano la nota «abbinato dal contratto…».

Si vede nella **scheda economica del mezzo** › «Storico del mezzo», con i filtri Tutto · Centro di costo · Disponibilità e stato · Noleggi e assegnazioni.

Limite: lo storico parte dal giorno in cui si usa questa versione; le modifiche precedenti non sono ricostruibili.
