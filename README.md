# Matherion Fleet

Gestionale web Matherion per la gestione della flotta.

## Ambiente attuale

- **Produzione:** branch `main`
- **Hosting:** GitHub Pages
- **URL produzione:** https://fleet.matherion.com/
- **Sviluppo:** branch `sviluppo`
- **Backup stabile:** branch `backup-stabile-2026.10.05`
- **Versione baseline:** 2026.10.05
- **Autenticazione:** Microsoft Entra ID
- **Dati operativi:** SharePoint / Microsoft 365

GitHub ospita il codice dell'applicazione. I dati operativi della flotta non sono
contenuti nel repository: vengono letti e scritti su SharePoint dopo
l'autenticazione Microsoft.

## File principali

| Percorso | Funzione |
|---|---|
| `index.html` | gestionale principale |
| `fleet-ui.css` | interfaccia grafica Matherion |
| `config.json` | configurazione Entra ID e SharePoint |
| `sw.js` | service worker e gestione cache |
| `manifest.webmanifest` | manifest PWA principale |
| `icons/` | icone dell'app |
| `burago.html` | versione dedicata alla filiale Amazon Burago |
| `app/` | applicazione mobile separata per autisti/responsabili |
| `ACCESSI.md` | documentazione accessi e ruoli |
| `AGGIORNARE.md` | procedura sicura per gli aggiornamenti |

## Regole di sicurezza

1. Non lavorare direttamente su `main` per modifiche da provare.
2. Preparare e verificare le modifiche su `sviluppo`.
3. Non sostituire `config.json` durante un aggiornamento dell'interfaccia.
4. Non modificare Tenant ID, Client ID, percorso SharePoint, DNS o Redirect URI
   se l'aggiornamento riguarda soltanto grafica o funzioni del gestionale.
5. Prima di portare una nuova versione in produzione verificare accesso
   Microsoft, apertura del registro SharePoint e corretto caricamento dei dati.
6. La branch `backup-stabile-2026.10.05` è un punto di ripristino e non deve
   essere usata per lo sviluppo.

## Flusso consigliato

`sviluppo` → test → confronto delle modifiche → `main` → GitHub Pages →
`fleet.matherion.com`.

In caso di problemi in produzione, la baseline 2026.10.05 rimane conservata
nella branch `backup-stabile-2026.10.05`.

## Nota su Vercel

`vercel.json` è un residuo della precedente configurazione di hosting. Al
momento non è utilizzato da GitHub Pages e viene conservato temporaneamente
solo come riferimento storico.
