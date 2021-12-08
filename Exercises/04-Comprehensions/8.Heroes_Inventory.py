heroes = input().split(', ')

inventory = {hero: {} for hero in heroes}

line = input()
while not line == 'End':
    hero, item, price = line.split('-')

    if item not in inventory[hero]:
        inventory[hero][item] = int(price)

    line = input()

for hero in heroes:
    print(f'{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}')

