def calculate_net_sales(S):
    slabs = [
        (100000, 0),
        (100000, 5),
        (100000, 10),
        (100000, 15),
        (100000, 20),
        (100000, 25),
        (None, 30)
    ]
    tax = 0
    remaining = S
    for max_amount, rate in slabs:
        if remaining <= 0:
            break
        if max_amount is None:
            amount = remaining
        else:
            amount = min(max_amount, remaining)
        tax += (amount * rate) // 100  # Using integer division as pe