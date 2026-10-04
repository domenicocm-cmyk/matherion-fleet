# L'app dei telefoni

Gli autisti aprono e chiudono la giornaliera dal telefono, con le foto del
mezzo. Il responsabile vede chi ha aperto e chi no. Sta all'indirizzo
**`/app`** dello stesso sito.

## Come sono collegate

Il telefono **non apre mai il registro Excel**: sarebbero quattro megabyte a
ogni salvataggio sulla rete mobile, e venti telefoni che riscrivono lo stesso
file si cancellerebbero il lavoro a vicenda.

Al suo posto, dentro la cartella di lavoro nasce una sottocartella `App`:

```
Flotta/
  Registro_Noleggio_Furgoni.xlsx
  Allegati/ …
  App/
    indice.json          il gestionale lo pubblica: mezzi, dipendenti,
                         assegnazioni, scadenze, utenti — una ventina di kB
    Posta/
      2026-10-04/
        <riferimento>.json         una giornaliera, scritta dal telefono
        <riferimento>_anteriore.jpg
```

Un file per record, scritto una volta sola: nessuna concorrenza. Il gestionale
raccoglie, riversa nel registro, sposta le foto negli allegati e svuota la
cassetta. Succede **da solo** a ogni apertura del registro, e l'indice si
ripubblica a ogni salvataggio.

Funziona identico sia con la cartella sincronizzata sia con SharePoint
diretto, perché passa dagli stessi gestori di file.

## Chi vede che cosa

Il ruolo arriva dall'account aziendale, non si sceglie.

| Chi | Come viene riconosciuto | Che cosa vede |
|---|---|---|
| **Autista** | la sua email è nell'anagrafica **Dipendenti** | solo sé stesso e il mezzo che gli è assegnato |
| **Filiale** | è nel foglio **Utenti** con ruolo Filiale | i mezzi e i dipendenti del suo centro di costo |
| **Officina** | foglio Utenti, ruolo Officina | i veicoli fermi, su tutta la flotta |
| **Master** | foglio Utenti, ruolo Master | tutto |

Un autista non va registrato due volte: basta che il campo *Email* della sua
scheda dipendente sia quello con cui accede a Microsoft 365.

## Da fare una volta sola

1. **In Entra ID**, nella stessa registrazione applicazione del gestionale,
   aggiungi l'URI di reindirizzamento della piattaforma *Single-page
   application*:
   `https://IL-TUO-INDIRIZZO.vercel.app/app/` — con la barra finale.
2. **Configurazione**: l'app legge `config.json` accanto a sé e, se non lo
   trova, quello del gestionale un livello sopra. Se hai già `config.json`
   nella radice non devi fare nulla.
3. **Sui telefoni**: aprire `.../app`, poi *Condividi → Aggiungi a Home* su
   iPhone, *menu → Installa app* su Android. Si apre a tutto schermo, con la
   sua icona.

## Che cosa succede senza rete

Tutto quello che l'autista fa — aprire, chiudere, fotografare, consultare il
mezzo — funziona a rete assente. Le operazioni vanno in una coda sul telefono
che **sopravvive alla chiusura dell'app e al riavvio**, e partono da sole al
primo segnale, con tentativi sempre più radi (10 secondi, 30, 2 minuti, 10,
30). Dopo due giorni l'app smette di ritentare da sola e lo dichiara, ma non
butta via niente: resta il pulsante *Invia ora*.

In fondo alla schermata Oggi, e in *Altro → Da inviare*, si vede sempre quanto
c'è in attesa.

## Le foto

Ridotte a 1.600 pixel di lato lungo e qualità 72 prima di partire: circa
200 kB l'una invece di quattro megabyte. Un turno completo — apertura,
chiusura e otto foto — consuma meno di due megabyte e mezzo.

Nella schermata di scatto c'è scritto *«Inquadra il mezzo, non le persone»*:
non è una gentilezza, è il confine che tiene l'app dentro l'esenzione
dell'articolo 4 dello Statuto dei lavoratori. Per la stessa ragione **l'app
non registra la posizione**, né continua né puntuale.

## Aspetto

Chiaro, scuro o come il telefono, da *Altro → Aspetto*. I colori vengono dal
marchio Matherion; ogni coppia testo-fondo è verificata sopra il rapporto di
contrasto 4,5 in entrambi i temi.

## Se qualcosa non va

- **«Non sei abilitato»**: l'email dell'account non è né fra i dipendenti né
  fra gli utenti. Si corregge nel gestionale, poi l'app si aggiorna da sola
  entro un'ora, o subito con *Altro → Aggiorna i dati della flotta*.
- **«Il gestionale non ha ancora pubblicato l'indice»**: apri il registro dal
  computer una volta, oppure premi *Parametri → App dei telefoni → Pubblica
  l'indice adesso*.
- **Le giornaliere non arrivano nel registro**: aprilo dal computer; la
  raccolta parte da sola dopo un secondo e mezzo. In alternativa
  *Parametri → App dei telefoni → Raccogli dai telefoni*.
- **AADSTS9002326 o errore di reindirizzamento**: manca l'URI `/app/` nella
  registrazione Entra ID (punto 1).
