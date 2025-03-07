import json

def convert_key(data):
    """แปลง key ของ dictionary จาก string เป็น int"""
    return {int(k): v for k, v in data.items()}

def coin_exchange(amount, coins):
    """ใช้ Dynamic Programming หาเหรียญที่ต้องใช้ให้น้อยที่สุด"""
    dp = [float('inf')] * (amount + 1)  # กำหนดค่าเริ่มต้นเป็น infinity
    dp[0] = 0  # ไม่ต้องใช้เหรียญในการแลก 0 บาท
    coin_used = {}  # ใช้บันทึกว่าแต่ละจำนวนเงินใช้เหรียญอะไร

    for coin in coins:
        for value in range(coin, amount + 1):
            if dp[value - coin] + 1 < dp[value] and coins[coin] > 0:
                dp[value] = dp[value - coin] + 1
                coin_used[value] = coin

    # ถ้าค่า dp[amount] ยังเป็น infinity แสดงว่าไม่สามารถแลกเหรียญได้
    if dp[amount] == float('inf'):
        return None

    # หาเหรียญที่ใช้จริง
    result = {coin: 0 for coin in coins}  # ตั้งค่าทุกเหรียญให้เริ่มต้นเป็น 0
    remaining = amount
    while remaining > 0:
        if remaining not in coin_used:
            return None  # กรณีเหรียญมีไม่พอ
        coin = coin_used[remaining]
        result[coin] += 1
        remaining -= coin
        coins[coin] -= 1  # ลดจำนวนเหรียญที่มีลง

    return result

def main():
    amount = int(input())  # รับค่าจำนวนเงินที่ต้องการแลก
    coins = convert_key(json.loads(input()))  # รับค่าจำนวนเหรียญที่มี

    print(f"Amount: {amount}")
    
    result = coin_exchange(amount, coins)
    
    if result is None:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        total_coins = sum(result.values())  # นับจำนวนเหรียญทั้งหมด
        for coin in sorted(coins.keys(), reverse=True):  # เรียงจากเหรียญที่มีค่ามากสุดไปน้อยสุด
            print(f"  {coin} baht = {result[coin]} coins")
        print(f"Number of coins: {total_coins}")

main()
