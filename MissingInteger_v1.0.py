def solution(A):
    if len(A)==0:
        return(1)
    elif len(A) == 1:
        if A[0] == 1:
            return(2)
        else:
            return(1)
    A.sort()

    h = 0
    for i in range (0,len(A)-1,1):
        if h == 0:
            if A[i-1]==1:
                h = 1
        elif A[i] -1  != A[i-1] and A[i] != A[i-1]:
            a = A[i-1]+1
            return((a))
    if h==1:
        if A[len(A)-1] == A[len(A)-2]+1:
            return(A[len(A)-1]+1)
        else:
            return(A[len(A)-2]+1)
    return(1)