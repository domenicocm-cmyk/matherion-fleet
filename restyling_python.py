"""Genera il tema e illustrazioni SVG incorporate, senza dipendenze esterne.
Uso: python restyling_python.py CARTELLA_ORIGINALI CARTELLA_OUTPUT
"""
from pathlib import Path
from urllib.parse import quote
import re, sys

def svg_uri(content, box='0 0 24 24'):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box}">{content}</svg>'
    return 'data:image/svg+xml,'+quote(svg, safe='')

def illustration():
    parts=['<defs><linearGradient id="sky" x2="1" y2="1"><stop stop-color="#edf8fd"/><stop offset="1" stop-color="#d4f4ed"/></linearGradient><linearGradient id="van" x2="0" y2="1"><stop stop-color="#fff"/><stop offset="1" stop-color="#d7e9f1"/></linearGradient></defs>', '<rect width="640" height="260" rx="24" fill="url(#sky)"/>']
    # Percorso logistico illustrativo: non rappresenta dati o posizioni reali.
    for x,y,h in [(45,88,100),(105,63,125),(164,106,82),(455,76,112),(522,48,140),(579,98,90)]:
        parts.append(f'<rect x="{x}" y="{y}" width="44" height="{h}" rx="5" fill="#b7d9e5" opacity=".5"/>')
        for yy in range(y+12,180,20):
            for xx in [x+9,x+26]: parts.append(f'<rect x="{xx}" y="{yy}" width="8" height="8" rx="2" fill="#fff" opacity=".8"/>')
    parts+=['<path d="M18 215H622" stroke="#9bc8d8" stroke-width="2"/>','<path d="M64 63C145 8 204 70 300 48S463 20 552 62" stroke="#53b9bd" stroke-width="2" stroke-dasharray="5 7" fill="none"/>']
    for x,y in [(64,63),(300,48),(552,62)]:
        parts.append(f'<circle cx="{x}" cy="{y}" r="12" fill="#fff"/><circle cx="{x}" cy="{y}" r="5" fill="#169ca6"/>')
    parts+=['<ellipse cx="327" cy="220" rx="145" ry="13" fill="#7baeba" opacity=".2"/>','<path d="M190 188v-62a13 13 0 0 1 13-13h144v75" fill="#246c96"/>','<path d="M215 181v-75a12 12 0 0 1 12-12h129v87" fill="url(#van)" stroke="#91b5c6" stroke-width="2"/>','<path d="M356 117h40l39 45v40H356Z" fill="#f5fbff" stroke="#91b5c6" stroke-width="2"/>','<path d="M369 126h23l27 34h-50Z" fill="#246080"/>','<path d="M215 180h220v22H215Z" fill="#168c9b"/>','<path d="M230 165h105" stroke="#aecbd7" stroke-width="2"/>','<path d="M369 170h12" stroke="#7194a7" stroke-width="3" stroke-linecap="round"/>','<rect x="422" y="178" width="14" height="9" rx="3" fill="#f1cd79"/>','<circle cx="257" cy="204" r="21" fill="#17384f"/><circle cx="257" cy="204" r="10" fill="#d2e5ed"/><circle cx="396" cy="204" r="21" fill="#17384f"/><circle cx="396" cy="204" r="10" fill="#d2e5ed"/>','<path d="m260 130 10 10 22-24" fill="none" stroke="#1499a5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>','<rect x="477" y="154" width="42" height="45" rx="6" fill="#fff" stroke="#9cc8d5" stroke-width="2"/><path d="m487 176 7 7 15-18" fill="none" stroke="#179c9d" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>']
    return svg_uri(''.join(parts),'0 0 640 260')

paths={
'cruscotto':'M3 3h7v7H3zM14 3h7v7h-7zM3 14h7v7H3zM14 14h7v7h-7z',
'contratti':'M6 3h9l4 4v14H6zM14 3v5h5M9 12h7M9 16h7',
'stampa':'M7 8V3h10v5M6 17H3V9h18v8h-3M7 14h10v7H7z',
'fatturazione':'M6 3h12v18l-3-2-3 2-3-2-3 2zM9 8h6M9 12h6M9 16h3',
'cp':'M7 3h10v18H7zM10 7h4M10 11h4M10 15h4',
'vrb':'M12 3 2 21h20zM12 9v5M12 17v1',
'rinotifiche':'M4 4v6h6M4 10a8 8 0 1 1 1 8',
'archivio':'M3 3h18v5H3zM5 8v13h14V8M9 12h6',
'soc':'M4 21V7l8-4 8 4v14M9 21v-5h6v5M8 9h1M15 9h1M8 12h1M15 12h1',
'capfin':'M3 20h18M6 16v-5M12 16V7M18 16V3',
'anag':'M12 21s7-7 7-12A7 7 0 0 0 5 9c0 5 7 12 7 12zM15 9a3 3 0 1 1-6 0 3 3 0 0 1 6 0',
'docs':'M4 5h6l2 3h8v13H4zM8 13h8M8 17h5',
'parametri':'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8ZM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2',
}

def build(src, out):
    out.mkdir(parents=True,exist_ok=True)
    source=(src/'index(4).html').read_text()
    for k,v in re.findall(r"^\s*(\w+):'([^']+)'",source[source.find('const ICO={'):source.find('const aspetto=')],re.M):paths.setdefault(k,v)
    paths['calendario']=paths.get('cal',paths['cruscotto'])
    css='''
/* Matherion Studio 2026.10.16 — solo presentazione. */
:root{--navy:#185b87;--navy-2:#2279a4;--gold:#27b7bc;--gold-soft:#e9f7f8;--gold-ink:#15616d;--ink:#18354b;--muted:#586f80;--line:#dde7ee;--bg:#f1f5fa;--surface:#fff;--surface-2:#edf3f8;--bar:#102d46;--r:14px;--studio-shadow:0 5px 22px #163b5910;--studio-art-opacity:1}
:root[data-theme="dark"]{--navy:#8acfe9;--navy-2:#a8e1f1;--gold:#53cbd0;--gold-soft:#173e4a;--gold-ink:#9fdee4;--ink:#e6eff7;--muted:#a5bac9;--line:#2b4559;--bg:#0e1d2c;--surface:#152b3e;--surface-2:#1c354b;--bar:#0b1e30;--studio-shadow:0 5px 22px #0002;--studio-art-opacity:.85}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--navy:#8acfe9;--navy-2:#a8e1f1;--gold:#53cbd0;--gold-soft:#173e4a;--gold-ink:#9fdee4;--ink:#e6eff7;--muted:#a5bac9;--line:#2b4559;--bg:#0e1d2c;--surface:#152b3e;--surface-2:#1c354b;--bar:#0b1e30;--studio-shadow:0 5px 22px #0002;--studio-art-opacity:.85}}
@media screen{
body{background:radial-gradient(ellipse at 95% 0%,color-mix(in srgb,var(--gold) 8%,transparent),transparent 45%),var(--bg);font-size:14px;letter-spacing:-.01em}
.bar{background:linear-gradient(110deg,#0e2942,#174762 75%,#146576);border-bottom:1px solid #ffffff15;box-shadow:0 4px 20px #102d4618}
.bar-in{padding:18px 28px;gap:12px}
.brand h1{font-size:21px;letter-spacing:-.035em}.brand .file{font-size:12px;color:#c2dce8;opacity:1}
.bar .btn{background:#ffffff08;border-color:#ffffff35;border-radius:11px}.bar .btn:hover{background:#ffffff18}.bar .btn.gold{background:#6cd5d5;color:#102d46;border-color:#6cd5d5}
.layout main{padding:28px 30px 60px}.side{width:258px;padding:22px 13px;background:var(--surface);scrollbar-width:thin;scrollbar-color:var(--line) transparent}
.brandbox{padding:0 8px 20px}.brandbox img{padding:6px;border-radius:12px;background:var(--gold-soft);height:46px}.brandbox b{font-size:18px;letter-spacing:-.03em}.brandbox small{font-size:10px;line-height:1.8}
.sgroup{font-size:10px;letter-spacing:.11em;color:var(--muted);margin-top:23px}
.sitem{padding:11px 12px;border-radius:11px;font-size:12px;font-weight:600;margin-bottom:4px;transition:background .18s,color .18s}
.sitem>span:first-child{display:flex;align-items:center;gap:10px;line-height:1.4}
.sitem[data-tab]>span:first-child::before{content:"";width:19px;height:19px;flex:0 0 19px;background:currentColor;mask:var(--studio-icon) center / contain no-repeat;-webkit-mask:var(--studio-icon) center / contain no-repeat;opacity:.85}
.sitem[aria-current="page"]{background:linear-gradient(100deg,var(--gold-soft),var(--surface-2));color:var(--navy);box-shadow:inset 3px 0 var(--gold)}
.sbadge{font-size:10px;padding:3px 7px}.sitem[aria-current="page"] .sbadge{color:var(--gold-ink);background:var(--surface)}
.pagehead{padding:22px 24px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(115deg,var(--surface) 60%,var(--gold-soft));box-shadow:var(--studio-shadow);margin-bottom:22px;align-items:center}
.pagehead h2{font-size:27px;color:var(--ink);letter-spacing:-.04em;line-height:1.2}
.pagehead h2::before{content:"MATHERION / WORKSPACE";display:block;font-size:9px;font-weight:750;color:var(--gold-ink);letter-spacing:.17em;margin-bottom:9px}
.pagehead p{font-size:12px;line-height:1.6;margin-top:7px}
.btn{border-radius:10px;font-size:12px;min-height:42px;transition:box-shadow .18s,background .18s,border-color .18s}
.btn.primary{background:var(--navy);box-shadow:0 4px 10px #185b871a}.btn.primary:hover{background:var(--navy-2);box-shadow:0 5px 14px #185b8728}
.btn:focus-visible,.sitem:focus-visible,.kpi:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
.kpis{gap:14px;grid-template-columns:repeat(auto-fit,minmax(205px,1fr));margin-bottom:24px}
.kpi{position:relative;isolation:isolate;overflow:hidden;min-height:130px;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:16px;padding:22px 20px 18px;box-shadow:var(--studio-shadow);transition:transform .18s,box-shadow .18s}
.kpi b{font-size:30px;line-height:1.2;letter-spacing:-.05em;color:var(--ink);padding-right:34px;overflow-wrap:anywhere;max-width:100%;z-index:1}
.kpi span{font-size:12px;line-height:1.5;margin-top:12px;max-width:95%;z-index:1}
.kpi::before{content:"";position:absolute;right:16px;top:17px;width:23px;height:23px;background:var(--navy);mask:var(--studio-icon) center / contain no-repeat;-webkit-mask:var(--studio-icon) center / contain no-repeat;z-index:1}
.kpi::after{content:"";position:absolute;right:-10px;top:-12px;width:74px;height:74px;border-radius:24px;background:var(--gold-soft);transform:rotate(12deg);z-index:0}
.kpi.hot{border-color:color-mix(in srgb,var(--danger) 28%,var(--line));border-top-color:var(--danger);background:var(--surface)}.kpi.hot b{color:var(--danger)}.kpi.hot::before{background:var(--danger)}.kpi.hot::after{background:var(--danger-soft)}
.kpi.warn{border-top-color:var(--warn)}.kpi:hover{transform:translateY(-3px);box-shadow:0 9px 26px #163b591a}
.toolbar{background:var(--surface);border:1px solid var(--line);border-radius:14px;box-shadow:var(--studio-shadow);padding:16px;gap:12px}
.field label,.flabel{font-size:11px;font-weight:650;letter-spacing:.01em}
.input,select.input,textarea.input{background:var(--surface);border-radius:10px;border-color:var(--line);min-height:42px;font-size:13px}
.input:hover{border-color:color-mix(in srgb,var(--navy) 40%,var(--line))}.input:focus{border-color:var(--gold);box-shadow:0 0 0 3px color-mix(in srgb,var(--gold) 16%,transparent)}
.tablewrap{border-radius:15px;box-shadow:var(--studio-shadow)}
.grid th{font-size:10px;font-weight:750;letter-spacing:.045em;background:var(--surface-2);color:var(--muted);padding:14px 13px;border-bottom:1px solid var(--line)}
.grid td{font-size:12px;padding:13px;border-bottom-color:color-mix(in srgb,var(--line) 70%,transparent)}
.grid tbody tr:not(.rowerr):not(.rowwarn):not(.rownc):nth-child(even){background:color-mix(in srgb,var(--surface-2) 28%,transparent)}
.grid tbody tr:hover{background:var(--gold-soft)!important}.grid .sub{font-size:11px;line-height:1.6}
.plate{border-color:#8699ac;box-shadow:0 2px 3px #17384f0a;letter-spacing:.07em}.pill{padding:4px 10px;font-size:10px;line-height:1.5}
.panel,.card,.hero-card{border-radius:16px;box-shadow:var(--studio-shadow)}.panel{padding:22px}.panel h3{font-size:15px;color:var(--ink)}
.ledger{border:1px solid var(--line);border-radius:15px;box-shadow:var(--studio-shadow)}.ledger div{padding:18px 20px}.ledger b{font-size:26px;color:var(--navy)}.ledger small{font-size:11px}
.ltile.on{background:var(--gold-soft);box-shadow:inset 0 -3px var(--gold)}
.kanban{gap:14px}.kcol{border-radius:14px;padding:12px}.khead{padding:4px 3px 14px}.kcard{padding:14px;border-radius:12px;border-left-color:var(--gold);box-shadow:0 3px 9px #163b5908}.kcard:hover{box-shadow:var(--studio-shadow)}
.calday{border-radius:12px;padding:9px}.calday.today{background:var(--gold-soft);border-color:var(--gold)}.cev{padding:4px 6px;border-radius:5px}
.drawer{box-shadow:-16px 0 70px #0b22342b}.drawer header{background:var(--surface);color:var(--ink);border-bottom:1px solid var(--line)}.drawer header h2{font-size:20px}.drawer footer{background:var(--surface-2)}
.scrim,.modal{backdrop-filter:blur(4px)}.modal .box{border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:20px;box-shadow:0 24px 90px #071d3a38}
.drop{border-color:color-mix(in srgb,var(--gold) 45%,var(--line));background:var(--gold-soft);border-radius:16px;padding:28px}
.hero{max-width:1250px;margin:18px auto;gap:44px;padding:28px 10px 50px}.hero h2{font-size:clamp(30px,3.1vw,46px);letter-spacing:-.05em;line-height:1.12;color:var(--ink);max-width:20ch}
.hero h2::before{content:"MATHERION · FLEET MANAGEMENT";display:block;font-size:10px;letter-spacing:.15em;color:var(--gold-ink);margin:22px 0 12px}.hero p{font-size:14px;line-height:1.8;margin-top:17px}.hero .actions{gap:10px;margin-top:22px}
.hero .logobox{display:block;width:max-content;padding:14px 18px;border:1px solid var(--line);box-shadow:var(--studio-shadow);border-radius:16px}.hero .logobox img{height:65px}.hero .plate.lg{height:27px;font-size:14px;margin-top:7px;vertical-align:middle}.hero .plate.lg::before,.hero .plate.lg::after{width:9px}.hero .plate.lg span{padding:0 9px}
.hero-card{padding:24px;background:var(--surface);border:1px solid var(--line);overflow:hidden}.hero-card::before{content:"";display:block;height:205px;background:var(--studio-fleet) center / contain no-repeat;margin:-4px -4px 22px;opacity:var(--studio-art-opacity)}
.hero-card h3{font-size:17px;color:var(--ink);margin-bottom:17px}.hero-card ol{list-style:none;padding:0;counter-reset:steps}.hero-card li{position:relative;padding-left:35px;margin:15px 0;font-size:12px;line-height:1.65;counter-increment:steps}.hero-card li::before{content:counter(steps,decimal-leading-zero);position:absolute;left:0;top:0;display:grid;place-items:center;width:25px;height:25px;background:var(--gold-soft);color:var(--gold-ink);border-radius:8px;font-size:10px;font-weight:750}
.hero-card .dl{gap:5px}.hero-card .dl .btn{white-space:normal;text-align:left;min-height:36px;font-size:11px}
body.app .pagehead{padding:16px;margin-bottom:16px}body.app .pagehead h2{font-size:22px}body.app .pagehead h2::before{font-size:8px;margin-bottom:6px}body.app .oggi-h{padding:18px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(120deg,var(--surface),var(--gold-soft))}
body.app .oggi-k button{border-radius:15px;box-shadow:var(--studio-shadow);padding:18px;border-left:0;border-top:3px solid var(--gold);min-height:100px}body.app .oggi-k button.hot{border-top-color:var(--danger)}body.app .oggi-k b{font-size:30px}body.app .oggi-k small{line-height:1.5;margin-top:8px}
body.app .scheda{border-radius:14px;padding:15px;box-shadow:var(--studio-shadow)}body.app .tabbar{background:var(--surface);box-shadow:0 -6px 25px #102d4610;padding-top:8px}body.app .tabbar button.on{background:var(--gold-soft)}body.app .fab{background:linear-gradient(135deg,#185b87,#158e9b);box-shadow:0 8px 22px #185b8750}body.app .drawer .indietro{background:var(--gold-soft);color:var(--navy)}
@media(min-width:1500px){.layout main{padding:32px 40px 64px}.kpis{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:1100px){.hero{gap:24px}.hero-card{padding:20px}.hero-card::before{height:170px}.layout main{padding:22px 20px 70px}}
@media(max-width:900px){.side{width:min(310px,86vw)}.hero{grid-template-columns:1fr;max-width:650px;padding:12px 0 35px;margin:0 auto}.hero h2{max-width:24ch}.hero-card::before{height:190px}.bar-in{padding:12px 16px}.brand h1{font-size:18px}.pagehead{padding:18px}.pagehead h2{font-size:24px}.drawer{border-radius:0}}
@media(max-width:620px){.layout main{padding:18px 14px 90px}.brand h1{font-size:16px}.hero h2{font-size:32px}.hero .logobox img{height:52px}.hero .actions{flex-direction:column}.hero .actions .btn{justify-content:center;min-height:46px}.hero-card::before{height:145px}.hero-card{padding:20px}.kpis{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.kpi{padding:17px 13px;min-height:130px}.kpi b{font-size:24px;padding-right:0;max-width:calc(100% - 22px)}.kpi span{font-size:11px}.kpi::before{right:10px;top:16px;width:17px;height:17px}.kpi::after{width:52px;height:52px}.pagehead h2::before{font-size:8px}.ledger div{padding:12px}.toolbar{padding:12px}.panel{padding:17px}.input,select.input,textarea.input{font-size:16px}body.app .drawer header{padding:14px}body.app .drawer header h2{font-size:18px}body.app .pagehead .piu{flex-shrink:0}}
}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}.kpi:hover{transform:none}}
@media print{.hero-card::before,.pagehead h2::before,.kpi::before,.kpi::after{display:none!important}.pagehead,.kpi,.panel,.card,.ledger,.hero-card{box-shadow:none!important;background:white}.pagehead{padding:0;border:0}.grid tbody tr{background:white!important}}
'''
    css+='\n:root{--studio-fleet:url("'+illustration()+'")}\n'
    default_uri=svg_uri('<path d="M6 3h9l4 4v14H6zM14 3v5h5M9 12h7M9 16h7" fill="none" stroke="black" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')
    css+='.sitem[data-tab],.kpi[data-go]{--studio-icon:url("'+default_uri+'")}\n'
    for k,path in paths.items():
        uri=svg_uri(f'<path d="{path}" fill="none" stroke="black" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')
        css+=f'.sitem[data-tab="{k}"],.kpi[data-go="{k}"]{{--studio-icon:url("{uri}")}}\n'
    for srcname,dstname in [('index(4).html','index.html'),('burago.html','burago.html')]:
        text=(src/srcname).read_text()
        text=text.replace('</head>','<style id="matherion-studio-20261016">'+css+'</style>\n</head>',1)
        text=text.replace("const APP_VERSION='2026.10.17';","const APP_VERSION='2026.10.17-studio.1';")
        (out/dstname).write_text(text)
    sw=(src/'sw.js').read_text().replace("const VER = 'flotta-2026.10.17';","const VER = 'flotta-2026.10.17-studio.1';")
    (out/'sw.js').write_text(sw)
    print('Creati index.html, burago.html e sw.js; SVG e icone incorporati.')

if __name__=='__main__':
    build(Path(sys.argv[1] if len(sys.argv)>1 else 'upload'),Path(sys.argv[2] if len(sys.argv)>2 else 'output'))
