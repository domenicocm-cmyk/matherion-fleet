#!/usr/bin/env python3
"""Mette in linea una versione nuova del gestionale.

    python3 strumenti/aggiorna.py ~/Downloads/Gestionale_Flotta_Noleggi.html

Prende il file che ti è stato consegnato (quello che useresti su OneDrive) e:
  1. ne ricava `index.html`, la versione web della sede centrale;
  2. ne ricava `burago.html`, la copia bloccata sulla filiale Amazon Burago;
  3. allinea la versione in `sw.js`, così le postazioni ricevono l'aggiornamento;
  4. aggiunge una riga a `CHANGELOG.md`.

Poi basta:  git add -A && git commit -m "aggiornamento" && git push

Serve python3 (su macOS c'è già, o si installa con gli strumenti da riga di
comando di Xcode). Se preferisci non usarlo, sostituisci a mano `index.html` e
`burago.html` con i due file che ti vengono consegnati già pronti e alza di una
unità la riga `const VER` in `sw.js`.
"""
import sys, re, os, datetime

FILIALE = "Amazon Burago"          # nome del centro di costo, come in anagrafica
QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def leggi(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def scrivi(p, s):
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)
    return len(s)


def sost(s, a, b, dove, attese=1):
    if s.count(a) != attese:
        raise SystemExit("Il file sorgente non ha la forma attesa (%s). "
                         "Probabilmente è cambiato: chiedi il pacchetto già pronto." % dove)
    return s.replace(a, b, 1)


# ---------- 1. versione web ----------
def versione_web(s, manifest, suff="", titolo="Flotta", colore="#1F3864"):
    head = """<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="{colore}">
<meta name="color-scheme" content="light">
<meta name="description" content="Gestione della flotta: mezzi, noleggi, giornaliere, manutenzioni, sinistri e scadenze.">
<link rel="manifest" href="{manifest}">
<link rel="icon" href="/icons/favicon{suff}.ico" sizes="48x48 32x32 16x16">
<link rel="icon" type="image/png" href="/icons/favicon-32{suff}.png" sizes="32x32">
<link rel="icon" type="image/png" href="/icons/favicon-16{suff}.png" sizes="16x16">
<link rel="icon" type="image/png" href="/icons/icon-192{suff}.png" sizes="192x192">
<link rel="apple-touch-icon" href="/icons/apple-touch-icon{suff}.png">
<link rel="apple-touch-icon" sizes="152x152" href="/icons/apple-touch-icon-152{suff}.png">
<link rel="apple-touch-icon" sizes="167x167" href="/icons/apple-touch-icon-167{suff}.png">
<link rel="apple-touch-icon" sizes="180x180" href="/icons/apple-touch-icon{suff}.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="{titolo}">
<meta name="mobile-web-app-capable" content="yes">
<meta name="application-name" content="{titolo}">
<meta name="msapplication-TileColor" content="{colore}">
<meta name="msapplication-TileImage" content="/icons/icon-192{suff}.png">""".format(
        manifest=manifest, suff=suff, titolo=titolo, colore=colore)
    s = sost(s, '<meta name="viewport" content="width=device-width, initial-scale=1">', head, "intestazione")

    sw = """
/* ---------- app installabile (solo quando è pubblicata su web) ---------- */
const WEB=location.protocol==='https:'||location.protocol==='http:';
function avvisoAggiornamento(reg){
  const d=document.createElement('div');d.className='modal';
  d.innerHTML=`<div class="box" role="dialog" aria-modal="true"><h3>C’è una versione nuova</h3>
    <div class="muted">È stato pubblicato un aggiornamento del gestionale. Ricarica per usarlo: i dati sono nel registro, non si perde nulla.${S.dirty?'<br><br><b>Hai modifiche non salvate:</b> salva prima di ricaricare.':''}</div>
    <div class="acts"><button class="btn" data-a="0">Più tardi</button><button class="btn primary" data-a="1">Ricarica ora</button></div></div>`;
  d.addEventListener('click',e=>{const a=e.target.closest('[data-a]');if(!a&&e.target!==d)return;
    const ok=a&&a.dataset.a==='1';d.remove();
    if(ok){try{reg.waiting&&reg.waiting.postMessage('aggiorna');}catch(err){}setTimeout(()=>location.reload(),300);}});
  document.body.appendChild(d);
}
if(WEB&&'serviceWorker' in navigator){
  window.addEventListener('load',()=>{
    navigator.serviceWorker.register('/sw.js').then(reg=>{
      if(reg.waiting&&navigator.serviceWorker.controller)avvisoAggiornamento(reg);
      reg.addEventListener('updatefound',()=>{
        const w=reg.installing;if(!w)return;
        w.addEventListener('statechange',()=>{
          if(w.state==='installed'&&navigator.serviceWorker.controller)avvisoAggiornamento(reg);
        });
      });
      setInterval(()=>reg.update().catch(()=>{}),30*60*1000);
    }).catch(()=>{});
  });
}
try{const v=new URLSearchParams(location.search).get('vai');if(v)sessionStorage.setItem('vai',v);}catch(e){}
"""
    s = sost(s, "function afterOpenExtras(){",
             sw + """function afterOpenExtras(){
  try{const v=sessionStorage.getItem('vai');if(v){sessionStorage.removeItem('vai');
    if(VIEWS[v]&&(!filiale()||FILIALE_TABS.includes(v))){S.tab=v;render();}}}catch(e){}""",
             "aggancio del service worker")
    return s


# ---------- 2. copia bloccata sulla filiale ----------
def versione_filiale(s, nome):
    s = sost(s,
             """function filiale(){
  const u=utenteCorrente();
  if(u&&ruoloKey(u.ruolo)==='filiale')return u.centroCosto||'';   /* deciso dall'account */
  try{return localStorage.getItem('filiale')||'';}catch(e){return '';}
}
function setFiliale(v){try{if(v)localStorage.setItem('filiale',v);else localStorage.removeItem('filiale');}catch(e){}}""",
             """const FILIALE_FISSA=%s;
function filiale(){
  const u=utenteCorrente();
  if(u&&ruoloKey(u.ruolo)==='filiale')return u.centroCosto||'';   /* se c'e' un accesso, decide l'account */
  if(!S.cdc||!S.cdc.length)return FILIALE_FISSA;
  const n=FILIALE_FISSA.toLowerCase();
  const c=S.cdc.find(x=>String(x.nome||'').toLowerCase()===n);
  return c?(c.etichetta||cdcLabel(c)):FILIALE_FISSA;
}
function setFiliale(){}""" % ('"%s"' % nome), "blocco della filiale")
    s = sost(s, """  if((e.ctrlKey||e.metaKey)&&e.altKey&&e.key.toLowerCase()==='f'&&S.wb){e.preventDefault();scegliFiliale();}\n""",
             "", "scorciatoia di cambio postazione")
    s = sost(s, """function afterOpenExtras(){""",
             """function afterOpenExtras(){
  if(!operatore())setTimeout(chiediOperatore,600);""", "richiesta del nome della postazione")
    s = sost(s, """/* ---------- postazione, blocco e conflitti ---------- */""",
             """function chiediOperatore(){
  const m=document.createElement('div');m.className='modal';
  m.innerHTML=`<div class="box" role="dialog" aria-modal="true"><h3>Chi lavora su questa postazione?</h3>
    <div class="muted">Serve solo a segnalare agli altri chi ha il registro aperto. Resta su questo computer.</div>
    <div class="field" style="margin:12px 0"><label for="opNome">Nome e cognome</label><input class="input" id="opNome" placeholder="Es. Mario Rossi"></div>
    <div class="acts"><button class="btn" data-a="0">Più tardi</button><button class="btn primary" data-a="1">Salva</button></div></div>`;
  m.addEventListener('click',e=>{const a=e.target.closest('[data-a]');if(!a&&e.target!==m)return;
    if(a&&a.dataset.a==='1'){const v=m.querySelector('#opNome').value.trim();if(v){setOperatore(v);writeLock();toast('Postazione: '+v);}}
    m.remove();});
  document.body.appendChild(m);m.querySelector('#opNome').focus();
}
/* ---------- postazione, blocco e conflitti ---------- */""", "finestra del nome della postazione")
    s = re.sub(r'<title>[^<]*</title>', '<title>Gestionale flotta – filiale %s</title>' % nome, s, count=1)
    return s


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    sorgente = os.path.expanduser(sys.argv[1])
    base = leggi(sorgente)

    ver = re.search(r"APP_VERSION='([^']*)'", base)
    if not ver:
        raise SystemExit("Nel file non trovo la versione: non sembra il gestionale.")
    ver = ver.group(1)

    n1 = scrivi(os.path.join(QUI, "index.html"), versione_web(base, "/manifest.webmanifest"))
    n2 = scrivi(os.path.join(QUI, "burago.html"),
                versione_web(versione_filiale(base, FILIALE), "/manifest-burago.webmanifest",
                             suff="-burago", titolo="Burago", colore="#8A6B10"))

    p = os.path.join(QUI, "sw.js")
    sw = leggi(p)
    sw = re.sub(r"const VER = '[^']*';", "const VER = 'flotta-%s';" % ver, sw, count=1)
    scrivi(p, sw)

    p = os.path.join(QUI, "CHANGELOG.md")
    riga = "- **%s** — pubblicata il %s\n" % (ver, datetime.date.today().strftime("%d/%m/%Y"))
    testo = leggi(p) if os.path.exists(p) else "# Versioni pubblicate\n\n"
    if riga not in testo:
        scrivi(p, testo.rstrip("\n") + "\n" + riga)

    print("index.html   %8d byte" % n1)
    print("burago.html  %8d byte  (filiale %s)" % (n2, FILIALE))
    print("sw.js        versione flotta-%s" % ver)
    print("\nOra:  git add -A && git commit -m \"gestionale %s\" && git push" % ver)


if __name__ == "__main__":
    main()
