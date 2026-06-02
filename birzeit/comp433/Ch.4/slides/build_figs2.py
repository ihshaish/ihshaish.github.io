STYLE='''  <style>
    .uml-text { font-family:"Inter Tight",-apple-system,Helvetica,Arial,sans-serif; font-size:12px; fill:#0f1419; }
    .uml-line { stroke:#0f1419; stroke-width:1.4; fill:none; }
    .uml-line-dashed { stroke:#0f1419; stroke-width:1.2; fill:none; stroke-dasharray:4,3; }
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

# ===== Figure C: MHC-PMS use case diagram =====
defsC='<defs><marker id="mhcArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#4a8bb8"/></marker></defs>'
C=[defsC]
C.append('<rect x="250" y="70" width="800" height="640" rx="8" class="uml-box" fill="#faf7f2" stroke-width="1.8"/>')
C.append('<text x="650" y="60" text-anchor="middle" class="uml-text" font-weight="600" font-size="13">MHC-PMS</text>')
C.append(actor(70,230,"Medical","receptionist"))
C.append(actor(70,560,"Nurse",""))
C.append(actor(1210,150,"Manager",""))
C.append(actor(1210,540,"Doctor",""))
C.append(actor(1130,90,"Patient record","system"))
# use cases
C.append(uc(430,130,"Transfer data",rx=82))
C.append(uc(430,220,"Register patient",rx=88))
C.append(uc(430,310,"Unregister patient",rx=92))
C.append(uc(430,400,"Contact patient",rx=88))
C.append(uc(660,120,"View patient info",rx=90))
C.append(uc(880,185,"Export statistics\nreport",rx=86))
C.append(uc(880,300,"Generate medical\nreport",rx=90))
C.append(uc(620,470,"View patient\nmedical record",rx=92))
C.append(uc(620,560,"Edit patient\nmedical record",rx=92))
C.append(uc(850,620,"Setup consultation",rx=92))
# receptionist associations
for tx,ty in [(348,130),(342,220),(338,310),(342,400)]:
    C.append(bl(94,255,tx,ty))
C.append(bl(94,250,572,124))   # receptionist -> view info
# transfer data -> PRS (directed association, leaving boundary)
C.append(f'<line x1="512" y1="125" x2="1128" y2="112" class="uml-line-blue" marker-end="url(#mhcArrow)"/>')
# manager
C.append(bl(1210,178,748,120))   # manager -> view info
C.append(bl(1210,180,966,185))   # manager -> export stats
C.append(bl(1210,182,970,300))   # manager -> generate report
# doctor
C.append(bl(1210,568,712,470))   # doctor -> view med record
C.append(bl(1210,570,712,560))   # doctor -> edit med record
C.append(bl(1210,572,942,620))   # doctor -> setup consultation
C.append(bl(1210,566,970,305))   # doctor -> generate report
# nurse
C.append(bl(94,585,528,470))     # nurse -> view med record
C.append(bl(94,588,528,560))     # nurse -> edit med record
figC="".join(C)

# ===== Figure D: Library Borrow/Return swimlane activity (fork/join + loop) =====
defsD='<defs><marker id="dArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'
def act(cx,cy,label,w=140,h=40):
    return f'<rect x="{cx-w//2}" y="{cy-h//2}" width="{w}" height="{h}" rx="{h//2}" class="uml-box"/><text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text">{label}</text>'
def arr(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line" marker-end="url(#dArrow)"/>'
def pl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line"/>'
def poly(pts): return f'<polyline points="{pts}" class="uml-line" marker-end="url(#dArrow)"/>'
def dia(cx,cy,t=""):
    p=f'<polygon points="{cx},{cy-22} {cx+36},{cy} {cx},{cy+22} {cx-36},{cy}" class="uml-box"/>'
    if t: p+=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="10">{t}</text>'
    return p
def bar(cx,y,w=200): return f'<rect x="{cx-w//2}" y="{y}" width="{w}" height="7" rx="2" fill="#2c3540"/>'
def gl(x,y,t,anc="start"): return f'<text x="{x}" y="{y}" text-anchor="{anc}" class="uml-text" font-size="11">{t}</text>'
D=[defsD]
# lanes
D.append('<rect x="40" y="60" width="390" height="650" fill="#faf7f2" stroke="#d8cfc0"/>')
D.append('<rect x="430" y="60" width="380" height="650" fill="white" stroke="#d8cfc0"/>')
D.append('<text x="235" y="86" text-anchor="middle" class="uml-text" font-weight="600">Member</text>')
D.append('<text x="620" y="86" text-anchor="middle" class="uml-text" font-weight="600">Librarian</text>')
D.append('<line x1="40" y1="100" x2="810" y2="100" class="uml-line"/>')
# Member lane
D.append('<circle cx="200" cy="128" r="9" fill="#0f1419"/>')
D.append(arr(200,137,200,156))
D.append(dia(200,180,"borrow /"))
D.append('<text x="200" y="192" text-anchor="middle" class="uml-text" font-size="10">return?</text>')
# [borrow] -> cross to Librarian Locate copy
D.append(poly("236,180 330,180 330,178 540,178")); D.append(gl(250,170,"[borrow]"))
# [return] -> down then cross to Record book return
D.append(pl(200,202,200,520)); D.append(gl(208,360,"[return]"))
D.append(poly("200,520 200,560 470,560")); 
# Librarian lane
D.append(act(620,178,"Locate copy"))
D.append(arr(620,198,620,238))
D.append(bar(620,239))                       # fork
D.append(pl(540,246,540,290)); D.append(arr(540,290,540,290))
D.append(pl(540,246,540,270)); D.append(arr(540,270,540,290))
D.append(act(540,312,"Stamp book",w=120))
D.append(pl(700,246,700,270)); D.append(arr(700,270,700,290))
D.append(act(700,312,"Record borrowing",w=140))
D.append(pl(540,332,540,372)); D.append(pl(700,332,700,372))
D.append(bar(620,373))                        # join
D.append(arr(620,380,620,468))                # join -> merge
D.append(act(470,560,"Record book return",w=160))
D.append(dia(620,490,""))                      # merge
D.append(pl(470,540,470,512)); D.append(arr(470,512,588,492))   # return -> merge
D.append(arr(620,512,620,575))                 # merge -> decision
D.append(dia(620,600,""))
D.append('<text x="620" y="604" text-anchor="middle" class="uml-text" font-size="10">more?</text>')
# [another book] loop back to D1 (left, up)
D.append(poly("584,600 120,600 120,180 164,180")); D.append(gl(126,460,"[another book]"))
# [no] -> final
D.append(arr(656,600,720,600))
D.append('<circle cx="745" cy="600" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="745" cy="600" r="5" fill="#0f1419"/>')
D.append(gl(660,590,"[no]"))
figD="".join(D)

def standalone(inner,vb,w,h,out):
    open(out,"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">\n{STYLE}\n<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>\n{inner}\n</svg>\n')
standalone(figC,"0 0 1300 760",1300,760,"figC_mhcpms_usecase.svg")
standalone(figD,"0 0 820 740",820,740,"figD_borrow_return_activity.svg")
open("figC_inner.txt","w").write(figC); open("figD_inner.txt","w").write(figD)
print("wrote figC, figD")
