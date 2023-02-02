n = int(input())
real_sum = sum(range(n + 1))
provided_sum = sum(map(int, input().split(' ')))

print(real_sum - provided_sum)
