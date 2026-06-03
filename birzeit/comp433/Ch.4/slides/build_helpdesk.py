# Helpdesk (second domain): two animated builders on one page (use case + activity),
# instance-based engine (multiple builders per page) -- the pattern reused for integration.

# ---------- shared svg helpers ----------
def uc(cx,cy,label,rx=86,ry=24):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{label}</text>'
def actorNL(x,y):
    return (f'<g transform="translate({x},{y})"><circle cx="16" cy="6" r="7" class="actor-blue"/>'
            f'<line x1="16" y1="13" x2="16" y2="36" class="uml-line-blue"/><line x1="16" y1="19" x2="4" y2="28" class="uml-line-blue"/><line x1="16" y1="19" x2="28" y2="28" class="uml-line-blue"/><line x1="16" y1="36" x2="4" y2="50" class="uml-line-blue"/><line x1="16" y1="36" x2="28" y2="50" class="uml-line-blue"/></g>')
def nm(x,y,t): return f'<text x="{x}" y="{y}" text-anchor="middle" class="uml-text" font-size="10" font-weight="600">{t}</text>'
def bl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-blue"/>'
def assoc(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-blue" marker-end="url(#hdAssoc)"/>'
def inc(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-dashed" marker-end="url(#hdOpen)"/>'
def extl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7a3a23" stroke-width="1.2" stroke-dasharray="4,3" fill="none" marker-end="url(#hdOpenR)"/>'
def gen(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#hdGen)"/>'
def lblm(x,y,t,c="#2c3540"): return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="{c}" font-weight="600">{t}</text>'
def gs(n,*p): return f'<g class="bstep" data-step="{n}">'+''.join(p)+'</g>'
UCDEFS=('<defs>'
 '<marker id="hdAssoc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#4a8bb8"/></marker>'
 '<marker id="hdOpen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#2c3540" stroke-width="1.4"/></marker>'
 '<marker id="hdOpenR" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#7a3a23" stroke-width="1.4"/></marker>'
 '<marker id="hdGen" viewBox="0 0 14 14" refX="13" refY="7" markerWidth="14" markerHeight="14" orient="auto"><path d="M 1 1 L 13 7 L 1 13 Z" fill="white" stroke="#0f1419" stroke-width="1.2"/></marker>'
 '</defs>')

# ---------- USE CASE build ----------
U=[UCDEFS]
U.append(gs(1,'<rect x="240" y="70" width="700" height="520" rx="8" class="uml-box" fill="#faf7f2" stroke-width="1.8"/>','<text x="590" y="60" text-anchor="middle" class="uml-text" font-weight="600" font-size="13">Help Desk System</text>'))
U.append(gs(2, actorNL(60,250), nm(76,316,"Customer")))
U.append(gs(3, uc(400,160,"Submit ticket"), bl(92,266,314,166)))
U.append(gs(4, uc(400,270,"Track ticket"), bl(92,272,314,270)))
U.append(gs(5, uc(400,380,"Reopen ticket"), bl(92,278,314,380)))
U.append(gs(6, actorNL(1090,140), nm(1106,128,"Support Agent")))
U.append(gs(7, uc(650,300,"Resolve ticket"), bl(1090,166,736,296)))
U.append(gs(8, uc(450,490,"Search knowledge base",rx=100), inc(588,322,512,468), lblm(580,398,"&lt;&lt;include&gt;&gt;")))
U.append(gs(9, uc(800,470,"Notify customer"), inc(706,318,746,448), lblm(752,388,"&lt;&lt;include&gt;&gt;")))
U.append(gs(10, actorNL(1090,500), nm(1106,566,"Notification Service"), assoc(886,472,1086,512)))
U.append(gs(11, uc(820,190,"Escalate ticket"), extl(760,212,673,287), lblm(648,236,"&lt;&lt;extend&gt;&gt;","#7a3a23"), lblm(648,253,"[complex]","#7a3a23")))
U.append(gs(12, actorNL(1090,330), nm(1106,396,"Senior Agent"), gen(1106,330,1106,212), bl(1090,352,890,212)))
UC_SVG="".join(U)
UC_NARR=[
 "A second worked example: a Help Desk system. The same notation, a new domain. Use Next, or press Play.",
 "The system boundary: the Help Desk System.",
 "The Customer is a primary actor, the person who raises and follows tickets.",
 "Submit ticket is the Customer's first task, joined by a plain association.",
 "The Customer can also Track ticket, to follow its progress.",
 "and Reopen ticket if the problem comes back. One actor usually has several use cases.",
 "The Support Agent is the actor who works on tickets.",
 "Resolve ticket is the agent's main task.",
 "Resolving a ticket always starts by checking the knowledge base, so Search knowledge base is an &lt;&lt;include&gt;&gt;: an always-performed sub-task, with the arrow from the base to the included use case.",
 "It also always ends by telling the customer, so Notify customer is a second &lt;&lt;include&gt;&gt;.",
 "Notify customer reaches an external Notification Service, a secondary actor outside the boundary, with the association arrow pointing to it.",
 "Hard tickets are sometimes escalated. Escalate ticket is an &lt;&lt;extend&gt;&gt; on Resolve ticket, firing only under the guard [complex]; its arrow points back to the base.",
 "A Senior Agent is a kind of Support Agent (the hollow triangle points to the general actor): it inherits every Support Agent use case and also handles escalations. That is actor generalisation.",
]

# ---------- ACTIVITY build ----------
def act(cx,cy,label,w=150,h=38):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{label}</text>'
def dia(cx,cy,t,hw=46,hh=26): return f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t}</text>'
def aarr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#hdA)"/>'
def apl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line"/>'
def aparr(pts): return f'<polyline points="{pts}" class="uml-line" fill="none" marker-end="url(#hdA)"/>'
def appl(pts): return f'<polyline points="{pts}" class="uml-line" fill="none"/>'
def agl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="11">{t}</text>'
def initial(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="9" fill="#0f1419"/>'
def final(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="{cx}" cy="{cy}" r="5" fill="#0f1419"/>'
ADEFS='<defs><marker id="hdA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'
def abar(cx,y,w=384): return f'<rect x="{cx-w//2}" y="{y}" width="{w}" height="7" rx="2" fill="#2c3540"/>'
A=[ADEFS]
A.append(gs(1,'<rect x="40" y="60" width="320" height="800" fill="#faf7f2" stroke="#d8cfc0"/>','<rect x="360" y="60" width="400" height="800" fill="white" stroke="#d8cfc0"/>','<rect x="760" y="60" width="300" height="800" fill="#faf7f2" stroke="#d8cfc0"/>',
 '<text x="200" y="88" text-anchor="middle" class="uml-text" font-weight="600">Customer</text>','<text x="560" y="88" text-anchor="middle" class="uml-text" font-weight="600">Support Agent</text>','<text x="910" y="88" text-anchor="middle" class="uml-text" font-weight="600">Notification Service</text>','<line x1="40" y1="112" x2="1060" y2="112" class="uml-line"/>'))
A.append(gs(2, initial(200,142), aarr(200,151,200,176), act(200,198,"Submit ticket")))
A.append(gs(3, aarr(276,198,485,198), act(560,198,"Log ticket")))
A.append(gs(4, aarr(560,217,560,254), act(560,288,"Search knowledge base",w=180)))
A.append(gs(5, aarr(560,307,560,338), dia(560,366,"resolved?")))
A.append(gs(6, aparr("560,392 560,440"), agl(572,422,"[no]"), act(560,464,"Escalate to senior",w=170)))
A.append(gs(7, aarr(560,483,560,540), aparr("606,366 700,366 700,560 590,560"), agl(712,360,"[yes]"), dia(560,560,"",hw=30,hh=18)))
A.append(gs(8, aarr(560,578,560,606), abar(735,608), aarr(560,615,560,648), act(560,670,"Update knowledge base",w=180), aarr(910,615,910,648), act(910,670,"Notify customer",w=156)))
A.append(gs(9, apl(560,692,560,728), apl(910,692,910,728), abar(735,728), aarr(560,735,560,768), act(560,790,"Close ticket"), aarr(560,809,560,819), final(560,831)))
ACT_SVG="".join(A)
ACT_NARR=[
 "Now the Resolve ticket flow as an activity diagram, across three lanes. Use Next, or press Play.",
 "Three swimlanes: the Customer, the Support Agent, and the external Notification Service.",
 "The initial node starts the flow; the Customer submits a ticket.",
 "Control hands off to the Support Agent, who logs the ticket.",
 "The agent searches the knowledge base for a known fix.",
 "A decision: was it resolved?",
 "If not, the agent escalates it to a senior, who resolves it.",
 "If it was resolved, that branch skips ahead; either way a merge brings the two paths back together.",
 "Then a fork splits the flow so two things happen in parallel: the agent updates the knowledge base while the Notification Service notifies the customer.",
 "A join waits for both to finish; the agent then closes the ticket and the flow ends at the final node.",
]

import json
def builder(bid, svg, vb, narr, title, sub):
    return f'''  <h2>{title}</h2>
  <p class="sub">{sub}</p>
  <div class="builder" id="{bid}">
    <div class="controls">
      <button class="bprev">Previous</button><button class="bnext">Next</button>
      <button class="breset secondary">Reset</button><button class="bplay secondary">&#9658; Play</button>
      <span class="lbl steplabel"></span>
    </div>
    <div class="prog"><div class="pfill"></div></div>
    <div class="narr"></div>
    <svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" class="dsvg" role="img" aria-label="{title}">{svg}</svg>
  </div>'''
HTML=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Help Desk: worked example</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {{ --ink:#0f1419; --ink-soft:#2c3540; --ink-mute:#5a6473; --paper:#faf7f2; --paper-warm:#f3ede2; --accent:#b85c38; --steel:#2c5f7c; --rule:#d8cfc0;
    --serif:'Fraunces',Georgia,serif; --sans:'Inter Tight',-apple-system,sans-serif; --mono:'JetBrains Mono',monospace; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:var(--sans); color:var(--ink); background:#fbfaf8; margin:0; padding:44px 24px 90px; line-height:1.55; }}
  .wrap {{ max-width:1120px; margin:0 auto; }}
  .eyebrow {{ font-family:var(--mono); font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--accent); font-weight:600; margin-bottom:10px; }}
  h1 {{ font-family:var(--serif); font-weight:500; font-size:34px; letter-spacing:-.02em; margin:0 0 10px; }}
  h2 {{ font-family:var(--serif); font-weight:600; font-size:21px; margin:30px 0 4px; }}
  p {{ color:var(--ink-soft); }} .lead {{ font-size:16px; max-width:900px; }} .sub {{ font-size:14px; color:var(--ink-mute); margin:0 0 8px; }}
  .scenario {{ background:#fff; border:1px solid var(--rule); border-radius:12px; padding:16px 20px; margin-top:14px; font-size:14.5px; }}
  .builder {{ border:1px solid var(--rule); border-radius:16px; padding:16px 18px 22px; margin-top:8px; background:#fff; box-shadow:0 8px 28px rgba(15,20,25,.06); }}
  .controls {{ display:flex; align-items:center; gap:10px; }}
  button {{ background:var(--steel); color:#fff; border:none; padding:9px 16px; border-radius:7px; font-family:var(--mono); font-size:12px; letter-spacing:.06em; text-transform:uppercase; font-weight:600; cursor:pointer; }}
  button.secondary {{ background:#fff; color:var(--steel); border:1px solid var(--steel); }}
  button:disabled {{ opacity:.4; cursor:default; }}
  .lbl {{ font-family:var(--mono); font-size:12px; color:var(--ink-mute); margin-left:auto; }}
  .prog {{ height:4px; background:#efe7da; border-radius:3px; margin:12px 0 8px; overflow:hidden; }}
  .pfill {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#d98a5f); border-radius:3px; transition:width .35s ease; }}
  .narr {{ background:var(--paper-warm); border-left:4px solid var(--accent); border-radius:0 8px 8px 0; padding:14px 18px; margin:4px 0 14px; font-size:15.5px; color:var(--ink-soft); line-height:1.5; min-height:52px; }}
  .dsvg {{ width:100%; height:auto; display:block; }}
  .uml-text {{ font-family:var(--sans); font-size:12px; fill:var(--ink); }}
  .uml-line {{ stroke:var(--ink); stroke-width:1.4; fill:none; }}
  .uml-line-dashed {{ stroke:var(--ink); stroke-width:1.2; fill:none; stroke-dasharray:4,3; }}
  .uml-line-blue {{ stroke:#4a8bb8; stroke-width:1.4; fill:none; }}
  .uml-box {{ stroke:var(--ink); stroke-width:1.4; fill:#fff; }}
  .actor-blue {{ stroke:#2c6e9a; stroke-width:1.4; fill:#eaf3f9; }}
  .bstep {{ opacity:0; transform:translateY(10px) scale(.94); transform-box:fill-box; transform-origin:center; transition:opacity .3s ease, transform .42s cubic-bezier(.2,.8,.3,1), filter .35s ease; }}
  .bstep.on {{ opacity:1; transform:translateY(0) scale(1); }}
  .bstep.current {{ filter:drop-shadow(0 0 6px rgba(184,92,56,.5)); }}
</style></head>
<body><div class="wrap">
  <div class="eyebrow">COMP433 &middot; Chapter 4 &middot; worked example</div>
  <h1>A second domain: the Help Desk system</h1>
  <p class="lead">The same use case and activity notations applied to a fresh scenario, so you can see the method again, end to end.</p>
  <div class="scenario"><strong>Scenario.</strong> Customers raise support tickets. A support agent works each ticket: they always check the knowledge base first and always notify the customer of the outcome through an external notification service. Hard ("complex") tickets are escalated to a senior agent, who is a more capable kind of support agent. The system also lets agents follow tickets through to closure.</div>
{builder("hduc", UC_SVG, "0 0 1180 620", UC_NARR, "Use case diagram", "Built from the scenario: actors, use cases, include, extend, a secondary actor, and actor generalisation.")}
{builder("hdact", ACT_SVG, "0 0 1080 880", ACT_NARR, "Activity diagram", "The Resolve ticket flow across three swimlanes, with a decision, a merge, and an external hand-off.")}
</div>
<script>
const NARR={{ "hduc": {json.dumps(UC_NARR)}, "hdact": {json.dumps(ACT_NARR)} }};
function makeBuilder(root){{
  const narr=NARR[root.id], MAX=narr.length-1; let cur=0, timer=null;
  const el=s=>root.querySelector(s);
  function render(){{
    root.querySelectorAll('[data-step]').forEach(e=>{{ const n=parseInt(e.getAttribute('data-step')); e.classList.toggle('on', n<=cur); if(e.classList.contains('bstep')) e.classList.toggle('current', n===cur); }});
    el('.narr').innerHTML=narr[cur];
    el('.lbl').textContent='Step '+cur+' of '+MAX;
    el('.pfill').style.width=(cur/MAX*100)+'%';
    el('.bprev').disabled=cur===0; el('.bnext').disabled=cur===MAX;
  }}
  function stop(){{ if(timer){{clearInterval(timer);timer=null;el('.bplay').innerHTML='&#9658; Play';}} }}
  el('.bprev').onclick=()=>{{ if(cur>0){{cur--;render();}} }};
  el('.bnext').onclick=()=>{{ if(cur<MAX){{cur++;render();}} }};
  el('.breset').onclick=()=>{{ cur=0; stop(); render(); }};
  el('.bplay').onclick=()=>{{ if(timer){{stop();return;}} if(cur===MAX)cur=0; el('.bplay').textContent='Pause'; timer=setInterval(()=>{{ if(cur>=MAX){{stop();return;}} cur++; render(); }}, 2100); }};
  render();
}}
document.querySelectorAll('.builder').forEach(makeBuilder);
</script>
</body></html>'''
open("poc_helpdesk.html","w",encoding="utf-8").write(HTML)
print("wrote helpdesk; uc steps:", len(UC_NARR)-1, "act steps:", len(ACT_NARR)-1)
