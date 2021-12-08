from collections import deque


def stock_availability(list, *args):

    if args[0] == 'delivery':
        for i in args[1:]:
            list.append(i)
        return list

    elif args[0] == 'sell':
        products = deque(list)

        if len(args) == 1:
            products.popleft()
            list = [str(x) for x in products]

        elif isinstance(args[-1], str):
            cupcakes = args[1:]
            new = []
            for i in products:
                if i not in new:
                    new.append(i)
            for s in cupcakes:
                if s in new:
                    new.remove(s)

            # for sweet in cupcakes:
            #     products = [i for i in products if not i == sweet]
            # list = [str(x) for x in products]

            return new

        elif isinstance(args[-1], int):
            number = int(args[-1])
            if len(products) >= number and number > 0:
                for i in range(number):
                    products.popleft()
            list = [str(x) for x in products]

        return list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
