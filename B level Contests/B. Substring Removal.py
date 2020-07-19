n=int(input())
s=input()
first=s[0]
last = s[n-1]

count_first =1
count_last  =1



#if same first and last char
	#eg aacdaa
	# |aacd|aa , |aacda|a ,|aacdaa| (3 ways to cut for 1st)
	# a|acdaa|,a|acda|a , a|acd|aa   (3 ways to cut for second)
	#aa|cdaa| ,aa|cd|aa , aa|cda|a   (3 ways to cut)



for char in s:
	if char==first:
		count_first+=1
	else:
		break

		
		
#aacdeee
	#if first two same then 3ways to remove it(aa,cdeee| a,acdee | ,aacdee |)
	#last charachter(aacd,eee | aacde,ee | aacdee,e | aacdeee, | )
	#we have considered removing all character WAY twice 
	#so lets subtract one!!!!
for char in s[::-1]:
	if char == last:
		count_last+=1
	else:
		break

		
	
if first == last:
	print((count_last*count_first) % 998244353)
else:
	print((count_last+count_first-1) % 998244353)
