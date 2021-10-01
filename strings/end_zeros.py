def end_zeros(num: int) -> int:
    a=len(str(num))
    b=len(str(num).rstrip('0'))
    return ((a) - (b))

print(end_zeros(0))
print(end_zeros(5000))

