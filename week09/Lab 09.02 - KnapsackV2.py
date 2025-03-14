import json

itemList_str = input()
W = int(input())

itemList = json.loads(itemList_str)

itemList.sort(key=lambda x: x[0])
n = len(itemList)

dp = []
for _ in range(n + 1):
    row = []
    for _ in range(W + 1):
        row.append((0, []))
    dp.append(row)

for i in range(1, n + 1):
    name, value, weight = itemList[i - 1]
    for w in range(W + 1):
        dp[i][w] = dp[i - 1][w]
        if w >= weight:
            prev_value, prev_selected = dp[i - 1][w - weight]
            new_value = prev_value + value
            new_selected = sorted(prev_selected + [name])
            if new_value > dp[i - 1][w][0]:
                dp[i][w] = (new_value, new_selected)
            elif new_value == dp[i - 1][w][0]:
                if new_selected < dp[i - 1][w][1]:
                    dp[i][w] = (new_value, new_selected)

total_value, selected_items = dp[n][W]

print(f"Total: {total_value}")
for item in selected_items:
    for it in itemList:
        if it[0] == item:
            print(f"{item} -> {it[2]} kg -> {it[1]} THB")
            break
