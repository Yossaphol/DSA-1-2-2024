def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main():
    import json
    money = int(input())
    data = convert_key(json.loads(input()))
    
    mon = money
    used = {10: 0, 5: 0, 2: 0, 1: 0}

    for coin in [10,5,2,1]:
        while money >= coin and data[coin] > 0:
            money -= coin
            data[coin] -= 1
            used[coin] += 1 

    print(f"Amount: {mon}")
    if money == 0:
        print("Coin exchange result:")
        for coin in [10, 5, 2, 1]:
            print(f"  {coin} baht = {used[coin]} coins")
        
        print(f"Number of coins: {sum(used.values())}")
    else:
        print("Coins are not enough.")
main()