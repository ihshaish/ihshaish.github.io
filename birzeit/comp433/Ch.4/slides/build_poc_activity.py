# Animated build of an ACTIVITY diagram, unpacking the Book room use case.
def act(cx,cy,label,w=150,h=40):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text">{label}</text>'
def arr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#fArrow)"/>'
def parr(pts): return f'<polyline points="{pts}" class="uml-line" fill="none" marker-end="url(#fArrow)"/>'
def dia(cx,cy,t1,t2="",hw=40,hh=24):
    p=f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" class="uml-box"/>'
    if t2: p+=f'<text x="{cx}" y="{cy-2}" text-anchor="middle" class="uml-text" font-size="10">{t1}</text><text x="{cx}" y="{cy+10}" text-anchor="middle" class="uml-text" font-size="10">{t2}</text>'
    else: p+=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t1}</text>'
    return p
def gl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="11">{t}</text>'
def bar(x1,x2,y): return f'<rect x="{x1}" y="{y-3}" width="{x2-x1}" height="6" rx="2" fill="#2c3540"/>'
def g(n,*p,cls="bstep"): return f'<g class="{cls}" data-step="{n}">'+''.join(p)+'</g>'

S=['<defs><marker id="fArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>']
# 1 lanes
S.append(g(1,
 '<rect x="40" y="60" width="370" height="840" fill="#faf7f2" stroke="#d8cfc0"/>',
 '<rect x="410" y="60" width="370" height="840" fill="white" stroke="#d8cfc0"/>',
 '<rect x="780" y="60" width="320" height="840" fill="#faf7f2" stroke="#d8cfc0"/>',
 '<text x="225" y="88" text-anchor="middle" class="uml-text" font-weight="600">Guest</text>',
 '<text x="595" y="88" text-anchor="middle" class="uml-text" font-weight="600">Booking System</text>',
 '<text x="940" y="88" text-anchor="middle" class="uml-text" font-weight="600">Payment Provider</text>',
 '<line x1="40" y1="112" x2="1100" y2="112" class="uml-line"/>'))
# 2 initial + Search rooms
S.append(g(2,'<circle cx="225" cy="142" r="9" fill="#0f1419"/>', arr(225,151,225,178), act(225,200,"Search rooms")))
# 3 hand-off + Find available rooms
S.append(g(3, arr(300,200,505,200), act(595,200,"Find available rooms",w=170)))
# 4 decision rooms available?
S.append(g(4, arr(595,220,595,262), dia(595,290,"rooms","available?",hw=52,hh=28)))
# 5 [no] -> final
S.append(g(5, parr("595,318 595,360 470,360"), gl(498,352,"[no]"),
 '<circle cx="455" cy="360" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="455" cy="360" r="5" fill="#0f1419"/>'))
# 6 [yes] -> Select room
S.append(g(6, parr("647,290 700,290 700,420 300,420"), gl(662,283,"[yes]"), act(225,420,"Select room")))
# 7 Enter payment details
S.append(g(7, arr(225,440,225,478), act(225,500,"Enter payment details")))
# 8 hand-off -> Authorise payment
S.append(g(8, arr(300,500,865,500), act(940,500,"Authorise payment",w=160)))
# 9 decision approved?
S.append(g(9, arr(940,520,940,556), dia(940,590,"approved?",hw=46)))
# 10 [declined] retry loop
S.append(g(10, parr("940,614 940,880 225,880 225,522"), gl(582,872,"[declined]: retry payment","middle")))
# 11 [approved] -> Reserve room
S.append(g(11, parr("894,590 595,590 595,628"), gl(735,583,"[approved]"), act(595,650,"Reserve room")))
# 12 fork
S.append(g(12, arr(595,670,595,692), bar(560,975,698)))
# 13 parallel branches: Confirm booking || Capture payment
S.append(g(13, arr(595,701,595,727), act(595,748,"Confirm booking"),
               arr(940,701,940,727), act(940,748,"Capture payment",w=160)))
# 14 join
S.append(g(14, arr(595,768,595,792), arr(940,768,940,792), bar(560,975,796)))
# 15 final
S.append(g(15, arr(595,802,595,828), '<circle cx="595" cy="841" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="595" cy="841" r="5" fill="#0f1419"/>'))
SVG="".join(S)

NARR=[
 "This activity diagram unpacks one use case, Book room, into its flow of work. The steps come from the use case description on the left, watch each one light up. Use Next, or press Play.",
 "First, swimlanes: one column per participant, the Guest, the Booking System, and the external Payment Provider. Each action goes in the lane of whoever performs it, and an arrow that crosses a lane boundary is a hand-off.",
 "The initial node, a filled circle, marks where the flow begins. There is exactly one. The Guest's first action is Search rooms.",
 "Control hands off to the Booking System, which finds the available rooms. The arrow crossing into the system's lane is that hand-off.",
 "A decision node, the diamond, asks whether rooms are available. A decision has guarded branches and exactly one is taken. It reflects the pre-condition that a room must be available.",
 "If none are available, the flow stops at a final node. An activity can have more than one final node, this is one way it can end.",
 "Otherwise the Guest selects a room: workflow step 1 of the description.",
 "and enters payment details: step 2.",
 "Now a hand-off to the external Payment Provider, the same secondary actor from the use case diagram, shown here as its own lane. It authorises the payment: step 3.",
 "A second decision: was the payment approved?",
 "If declined, the flow loops back to Enter payment details so the Guest can try again. This is a retry loop, a decision branch that returns into the flow, the alternative path named in the description.",
 "If approved, the Booking System reserves the room: step 4.",
 "Now two things happen at once. A fork node, the heavy bar, splits the flow into concurrent branches that proceed independently.",
 "The Booking System confirms the booking to the Guest (step 5) while, in parallel, the Payment Provider captures the authorised payment. Neither branch waits for the other.",
 "A join node, the second bar, synchronises the branches: the flow waits until both have finished before it goes on.",
 "The bull's-eye final node ends the successful path. The diagram is complete: swimlanes, an initial node, actions, two decisions, a retry loop, a hand-off to an external provider, a parallel fork and join, and two final nodes, all unpacked from one use case.",
]
MAX=len(NARR)-1
HL={4:['wf-pre'],6:['wf1'],7:['wf2'],8:['wf3'],10:['wf-alt'],11:['wf4'],13:['wf5']}
import json
HTML=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Activity diagram: animated build</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
  :root {{ --ink:#0f1419; --ink-soft:#2c3540; --ink-mute:#5a6473; --paper:#faf7f2; --paper-warm:#f3ede2; --accent:#b85c38; --steel:#2c5f7c; --rule:#d8cfc0;
    --serif:'Fraunces',Georgia,serif; --sans:'Inter Tight',-apple-system,sans-serif; --mono:'JetBrains Mono',monospace; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:var(--sans); color:var(--ink); background:#fbfaf8; margin:0; padding:44px 24px 90px; line-height:1.55; }}
  .wrap {{ max-width:1080px; margin:0 auto; }}
  .eyebrow {{ font-family:var(--mono); font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--accent); font-weight:600; margin-bottom:10px; }}
  h1 {{ font-family:var(--serif); font-weight:500; font-size:36px; letter-spacing:-.02em; margin:0 0 12px; }}
  h2 {{ font-family:var(--serif); font-weight:600; font-size:20px; margin:28px 0 10px; }}
  p {{ max-width:900px; color:var(--ink-soft); }} .lead {{ font-size:16px; }} .lead strong {{ color:var(--ink); }}
  .layout {{ display:grid; grid-template-columns:320px 1fr; gap:18px; align-items:start; margin-top:16px; }}
  @media (max-width:900px) {{ .layout {{ grid-template-columns:1fr; }} }}
  .card {{ background:#fff; border:1px solid var(--rule); border-radius:12px; padding:16px 18px; box-shadow:0 1px 0 rgba(15,20,25,.03); position:sticky; top:16px; }}
  .card h3 {{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--steel); margin:0 0 10px; }}
  .card .row {{ font-size:13.5px; padding:5px 0; border-bottom:1px dashed var(--rule); }}
  .card .row:last-child {{ border-bottom:none; }} .card .k {{ font-family:var(--mono); font-size:11px; color:var(--steel); }}
  .hl {{ background:#fbe3d0; border-radius:3px; padding:0 3px; box-shadow:0 0 0 1px #eebf9f; }}
  .builder {{ border:1px solid var(--rule); border-radius:16px; padding:18px 20px 24px; background:#fff; box-shadow:0 10px 34px rgba(15,20,25,.07); }}
  .controls {{ display:flex; align-items:center; gap:10px; }}
  button {{ background:var(--steel); color:#fff; border:none; padding:9px 16px; border-radius:7px; font-family:var(--mono); font-size:12px; letter-spacing:.06em; text-transform:uppercase; font-weight:600; cursor:pointer; }}
  button.secondary {{ background:#fff; color:var(--steel); border:1px solid var(--steel); }}
  button:disabled {{ opacity:.4; cursor:default; }}
  .steplabel {{ font-family:var(--mono); font-size:12px; color:var(--ink-mute); margin-left:auto; }}
  .prog {{ height:4px; background:#efe7da; border-radius:3px; margin:12px 0 8px; overflow:hidden; }}
  .prog-fill {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#d98a5f); border-radius:3px; transition:width .35s ease; }}
  .narration {{ background:var(--paper-warm); border-left:4px solid var(--accent); border-radius:0 8px 8px 0; padding:15px 19px; margin:4px 0 14px; font-size:16px; color:var(--ink-soft); line-height:1.5; min-height:66px; }}
  svg {{ width:100%; height:auto; display:block; }}
  .uml-text {{ font-family:var(--sans); font-size:12px; fill:var(--ink); }}
  .uml-line {{ stroke:var(--ink); stroke-width:1.4; fill:none; }}
  .uml-box {{ stroke:var(--ink); stroke-width:1.4; fill:#fff; }}
  .bstep {{ opacity:0; transform:translateY(12px) scale(.92); transform-box:fill-box; transform-origin:center; transition:opacity .3s ease, transform .42s cubic-bezier(.2,.8,.3,1), filter .35s ease; }}
  .bstep.on {{ opacity:1; transform:translateY(0) scale(1); }}
  .bstep.current {{ filter:drop-shadow(0 0 7px rgba(184,92,56,.55)); }}
</style></head>
<body><div class="wrap">
  <div class="eyebrow">COMP433 &middot; Chapter 4 &middot; building an activity diagram</div>
  <h1>Unpacking a use case into an activity diagram</h1>
  <p class="lead">A use case diagram says <em>what</em> the system does; an <strong>activity diagram</strong> shows <em>how one use case flows</em>, in what order, with which decisions, and who does each step. Here we take the <strong>Book room</strong> use case and unpack its description (left) into a flow.</p>

  <div class="layout">
    <div class="card"><h3>Book room &middot; use case description</h3>
      <div class="row"><span class="k">Actors</span> &nbsp;Guest, Payment Provider</div>
      <div class="row" id="wf-pre"><span class="k">Pre</span> &nbsp;at least one room is available</div>
      <div class="row" id="wf1"><span class="k">1</span> &nbsp;Guest selects a room</div>
      <div class="row" id="wf2"><span class="k">2</span> &nbsp;Guest enters details and card</div>
      <div class="row" id="wf3"><span class="k">3</span> &nbsp;System requests authorisation from the provider</div>
      <div class="row" id="wf4"><span class="k">4</span> &nbsp;On approval, the room is reserved</div>
      <div class="row" id="wf5"><span class="k">5</span> &nbsp;Booking is confirmed</div>
      <div class="row" id="wf-alt"><span class="k">Alt</span> &nbsp;if declined, re-enter and retry; if no room, end</div>
    </div>
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
      <svg viewBox="0 0 1140 920" xmlns="http://www.w3.org/2000/svg" id="buildSvg" role="img" aria-label="Activity diagram being constructed step by step from the Book room use case.">{SVG}</svg>
    </div>
  </div>
</div>
<script>
const NARR={json.dumps(NARR)}, HL={json.dumps(HL)}, MAX={MAX};
let cur=0, timer=null;
function render(){{
  document.querySelectorAll('#buildSvg .bstep').forEach(g=>{{ const n=parseInt(g.getAttribute('data-step')); g.classList.toggle('on', n<=cur); g.classList.toggle('current', n===cur); }});
  document.querySelectorAll('.hl').forEach(e=>e.classList.remove('hl'));
  (HL[cur]||[]).forEach(id=>{{ const e=document.getElementById(id); if(e) e.classList.add('hl'); }});
  document.getElementById('narr').innerHTML=NARR[cur];
  document.getElementById('lbl').textContent='Step '+cur+' of '+MAX;
  document.getElementById('progfill').style.width=(cur/MAX*100)+'%';
  document.getElementById('prev').disabled=cur===0;
  document.getElementById('next').disabled=cur===MAX;
}}
function bNext(){{ if(cur<MAX){{cur++;render();}} }}
function bPrev(){{ if(cur>0){{cur--;render();}} }}
function bReset(){{ cur=0; stopPlay(); render(); }}
function stopPlay(){{ if(timer){{clearInterval(timer);timer=null;document.getElementById('play').innerHTML='&#9658; Play';}} }}
function bPlay(){{ if(timer){{stopPlay();return;}} if(cur===MAX)cur=0; document.getElementById('play').textContent='Pause'; timer=setInterval(()=>{{ if(cur>=MAX){{stopPlay();return;}} cur++; render(); }}, 2100); }}
render();
</script>
</body></html>'''
open("poc_activity_build.html","w",encoding="utf-8").write(HTML)
print("wrote activity build; steps:", MAX)
