import pikepdf, sys
import os
src=sys.argv[1]
T={2:[(40,505,458,502)],
   4:[(245,520,316,350),(245,520,644,679)],
   6:[(40,552,190,258),(40,552,300,360),(40,552,398,444),(214,336,480,554),(388,556,480,554)],
   7:[(40,300,140,188),(465,556,557,576),(40,300,450,486)],
   3:[(40,400,720,740)],
   5:[(40,552,360,396)]}
H=841.92
def mul(a,b): return [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3],a[4]*b[0]+a[5]*b[2]+b[4],a[4]*b[1]+a[5]*b[3]+b[5]]
p=pikepdf.open(src)
for pi,boxes in T.items():
    pg=p.pages[pi]; ops=pikepdf.parse_content_stream(pg)
    out=[];stack=[];ctm=[1,0,0,1,0,0];buf=None;pos=None;removed=0
    for a,o in ops:
        s=str(o)
        if buf is not None:
            buf.append((a,o))
            if s=='Tm' and pos is None:
                m=mul([float(x) for x in a],ctm); pos=(m[4],H-m[5])
            if s=='ET':
                hit=pos and any(x0<=pos[0]<=x1 and y0<=pos[1]<=y1 for x0,x1,y0,y1 in boxes)
                if hit: removed+=1
                else: out+=buf
                buf=None
            continue
        if s=='q': stack.append(ctm[:])
        elif s=='Q': ctm=stack.pop()
        elif s=='cm': ctm=mul([float(x) for x in a],ctm)
        if s=='BT': buf=[(a,o)];pos=None;continue
        out.append((a,o))
    pg.Contents=p.make_stream(pikepdf.unparse_content_stream(out))
    print('page',pi+1,'removed',removed)
p.save(sys.argv[2])
