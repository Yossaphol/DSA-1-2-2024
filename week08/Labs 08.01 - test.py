def convert_key(data):
    """Convert JSON keys to integers"""
    return {int(k): v for k, v in data.items()}

def coinExchange(amount, coins):
    print(f"Amount: {amount}")
    available_coins = sorted(coins.keys(), reverse=True)  # Sort coins in descending order
    change = {}
    total_coins_used = 0
    remaining_amount = amount
    
    for coin in available_coins:
        if remaining_amount <= 0:
            break
        
        num_coins = min(remaining_amount // coin, coins[coin])  # Use the max possible coins available
        change[coin] = num_coins
        total_coins_used += num_coins
        remaining_amount -= num_coins * coin
    
    if remaining_amount > 0:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin in available_coins:
            print(f"  {coin} baht = {change.get(coin, 0)} coins")
        print(f"Number of coins: {total_coins_used}")

def main():
    import json
    amount = int(input())
    coins = convert_key(json.loads(input()))
    coinExchange(amount, coins)
main()
