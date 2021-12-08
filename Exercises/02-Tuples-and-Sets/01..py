nums = tuple([float(x) for x in input().split()])

result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1

for key, value in result.items():
    print(f"{key} - {value} times")

# [print(f"{key} - {value} times") for key, value in result.items()]

# from collections import defaultdict
#
# d = defaultdict(int)
# num = map(float, input().split(' '))
#
# for n in num:
#     d[n] += 1
#
# for n, o in d.items():
#     print(f'{n} - {o} items')