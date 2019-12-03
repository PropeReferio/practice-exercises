def series_sum(n):
    sum = 0.0
    for i in range(0, n):
        sum += 1 / (1 + 3 * i)
    return format(sum, '.2f')

print(series_sum(0))