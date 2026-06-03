# Use case notation spotlights v2: four cards, each diagram + a what/when/why explanation
# beside it. Generalisation drawn vertically in black (hollow triangle) so it reads
# distinctly from the blue associations. One reveal engine across all [data-step] elements.
def uc(cx,cy,label,rx=82,ry=23):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{label}</text>'
def actorNL(x,y):
    return (f'<g transform="translate({x},{y})"><circle cx="16" cy="6" r="7" class="actor-blue"/>'
            f'<line x1="16" y1="13" x2="16" y2="34" class="uml-line-blue"/><line x1="16" y1="18" x2="5" y2="27" class="uml-line-blue"/><line x1="16" y1="18" x2="27" y2="27" class="uml-line-blue"/><line x1="16" y1="34" x2="5" y2="46" class="uml-line-blue"/><line x1="16" y1="34" x2="27" y2="46" class="uml-line-blue"/></g>')
def nm(x,y,t): return f'<text x="{x}" y="{y}" text-anchor="middle" class="uml-text" font-size="10" font-weight="600">{t}</text>'
def bl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-blue"/>'
def gen(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#gen)"/>'
def ext(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7a3a23" stroke-width="1.2" stroke-dasharray="4,3" fill="none" marker-end="url(#open)"/>'
def lblm(x,y,t,c="#2c3540",anc="middle"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" font-family="JetBrains Mono, monospace" font-size="9.5" fill="{c}" font-weight="600">{t}</text>'
def grid_icon(x,y): return f'<rect x="{x}" y="{y}" width="13" height="13" fill="none" stroke="#2c5f7c" stroke-width="1.1"/><line x1="{x+6.5}" y1="{y}" x2="{x+6.5}" y2="{y+13}" stroke="#2c5f7c" stroke-width="1"/><line x1="{x}" y1="{y+6.5}" x2="{x+13}" y2="{y+6.5}" stroke="#2c5f7c" stroke-width="1"/>'
def gs(n,*p): return f'<g class="bstep" data-step="{n}">'+''.join(p)+'</g>'
DEFS='<defs><marker id="gen" viewBox="0 0 14 14" refX="13" refY="7" markerWidth="14" markerHeight="14" orient="auto"><path d="M 1 1 L 13 7 L 1 13 Z" fill="white" stroke="#0f1419" stroke-width="1.2"/></marker><marker id="open" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#7a3a23" stroke-width="1.4"/></marker></defs>'

# ---- Card 1: actor generalisation ----
c1=DEFS+''.join([
 gs(1, actorNL(200,52), nm(216,40,"Library user"), uc(460,76,"Search catalogue",rx=86), bl(230,76,374,76)),
 gs(2, actorNL(200,158), nm(216,224,"Member"),
    gen(216,158,216,106), lblm(150,130,"generalisation","#5a6473"),
    uc(460,182,"Borrow book",rx=86), bl(230,182,374,182)),
])
e1="A specialised actor is a kind of a more general one, and it inherits all of the general actor's use cases. Reach for it when two roles overlap heavily, one can do everything the other can and a little more, so the shared use cases are drawn once on the general actor instead of being repeated."

# ---- Card 2: use-case generalisation ----
c2=DEFS+''.join([
 gs(3, actorNL(40,96), nm(56,162,"Customer"), uc(250,120,"Pay",rx=64), bl(72,120,186,120)),
 gs(4, uc(470,80,"Pay by card",rx=82), gen(392,90,320,112)),
 gs(5, uc(470,176,"Pay by cash",rx=82), gen(392,166,320,130)),
])
e2="One use case can be a specific variant of another, inheriting its behaviour and adding its own steps. Use it when several use cases are the same task done in different ways, to capture the shared behaviour once and let each variant specialise it."

# ---- Card 3: composite / multi-level ----
c3=DEFS+''.join([
 gs(6, uc(150,130,"Manage booking",rx=92), grid_icon(222,123)),
 gs(7, '<rect x="350" y="60" width="230" height="170" rx="6" fill="none" stroke="#bcae97" stroke-dasharray="4,3"/>',
    '<text x="465" y="80" text-anchor="middle" class="uml-text" font-size="10" fill="#5a6473">first-level diagram</text>',
    uc(465,120,"Change dates",rx=78), uc(465,185,"Cancel booking",rx=78),
    '<line x1="244" y1="130" x2="350" y2="120" class="uml-line-dashed"/>', lblm(300,116,"decomposes","#5a6473")),
])
e3="A composite use case stands in for a group of finer ones and is expanded in its own lower-level diagram. Use it when a system has too many use cases for one readable page: the top diagram stays a map, and each composite opens into its own detail."

# ---- Card 4: extension points ----
c4=DEFS+''.join([
 gs(8, '<ellipse cx="170" cy="120" rx="118" ry="56" class="uml-box"/>',
    '<text x="170" y="98" text-anchor="middle" class="uml-text" font-size="11" font-weight="600">Checkout</text>',
    '<line x1="70" y1="110" x2="270" y2="110" class="uml-line"/>',
    '<text x="170" y="128" text-anchor="middle" class="uml-text" font-size="9.5" fill="#5a6473">extension points</text>',
    '<text x="170" y="144" text-anchor="middle" class="uml-text" font-size="9.5">afterTotals</text>'),
 gs(9, uc(500,120,"Apply coupon",rx=80), ext(420,120,292,120),
    lblm(356,109,"&lt;&lt;extend&gt;&gt;","#7a3a23"), lblm(356,132,"[has coupon]","#7a3a23")),
])
e4="An extension point is a named place in a base use case where an extension can attach. Use them when a base has more than one optional or exceptional path, so each extend states exactly where it fires rather than vaguely somewhere inside."

CARDS=[("Actor generalisation",c1,"0 0 600 250",e1,1),
       ("Use-case generalisation  (inherit)",c2,"0 0 600 240",e2,3),
       ("Composite (multi-level) use case",c3,"0 0 600 250",e3,6),
       ("Extension points",c4,"0 0 600 210",e4,8)]

NARR=[
 "These are the use case notations that the main example did not need. Each appears with a small example and a note on what it is and when to use it. Use Next, or press Play.",
 "Actor generalisation. The general actor, a Library user, can Search the catalogue.",
 "A Member is a kind of Library user: the hollow triangle points to the general actor. The Member inherits Search catalogue and adds its own use case, Borrow book.",
 "Use-case generalisation. A Customer can Pay.",
 "Pay by card is a kind of Pay: the triangle points to the general use case. It inherits Pay and adds the card-specific steps.",
 "Pay by cash is another variant of Pay. Both share Pay's behaviour and specialise it.",
 "Composite use cases. Manage booking, marked with the small grid icon, stands for a group of finer use cases.",
 "It is expanded in its own lower-level diagram, into Change dates and Cancel booking, so the top diagram stays readable.",
 "Extension points. The base use case Checkout names a point in its flow, afterTotals, in a second compartment.",
 "An extend attaches there: Apply coupon extends Checkout at afterTotals when [has coupon]. The named point says exactly where the optional behaviour fires.",
]
MAX=len(NARR)-1
import json
cards_html=""
for ti,svg,vb,expl,estep in CARDS:
    cards_html+=f'''    <div class="ncard">
      <div class="ndiagram"><svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" class="cardsvg" role="img" aria-label="{ti} example.">{svg}</svg></div>
      <div class="nexplain estep" data-step="{estep}"><h4>{ti}</h4><p>{expl}</p></div>
    </div>
'''
HTML=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Use case notations</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {{ --ink:#0f1419; --ink-soft:#2c3540; --ink-mute:#5a6473; --paper:#faf7f2; --paper-warm:#f3ede2; --accent:#b85c38; --steel:#2c5f7c; --rule:#d8cfc0;
    --serif:'Fraunces',Georgia,serif; --sans:'Inter Tight',-apple-system,sans-serif; --mono:'JetBrains Mono',monospace; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:var(--sans); color:var(--ink); background:#fbfaf8; margin:0; padding:24px 22px 44px; line-height:1.55; }}
  .wrap {{ max-width:1180px; margin:0 auto; }}
  .eyebrow {{ font-family:var(--mono); font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--accent); font-weight:600; margin-bottom:8px; }}
  h1 {{ font-family:var(--serif); font-weight:500; font-size:25px; letter-spacing:-.02em; margin:0 0 8px; }}
  p {{ color:var(--ink-soft); }} .lead {{ font-size:16px; max-width:900px; }}
  .builder {{ border:1px solid var(--rule); border-radius:16px; padding:18px 20px 22px; margin-top:16px; background:#fff; box-shadow:0 10px 34px rgba(15,20,25,.07); }}
  .controls {{ display:flex; align-items:center; gap:10px; }}
  button {{ background:var(--steel); color:#fff; border:none; padding:9px 16px; border-radius:7px; font-family:var(--mono); font-size:12px; letter-spacing:.06em; text-transform:uppercase; font-weight:600; cursor:pointer; }}
  button.secondary {{ background:#fff; color:var(--steel); border:1px solid var(--steel); }}
  button:disabled {{ opacity:.4; cursor:default; }}
  .steplabel {{ font-family:var(--mono); font-size:12px; color:var(--ink-mute); margin-left:auto; }}
  .prog {{ height:4px; background:#efe7da; border-radius:3px; margin:12px 0 8px; overflow:hidden; }}
  .prog-fill {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#d98a5f); border-radius:3px; transition:width .35s ease; }}
  .narration {{ background:var(--paper-warm); border-left:4px solid var(--accent); border-radius:0 8px 8px 0; padding:14px 18px; margin:4px 0 16px; font-size:15.5px; color:var(--ink-soft); line-height:1.5; min-height:52px; }}
  .ncard {{ display:grid; grid-template-columns:1.55fr 1fr; gap:20px; align-items:center; padding:16px 0; border-bottom:1px dashed #e9e0d0; }}
  .ncard:last-child {{ border-bottom:none; }}
  @media (max-width:780px) {{ .ncard {{ grid-template-columns:1fr; }} }}
  .cardsvg {{ width:100%; height:auto; display:block; }}
  .nexplain h4 {{ font-family:var(--serif); font-size:18px; font-weight:600; margin:0 0 6px; }}
  .nexplain p {{ margin:0; font-size:14.5px; }}
  .uml-text {{ font-family:var(--sans); font-size:13px; fill:var(--ink); }}
  .uml-line {{ stroke:var(--ink); stroke-width:1.4; fill:none; }}
  .uml-line-dashed {{ stroke:var(--ink); stroke-width:1.2; fill:none; stroke-dasharray:4,3; }}
  .uml-line-blue {{ stroke:#4a8bb8; stroke-width:1.4; fill:none; }}
  .uml-box {{ stroke:var(--ink); stroke-width:1.4; fill:#fff; }}
  .actor-blue {{ stroke:#2c6e9a; stroke-width:1.4; fill:#eaf3f9; }}
  .bstep {{ opacity:0; transform:translateY(8px) scale(.94); transform-box:fill-box; transform-origin:center; transition:opacity .3s ease, transform .42s cubic-bezier(.2,.8,.3,1), filter .35s ease; }}
  .bstep.on {{ opacity:1; transform:translateY(0) scale(1); }}
  .bstep.current {{ filter:drop-shadow(0 0 6px rgba(184,92,56,.5)); }}
  .estep {{ opacity:.25; transform:translateY(6px); transition:opacity .35s ease, transform .4s ease; }}
  .estep.on {{ opacity:1; transform:none; }}
</style></head>
<body><div class="wrap">
  <div class="eyebrow">COMP433 &middot; Chapter 4 &middot; use case notations</div>
  <h1>Use case diagrams: the remaining notations</h1>
  <p class="lead">The core diagram uses actors, use cases, associations, include and extend. Four more notations appear in larger systems, each shown here on a small example, with a note on what it is and when to use it.</p>
  <div class="builder">
    <div class="controls">
      <button id="prev" onclick="bPrev()">Previous</button>
      <button id="next" onclick="bNext()">Next</button>
      <button class="secondary" onclick="bReset()">Reset</button>
      <button class="secondary" id="play" onclick="bPlay()">&#9658; Play</button>
      <span class="steplabel" id="lbl"></span>
    </div>
    <div class="prog"><div class="prog-fill" id="progfill"></div></div>
    <div class="narration" id="narr"></div>
{cards_html}  </div>
</div>
<script>
const NARR={json.dumps(NARR)}, MAX={MAX};
let cur=0, timer=null;
function render(){{
  document.querySelectorAll('[data-step]').forEach(el=>{{ const n=parseInt(el.getAttribute('data-step')); el.classList.toggle('on', n<=cur); if(el.classList.contains('bstep')) el.classList.toggle('current', n===cur); }});
  document.getElementById('narr').innerHTML=NARR[cur];
  document.getElementById('lbl').textContent='Step '+cur+' of '+MAX;
  document.getElementById('progfill').style.width=(cur/MAX*100)+'%';
  document.getElementById('prev').disabled=cur===0; document.getElementById('next').disabled=cur===MAX;
}}
function bNext(){{ if(cur<MAX){{cur++;render();}} }}
function bPrev(){{ if(cur>0){{cur--;render();}} }}
function bReset(){{ cur=0; stopPlay(); render(); }}
function stopPlay(){{ if(timer){{clearInterval(timer);timer=null;document.getElementById('play').innerHTML='&#9658; Play';}} }}
function bPlay(){{ if(timer){{stopPlay();return;}} if(cur===MAX)cur=0; document.getElementById('play').textContent='Pause'; timer=setInterval(()=>{{ if(cur>=MAX){{stopPlay();return;}} cur++; render(); }}, 2100); }}
render();
</script>
</body></html>'''
open("poc_usecase_notations.html","w",encoding="utf-8").write(HTML)
print("wrote notations v2; steps:", MAX)
