n=int(input())
x=int(input())
a=int(input())
s=0

for k in range(-0, n+1):
        s = s + int(x**k)*((a**n)-(a**k))
print(s)