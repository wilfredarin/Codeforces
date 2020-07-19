#https://codeforces.com/contest/1375/problem/B
def nbr(arr,n,m):
	for i in range(n):
		for j in range(m):
			nbr = 0
			if (i>0 and j>0) and (i<n-1 and j<m-1):
				nbr = 4 
			elif (i==0 and j==0) or (i==n-1 and j==m-1):
				nbr=2
			elif (i==n-1 and j==0) or (j==m-1 and i==0):
				nbr = 2
			else:
			    nbr =3
			if nbr<arr[i][j]:
				# print("No",i,j,nbr,arr[i][j])
				print("No")
				return 
			else:
				arr[i][j]=nbr
	print("Yes")
	for i in range(n):
		for j in range(m):
			print(arr[i][j],end=" ")
		print("")
	return 

t = int(input())
for i in range(t):
	n,m = map(int,input().split())
	arr = []
	for i in range(n):
		arr.append(list(map(int,input().split())))
	nbr(arr,n,m)


