def solution(X, A):
    P={}
    i=0
    if len(A) == 1:
        if (A[0]!=X):
            return(-1)
        else:
            return(0)

    for i in range(0,len(A)):
        if X > len(P) and X !=0:
            if A[i] <= X:  
                P[A[i]] = 1
        else:
            return(i-1)
    return(-1)