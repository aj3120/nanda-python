import sys
cache={}
def factMemo(n):
    if n in cache.keys():
        return cache[n]
    else:
        cache[n]=factorial(n)
        return cache[n]

def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)

def combination(n,r):
    c=int(factMemo(n)/(factMemo(n-r)*factMemo(r)))
    return c

def pascal():
    inp = int(sys.argv[1])
    for i in range(inp):
        for k in range(i):
            print(' ',end="")
        for j in range(inp-i):
            print(combination(inp-i-1,j),end=" ")
        print('')

pascal()