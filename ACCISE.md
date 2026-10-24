# Rimborso accise sul gasolio commerciale

**Amministrazione › Rimborso accise gasolio.** Per i veicoli di massa
complessiva da 7,5 t (75 quintali) in su, Euro 5 o superiore (art. 24-ter
D.Lgs. 504/1995).

- **Calcolo del trimestre**: sceglie anno e trimestre, prende i rifornimenti
  dei Movimenti (tipo «Rifornimento»), e per ognuno usa l'accisa in vigore
  *quel giorno*; rimborso = accisa − aliquota agevolata (403,22 €/1.000 l,
  Parametri). I totali sono per **Quadro**, con un solo arrotondamento.
- **Esclusi, con il motivo**: AdBlue e altri prodotti, rifornimenti all'estero
  (nuovo campo sul movimento), veicoli sotto 7,5 t o Euro ≤ 4, mezzi a noleggio
  (il rimborso spetta al cliente: l'Excel ha un foglio «Per cliente»),
  rifornimenti senza targa o con aliquota mancante («da correggere»).
- **Limite 1 litro per km**: si scrivono i km di ogni veicolo nella tabella;
  se i litri superano i km, vengono ridotti in proporzione.
- **Aliquote**: tabella modificabile («Aliquote»); «Carica le aliquote
  ufficiali» inserisce quelle di ottobre 2026. Il 4° trimestre 2026 è
  provvisorio: va aggiornato con la nota dell'Agenzia delle dogane.
- **Parametri** (righe 39–40): aliquota agevolata e «la società ha diritto»
  (Albo conto terzi / licenza conto proprio).
- **Scadenza**: ultimo giorno del mese dopo il trimestre (primo giorno
  lavorativo se festivo). Compensazione F24 codice 6740; dal 1/10/2026 invio
  telematico E.D.I.

Il programma non invia la dichiarazione: prepara quadri ed elenchi da
controllare e inserire nel software dell'Agenzia. Interpretazioni del
programma (non scritte dall'Agenzia): ripartizione proporzionale oltre
1 l/km, arrotondamento per quadro, numerazione dei quadri, prudenza sull'HVO
senza informazioni. Distinto dal credito d'imposta caro gasolio.
