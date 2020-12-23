def solution(N, A):
    S={}
    for i in range(1,N+1):
        S[i] = 0
    for i in A:
        if i <=N:
            S[i]=S[i]+1
        elif i > N:
            a = max(S.values())
            for i in range(1,N+1):
                S[i] = a
    return (list(S.values()))
    
