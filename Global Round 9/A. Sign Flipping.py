#https://codeforces.com/contest/1375/problem/A
t = int(input())
for c in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a = [abs(i) for i in a]
    for i in range(n):
        if i%2==0:
            a[i] = -1*a[i]
    for i in a:
        print(i,end=" ")
    print("")