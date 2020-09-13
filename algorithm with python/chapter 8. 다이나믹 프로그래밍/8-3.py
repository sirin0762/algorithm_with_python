# 호출 되는 함수 확인

d = [0] * 100

def pibo(n):
    print('f(' + str(n) + ')')
    if n == 1 or n == 2:
        return 1

    if d[n]:
        return d[n]
    
    d[n] = pibo(n - 1) + pibo(n - 2)

    return d[n]

pibo(6)