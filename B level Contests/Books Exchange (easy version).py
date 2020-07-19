for i in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	a =[0]*n
	for i in range(n):
		if not a[i]:
			pos = l[i]-1
			ans = 1
			while pos != i:
			    ans += 1
			    pos = l[pos]-1
			a+=str(ans)+" "
			a[i]=ans
			pos = l[i]-1
			#this is the OBSERVATION :WilfredarinHack
			#same ans if in same loop of books
			while pos!=i:
				a[pos] = ans
				pos = l[pos]-1
	for i in range(n):
		print(a[i],end=" ")
	print()
 
