categories = input().split(', ')

n = int(input())

bunker = {category: [] for category in categories}

for _ in range(n):
    category, item, quality_quantity = input().split(' - ')
    quantity, quality = quality_quantity.split(';')
    quantity, quality = quantity.split(':')[1], quality.split(':')[1]
    quantity, quality = int(quantity), int(quality)

    bunker[category].append({'name': item, 'quality': quality, 'quantity': quantity})

total_items = sum([item['quantity']for items in bunker.values() for item in items])
avrg_quality = sum([item['quality']for items in bunker.values() for item in items])
avrg_quality /= len(categories)

print(f'Count of items: {total_items}')
print(f'Average quality: {avrg_quality:.2f}')
print('\n'.join(f"{category} -> {', '.join(item['name'] for item in bunker[category])}" for category in categories))
