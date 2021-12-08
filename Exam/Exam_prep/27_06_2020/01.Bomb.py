from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = deque([int(x) for x in input().split(', ')])

bombs_type = {
    60: 'Cherry Bombs',
    40: 'Datura Bombs',
    120: 'Smoke Decoy Bombs',
}

produced = {
    'Cherry Bombs': 0,
    'Datura Bombs': 0,
    'Smoke Decoy Bombs': 0,
}

def is_bomb_pouch_full(produced) -> bool:
    return all([value >= 3 for value in produced.values()])


while len(bomb_effects) > 0 and len(bomb_casings) > 0 and not is_bomb_pouch_full(produced):
    bomb_effect = bomb_effects.popleft()
    bomb_casing = bomb_casings.pop()
    bomb_sum = bomb_effect + bomb_casing

    manage_to_produced = False

    if bomb_sum in bombs_type:
        bomb = bombs_type[bomb_sum]
        manage_to_produced = True
        produced[bomb] += 1

    if not manage_to_produced:
        bomb_casing -= 5

        if bomb_casing >= 0:
            bomb_effects.appendleft(bomb_effect)
            bomb_casings.append(bomb_casing)

if not is_bomb_pouch_full(produced):
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

print(f"Bomb Effects: {', '.join(map(str, bomb_effects)) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casings)) if bomb_casings else  'empty'}")

for key, value in produced.items():
    print(f"{key}: {value}")
