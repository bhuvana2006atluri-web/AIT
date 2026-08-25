def mm(b, maxp, a=-99, z=99):
    for p,s in [('O',1),('X',-1)]:
        if any(all(b[i]==p for i in l) for l in L): return s
    if ' ' not in b: return 0

    v = -99 if maxp else 99
    for i in range(9):
        if b[i]==' ':
            b[i]='O' if maxp else 'X'
            x=mm(b,not maxp,a,z)
            b[i]=' '
            v=max(v,x) if maxp else min(v,x)
            a=max(a,v) if maxp else a
            z=min(z,v) if not maxp else z
            if z<=a: break
    return v

L=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
b=[' ']*9

while True:
    print(b[:3],b[3:6],b[6:])
    h=int(input("Enter position (1-9): "))-1
    b[h]='X'

    if mm(b,True)==-1: print("Human wins"); break
    if ' ' not in b: print("Draw"); break

    m=max((mm(b[:i]+['O']+b[i+1:],False),i) for i in range(9) if b[i]==' ')[1]
    b[m]='O'
    print("Computer:",m+1)

    if mm(b,False)==1: print("Computer wins"); break
