n = int(input())
crops = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    cost = int(parts[1])
    growth_time = int(parts[2])
    daily_growth = int(parts[3])
    days_to_fruit = int(parts[4])
    yield_val = int(parts[5])
    sell_price = int(parts[6])
    total_harvests = int(parts[7])
    
    profit = (yield_val * sell_price * total_harvests) - cost
    time = days_to_fruit + (total_harvests - 1) * daily_growth
    per_day = profit / time if time != 0 else 0  # avo