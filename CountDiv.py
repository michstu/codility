def solution(A, B, K):
    if B == 0:
        return(0)
    r = 0
    for i in range (A,B+1,1):
        d = i % K
        if d == 0:
            r += 1
    return(r)





def solution(A, B, K):
    if B == 0:
        return(0)
    r = o = 0
    for i in range (A,B+1,1):
        d = i % K
        print(i,d)
        if o == 0:
            if d == 0:
                o = i
        else:
            r = (B-o) // K +1

    return(r)


v2
#87%
#For example, for the input [0, 2000000000, 2000000000] the solution returned a wrong answer (got 1 expected 2).
#??
def solution(A, B, K):
    ad = 0
    if A <=0:
        ad = 1

    if B == 0:
        return(1)
    elif K > B:

        return(0)
    elif K == B:
        return(1+ad)
    else:
        RB = B // K 
        RA = A // K
        if (A % K) == 0:
            r = RB - RA + 1
        else:
            r = RB - RA
            
    return(r)