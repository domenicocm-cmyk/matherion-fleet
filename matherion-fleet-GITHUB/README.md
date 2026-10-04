# Gestionale flotta — app web su Vercel

Questo è il gestionale che già usi, pronto da pubblicare come **app installabile**.
Non cambia niente nel modo di lavorare: i dati restano nel registro
`Registro_Noleggio_Furgoni.xlsx` della cartella OneDrive. Vercel ospita solo
l'applicazione, non i dati.

## Cosa c'è dentro

| File | A cosa serve |
|---|---|
| `index.html` | il gestionale completo (sede centrale) |
| `burago.html` | la copia bloccata sulla filiale Amazon Burago → indirizzo `/burago` |
| `manifest.webmanifest`, `manifest-burago.webmanifest` | nome, icona e colori dell'app installata |
| `sw.js` | fa funzionare l'app anche senza connessione e avvisa quando pubblichi un aggiornamento |
| `icons/` | icone per desktop, Android e iPhone |
| `config.json` | accesso con account Microsoft e collegamento a SharePoint (facoltativo: senza, il gestionale si apre come prima) |
| `ACCESSI.md` | come registrare l'applicazione in Entra ID, dare i ruoli e spostare il registro su SharePoint |
| `app/` | l'app dei telefoni per autisti e responsabili → indirizzo `/app` |
| `APP.md` | come funziona l'app, chi vede che cosa, che cosa fare una volta sola |
| `vercel.json` | indirizzi puliti, cache e intestazioni di sicurezza |
| `robots.txt` | tiene il sito fuori dai motori di ricerca |

## Pubblicare — tre strade

### 1. Trascinare la cartella (la più veloce)

1. Vai su **vercel.com/new**, accedi.
2. In fondo scegli **Deploy a folder / Upload** e trascina questa cartella
   (scompattata, non lo .zip).
3. Dopo un minuto hai un indirizzo tipo `https://flotta-matherion.vercel.app`.

### 2. Da riga di comando

```bash
npm i -g vercel
cd questa-cartella
vercel          # anteprima
vercel --prod   # pubblicazione definitiva
```

### 3. Da GitHub — **consigliata**

Questa cartella è già un repository git con il primo commit fatto. Devi solo
collegarla a GitHub e poi a Vercel.

```bash
cd questa-cartella
git remote add origin https://github.com/<tuo-utente>/flotta-matherion.git
git branch -M main
git push -u origin main
```

Il repository su GitHub crealo **privato** (New repository → Private), senza
README né .gitignore: ci sono già.

Poi su Vercel: **Add New → Project → Import Git Repository**, scegli il
repository e conferma. Framework Preset **Other**, Build Command e Output
Directory lasciali vuoti.

Da lì in poi ogni `git push` pubblica la versione nuova: vedi `AGGIORNARE.md`.

## Dopo la pubblicazione

**Proteggi l'indirizzo.** Il sito non contiene dati, ma è pubblico. Su Vercel:
*Project → Settings → Deployment Protection → Vercel Authentication* lo chiude
a chi non è nel tuo team (serve un piano Pro). In alternativa usa un nome di
progetto non indovinabile: `robots.txt` e l'intestazione `noindex` tengono già
fuori i motori di ricerca.

**Installa l'app.** Apri l'indirizzo in Chrome o Edge: nella barra degli
indirizzi compare l'icona per installare. Su Android, menu → *Installa app*.
Su iPhone, Condividi → *Aggiungi a Home*. Da installata si apre a tutto schermo,
con la sua icona, e funziona anche senza connessione.

La filiale installa `/burago`: è un'app a sé, con la sua icona e il suo nome.

**La prima volta ogni postazione deve ridare l'accesso alla cartella.** Il
browser considera l'indirizzo web un posto diverso dal file aperto in locale,
quindi al primo avvio si rifà «Apri dalla cartella» e si sceglie la cartella
Flotta. Da lì in poi se la ricorda.

> Se su qualche postazione avevi allegati «salvati nel browser» invece che nella
> cartella, **esportali prima** da Parametri → *Esporta allegati (.zip)*: non
> seguono il cambio di indirizzo. Se lavori con la cartella di lavoro — il caso
> normale — gli allegati sono già nella sottocartella `Allegati` e non si tocca
> niente.

**Browser.** La scelta della cartella di lavoro funziona in **Chrome ed Edge su
computer**. Su iPhone e iPad, e su Firefox, resta la modalità a scaricamento:
l'app si apre, ma il registro va caricato e riscaricato a mano. Per il lavoro
quotidiano in filiale usa Chrome o Edge.

## Su cellulare e tablet

Aperto da un telefono o da un tablet, il gestionale si presenta come
un'applicazione: barra delle sezioni in basso, schermata **Oggi** con il lavoro
della giornata, elenchi a schede invece che a tabelle, schede dei record a
tutto schermo. Sul computer resta la vista estesa con il menu laterale.

La scelta è automatica e si può forzare da *Parametri → Aspetto*
(Automatico / Applicazione / Computer).

Installandola — su iPhone *Condividi → Aggiungi a Home*, su Android
*menu → Installa app*, su computer l'icona nella barra degli indirizzi — si
apre a tutto schermo con la sua icona, senza barra del browser.

## L'app dei telefoni

All'indirizzo `/app` c'è un'applicazione a sé, per chi lavora fuori: apre e
chiude la giornaliera con le foto guidate del mezzo, segnala i danni, mostra
scadenze e documenti. Pesa 240 kB, funziona senza rete e deposita quello che
registra in una cartella su SharePoint, che il gestionale raccoglie da solo.

Non apre mai il registro Excel: i dettagli sono in **[APP.md](APP.md)**.

## Accessi e SharePoint

Di serie il gestionale si apre senza accesso: chi lo apre ha pieni poteri, e i
dati stanno nella cartella di lavoro. Per chiedere l'accesso con l'account
aziendale, dare ruoli diversi alle persone e leggere il registro direttamente
da SharePoint — anche da iPad e iPhone — si parte da **[ACCESSI.md](ACCESSI.md)**.

In breve: una registrazione applicazione in Entra ID, i suoi due
identificativi in `config.json`, e una riga per persona in
*Parametri → Utenti e accessi*.

## Aggiornamenti

Quando pubblichi una versione nuova, chi ha l'app aperta vede un avviso
*«C'è una versione nuova»* con il pulsante per ricaricare. Chi la riapre parte
già aggiornato. Se cambi `index.html` o `burago.html` ricordati di alzare la
riga `const VER` in `sw.js`: è quella che fa pulire la cache vecchia.

## Da sapere

- **I dati non passano da Vercel.** Il registro e gli allegati restano nella
  cartella OneDrive, sul computer. Il sito serve solo l'applicazione.
- Il file pesa circa 4 MB perché si porta dentro tutte le librerie: è quello che
  gli permette di funzionare offline.
- Pubblicare qui non sostituisce il file su OneDrive: puoi tenere entrambi.

## Icone

Le icone in `icons/` sono già pronte: blu per la sede centrale, oro per la
filiale, così sul telefono le due app installate non si confondono. Ci sono
tutte le misure che servono a Windows, Android e iPhone, più le versioni
"maskable" che Android ritaglia a cerchio.

Si rigenerano solo se cambia il marchio:

```bash
pip install cairosvg
python3 strumenti/icone.py
```

Per aggiungere una filiale basta una riga in `TEMI` dentro `strumenti/icone.py`
con i due colori del fondo e quello del marchio.
