def reverse(num):
    n = 0
    while(int(num)):
        rem = int(num)%10
        n = n*10+rem
        num = int(num)/10
    return n
A,B = map(int,input().split())
A = reverse(A)
B = reverse(B)
C = A+B
print(reverse(C))