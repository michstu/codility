def solution(N, A):
    if N == 0:
        return(-1)
    S ={}
    U = m = 0
    for i in A:
        if i <=N:
            if i in S:
                if S[i] < m:
                    S[i]+=1+m
                else:
                    S[i]+=1
            else:
                S[i]=1+m

        else:
            U = m = max(S.values())

    W = []
    for i in range(1,N+1):
        if i in S and S[i]>=m:
            W.append(S[i])
        else:
            W.append(m)

    return (W)