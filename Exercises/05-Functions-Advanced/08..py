def expression(nums, current_result=0, current_expression=''):
    if not nums:
        print(f'{current_expression}={current_result}')
        return
    expression(nums[1:], current_result + nums[0], f'{current_expression}+{nums[0]}')
    expression(nums[1:], current_result - nums[0], f'{current_expression}-{nums[0]}')

nums = [int(x) for x in input().split(', ')]
expression((nums))


# import itertools
# numbers = [int(n) for n in input().split(', ')]
# n = len(numbers)
#
# prem = set(itertools.permutations(['-'] * n + ['+'] * n, n))
#
# for p in prem:
#     expr = ''.join(itertools.chain(*zip(p, numbers)))
#     res = eval(expr)
#     print(f'{expr}={res}')
