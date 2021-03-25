price = int(input())
if price >= 300:
    discounted = price - price*(30/100)
    print(int(discounted))
elif price >=200 and price <300:
    discounted = price - price * (20 / 100)
    print (int (discounted))
elif price >=100 and price <200:
    discounted = price - price * (10 / 100)
    print (int (discounted))
elif price >=0 and price <300:
    discounted = price - price * (5 / 100)
    print (int (discounted))
else:
    print(int(price))