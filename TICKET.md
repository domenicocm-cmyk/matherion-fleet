# Ticket per manutenzioni e sinistri (dalla 2026.10.40)

Ogni richiesta ha un ticket con un tempo massimo di gestione: **4 ore** dalla richiesta.

- Se alla scadenza non è chiuso va **integrato** (pulsante *Integra*, con nota
  obbligatoria): il tempo si rinnova per la **metà del tempo precedente**
  (4 h → 2 h → 1 h → 30 min → 15 min, mai sotto il minimo).
- Il ticket scaduto resta evidenziato; chiuso dopo la scadenza risulta *chiuso fuori tempo*.
- Si apre in automatico con ogni nuova manutenzione o sinistro (o con il pulsante
  *Ticket* sulla riga), e si chiude da solo quando la pratica si chiude.
- Storico di ogni integrazione e chiusura con data, ora, chi e nota; scheda
  *Storico e tempi* con % chiusi nei tempi e tempo medio per tipo e per gestore.
- Parametri: `tktOre` (4), `tktRinnovo` (50 %), `tktMinimo` (15 min),
  `tktProgressivo` (Sì = metà del tempo precedente; No = metà del tempo iniziale),
  `tktAuto` (Sì).
