def solution(N, A):
    if N == 0:
        return(-1)
    S = [0]*N
    for i in A:
        if i <=N:
            S[i-1]+=1
            print (i)
        else:
            m=max(S)
            S=[m]*N

    return (S)