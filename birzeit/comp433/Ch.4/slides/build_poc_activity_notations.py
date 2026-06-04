# Activity notation spotlights: fork/join (parallelism) and decision/merge (choice).
def act(cx,cy,label,w=140,h=38):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{label}</text>'
def dia(cx,cy,t,hw=44,hh=26): return f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t}</text>'
def bar(cx,y,w=170): return f'<rect x="{cx-w//2}" y="{y}" width="{w}" height="7" rx="2" fill="#2c3540"/>'
def arr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#aArrow)"/>'
def pl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line"/>'
def parr(pts): return f'<polyline points="{pts}" class="uml-line" fill="none" marker-end="url(#aArrow)"/>'
def ppl(pts): return f'<polyline points="{pts}" class="uml-line" fill="none"/>'
def gl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="11">{t}</text>'
def initial(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="9" fill="#0f1419"/>'
def final(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="{cx}" cy="{cy}" r="5" fill="#0f1419"/>'
def gs(n,*p): return f'<g class="bstep" data-step="{n}">'+''.join(p)+'</g>'
DEFS='<defs><marker id="aArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'

# Card A: fork / join (parallel)
cA=DEFS+''.join([
 gs(1, initial(230,40), arr(230,49,230,70), act(230,92,"Confirm order")),
 gs(2, arr(230,111,230,140), bar(230,141),
    arr(160,148,160,192), act(160,214,"Pack items",w=118),
    arr(310,148,310,192), act(310,214,"Charge card",w=118)),
 gs(3, pl(160,233,160,286), pl(310,233,310,286), bar(230,286),
    arr(230,293,230,322), act(230,344,"Dispatch order"),
    arr(230,363,230,392), final(230,404)),
])
eA="Fork and join model concurrency. A fork (the bar) starts several flows at once; a join (the matching bar) waits for all of them to finish before the flow continues. Use them when steps genuinely happen in parallel and none of the later work may start until every branch is done."

# Card B: decision / merge (choice)
cB=DEFS+''.join([
 gs(4, initial(230,40), arr(230,49,230,70), act(230,92,"Check stock")),
 gs(5, arr(230,111,230,138), dia(230,168,"in stock?")),
 gs(6, parr("186,168 150,168 150,236"), gl(120,150,"[yes]"), act(150,258,"Reserve item",w=120),
       parr("274,168 330,168 330,236"), gl(300,150,"[no]"), act(340,258,"Backorder",w=110)),
 gs(7, ppl("150,277 150,330"), pl(150,330,200,330),
       ppl("340,277 340,330"), pl(340,330,260,330),
       dia(230,330,"",hw=30,hh=18),
       arr(230,348,230,378), act(230,400,"Notify customer"),
       arr(230,419,230,448), final(230,460)),
])
eB="A decision chooses one of several guarded branches; the matching merge brings them back to a single path. Use them for alternatives, where exactly one branch runs. This is the counterpart to fork and join: a decision is a choice, a fork is concurrency, so a merge re-joins choices while a join waits for parallel flows."

CARDS=[("Fork and join  (parallel work)",cA,"0 0 460 430",eA,1),
       ("Decision and merge  (choosing a path)",cB,"0 0 460 490",eB,4)]
NARR=[
 "Two activity-diagram notations the booking flow did not need: parallel work with a fork and join, and the merge that closes a decision. Use Next, or press Play.",
 "Fork and join show work that happens at the same time. After Confirm order,",
 "a fork, the bar, splits the flow into parallel branches: Pack items and Charge card proceed together, in either order.",
 "A join waits for every branch to finish before the flow continues to Dispatch order. The rule: a fork starts all branches, a join waits for all of them.",
 "A merge closes a decision. After Check stock,",
 "a decision, the diamond, tests a condition with guarded branches.",
 "Exactly one branch runs: Reserve item if it is in stock, or Backorder if not.",
 "A merge brings the two branches back to one path before Notify customer. Every decision pairs with a merge. Do not confuse a merge with a join: a merge re-joins a choice (one branch ran), a join waits for parallel flows (all branches ran).",
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
<title>Activity notations: fork/join and merge</title>
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
  .controls {{ display:flex; align-items:center; gap:10px; position:sticky; top:0; background:#fff; z-index:5; padding:6px 0 8px; border-bottom:1px solid var(--rule); }}
  .builder:fullscreen {{ background:#fbfaf8; padding:16px 28px; overflow:auto; border-radius:0; }}
  .fsbtn {{ margin-left:6px; }}
  button {{ background:var(--steel); color:#fff; border:none; padding:9px 16px; border-radius:7px; font-family:var(--mono); font-size:12px; letter-spacing:.06em; text-transform:uppercase; font-weight:600; cursor:pointer; }}
  button.secondary {{ background:#fff; color:var(--steel); border:1px solid var(--steel); }}
  button:disabled {{ opacity:.4; cursor:default; }}
  .steplabel {{ font-family:var(--mono); font-size:12px; color:var(--ink-mute); margin-left:auto; }}
  .prog {{ height:4px; background:#efe7da; border-radius:3px; margin:12px 0 8px; overflow:hidden; }}
  .prog-fill {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#d98a5f); border-radius:3px; transition:width .35s ease; }}
  .narration {{ background:var(--paper-warm); border-left:4px solid var(--accent); border-radius:0 8px 8px 0; padding:14px 18px; margin:4px 0 16px; font-size:15.5px; color:var(--ink-soft); line-height:1.5; min-height:52px; }}
  .ncard {{ display:grid; grid-template-columns:1.3fr 1fr; gap:20px; align-items:center; padding:16px 0; border-bottom:1px dashed #e9e0d0; }}
  .ncard:last-child {{ border-bottom:none; }}
  @media (max-width:780px) {{ .ncard {{ grid-template-columns:1fr; }} }}
  .cardsvg {{ width:100%; height:auto; max-height:620px; display:block; }}
  .nexplain h4 {{ font-family:var(--serif); font-size:18px; font-weight:600; margin:0 0 6px; }}
  .nexplain p {{ margin:0; font-size:14.5px; }}
  .uml-text {{ font-family:var(--sans); font-size:13px; fill:var(--ink); }}
  .uml-line {{ stroke:var(--ink); stroke-width:1.4; fill:none; }}
  .uml-box {{ stroke:var(--ink); stroke-width:1.4; fill:#fff; }}
  .bstep {{ opacity:0; transform:translateY(8px) scale(.95); transform-box:fill-box; transform-origin:center; transition:opacity .3s ease, transform .42s cubic-bezier(.2,.8,.3,1), filter .35s ease; }}
  .bstep.on {{ opacity:1; transform:translateY(0) scale(1); }}
  .bstep.current {{ filter:drop-shadow(0 0 6px rgba(184,92,56,.5)); }}
  .estep {{ opacity:.25; transform:translateY(6px); transition:opacity .35s ease, transform .4s ease; }}
  .estep.on {{ opacity:1; transform:none; }}
</style></head>
<body><div class="wrap">
  <div class="eyebrow">COMP433 &middot; Chapter 4 &middot; activity notations</div>
  <h1>Activity diagrams: parallel work and choices</h1>
  <p class="lead">The booking flow used an initial node, actions, decisions, a loop and final nodes. Two more notations complete the set: the fork and join for parallel work, and the merge that closes a decision.</p>
  <div class="builder" id="builder">
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
function bPlay(){{ if(timer){{stopPlay();return;}} if(cur===MAX)cur=0; const _b=document.getElementById('builder'); if(_b&&!document.fullscreenElement&&_b.requestFullscreen) _b.requestFullscreen(); document.getElementById('play').textContent='Pause'; timer=setInterval(()=>{{ if(cur>=MAX){{stopPlay();return;}} cur++; render(); }}, 2100); }}
render();
</script>
</body></html>'''
open("poc_activity_notations.html","w",encoding="utf-8").write(HTML)
print("wrote activity notations; steps:", MAX)
