#!/usr/bin/env python3
"""Rigenera le icone dell'app (cartella `icons/`).

    python3 strumenti/icone.py

Serve solo se cambia il marchio o si aggiunge una filiale. Le icone che trovi
nella cartella sono gia' pronte: normalmente questo file non va toccato.

Richiede:  pip install cairosvg
"""
import os, io, sys

QUI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUORI = os.path.join(QUI, "icons")
TRACCIATO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "marchio.path")

# il marchio Matherion, ricavato dal logo e vettorializzato: 126 x 191
D = open(TRACCIATO, encoding="utf-8").read().strip()
MW, MH = 126.0, 191.0

TEMI = {
    # nome:  (fondo alto, fondo basso, colore del marchio)
    "":        ("#2B4A7F", "#16284A", "#FFFFFF"),   # sede centrale: blu
    "burago":  ("#D4AC2B", "#A17C12", "#16284A"),   # filiale: oro
}


def svg(size, tema, quota=0.60, raggio=None, bordo=True):
    """Una piastrella quadrata con il marchio al centro."""
    alto, basso, segno = TEMI[tema]
    h = size * quota
    w = h * MW / MH
    x = (size - w) / 2.0
    y = (size - h) / 2.0
    k = h / MH
    r = size * 0.225 if raggio is None else raggio
    luce = ""
    if bordo:
        luce = ('<rect x="0" y="0" width="%g" height="%g" rx="%g" fill="url(#luce)"/>'
                '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="none" '
                'stroke="#FFFFFF" stroke-opacity=".10" stroke-width="%g"/>'
                % (size, size, r, size * .012, size * .012, size * .976, size * .976,
                   max(0, r - size * .012), size * .012))
    return """<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 {s} {s}">
<defs>
<linearGradient id="fondo" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{alto}"/><stop offset="1" stop-color="{basso}"/>
</linearGradient>
<radialGradient id="luce" cx=".28" cy=".16" r=".95">
<stop offset="0" stop-color="#FFFFFF" stop-opacity=".16"/>
<stop offset=".6" stop-color="#FFFFFF" stop-opacity="0"/>
</radialGradient>
</defs>
<rect x="0" y="0" width="{s}" height="{s}" rx="{r}" fill="url(#fondo)"/>
{luce}
<g transform="translate({x},{y}) scale({k})"><path d="{d}" fill="{segno}"/></g>
</svg>""".format(s=size, r=r, alto=alto, basso=basso, segno=segno,
                 x=x, y=y, k=k, d=D, luce=luce)


def scrivi(nome, size, tema, **kw):
    import cairosvg
    p = os.path.join(FUORI, nome)
    cairosvg.svg2png(bytestring=svg(size, tema, **kw).encode(), write_to=p,
                     output_width=size, output_height=size)
    return p, os.path.getsize(p)


def main():
    os.makedirs(FUORI, exist_ok=True)
    fatti = []
    for tema, suff in (("", ""), ("burago", "-burago")):
        # icone normali: piastrella con angoli arrotondati
        for s in (48, 64, 96, 128, 192, 256, 384, 512):
            fatti.append(scrivi("icon-%d%s.png" % (s, suff), s, tema, quota=.64))
        # icone "maskable": a tutto quadro, marchio dentro la zona sicura
        for s in (192, 512):
            fatti.append(scrivi("maskable-%d%s.png" % (s, suff), s, tema,
                                quota=.50, raggio=0, bordo=False))
        # iOS: a tutto quadro, l'angolo lo arrotonda il sistema
        for s, n in ((152, "apple-touch-icon-152%s.png"), (167, "apple-touch-icon-167%s.png"),
                     (180, "apple-touch-icon%s.png")):
            fatti.append(scrivi(n % suff, s, tema, quota=.58, raggio=0, bordo=False))
        # favicon: piccolissima, il marchio deve riempire
        for s in (16, 32, 48):
            fatti.append(scrivi("favicon-%d%s.png" % (s, suff), s, tema,
                                quota=.80, raggio=max(2, s * .18), bordo=False))

    # favicon.ico con le tre misure dentro
    try:
        from PIL import Image
        for suff in ("", "-burago"):
            base = Image.open(os.path.join(FUORI, "favicon-48%s.png" % suff))
            base.save(os.path.join(FUORI, "favicon%s.ico" % suff),
                      sizes=[(16, 16), (32, 32), (48, 48)])
    except Exception as e:
        print("favicon.ico non creata:", e)

    for p, n in fatti:
        print("%-34s %7d byte" % (os.path.basename(p), n))
    print("\n%d icone in %s" % (len(fatti), FUORI))


if __name__ == "__main__":
    main()
