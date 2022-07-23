def f(N):
    a=''
    mas=[]
    n=bin(N)[2:]
    for i in range(len(n)):
        mas.append(n[i])
    for i in range(1,len(mas),2):
        mas[i]=1
    for i in range(len(mas)):
        a += str(mas[i])
    return int(a,2)

N=1
k=0
while True:
    if f(N) == 106:
        print(N)
    N +=1
