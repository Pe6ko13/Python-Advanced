def numbers_searching(*args):
    x = list(args)
    list2 = []
    missing = 0

    while x:
        if x[0] in x[1:] and x[0] not in list2:
            list2.append(x[0])
        x.pop(0)

    # for i in range(min(args), max(args) + 1):
    #     if args.count(i) > 1:
    #         list2.append(i)

    new_list = sorted(list2)

    if new_list:
        for i in range(min(new_list), max(new_list)):
            if i not in new_list:
                missing = i
                break

    return [missing, new_list]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
