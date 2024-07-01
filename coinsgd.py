#minimum count and coins used for amount using greedy
def coinsgd(coins,amount):
    coins.sort(reverse=True)
    indx=0
    l=[]
    while amount>0 and indx<len(coins):
        coinvalue=coins[indx]
        if amount>=coinvalue:
            amount=amount-coinvalue
            l.append(coinvalue)
        else:
            indx+=1
    if amount==0:
        print(l)
        return len(l)
    else:
        return -1
        
coins = [1,2,5]
amount = 11
print(coinsgd(coins,amount))