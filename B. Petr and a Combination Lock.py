#brute force
n = int(input())

#every element in this  list would inputdicate 	one 	way
l = [0]
for i in range(n):
	temp = []
	a = int(input())
	#either we'll add this no or subtract it to the elements of our list
	for e in l:
		temp.extend([e+a,e-a])

	l=temp


for i in l:
	if i%360==0:
		print("YES")
		exit()
print("NO")

#wilfredarin
