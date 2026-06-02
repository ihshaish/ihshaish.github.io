STYLE='''  <style>
    .uml-text { font-family:"Inter Tight",-apple-system,Helvetica,Arial,sans-serif; font-size:12px; fill:#0f1419; }
    .uml-line { stroke:#0f1419; stroke-width:1.4; fill:none; }
    .uml-line-blue { stroke:#4a8bb8; stroke-width:1.4; fill:none; }
    .uml-box { stroke:#0f1419; stroke-width:1.4; fill:white; }
    .actor-blue { stroke:#2c6e9a; stroke-width:1.4; fill:#eaf3f9; }
  </style>'''

def actor(x,y,name,sub=""):
    s=f'<g transform="translate({x},{y})">'
    s+='<circle cx="20" cy="6" r="8" class="actor-blue"/>'
    s+='<line x1="20" y1="14" x2="20" y2="42" class="uml-line-blue"/><line x1="20" y1="22" x2="6" y2="32" class="uml-line-blue"/><line x1="20" y1="22" x2="34" y2="32" class="uml-line-blue"/><line x1="20" y1="42" x2="6" y2="58" class="uml-line-blue"/><line x1="20" y1="42" x2="34" y2="58" class="uml-line-blue"/>'
    s+=f'<text x="20" y="76" text-anchor="middle" class="uml-text" font-size="11" font-weight="600">{name}</text>'
    if sub: s+=f'<text x="20" y="90" text-anchor="middle" class="uml-text" font-size="10" fill="#5a6473">{sub}</text>'
    return s+'</g>'

def uc(cx,cy,label,rx=96,ry=26):
    lines=label.split("\n")
    if len(lines)==1:
        t=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{lines[0]}</text>'
    else:
        t=f'<text x="{cx}" y="{cy-3}" text-anchor="middle" class="uml-text" font-size="11">{lines[0]}</text><text x="{cx}" y="{cy+12}" text-anchor="middle" class="uml-text" font-size="11">{lines[1]}</text>'
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="uml-box"/>{t}'

def bl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-blue"/>'

# ============ Figure C: MHC-PMS use case diagram (relaid for clarity) ============
defsC='<defs><marker id="mhcArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#4a8bb8"/></marker></defs>'
C=[defsC]
C.append('<rect x="250" y="80" width="820" height="620" rx="8" class="uml-box" fill="#faf7f2" stroke-width="1.8"/>')
C.append('<text x="660" y="70" text-anchor="middle" class="uml-text" font-weight="600" font-size="13">MHC-PMS</text>')
C.append(actor(60,300,"Medical","receptionist"))
C.append(actor(60,580,"Nurse",""))
C.append(actor(1240,280,"Manager",""))
C.append(actor(1240,560,"Doctor",""))
C.append(actor(1120,40,"Patient record","system"))
# use cases
C.append(uc(430,150,"Transfer data",rx=82))
C.append(uc(430,250,"Register patient",rx=88))
C.append(uc(430,340,"Unregister patient",rx=92))
C.append(uc(430,430,"Contact patient",rx=88))
C.append(uc(665,170,"View patient info",rx=92))
C.append(uc(905,250,"Export statistics\nreport",rx=90))
C.append(uc(905,375,"Generate medical\nreport",rx=92))
C.append(uc(650,515,"View patient\nmedical record",rx=94))
C.append(uc(650,605,"Edit patient\nmedical record",rx=94))
C.append(uc(890,645,"Setup consultation",rx=94))
# receptionist associations
C.append(bl(94,318,348,150))
C.append(bl(94,324,342,250))
C.append(bl(94,332,338,340))
C.append(bl(94,340,342,430))
C.append(bl(94,316,573,170))     # -> view info
# Transfer data -> PRS : orthogonal route up & across the top (isolated)
C.append('<polyline points="430,124 430,100 1132,100 1132,108" class="uml-line-blue" fill="none" marker-end="url(#mhcArrow)"/>')
# manager
C.append(bl(1234,300,757,170))   # -> view info
C.append(bl(1234,306,995,250))   # -> export stats
C.append(bl(1234,312,997,372))   # -> generate report
# doctor
C.append(bl(1234,586,744,515))   # -> view med rec
C.append(bl(1234,590,744,602))   # -> edit med rec
C.append(bl(1234,600,984,645))   # -> setup consultation
C.append(bl(1234,580,997,378))   # -> generate report
# nurse
C.append(bl(94,600,556,515))     # -> view med rec
C.append(bl(94,608,556,605))     # -> edit med rec
figC="".join(C)

# ============ Figure D: Library Borrow/Return swimlane activity (relaid) ============
defsD='<defs><marker id="dArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'
def act(cx,cy,label,w=140,h=40):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text">{label}</text>'
def arr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#dArrow)"/>'
def pl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line"/>'
def parr(pts): return f'<polyline points="{pts}" class="uml-line" fill="none" marker-end="url(#dArrow)"/>'
def ppl(pts): return f'<polyline points="{pts}" class="uml-line" fill="none"/>'
def bigdia(cx,cy,l1,l2,hw=52,hh=30):
    p=f'<polygon points="{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}" class="uml-box"/>'
    p+=f'<text x="{cx}" y="{cy-3}" text-anchor="middle" class="uml-text" font-size="11">{l1}</text>'
    p+=f'<text x="{cx}" y="{cy+12}" text-anchor="middle" class="uml-text" font-size="11">{l2}</text>'
    return p
def dia(cx,cy,t=""):
    p=f'<polygon points="{cx},{cy-22} {cx+36},{cy} {cx},{cy+22} {cx-36},{cy}" class="uml-box"/>'
    if t: p+=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t}</text>'
    return p
def bar(cx,y,w=200): return f'<rect x="{cx-w//2}" y="{y}" width="{w}" height="7" rx="2" fill="#2c3540"/>'
def gl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="11">{t}</text>'
D=[defsD]
D.append('<rect x="40" y="60" width="400" height="660" fill="#faf7f2" stroke="#d8cfc0"/>')
D.append('<rect x="440" y="60" width="380" height="660" fill="white" stroke="#d8cfc0"/>')
D.append('<text x="240" y="88" text-anchor="middle" class="uml-text" font-weight="600">Member</text>')
D.append('<text x="630" y="88" text-anchor="middle" class="uml-text" font-weight="600">Librarian</text>')
D.append('<line x1="40" y1="105" x2="820" y2="105" class="uml-line"/>')
# Member
D.append('<circle cx="210" cy="135" r="9" fill="#0f1419"/>')
D.append(arr(210,144,210,164))
D.append(bigdia(210,196,"borrow /","return?"))
# [borrow] straight across to Locate copy
D.append(arr(262,196,558,196)); D.append(gl(400,187,"[borrow]","middle"))
# [return] down then across to Record book return
D.append(parr("210,226 210,575 498,575")); D.append(gl(218,390,"[return]"))
# Librarian
D.append(act(630,196,"Locate copy"))
D.append(arr(630,216,630,254))
D.append(bar(630,255))
D.append(arr(555,262,555,300))
D.append(act(555,320,"Stamp book",w=120))
D.append(arr(715,262,715,300))
D.append(act(715,320,"Record borrowing",w=140))
D.append(pl(555,340,555,386)); D.append(pl(715,340,715,386))
D.append(bar(630,386))
D.append(arr(630,393,630,445))            # join -> merge (top vertex 467-22=445)
D.append(dia(630,467,""))                 # merge
D.append(act(580,575,"Record book return",w=170))
D.append(ppl("580,555 580,467")); D.append(arr(580,467,596,467))   # return -> merge left
D.append(arr(630,489,630,620))            # merge -> decision (top 642-22=620)
D.append(dia(630,642,"more?"))
# [no] -> final
D.append(arr(666,642,732,642)); D.append(gl(688,632,"[no]"))
D.append('<circle cx="758" cy="642" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="758" cy="642" r="5" fill="#0f1419"/>')
# [another book] loop back to D1 left vertex (158,196)
D.append(parr("594,642 110,642 110,196 158,196")); D.append(gl(118,420,"[another book]"))
figD="".join(D)

def standalone(inner,vb,w,h,out):
    open(out,"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">\n{STYLE}\n<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>\n{inner}\n</svg>\n')
standalone(figC,"0 0 1340 760",1340,760,"figC_mhcpms_usecase.svg")
standalone(figD,"0 0 840 760",840,760,"figD_borrow_return_activity.svg")
open("figC_inner.txt","w").write(figC); open("figD_inner.txt","w").write(figD)
print("wrote figC, figD")
