#https://codeforces.com/contest/1375/problem/C
t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	if a[0]>a[-1]:
		print("No")
	else:
		print("Yes")

