N, money, rate = map(int, input().split())

stock_price = list(map(int, input().split()))

loan = 0
stock = 0
for i in range(N - 2):
    if stock:
        money += stock * stock_price[i]
        stock = 0

    if stock_price[i] >= stock_price[i + 1]:
        continue

    if loan:
        money -= loan
        loan = 0

    if money * (rate + 1) >= stock_price[i]:
        loan = money * rate
        money += loan
        stock = money // stock_price[i]
        money -= stock * stock_price[i]

if stock:
    money += stock * stock_price[-2]
    stock = 0

stock = ((money - loan) * (rate + 1) // stock_price[-2])
if stock:
    temp_money = money - loan
    temp_money = (temp_money * (rate + 1)) - (stock_price[-2] * stock) + (stock_price[-1] * stock)

    money = max(money, temp_money)

print(money)
