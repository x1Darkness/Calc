def power(base, exponent=2):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

num, powNum = map(int, input().split())

print(power(num, powNum))
