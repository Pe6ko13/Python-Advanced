def math_operations(*nums, **keywords):
    counter = 1
    for i in nums:
        if counter == 1:
            keywords["a"] += i
            counter += 1

        elif counter == 2:
            keywords["s"] -= i
            counter += 1

        elif counter == 3:
            try:
                keywords['d'] /= i

            except ZeroDivisionError:
                pass
            counter += 1

        elif counter == 4:
                keywords["m"] *= i
                counter = 1


    return keywords



print(math_operations(2, 12, 0, -3, 6, -20, -11, a = 1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))