from random import randrange
def qSort ( A, nStart, nEnd ):
    if nStart >= nEnd: return
    L = nStart; R = nEnd
    X = A[(L+R)//2]
    while L <= R:
        while A[L] < X: L += 1 # разделение
        while A[R] > X: R -= 1
        if L <= R:
            A[L], A[R] = A[R], A[L]
            L += 1; R -= 1
    qSort ( A, nStart, R ) # рекурсивные вызовы
    qSort ( A, L, nEnd )

a = []
for i in range(10):
    a.append(randrange(1, 100))
quicksort(a, 0, len(a) - 1)
print(a)

