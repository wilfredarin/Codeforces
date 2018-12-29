n,k =map(int,input().split())
def block(x): 
      
    v = [] 
    a=[]
   
    print ("Blocks for %d : " %x, end="") 
    while (x > 0): 
        v.append(int(x % 2)) 
        x = int(x / 2) 
  
    
    for i in range(0, len(v)): 
        if (v[i] == 1): 
            a.append(i) 
    return (a)       


t=block(n)
print(t)
if len(t)>k or k>n:
	print("NO")
	exit()
l=[]
for i in t:
	l.append([j for j in range(i+1)])
print(l)
for i in l:
	
