# Pubblicare un aggiornamento — Matherion Fleet

La produzione è pubblicata con **GitHub Pages** all'indirizzo
https://fleet.matherion.com/.

## Branch

- `main`: produzione.
- `sviluppo`: modifiche e test.
- `backup-stabile-2026.10.05`: baseline stabile da non modificare.

## Procedura sicura

1. Parti sempre dalla branch `sviluppo`.
2. Aggiorna soltanto i file necessari.
3. **Non sovrascrivere `config.json`** quando aggiorni `index.html`,
   `fleet-ui.css` o altri componenti dell'interfaccia.
4. Se cambia una risorsa mantenuta in cache, aggiorna anche la versione della
   cache in `sw.js` per evitare che i browser continuino a usare file vecchi.
5. Verifica la differenza rispetto a `main` prima della pubblicazione.
6. Porta in `main` soltanto la versione già controllata.
7. Attendi il completamento del deployment GitHub Pages.

## Verifica dopo la pubblicazione

Apri https://fleet.matherion.com/ e controlla:

- versione e interfaccia corrette;
- accesso con account Microsoft;
- apertura del registro SharePoint;
- caricamento dei dati esistenti;
- menu, CSS e icone;
- assenza di errori evidenti.

Per una verifica più forte, eseguire una piccola modifica controllata su un
record di test e verificare che, dopo il salvataggio e il ricaricamento, il dato
sia ancora presente. Rimuovere poi il dato di test.

## File da trattare con particolare attenzione

### config.json

Contiene gli identificativi pubblici necessari alla SPA e il percorso
SharePoint. Non deve essere sostituito automaticamente con copie provenienti da
pacchetti o versioni precedenti.

### fleet-ui.css

È necessario per la grafica dell'interfaccia Matherion. Se manca, il gestionale
può caricarsi ma presentare menu e icone non correttamente dimensionati.

### sw.js

Gestisce la cache della PWA. Quando una nuova pubblicazione sembra non comparire
non bisogna presumere subito un errore dell'HTML: verificare anche la versione
della cache/service worker.

## Ripristino

Se una nuova versione presenta problemi, non modificare SharePoint, Entra ID,
DNS o `config.json` nel tentativo di correggere un problema puramente
applicativo.

La versione stabile 2026.10.05 è conservata nella branch
`backup-stabile-2026.10.05` e può essere usata come riferimento per riportare
il codice di produzione allo stato funzionante.

I dati della flotta sono su SharePoint e sono separati dal codice pubblicato su
GitHub Pages.
