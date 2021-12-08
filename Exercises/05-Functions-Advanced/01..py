def make_abs(seq):
    return [abs(el) for el in seq]

    # return list(map(abs, seq))

nums = [float(el) for el in input().split()]

print(make_abs(nums))