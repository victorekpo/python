def end_zeros(num):
    return len(s := str(num)) - len(s.rstrip("0"))

print(end_zeros(500))
