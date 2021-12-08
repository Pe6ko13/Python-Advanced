words = input().split(', ')

print(', '.join([f'{word} -> {len(word)}' for word in words]))

