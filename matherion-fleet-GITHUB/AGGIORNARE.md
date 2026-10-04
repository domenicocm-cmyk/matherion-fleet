# Pubblicare un aggiornamento

Una volta collegato il repository a Vercel, mettere in linea una versione nuova
è una cosa da due minuti.

## La strada normale: ti arrivano i file già pronti

Ti vengono consegnati `index.html` e `burago.html` già costruiti.

1. Copiali in questa cartella, sovrascrivendo quelli che ci sono.
2. Apri `sw.js` e porta la riga `const VER` alla versione nuova, per esempio
   `const VER = 'flotta-2026.11.14';`. È quella riga che fa buttare via la copia
   vecchia tenuta nei browser: se non la cambi, chi ha l'app già aperta continua
   a vedere la versione precedente.
3. Aggiungi una riga a `CHANGELOG.md`.
4. Poi:

```bash
git add -A
git commit -m "gestionale 2026.11.14"
git push
```

Vercel se ne accorge da solo e pubblica in meno di un minuto.

## La strada automatica: un comando solo

Se hai `python3` (su macOS di solito c'è; altrimenti si installa con
`xcode-select --install`), ti basta il file centrale — quello che metteresti su
OneDrive — e il resto lo fa lo script:

```bash
python3 strumenti/aggiorna.py ~/Downloads/Gestionale_Flotta_Noleggi.html
git add -A && git commit -m "gestionale 2026.11.14" && git push
```

Lo script ricava la versione web per la sede centrale, rigenera la copia bloccata
sulla filiale Amazon Burago, allinea la versione in `sw.js` e aggiorna il
`CHANGELOG.md`. Se il file sorgente dovesse cambiare forma lo script si ferma e
te lo dice, senza scrivere niente a metà.

### Aggiungere un'altra filiale

In `strumenti/aggiorna.py` c'è la riga `FILIALE = "Amazon Burago"`. Per una
seconda filiale duplica il blocco che genera `burago.html`, cambia nome del
centro di costo e del file (es. `cinisello.html`), e aggiungi un manifest
`manifest-cinisello.webmanifest` sul modello di quello esistente. Oppure chiedi
il file già pronto.

## Verifica dopo la pubblicazione

1. Apri l'indirizzo in una finestra anonima: in basso a sinistra, sotto il logo,
   deve comparire la versione nuova.
2. Su una postazione che ha l'app installata deve apparire l'avviso
   *«C'è una versione nuova»*. Se non appare entro mezz'ora, chiudi e riapri
   l'app: significa che `const VER` in `sw.js` non è stata cambiata.
3. Apri `/burago` e controlla che il menu si fermi a nove voci e che sotto il
   logo ci sia scritto *Filiale Amazon Burago*.

## Tornare indietro

Su Vercel, *Deployments* → scegli quello di prima → *Promote to Production*.
Ci vogliono pochi secondi e nessun dato è coinvolto: il registro `.xlsx` sta
nella cartella OneDrive e non viene toccato da nessuna pubblicazione.
