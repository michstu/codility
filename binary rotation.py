# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    B = bin(N)
    C = 0
    ST = B[2:]
    res = 0
    o = 0
    ct = 0
    for i in ST:
        if i == '1':
            if o == 1:
                if res < ct:
                    res = ct
                ct = 0
            else:
                o = 1
        else:
            ct = ct + 1        
    return (res)       
 
