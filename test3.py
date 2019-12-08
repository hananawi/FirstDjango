a, b, n = map(int, input().split())
l, r = 1, n
while(l<=r):
    m = l+r>>1
    tmp = a*m+b*len(str(m))
    if tmp>n: r=m-1
    else: l=m+1
print(min(int(1e9),min(l,r)))
