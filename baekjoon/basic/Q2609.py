# 최대공약수와 최소공배수

n, m = map(int, input().split())

def gcd(n, m):
    if m == 0: 
        return n
    else:
        return gcd(m, n % m)
    

num1 = gcd(n, m)
num2 = ((n * m) // num1)

print(num1)
print(num2)