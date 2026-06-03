# Animated build of an ACTIVITY diagram, unpacking the Book room use case.
def act(cx,cy,label,w=150,h=40):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text">{label}</text>'
def arr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#fArrow)"/>'
def parr(pts): return f'<polyline points="{pts}" class="uml-line" fill="none" marker-end="url(#fArrow)"/>'
def dia(cx,cy,t1,t2="",hw=40,hh=24):
    p=f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" class="uml-box"/>'
    if t2: p+=f'<text x="{cx}" y="{cy-2}" text-anchor="middle" class="uml-text" font-size="11">{t1}</text><text x="{cx}" y="{cy+11}" text-anchor="middle" class="uml-text" font-size="11">{t2}</text>'
    elif t1: p+=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{t1}</text>'
    return p
def gl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="12">{t}</text>'
def bar(x1,x2,y): return f'<rect x="{x1}" y="{y-3}" width="{x2-x1}" height="6" rx="2" fill="#2c3540"/>'
def fin(cx,cy): return f'<circle cx="{cx}" cy="{cy}" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="{cx}" cy="{cy}" r="5" fill="#0f1419"/>'
def g(n,*p,cls="bstep"): return f'<g class="{cls}" data-step="{n}">'+''.join(p)+'</g>'

S=['<defs><marker id="fArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>']
# 1 lanes
S.append(g(1,
 '<rect x="40" y="60" width="370" height="1020" fill="#faf7f2" stroke="#d8cfc0"/>',
 '<rect x="410" y="60" width="370" height="1020" fill="white" stroke="#d8cfc0"/>',
 '<rect x="780" y="60" width="320" height="1020" fill="#faf7f2" stroke="#d8cfc0"/>',
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
S.append(g(5, parr("595,318 595,360 470,360"), gl(498,352,"[no]"), fin(455,360)))
# 6 [yes] -> Select room
S.append(g(6, parr("647,290 700,290 700,420 300,420"), gl(662,283,"[yes]"), act(225,420,"Select room")))
# 7 promo decision (the activity form of the Apply promo code <<extend>>)
S.append(g(7, arr(225,440,225,461), dia(225,490,"has promo?",hw=60,hh=27)))
# 8 [yes] -> Apply promo code
S.append(g(8, parr("165,490 120,490 120,558"), gl(132,482,"[yes]","middle"), act(120,580,"Apply promo code",w=150)))
# 9 [no] + merge -> Enter payment details
S.append(g(9, parr("225,517 225,607"), gl(238,560,"[no]"),
              parr("120,600 120,625 197,625"),
              dia(225,625,"",hw=28,hh=18),
              arr(225,643,225,668), act(225,690,"Enter payment details")))
# 10 hand-off -> Authorise payment
S.append(g(10, arr(300,690,865,690), act(940,690,"Authorise payment",w=160)))
# 11 decision approved?
S.append(g(11, arr(940,710,940,748), dia(940,778,"approved?",hw=48)))
# 12 [declined] retry loop (routed clear of the fork/join on the right)
S.append(g(12, parr("988,778 1060,778 1060,1042 225,1042 225,712"), gl(582,1034,"[declined]: retry payment","middle")))
# 13 [approved] -> Reserve room
S.append(g(13, parr("892,778 595,778 595,803"), gl(735,771,"[approved]"), act(595,825,"Reserve room")))
# 14 fork
S.append(g(14, arr(595,845,595,867), bar(560,975,873)))
# 15 parallel branches: Confirm booking || Capture payment
S.append(g(15, arr(595,876,595,902), act(595,923,"Confirm booking"),
               arr(940,876,940,902), act(940,923,"Capture payment",w=160)))
# 16 join
S.append(g(16, arr(595,943,595,967), arr(940,943,940,967), bar(560,975,971)))
# 17 final
S.append(g(17, arr(595,977,595,1000), fin(595,1013)))
SVG="".join(S)

NARR=[
 "This activity diagram unpacks one use case, Book room, into its flow of work. The steps come from the use case description above, watch each one light up. Use Next, or press Play.",
 "First, swimlanes: one column per participant, the Guest, the Booking System, and the external Payment Provider. Each action goes in the lane of whoever performs it, and an arrow that crosses a lane boundary is a hand-off.",
 "The initial node, a filled circle, marks where the flow begins. There is exactly one. The Guest's first action is Search rooms.",
 "Control hands off to the Booking System, which finds the available rooms. The arrow crossing into the system's lane is that hand-off.",
 "A decision node, the diamond, asks whether rooms are available. A decision has guarded branches and exactly one is taken. It reflects the pre-condition that a room must be available.",
 "If none are available, the flow stops at a final node. An activity can have more than one final node, this is one way it can end.",
 "Otherwise the Guest selects a room: workflow step 1 of the description.",
 "Before paying comes an optional step (step 2): does the Guest have a promo code? This [has promo?] decision is the activity-diagram form of the Apply promo code <<extend>> you saw on the use case diagram.",
 "If they do, a promo code is applied and a discount taken; if not, the step is skipped. An optional extend use case appears in the flow as exactly this kind of guarded branch.",
 "The two branches merge, and the Guest enters payment details: step 3.",
 "A hand-off to the external Payment Provider, the same secondary actor from the use case diagram, shown here as its own lane. It authorises the payment: step 4.",
 "A second decision: was the payment approved?",
 "If declined, the flow loops back to Enter payment details so the Guest can try again. This is a retry loop, a decision branch that returns into the flow.",
 "If approved, the Booking System reserves the room: step 5.",
 "Now two things happen at once. A fork node, the heavy bar, splits the flow into concurrent branches that proceed independently.",
 "The Booking System confirms the booking to the Guest (step 6) while, in parallel, the Payment Provider captures the authorised payment. Neither branch waits for the other.",
 "A join node, the second bar, synchronises the branches: the flow waits until both finish before it goes on.",
 "The bull's-eye final node ends the successful path. The diagram is complete: swimlanes, an initial node, actions, three decisions (including the optional promo branch), a retry loop, a hand-off to an external provider, a parallel fork and join, and two final nodes, all traceable to the use case.",
]
MAX=len(NARR)-1
HL={4:['wf-pre'],6:['wf1'],7:['wf-promo'],8:['wf-promo'],9:['wf2'],10:['wf3'],12:['wf-alt'],13:['wf4'],15:['wf5']}
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
  body {{ font-family:var(--sans); color:var(--ink); background:#fbfaf8; margin:0; padding:24px 22px 44px; line-height:1.55; }}
  .wrap {{ max-width:1180px; margin:0 auto; }}
  .eyebrow {{ font-family:var(--mono); font-size:11px; letter-spacing:.2em; text-transform:uppercase; color:var(--accent); font-weight:600; margin-bottom:8px; }}
  h1 {{ font-family:var(--serif); font-weight:500; font-size:25px; letter-spacing:-.02em; margin:0 0 8px; }}
  h2 {{ font-family:var(--serif); font-weight:600; font-size:20px; margin:28px 0 10px; }}
  p {{ color:var(--ink-soft); }} .lead {{ font-size:14.5px; max-width:980px; margin:0 0 14px; }} .lead strong {{ color:var(--ink); }}
  .stage {{ display:grid; grid-template-columns:minmax(250px,0.36fr) 1fr; gap:18px; align-items:start; margin-top:4px; }}
  @media (max-width:820px) {{ .stage {{ grid-template-columns:1fr; }} .srccol {{ position:static !important; max-height:none !important; }} }}
  .srccol {{ position:sticky; top:6px; max-height:calc(100vh - 40px); overflow:auto; }}
  .diagram {{ min-width:0; }}
  .desc {{ background:#fff; border:1px solid var(--rule); border-radius:12px; padding:13px 16px; box-shadow:0 1px 0 rgba(15,20,25,.03); }}
  .desc h3 {{ font-family:var(--mono); font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--steel); margin:0 0 8px; }}
  .descrows {{ display:flex; flex-direction:column; }}
  .row {{ font-size:13px; padding:5px 0; border-bottom:1px dashed var(--rule); }}
  .row:last-child {{ border-bottom:none; }} .row .k {{ font-family:var(--mono); font-size:11px; color:var(--steel); margin-right:6px; }}
  .hl {{ background:#fbe3d0; border-radius:3px; padding:1px 5px; box-shadow:0 0 0 1px #eebf9f; }}
  .builder {{ border:1px solid var(--rule); border-radius:16px; padding:18px 20px 22px; background:#fff; box-shadow:0 10px 34px rgba(15,20,25,.07); }}
  .controls {{ display:flex; align-items:center; gap:10px; }}
  button {{ background:var(--steel); color:#fff; border:none; padding:9px 16px; border-radius:7px; font-family:var(--mono); font-size:12px; letter-spacing:.06em; text-transform:uppercase; font-weight:600; cursor:pointer; }}
  button.secondary {{ background:#fff; color:var(--steel); border:1px solid var(--steel); }}
  button:disabled {{ opacity:.4; cursor:default; }}
  .steplabel {{ font-family:var(--mono); font-size:12px; color:var(--ink-mute); margin-left:auto; }}
  .prog {{ height:4px; background:#efe7da; border-radius:3px; margin:12px 0 8px; overflow:hidden; }}
  .prog-fill {{ height:100%; width:0; background:linear-gradient(90deg,var(--accent),#d98a5f); border-radius:3px; transition:width .35s ease; }}
  .narration {{ background:var(--paper-warm); border-left:4px solid var(--accent); border-radius:0 8px 8px 0; padding:14px 18px; margin:4px 0 14px; font-size:16px; color:var(--ink-soft); line-height:1.5; min-height:58px; }}
  .narration code, .narration b {{ color:var(--ink); }}
  svg {{ width:100%; height:auto; display:block; max-height:none; }}
  .builder:fullscreen {{ background:#fbfaf8; padding:18px 28px; overflow:auto; border-radius:0; }}
  .builder:fullscreen .stage {{ grid-template-columns:minmax(300px,0.3fr) 1fr; }}
  .builder:fullscreen .narration {{ font-size:18px; }}
  .builder:fullscreen .srccol {{ max-height:calc(100vh - 150px); }}
  .fsbtn {{ margin-left:6px; }}
  .uml-text {{ font-family:var(--sans); font-size:13px; fill:var(--ink); }}
  .uml-line {{ stroke:var(--ink); stroke-width:1.4; fill:none; }}
  .uml-box {{ stroke:var(--ink); stroke-width:1.4; fill:#fff; }}
  .bstep {{ opacity:0; transform:translateY(12px) scale(.92); transform-box:fill-box; transform-origin:center; transition:opacity .3s ease, transform .42s cubic-bezier(.2,.8,.3,1), filter .35s ease; }}
  .bstep.on {{ opacity:1; transform:translateY(0) scale(1); }}
  .bstep.current {{ filter:drop-shadow(0 0 7px rgba(184,92,56,.55)); }}
</style></head>
<body><div class="wrap">
  <div class="eyebrow">COMP433 &middot; Chapter 4 &middot; building an activity diagram</div>
  <h1>Unpacking a use case into an activity diagram</h1>
  <p class="lead">A use case diagram says <em>what</em> the system does; an <strong>activity diagram</strong> shows <em>how one use case flows</em>, in what order, with which decisions, and who does each step. Here we take the <strong>Book room</strong> use case and unpack its description (beside the diagram) into a flow; as each action is drawn, the description line it comes from lights up. Press <strong>Full screen</strong> to see both at full size.</p>

  <div class="builder" id="builder">
    <div class="controls">
      <button id="prev" onclick="bPrev()">Previous</button>
      <button id="next" onclick="bNext()">Next</button>
      <button class="secondary" onclick="bReset()">Reset</button>
      <button class="secondary" id="play" onclick="bPlay()">&#9658; Play</button>
      <button class="secondary fsbtn" id="fs" onclick="toggleFs()">&#9974; Full screen</button>
      <span class="steplabel" id="lbl"></span>
    </div>
    <div class="prog"><div class="prog-fill" id="progfill"></div></div>
    <div class="narration" id="narr"></div>
    <div class="stage">
      <div class="srccol">
        <div class="desc"><h3>Book room &middot; use case description</h3>
          <div class="descrows">
            <span class="row"><span class="k">Actors</span>Guest, Payment Provider</span>
            <span class="row" id="wf-pre"><span class="k">Pre</span>at least one room is available</span>
            <span class="row" id="wf1"><span class="k">1</span>Guest selects a room</span>
            <span class="row" id="wf-promo"><span class="k">2</span>Guest may apply a promo code (optional)</span>
            <span class="row" id="wf2"><span class="k">3</span>Guest enters details and card</span>
            <span class="row" id="wf3"><span class="k">4</span>System requests authorisation from the provider</span>
            <span class="row" id="wf4"><span class="k">5</span>On approval, the room is reserved</span>
            <span class="row" id="wf5"><span class="k">6</span>Booking is confirmed</span>
            <span class="row" id="wf-alt"><span class="k">Alt</span>if declined, re-enter and retry; if no room, end</span>
          </div>
        </div>
      </div>
      <div class="diagram">
        <svg viewBox="0 0 1140 1080" xmlns="http://www.w3.org/2000/svg" id="buildSvg" role="img" aria-label="Activity diagram being constructed step by step from the Book room use case.">{SVG}</svg>
      </div>
    </div>
  </div>
</div>
<script>
const NARR={json.dumps(NARR)}, HL={json.dumps(HL)}, MAX={MAX};
let cur=0, timer=null;
function esc(s){{ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }}
function render(){{
  document.querySelectorAll('#buildSvg .bstep').forEach(g=>{{ const n=parseInt(g.getAttribute('data-step')); g.classList.toggle('on', n<=cur); g.classList.toggle('current', n===cur); }});
  document.querySelectorAll('.hl').forEach(e=>e.classList.remove('hl'));
  (HL[cur]||[]).forEach(id=>{{ const e=document.getElementById(id); if(e) e.classList.add('hl'); }});
  document.getElementById('narr').innerHTML=esc(NARR[cur]);
  document.getElementById('lbl').textContent='Step '+cur+' of '+MAX;
  document.getElementById('progfill').style.width=(cur/MAX*100)+'%';
  document.getElementById('prev').disabled=cur===0;
  document.getElementById('next').disabled=cur===MAX;
  if(cur>0){{ const cu=document.querySelector('#buildSvg .bstep.current'); if(cu&&cu.scrollIntoView) cu.scrollIntoView({{behavior:'smooth',block:'center'}}); }}
}}
function bNext(){{ if(cur<MAX){{cur++;render();}} }}
function bPrev(){{ if(cur>0){{cur--;render();}} }}
function toggleFs(){{ const b=document.getElementById('builder'); if(document.fullscreenElement){{document.exitFullscreen();}} else if(b.requestFullscreen){{b.requestFullscreen();}} }}
function bReset(){{ cur=0; stopPlay(); render(); }}
function stopPlay(){{ if(timer){{clearInterval(timer);timer=null;document.getElementById('play').innerHTML='&#9658; Play';}} }}
function bPlay(){{ if(timer){{stopPlay();return;}} if(cur===MAX)cur=0; document.getElementById('play').textContent='Pause'; timer=setInterval(()=>{{ if(cur>=MAX){{stopPlay();return;}} cur++; render(); }}, 2100); }}
render();
</script>
</body></html>'''
open("poc_activity_build.html","w",encoding="utf-8").write(HTML)
print("wrote activity build; steps:", MAX)
