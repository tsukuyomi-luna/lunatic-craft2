import zlib,struct,sys,random,math
N=32
random.seed(7)
def hx(s): return tuple(int(s[i:i+2],16) for i in (1,3,5))
img=[[None]*N for _ in range(N)]
def put(x,y,c):
    if 0<=x<N and 0<=y<N: img[y][x]=hx(c) if isinstance(c,str) else c
# sky gradient
top,bot=hx("#0b1030"),hx("#3a2660")
for y in range(N):
    t=y/(N-1); c=tuple(round(top[i]+(bot[i]-top[i])*t) for i in range(3))
    # banding like MC sky: quantize
    c=tuple((v//6)*6 for v in c)
    for x in range(N): img[y][x]=c
# stars
for (x,y,c) in [(3,3,"#ffffff"),(9,2,"#c9d6ff"),(14,6,"#ffffff"),(5,9,"#c9d6ff"),(29,15,"#ffffff"),(18,2,"#c9d6ff"),(1,14,"#ffffff"),(27,20,"#c9d6ff"),(16,4,"#8f9be0")]:
    put(x,y,c)
# crescent moon
cx,cy,r=25,6,4.8
for y in range(N):
    for x in range(N):
        d=math.hypot(x-cx,y-cy); d2=math.hypot(x-(cx+2.2),y-(cy-1.6))
        if d<=r and d2>4.2:
            put(x,y,"#f6edb8" if (x-cx)+(y-cy)<2 else "#d8c784")
# ground: grass blocks
for x in range(N):
    h=28+(1 if (x//4)%3==1 else 0)
    for y in range(h,N):
        if y==h: put(x,y,random.choice(["#5fa83f","#4f9433","#6bb548"]))
        elif y==h+1: put(x,y,random.choice(["#4f9433","#7a5232"]))
        else: put(x,y,random.choice(["#7a5232","#6a4428","#86603c"]))
# distant hills silhouette
for x in range(N):
    hh=25+round(1.5*math.sin(x/3.0)+math.sin(x/1.7))
    for y in range(hh,28+(1 if (x//4)%3==1 else 0)):
        put(x,y,"#1d2a3f")
# airship envelope
ex,ey,rx,ry=13.5,16.0,9.6,4.4
inside=lambda x,y: ((x-ex)/rx)**2+((y-ey)/ry)**2<=1.0
for y in range(N):
    for x in range(N):
        if not inside(x,y): continue
        if not all(inside(a,b) for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1))): c="#3b2a20"
        elif x in (8,14,19): c="#c9973a" if y<ey+2 else "#a5772a"
        elif y>=ey+2: c="#b9a37c"
        elif y<=ey-3: c="#fff4dc"
        else: c="#e9dcbc"
        put(x,y,c)
# tail fins
for (x,y) in [(3,13),(3,14),(4,14),(3,18),(3,19),(4,18)]: put(x,y,"#a5772a")
for (x,y) in [(2,13),(2,14),(2,18),(2,19)]: put(x,y,"#3b2a20")
# rigging
for (x,y) in [(9,20),(10,21),(18,20),(17,21)]: put(x,y,"#3b2a20")
# gondola (wood + brass trim)
for x in range(9,19):
    put(x,22,"#c9973a" if x%2==0 else "#e0b04a")
    put(x,23,"#8b5a2b" if x%3 else "#6b4420")
    put(x,24,"#6b4420")
for x in range(10,18): put(x,25,"#3b2a20")
# windows
for x in (11,14,17): put(x,23,"#ffd86b")
# propeller (rear) with cog hub
put(7,23,"#a5772a"); put(6,23,"#3b2a20")
for (x,y) in [(5,21),(5,22),(5,24),(5,25)]: put(x,y,"#d9d9d9")
put(5,23,"#c9973a")
# write PNG scaled
def png(path,scale):
    W=N*scale
    raw=b"".join(b"\x00"+b"".join(bytes(img[y//scale][x//scale]) for x in range(W)) for y in range(W))
    def chunk(t,d): return struct.pack(">I",len(d))+t+d+struct.pack(">I",zlib.crc32(t+d)&0xffffffff)
    open(path,"wb").write(b"\x89PNG\r\n\x1a\n"+chunk(b"IHDR",struct.pack(">IIBBBBB",W,W,8,2,0,0,0))+chunk(b"IDAT",zlib.compress(raw,9))+chunk(b"IEND",b""))
png(sys.argv[1]+"/icon.png",16)
png(sys.argv[1]+"/server-icon.png",2)
