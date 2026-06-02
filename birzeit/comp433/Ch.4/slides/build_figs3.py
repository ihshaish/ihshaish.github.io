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
def uc(cx,cy,label,rx=92,ry=26):
    L=label.split("\n")
    if len(L)==1: t=f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="uml-text" font-size="11">{L[0]}</text>'
    else: t=f'<text x="{cx}" y="{cy-3}" text-anchor="middle" class="uml-text" font-size="11">{L[0]}</text><text x="{cx}" y="{cy+12}" text-anchor="middle" class="uml-text" font-size="11">{L[1]}</text>'
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="uml-box"/>{t}'
def bl(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-blue"/>'
def lblm(x,y,t,c="#2c3540"): return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="{c}" font-weight="600">{t}</text>'

# ===== Figure E: Hotel booking use case diagram =====
defsE='<defs><marker id="ucOpenE" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" orient="auto"><path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="#2c3540" stroke-width="1.4"/></marker><marker id="assocE" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#4a8bb8"/></marker></defs>'
E=[defsE]
E.append('<rect x="250" y="70" width="740" height="600" rx="8" class="uml-box" fill="#faf7f2" stroke-width="1.8"/>')
E.append('<text x="620" y="60" text-anchor="middle" class="uml-text" font-weight="600" font-size="13">Hotel Booking System</text>')
E.append(actor(60,250,"Guest",""))
E.append(actor(60,560,"Hotel Manager",""))
E.append(actor(1110,420,"Payment Provider",""))
E.append(uc(440,160,"Search rooms",rx=86))
E.append(uc(440,300,"Book room",rx=86))
E.append(uc(440,440,"Cancel booking",rx=88))
E.append(uc(440,575,"Manage room\ninventory",rx=92))
E.append(uc(720,160,"Check availability",rx=90))
E.append(uc(720,300,"Apply discount code",rx=96))
E.append(uc(720,440,"Process payment",rx=90))
# associations
E.append(bl(94,268,354,165))      # Guest->Search
E.append(bl(94,274,354,300))      # Guest->Book
E.append(bl(94,280,352,440))      # Guest->Cancel
E.append(bl(94,585,348,575))      # Manager->Manage inventory
E.append(f'<line x1="810" y1="440" x2="1104" y2="424" class="uml-line-blue" marker-end="url(#assocE)"/>')  # Process payment->Payment Provider
# includes (base->sub) dashed open
def inc(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="uml-line-dashed" marker-end="url(#ucOpenE)"/>'
E.append(inc(526,160,630,160)); E.append(lblm(578,150,"&lt;&lt;include&gt;&gt;"))      # Search->Check
E.append(inc(520,290,632,172)); E.append(lblm(548,212,"&lt;&lt;include&gt;&gt;"))      # Book->Check
E.append(inc(520,312,632,432)); E.append(lblm(548,388,"&lt;&lt;include&gt;&gt;"))      # Book->Process payment
# extend (ext->base) dashed open, rust
E.append(f'<line x1="624" y1="300" x2="528" y2="300" stroke="#7a3a23" stroke-width="1.2" stroke-dasharray="4,3" fill="none" marker-end="url(#ucOpenE)"/>')
E.append(lblm(578,291,"&lt;&lt;extend&gt;&gt;","#7a3a23")); E.append(lblm(578,314,"[has code]","#7a3a23"))
figE="".join(E)

# ===== Figure F: Hotel booking activity (3 swimlanes, retry loop, external) =====
defsF='<defs><marker id="fArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M 0 0 L 10 5 L 0 10 Z" fill="#0f1419"/></marker></defs>'
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
F=[defsF]
# 3 lanes
F.append('<rect x="40" y="60" width="370" height="780" fill="#faf7f2" stroke="#d8cfc0"/>')
F.append('<rect x="410" y="60" width="370" height="780" fill="white" stroke="#d8cfc0"/>')
F.append('<rect x="780" y="60" width="320" height="780" fill="#faf7f2" stroke="#d8cfc0"/>')
F.append('<text x="225" y="88" text-anchor="middle" class="uml-text" font-weight="600">Guest</text>')
F.append('<text x="595" y="88" text-anchor="middle" class="uml-text" font-weight="600">Booking System</text>')
F.append('<text x="940" y="88" text-anchor="middle" class="uml-text" font-weight="600">Payment Provider</text>')
F.append('<line x1="40" y1="112" x2="1100" y2="112" class="uml-line"/>')
# Guest
F.append('<circle cx="225" cy="142" r="9" fill="#0f1419"/>')
F.append(arr(225,151,225,178))
F.append(act(225,200,"Search rooms"))
F.append(arr(300,200,505,200))                              # -> Find available rooms
F.append(act(595,200,"Find available rooms",w=170))
F.append(arr(595,220,595,262))
F.append(dia(595,290,"rooms","available?",hw=52,hh=28))
# [no] -> alt final
F.append(parr("595,318 595,360 470,360")); F.append(gl(498,352,"[no]"))
F.append('<circle cx="455" cy="360" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="455" cy="360" r="5" fill="#0f1419"/>')
# [yes] -> Select room (Guest)
F.append(parr("647,290 700,290 700,420 300,420")); F.append(gl(662,283,"[yes]"))
F.append(act(225,420,"Select room"))
F.append(arr(225,440,225,478))
F.append(act(225,500,"Enter payment details"))
F.append(arr(300,500,865,500))                              # -> Authorise payment (Payment Provider)
F.append(act(940,500,"Authorise payment",w=160))
F.append(arr(940,520,940,556))
F.append(dia(940,590,"approved?",hw=46))
# [declined] retry loop back to Enter payment details
F.append(parr("940,614 940,820 225,820 225,522")); F.append(gl(582,812,"[declined]: retry payment","middle"))
# [yes] -> Reserve room (Booking System)
F.append(parr("894,590 595,590 595,628")); F.append(gl(735,583,"[approved]"))
F.append(act(595,650,"Reserve room"))
F.append(arr(595,670,595,706))
F.append(act(595,728,"Confirm booking"))
F.append(arr(595,748,595,778))
F.append('<circle cx="595" cy="791" r="9" fill="white" stroke="#0f1419" stroke-width="1.4"/><circle cx="595" cy="791" r="5" fill="#0f1419"/>')
figF="".join(F)

def standalone(inner,vb,w,h,out):
    open(out,"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">\n{STYLE}\n<rect x="0" y="0" width="{w}" height="{h}" fill="white"/>\n{inner}\n</svg>\n')
standalone(figE,"0 0 1240 720",1240,720,"figE_hotel_usecase.svg")
standalone(figF,"0 0 1140 870",1140,870,"figF_hotel_activity.svg")
open("figE_inner.txt","w").write(figE); open("figF_inner.txt","w").write(figF)
print("wrote figE, figF")
