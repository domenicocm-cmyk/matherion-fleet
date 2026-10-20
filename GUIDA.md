# La Guida

Pulsante **Guida** in basso a destra (o `Ctrl + /`, oppure `?`).
Si scrive una domanda in italiano; la Guida risponde e, con **Guidami passo
passo**, evidenzia sullo schermo la voce di menu, il pulsante o il gruppo di
campi da usare. «Fallo per me» esegue il passo; «Avanti» prosegue; `Esc` esce.

Esempi: «come devo caricare un sinistro?», «dove trovo il riepilogo delle
spese del centro di costo Amazon?» (riconosce il centro di costo e lo apre),
«dove vedo lo storico della targa AB123CD», «come esporto i documenti dei
mezzi?», «come importo i movimenti Telepass?».

## Come funziona
- Gira nel gestionale, senza servizi esterni: le domande non lasciano il computer.
- Capisce parole chiave e coniugazioni (sinistro/sinistri, carico/caricare…),
  e riconosce centri di costo, targhe e società presenti nel registro.
- I passaggi di inserimento si ricavano dalle schede (gruppi, campi
  obbligatori, suggerimenti): se la scheda cambia, cambia anche la Guida.
- Rispetta i permessi: se il ruolo non vede la sezione o non può scrivere, lo dice.

## Limiti
Non è un modello linguistico: capisce le attività note (schede, contratti,
costi per centro di costo, movimenti, storico, documenti, scadenze,
proforma, riaddebiti). Se non capisce propone le attività più vicine.
Si estende in `amm28_guida.js` (`gCatalogo`, `G_CONCETTI`).
