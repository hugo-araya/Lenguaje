N = 10
M = 0
P = 0
Cont = 0
while Cont < N:
    N1 = int(input())
    Z = N1 % 2
    if Z == 0:
        P = P + 1
    else:
        M = M + 1
    Cont = Cont + 1
print(P)
print(M)
