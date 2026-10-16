# I modelli dei contratti

I contratti di noleggio si generano da un modello Word. Il gestionale usa,
nell'ordine:

1. **un modello caricato a mano** dalla pagina *Stampa* (vale solo per quella
   sessione: serve per una prova);
2. **il modello nella cartella del registro** — è quello da tenere su SharePoint;
3. **il modello predefinito del programma**, solo se in cartella non c'è niente.

## Dove mettere i file

Accanto al registro, con questi nomi:

- `Modello_Contratto_Noleggio_Furgoni.docx` — contratto singolo
- `Modello_Contratto_Quadro_Multiplo.docx` — contratto quadro con più veicoli

Cartelle controllate, nell'ordine: quella indicata in **Parametri → Cartella dei
modelli dei contratti** (se compilata), poi `Modelli`, `Modelli contratti`,
`Contratti/Modelli`, `Contratti` e infine la cartella principale. Se il nome è
diverso va bene lo stesso, purché cominci per «Modello», contenga «noleggio» o
«furgoni» (singolo) oppure «quadro» o «multiplo» (quadro), e finisca in `.docx`.

La cartella è quella in cui il gestionale lavora: con il collegamento diretto a
SharePoint, la cartella indicata in `config.json`; con la cartella sincronizzata,
quella scelta all'apertura.

## Come si vede quale modello è in uso

Nella pagina *Stampa*, sotto la scelta del modello, c'è la riga «Modello in
uso». Al momento di generare un contratto compare anche l'avviso «Uso il modello
della cartella: …».

## Quando si corregge il modello

Il file si rilegge a **ogni generazione**: se lo modifichi su SharePoint, il
contratto successivo esce già con la correzione. I contratti già generati non
cambiano.

## Se il modello ha un errore

I segnaposto tra graffe (`{targa}`, `{#contratti}` … `{/contratti}`) devono
essere scritti interi e le coppie apri/chiudi devono corrispondere. Un modello
con un errore non blocca la stampa: il gestionale lo segnala con la causa e usa
per quella volta il modello predefinito. I segnaposto sconosciuti restano
«________» nel contratto.

> Il modello predefinito del programma può essere diverso da quello su SharePoint
> (articoli aggiunti o modificati): per questo i contratti devono uscire dalla
> cartella, non dal programma.
