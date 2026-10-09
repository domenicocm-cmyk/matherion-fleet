# Accessi, ruoli e registro su SharePoint

Il gestionale può funzionare in tre modi, dal più semplice al più controllato.
Puoi fermarti al primo: gli altri due si aggiungono quando servono.

| | Dove stanno i dati | Chi entra |
|---|---|---|
| **1. Cartella sincronizzata** | raccolta SharePoint sincronizzata con il client OneDrive, vista come cartella | chi ha accesso alla cartella |
| **2. SharePoint diretto** | la stessa raccolta, letta via Microsoft 365 senza sincronizzazione | chi ha accesso alla raccolta |
| **3. Accesso con account** | come sopra | solo chi è nel foglio **Utenti**, con il ruolo che gli è stato dato |

---

## 1. Spostare il registro da OneDrive a SharePoint

Non serve cambiare niente nel gestionale: lui chiede una **cartella**, non sa
se dietro c'è OneDrive o SharePoint.

1. In SharePoint apri la raccolta documenti del sito (per esempio
   *Flotta → Documenti*) e premi **Sincronizza**.
2. Sposta nella raccolta il file `Registro_Noleggio_Furgoni.xlsx` con le sue
   sottocartelle `Allegati`, `Backup` e `Contratti`.
3. Nel gestionale: **Apri → Scegli la cartella di lavoro**, e indichi la
   raccolta sincronizzata.

Da qui in poi i permessi li governa SharePoint. È il punto importante: chi non
deve vedere certi dati non deve avere accesso al file, perché un'applicazione
che gira nel browser non può impedirgli di leggerlo una volta che lo apre.

Il limite di questa strada: serve il client di sincronizzazione e un browser
che sappia aprire cartelle, cioè Chrome o Edge su computer. Su iPad e iPhone
non funziona. Per quello c'è il punto 2.

## 2. Collegare il gestionale direttamente a SharePoint

Il gestionale legge e scrive la raccolta con Microsoft Graph: niente
sincronizzazione, niente scelta della cartella, e funziona anche da iPad,
iPhone e Safari. Richiede la registrazione del punto 3, perché per leggere
SharePoint bisogna prima essere entrati con il proprio account.

Quando è configurato, nella schermata iniziale compare **Apri il registro su
SharePoint**, e in testata si legge `SharePoint / Flotta / Registro…`.
Allegati, backup e contratti generati finiscono nelle stesse sottocartelle di
sempre, dentro la raccolta.

## 3. Registrare l'applicazione in Entra ID

Serve una volta sola, dal centro di amministrazione Microsoft Entra.

1. **Identità → App → Registrazioni app → Nuova registrazione**.
   Nome: `Gestionale flotta`. Account supportati: *solo questa
   organizzazione*.
2. **Aggiungi una piattaforma → Single-page application** (non «Web»: la
   differenza conta, perché solo la piattaforma SPA accetta PKCE senza
   segreti). URI di reindirizzamento:
   - `https://IL-TUO-INDIRIZZO.vercel.app/`
   - `https://IL-TUO-INDIRIZZO.vercel.app/burago` (se usi la copia di filiale)
3. **Autorizzazioni API → Microsoft Graph → Autorizzazioni delegate**:
   `User.Read`, `Files.ReadWrite.All`, `Sites.ReadWrite.All`.
   Poi **Concedi consenso amministratore**.
4. Niente certificati e nessun segreto client: un'applicazione che gira nel
   browser non può custodire un segreto, e Microsoft la rifiuterebbe.
5. Dalla pagina **Panoramica** copia *ID applicazione (client)* e
   *ID directory (tenant)*.

Poi, nel repository, copia `config.example.json` in `config.json`, incolla i
due identificativi e i dati del sito, e pubblica:

```json
{
  "organizzazione": "Fast Rent",
  "tenantId": "…",
  "clientId": "…",
  "sharepoint": { "host": "fastrent.sharepoint.com", "sito": "/sites/Flotta",
                  "raccolta": "Documenti", "cartella": "Flotta" }
}
```

Da quel momento il gestionale chiede l'accesso prima di aprire qualsiasi cosa.
Per provare la configurazione su una sola postazione, senza pubblicarla per
tutti, puoi inserirla in **Parametri → Accesso con account Microsoft**.

Se `config.json` non c'è, non cambia nulla: il gestionale si apre come prima,
senza accesso.

## 4. Dare un ruolo alle persone

In **Parametri → Utenti e accessi** si aggiunge una riga per persona:
nome, **email aziendale** (la stessa con cui accede a Microsoft 365), ruolo,
centro di costo ed eventuale disattivazione. L'elenco sta nel foglio `Utenti`
del registro, quindi si può leggere e correggere anche da Excel.

| Ruolo | Vede | Modifica |
|---|---|---|
| **Master** | tutto | tutto, compresi utenti e parametri |
| **Filiale** | solo il proprio centro di costo: mezzi, giornaliere, manutenzioni, sinistri, carte, dotazioni, dipendenti | quello che vede |
| **Officina** | mezzi, giornaliere, manutenzioni, dotazioni, su tutta la flotta | manutenzioni, giornaliere, dotazioni, allegati |
| **Amministrazione** | fatture passive e attive, prima nota, bolli, IVA, F24, margini per veicolo, più fatturazione, documenti e calendario; mezzi, contratti e anagrafiche in sola lettura | le sezioni dell'amministrazione, le proforma, gli allegati |
| **Sola lettura** | tutto il registro **tranne l'amministrazione** | niente |

**L'amministrazione è a parte.** Le otto sezioni del gruppo *Amministrazione*
(fatture passive, fatture attive, prima nota, bolli, liquidazione IVA, F24,
previsionale, margini per veicolo) non si vedono per esclusione ma **per
permesso esplicito**: solo Master e Amministrazione le hanno. Vale anche per la
**scheda economica** nella lista mezzi e per il riquadro dei margini nel
cruscotto: chi non ha il permesso non li vede comparire. Filiale, Officina e Sola lettura non le trovano nel menu e non possono
aprirle, neanche la sola lettura che vede tutto il resto. Anche le scadenze
fiscali del cruscotto seguono la stessa regola. Vedi AMMINISTRAZIONE.md.

> Il permesso **per singolo utente e per singolo modulo** — più fine del ruolo —
> è il passo successivo, ancora da fare.

Chi accede con un account che non è in elenco, o che è stato disattivato, vede
*«Questo account non è abilitato»* e nient'altro.

**Il primo accesso.** Finché il foglio `Utenti` è vuoto, chi entra è Master:
serve a configurare. Appena aggiungi la prima riga la regola diventa
vincolante, quindi **la prima riga dev'essere la tua**.

## Che cosa protegge che cosa

- **Entra ID** certifica l'identità: non si digita un nome, si entra con il
  proprio account aziendale, con l'autenticazione a più fattori se l'hai
  attivata.
- **Il foglio Utenti** decide che cosa si vede e che cosa si può cambiare.
- **SharePoint** è l'unico confine invalicabile. I ruoli vivono dentro
  l'applicazione: a chi non deve vedere un dato non va dato accesso al file.

Se una filiale non deve proprio poter leggere i dati delle altre, la strada è
tenere il suo registro in una raccolta separata, con i permessi SharePoint
che spettano solo a lei.

## Se qualcosa non va

- **«AADSTS9002326» o errore sul reindirizzamento**: la piattaforma della
  registrazione non è *Single-page application*, oppure l'URI non coincide
  con l'indirizzo da cui apri il gestionale, barra finale compresa.
- **«Accesso non più valido» dopo un giorno**: normale. Il token di
  un'applicazione a pagina singola dura 24 ore; si rientra con un clic.
- **«SharePoint non raggiungibile»**: controlla `host` e `sito` in
  `config.json` (`sito` comincia con `/sites/`), e che il consenso
  amministratore sia stato concesso.
- **Il gestionale non chiede l'accesso**: `config.json` non è raggiungibile,
  oppure mancano `tenantId` o `clientId`.
