import json

def coin_exchange(amount, coins):
    coins = json.loads(coins.replace("'", "\""))
    denominations = sorted(coins.keys(), key=int, reverse=True)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = [{} for _ in range(amount + 1)]
    for denom in denominations:
        denom = int(denom)
        max_count = coins[str(denom)]
        for count in range(1, max_count + 1):
            for i in range(amount, denom - 1, -1):
                if i - denom >= 0 and dp[i - denom] + 1 < dp[i]:
                    dp[i] = dp[i - denom] + 1
                    used_coins[i] = used_coins[i - denom].copy()
                    used_coins[i][denom] = used_coins[i].get(denom, 0) + 1
    print(f"Amount: {amount}")
    if dp[amount] == float('inf'):
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total_coins = 0
        for denom in denominations:
            denom = int(denom)
            count = used_coins[amount].get(denom, 0)
            print(f"  {denom} baht = {count} coins")
            total_coins += count
        print(f"Number of coins: {total_coins}")

amount = int(input())
coins = input()
coin_exchange(amount, coins)
