b=[]
x=int(input())
for i in range(x):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    a=sorted(a)
    for i in a:
        b.append(i)
print(sep=' ',*b)
