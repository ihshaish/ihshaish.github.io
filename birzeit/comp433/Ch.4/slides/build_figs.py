# Builds standalone SVGs (with inline style) for visual verification.
# The same <defs>+shapes markup is later embedded into the companion (which already defines the classes).

STYLE='''  <style>
    .uml-text { font-family: "Inter Tight", -apple-system, Helvetica, Arial, sans-serif; font-size: 12px; fill: #0f1419; }
    .uml-line { stroke: #0f1419; stroke-width: 1.4; fill: none; }
    .uml-line-dashed { stroke: #0f1419; stroke-width: 1.2; fill: none; stroke-dasharray: 4,3; }
    .uml-line-blue { stroke: #4a8bb8; stroke-width: 1.4; fill: none; }
    .uml-box { stroke: #0f1419; stroke-width: 1.4; fill: white; }
    .actor-blue { stroke: #2c6e9a; stroke-width: 1.4; fill: #eaf3f9; }
    .mono { font-family: "JetBrains Mono", monospace; }
  </style>'''

def actor(x,y,name,sub=""):
    s=f'<g transform="translate({x},{y})">'
    s+='<circle cx="20" cy="6" r="8" class="actor-blue"/>'
    s+='<line x1="20" y1="14" x2="20" y2="42" class="uml-line-blue"/>'
    s+='<line x1="20" y1="22" x2="6" y2="32" class="uml-line-blue"/>'
    s+='<line x1="20" y1="22" x2="34" y2="32" class="uml-line-blue"/>'
    s+='<line x1="20" y1="42" x2="6" y2="58" class="uml-line-blue"/>'
    s+='<line x1="20" y1="42" x2="34" y2="58" class="uml-line-blue"/>'
    s+=f'<text x="20" y="76" text-anchor="middle" class="uml-text" font-size="11" font-weight="600">{name}</text>'
    if sub: s+=f'<text x="20" y="90" text-anchor="middle" class="uml-text" font-size="10" fill="#5a6473">{sub}</text>'
    return s+'</g>'

def uc(cx,cy,label,rx=92,ry=27,fill="white"):
    # label may contain \n for two lines
    lines=label.split("\n")
    t=""
    if len(lines)==1:
        t=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{lines[0]}</text>'
    else:
        t=f'<text x="{cx}" y="{cy-3}" text-anchor="middle" class="uml-text" font-size="11">{lines[0]}</text>'
        t+=f'<text x="{cx}" y="{cy+12}" text-anchor="middle" class="uml-text" font-size="11">{lines[1]}</text>'
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="uml-box"/>{t}'

# ---------- Figure A: complete Library refinements ----------
defsA='''<defs>
  <marker id="ucOpen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#2c3540" stroke-width="1.4"/></marker>
  <marker id="ucTri" viewBox="0 0 14 14" refX="13" refY="7" markerWidth="15" markerHeight="15" orient="auto"><path d="M 1 1 L 13 7 L 1 13 Z" fill="white" stroke="#0f1419" stroke-width="1.2"/></marker>
</defs>'''
A=[defsA]
# boundary
A.append('<rect x="220" y="70" width="900" height="740" rx="8" class="uml-box" fill="#faf7f2" stroke-width="1.8"/>')
A.append('<text x="670" y="60" text-anchor="middle" class="uml-text" font-weight="600" font-size="13">Library System</text>')
# actors
A.append(actor(60,140,"BookBorrower","(member)"))
A.append(actor(60,480,"JournalBorrower","(staff)"))
A.append(actor(1170,110,"SystemTimer",""))
A.append(actor(1170,360,"Email System",""))
A.append(actor(1170,600,"Bank System",""))
# use cases
A.append(uc(370,150,"Borrow copy of a book"))
A.append(uc(370,260,"Renew loan of a book"))
A.append(uc(665,102,"Refuse loan",rx=72))
A.append(uc(645,220,"Compute return date"))
A.append(uc(370,470,"Pay fine",rx=78))
A.append(uc(370,600,"Pay by cash",rx=78))
A.append(uc(640,540,"Pay by credit card"))
A.append(uc(900,150,"Send reminder to\nlate loans"))
A.append(uc(900,300,"Send message\n(by email)"))
A.append(uc(900,460,"Send payment\nconfirmation"))
A.append(uc(900,620,"Validate payment"))
# associations (blue, no arrow)
A.append('<line x1="94" y1="165" x2="278" y2="150" class="uml-line-blue"/>')   # BB-Borrow
A.append('<line x1="94" y1="170" x2="278" y2="255" class="uml-line-blue"/>')   # BB-Renew
A.append('<line x1="94" y1="175" x2="292" y2="468" class="uml-line-blue"/>')   # BB-Payfine
A.append('<line x1="94" y1="505" x2="292" y2="475" class="uml-line-blue"/>')   # JB-Payfine
A.append('<line x1="1170" y1="135" x2="985" y2="150" class="uml-line-blue"/>') # SystemTimer-reminder
A.append('<line x1="992" y1="300" x2="1170" y2="370" class="uml-line-blue"/>') # message-email
A.append('<line x1="992" y1="620" x2="1170" y2="615" class="uml-line-blue"/>') # validate-bank
# includes (base -> sub) open arrow, dashed
def dash(x1,y1,x2,y2,marker="ucOpen"):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-dashed" marker-end="url(#{marker})"/>'
def lbl(x,y,t,color="#2c3540"):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="{color}" font-weight="600">{t}</text>'
A.append(dash(462,162,567,214)); A.append(lbl(515,205,"&lt;&lt;include&gt;&gt;"))      # Borrow->Compute
A.append(dash(462,258,567,226)); A.append(lbl(512,268,"&lt;&lt;include&gt;&gt;"))      # Renew->Compute
A.append(dash(900,180,900,270)); A.append(lbl(963,232,"&lt;&lt;include&gt;&gt;"))      # Send reminder -> Send message (base->sub)
A.append(dash(900,433,900,330)); A.append(lbl(963,400,"&lt;&lt;include&gt;&gt;"))       # confirmation(460)->message(300) up
A.append(dash(715,535,815,470)); A.append(lbl(792,520,"&lt;&lt;include&gt;&gt;"))       # credit card->confirmation
# extends (ext -> base) open arrow dashed, rust
def dashx(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#7a3a23" stroke-width="1.2" stroke-dasharray="4,3" fill="none" marker-end="url(#ucOpen)"/>'
A.append(dashx(596,110,452,136)); A.append(lbl(512,98,"&lt;&lt;extend&gt;&gt;","#7a3a23")); A.append(lbl(560,113,"[too many books]","#7a3a23"))  # Refuse->Borrow
A.append(dashx(880,600,700,558)); A.append(lbl(800,612,"&lt;&lt;extend&gt;&gt;","#7a3a23"))  # Validate->credit card
# inherit (special -> general) hollow triangle solid
def gen(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#ucTri)"/>'
A.append(gen(370,573,370,500)); A.append(lbl(330,540,"&lt;&lt;inherit&gt;&gt;"))         # cash->payfine up
A.append(gen(560,528,440,478)); A.append(lbl(520,486,"&lt;&lt;inherit&gt;&gt;"))         # credit->payfine
figA="".join(A)

# ---------- Figure B: process order activity (fork/join) ----------
defsB='<defs><marker id="actArrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'
def act(cx,cy,label,w=130,h=42):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text">{label}</text>'
def arr(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#actArrow2)"/>'
def plain(x1,y1,x2,y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line"/>'
def dia(cx,cy,t1,t2=""):
    p=f'<polygon points="{cx},{cy-22} {cx+34},{cy} {cx},{cy+22} {cx-34},{cy}" class="uml-box"/>'
    if t2:
        p+=f'<text x="{cx}" y="{cy-2}" text-anchor="middle" class="uml-text" font-size="10">{t1}</text><text x="{cx}" y="{cy+10}" text-anchor="middle" class="uml-text" font-size="10">{t2}</text>'
    else:
        p+=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t1}</text>'
    return p
def bar(cx,y,w=360):
    return f'<rect x="{cx-w//2}" y="{y}" width="{w}" height="7" rx="2" fill="#2c3540"/>'
def gl(x,y,t):
    return f'<text x="{x}" y="{y}" class="uml-text" font-size="11">{t}</text>'
B=[defsB]
B.append('<circle cx="360" cy="45" r="9" fill="#0f1419"/>')           # initial
B.append(arr(360,54,360,80))
B.append(act(360,101,"Receive Order"))
B.append(arr(360,122,360,150))
B.append(bar(360,151))                                                  # fork
B.append(plain(255,158,255,205)); B.append(arr(255,205,255,205))
B.append(plain(255,158,255,184)); B.append(arr(255,184,255,205))
B.append(act(255,226,"Fill Order"))
B.append(plain(485,158,485,184)); B.append(arr(485,184,485,205))
B.append(act(485,226,"Send Invoice"))
B.append(arr(255,247,255,288))                                          # fill->decision
B.append(dia(255,310,"Priority?"))
B.append(arr(221,310,200,380)); B.append(gl(78,348,"[priority order]"))
B.append(arr(289,310,350,380)); B.append(gl(340,348,"[else]"))
B.append(act(200,400,"Overnight",w=120,h=40))
B.append(act(350,400,"Regular",w=120,h=40))
B.append(plain(200,420,200,448)); B.append(arr(200,448,232,468))        # overnight->merge
B.append(plain(350,420,350,448)); B.append(arr(350,448,278,468))        # regular->merge
B.append(dia(255,470,""))
B.append(arr(255,492,255,557))                                          # merge->join
B.append(arr(485,247,485,300))                                          # invoice->payment
B.append(act(485,321,"Receive Payment"))
B.append(arr(485,342,485,557))                                          # payment->join
B.append(bar(360,558))                                                  # join
B.append(arr(360,565,360,595))
B.append(act(360,616,"Close Order"))
B.append(arr(360,637,360,663))
B.append('<circle cx="360" cy="676" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="360" cy="676" r="5" fill="#0f1419"/>')
figB="".join(B)

def standalone(inner,vb,w,h,out):
    open(out,"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">\n{STYLE}\n<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>\n{inner}\n</svg>\n')

standalone(figA,"0 0 1280 860",1280,860,"figA_library_refinements.svg")
standalone(figB,"0 0 720 720",720,720,"figB_process_order.svg")
print("wrote figA_library_refinements.svg, figB_process_order.svg")

open("figA_inner.txt","w").write(figA)
open("figB_inner.txt","w").write(figB)
print("emitted figA_inner.txt, figB_inner.txt")
