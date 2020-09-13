# 피보나치 수열, no dynamic programming

def pibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pibonacci(n-1) + pibonacci(n-2)

print(pibonacci(25))