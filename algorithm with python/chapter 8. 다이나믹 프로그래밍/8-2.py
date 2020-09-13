# 메모이제이션을 통한 피보나치 수열

m = [0] * 100

def pibonacci(n):
    if n == 1 or n == 2:
        return n

    if m[n]:
        return m[n]
    
    m[n] = pibonacci(n - 1) + pibonacci(n - 2)
    return m[n]

print(pibonacci(99))