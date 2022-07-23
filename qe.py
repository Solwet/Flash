def f(N):
    n=bin(N)[2:]
    a=n[-1]
    n=a+n[1:-1]+'1'
    return int(n,2)

N=2
k=0
suma=0
while True:
    if f(N) == 5:
        k+=1
        suma += N
        if k == 10:
            break
    N += 1
print(suma)
