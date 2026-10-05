# Il collegamento con la piattaforma dei turni

Turni DLO3 decide **chi lavora quando**. Il registro sa **che mezzi ci sono e
chi può guidarli**. Finché le due cose stanno separate, qualcuno ricopia a
mano: il piano della settimana da una parte, le giornaliere dall'altra.

Il collegamento elimina la ricopiatura in entrambi i versi, senza che una
piattaforma debba entrare nell'altra.

```
          Turni/flotta.json  ──────────▶   mezzi, autisti, assegnazioni
   REGISTRO                                           PIATTAFORMA TURNI
          Turni/turni.json   ◀──────────   il piano dei turni
```

Lo scambio passa dalla sottocartella `Turni` della cartella di lavoro,
esattamente come fa l'app dei telefoni con la sottocartella `App`. Funziona
identico sulla cartella sincronizzata e su SharePoint diretto.

## Che cosa diventa un turno

Un turno diventa una **giornaliera aperta**: data, autista, turno, orario
previsto e mezzo. L'autista poi la chiude dal telefono con km, carburante,
stato del mezzo e foto.

Il piano è una previsione, il telefono è il consuntivo. Perciò: **una
giornaliera già chiusa non si fa riscrivere gli orari dal piano**. Se il turno
cambia, cambia tutto il resto; gli orari reali restano quelli dell'autista.

## `Turni/flotta.json` — lo scrive il registro

Si ripubblica da solo ogni volta che il registro pubblica l'indice per i
telefoni, cioè a ogni salvataggio. A mano: *Parametri → Piattaforma dei turni
→ Pubblica la flotta per i turni*.

```json
{
  "generato": "2026-10-05T09:12:44.000Z",
  "versione": 1,
  "registro": "Registro_Noleggio_Furgoni.xlsx",
  "cdc": ["Amazon Burago – Fast Rent S.r.l."],
  "mezzi": [{
    "targa": "GA101AA", "marca": "Fiat", "modello": "Ducato",
    "tipologia": "Furgone", "centroCosto": "Amazon Burago – Fast Rent S.r.l.",
    "stato": "Disponibile", "disponibile": true
  }],
  "autisti": [{
    "codice": "DP-0002", "cognome": "Rossi", "nome": "Marco",
    "email": "marco.rossi@fastrent.it", "matricola": "M001",
    "mansione": "Autista", "centroCosto": "Amazon Burago – Fast Rent S.r.l.",
    "attivo": true,
    "patenteScadenza": "2029-04-18", "cqcScadenza": "2027-11-30"
  }],
  "assegnazioni": [{
    "targa": "GA101AA", "autista": "DP-0002",
    "dal": "2026-01-07", "al": ""
  }]
}
```

| Campo | Serve a |
|---|---|
| `mezzi[].targa` | l'unico identificatore del mezzo: è quello che il registro riconosce al rientro |
| `mezzi[].disponibile` | `false` se il mezzo è a noleggio, in officina o dismesso: non va messo in turno |
| `autisti[].codice` | la chiave del registro; se la piattaforma la conserva, l'abbinamento è esatto e non passa più dai nomi |
| `autisti[].attivo` | `false` per sospesi; i cessati non compaiono affatto |
| `patenteScadenza`, `cqcScadenza` | per non assegnare un turno a chi ha la patente scaduta il giorno dopo |
| `assegnazioni` | il mezzo già affidato a quell'autista: è la proposta di default |

I mezzi dismessi e gli autisti cessati non ci sono. Il file pesa una ventina
di kB.

## `Turni/turni.json` — lo legge il registro

Un file per volta o uno per settimana, il nome è libero: il registro legge
tutti i `.json`, `.csv`, `.tsv` e `.xlsx` che trova nella cartella `Turni`
(salta `flotta.json`). Da *Parametri → Piattaforma dei turni → Leggi dalla
cartella Turni*.

La forma che il registro preferisce — un array, o un oggetto con la chiave
`turni` o `shifts`:

```json
[{
  "id": "sh-001",
  "data": "2026-10-06",
  "autista": "DP-0002",
  "email": "marco.rossi@fastrent.it",
  "matricola": "M001",
  "targa": "GA101AA",
  "turno": "Mattino",
  "oraInizio": "06:45",
  "oraFine": "15:15",
  "presenza": "Presente",
  "sede": "DLO3 Burago",
  "note": "doppio giro"
}]
```

| Campo | Obbligatorio | Che cosa accetta |
|---|---|---|
| `id` | consigliato | qualunque stringa stabile. È la chiave anti-doppione: se cambia il turno ma resta l'`id`, la giornaliera viene **aggiornata**, non duplicata. Senza `id` la chiave diventa data + autista |
| `data` | **sì** | `2026-10-06`, `06/10/2026`, `6-10-26`, un datetime ISO, o il numero seriale di Excel. Senza data la riga non entra |
| autista | **sì** | basta **uno** fra `email`, `matricola`, `autista` (nome e cognome in qualunque ordine) o `cognome` + `nome`. Si cerca in quest'ordine: email, matricola, nome completo, cognome se non è ambiguo |
| `targa` | no | `GA101AA`, `GA 101 AA`, `ga-101-aa`, e anche dentro un testo: `Van 7 – GA101AA`. Se il mezzo non è in anagrafica la giornaliera entra **senza mezzo** e il fatto viene segnalato |
| `turno` | no | `Mattino`, `Pomeriggio`, `Notte`, `Giornata`, e gli equivalenti inglesi `morning`/`afternoon`/`night`/`full`, o `wave 1`/`wave 2`. Se manca si deduce dall'ora di inizio: prima di mezzogiorno mattino, prima delle 18 pomeriggio, dopo notte |
| `oraInizio`, `oraFine` | no | `06:45`, `6.45`, `0645`, `7` (diventa 07:00), un datetime, o la frazione di giornata di Excel |
| `presenza` | no | `Presente` di default. `Ferie`, `Permesso`, `Malattia`, `Infortunio`, `Riposo`, `Formazione`, `Assenza non giustificata`, e i corrispondenti inglesi (`holiday`, `sick`, `day off`, `training`, `no show`…). Un'assenza entra come giornaliera senza mezzo |
| `sede` | no | il nome della località come sta in anagrafica, anche solo contenuto nel testo |
| `note` | no | finisce nelle note della giornaliera, precedute da «Dai turni:» |

### Se la piattaforma non può scrivere nella cartella

Va bene anche il suo **export**: *Parametri → Piattaforma dei turni → Importa
i turni da un file*, e si dà in pasto il file così com'è — `.json`, `.csv`,
`.tsv`, `.xlsx`.

Le colonne vengono riconosciute da sole, in italiano e in inglese, e non
devono essere in un ordine preciso. Alcuni dei nomi accettati:

| Campo | Intestazioni riconosciute |
|---|---|
| data | Data, Giorno, Giornata, Date, Day, Shift date |
| autista | Autista, Dipendente, Nominativo, Operatore, Driver, Driver name, Employee |
| email | Email, Mail, Driver email, User email |
| matricola | Matricola, Badge, Employee ID, Transporter ID |
| targa | Targa, Mezzo, Veicolo, Van, Plate, License plate |
| turno | Turno, Fascia, Blocco, Shift, Wave, Slot |
| orari | Ora inizio, Dalle, Entrata, Start time, Checkin — e i corrispondenti di fine |
| presenza | Presenza, Stato, Causale, Motivo, Status, Attendance |
| sede | Sede, Stazione, Deposito, Station, Hub |

Prima di scrivere qualunque cosa il registro mostra **che colonna ha
riconosciuto per quale campo**, quanti turni ha capito e — soprattutto — quali
righe non è riuscito ad abbinare e perché. Da lì si conferma o si annulla.
Quello che non riesce ad abbinare non lo inventa.

### Lettura diretta dalla piattaforma

Se la piattaforma espone i turni con una chiamata autenticata, in
`config.json` accanto a `clientId` e `tenantId`:

```json
"turni": {
  "base": "https://turni-dlo3.vercel.app",
  "percorso": "/api/shifts",
  "token": "…",
  "giorni": 14
}
```

Il registro chiama `GET {base}{percorso}?from=oggi&to=oggi+giorni` con
`Authorization: Bearer {token}` e si aspetta un array, o un oggetto con la
chiave `turni`, `shifts`, `data` o `items`. Compare allora un pulsante
*Scarica dalla piattaforma*. Senza quella voce il pulsante non esiste: il
token sta nella configurazione del sito, come le credenziali di Microsoft, e
**non** dentro il registro.

Perché la chiamata funzioni dal browser, la piattaforma deve rispondere con
`Access-Control-Allow-Origin` sull'indirizzo del gestionale.

## Che cosa serve alla piattaforma, in pratica

Tre cose, in ordine di utilità:

1. **leggere `Turni/flotta.json`** e usare `targa` e `autisti[].codice` invece
   del testo libero. Da sola elimina quasi tutti gli abbinamenti mancati;
2. **scrivere `Turni/turni.json`** quando il piano viene pubblicato o cambia.
   Un file per settimana va benissimo;
3. **conservare l'`id` del turno**. È quello che permette di correggere un
   turno senza creare un doppione nel registro.

Finché la 2 non c'è, l'export a mano fa lo stesso lavoro con un clic in più.

## Se qualcosa non va

- **«Nella cartella Turni non c'è nessun piano da leggere»**: il file c'è ma
  l'estensione non è fra `.json`, `.csv`, `.tsv`, `.xlsx`, oppure si chiama
  `flotta.json` (quello lo scrive il registro e viene saltato).
- **«autista non trovato in anagrafica dipendenti»**: nella scheda del
  dipendente manca l'email o la matricola che usa la piattaforma, o il nome è
  scritto diversamente. Si corregge in anagrafica, non nel file.
- **«il mezzo … non è in anagrafica»**: targa scritta male, o mezzo non ancora
  inserito o già archiviato. La giornaliera entra comunque, senza mezzo.
- **«non ho trovato la colonna data»**: l'export non ha una colonna di data
  riconoscibile. Basta rinominarla `Data` e riprovare.
- **i turni entrano ma doppi**: l'export non porta un `id` stabile e le date o
  gli autisti cambiano fra una passata e l'altra. Con l'`id` il problema
  sparisce.
