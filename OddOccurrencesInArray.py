def solution(A):
    dic ={1:[], 2:[]}

    for i in A:
        if i not in dic[1]:
            dic[1].append(i)
        else:
            dic[1].remove(i)
    return (dic[1][0])    



def solution(A):
    A = sorted(A)
    for i in range(0,len(A),2):
        if i+1 == len(A):
            return(A[i])
        elif (A[i] != A[i+1]):
            return(A[i])