n = int(input())
a1=n%10
a2=n//10
if a2>a1:
        max=a2
        print(max-a1)
else :
       max=a1
       print(max-a2)
       