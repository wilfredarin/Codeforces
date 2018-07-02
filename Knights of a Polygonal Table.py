#	http://codeforces.com/contest/994/problem/B

n,k = map(int,input().split())
power = list(map(int,input().split()))
coins = list(map(int,input().split()))
ans = [0 in range(n)]
coins_on_sale = []
power_index = [[p[i],i] for i in range(n)]
power_index.sort()


for i in range(n):

	coin_wallet = 0

	for coin in coins_on_sale:
		coin_wallet += coin
	
	#add coin_walet in it's coin and put at correct index
	ans[power_index[i][1]] = coin_wallet + coins[power_index[i][1]]

	#put coins in coins_on_sale
	coins_on_sale.append(coins[power_index[i][1]])
	coins_on_sale.sort()

	if len(coins_on_sale) > k :
		z = z[1:]
		#keeps removing Smallestcoin if it exceeds the limit


for i in ans :
	print(i,end = " ")		





	









