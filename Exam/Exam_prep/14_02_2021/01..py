from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosive_powers = deque([int(x) for x in input().split(', ')])

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

firework_show = False

while firework_effects and explosive_powers:
    effect = firework_effects.popleft()
    power = explosive_powers.pop()
    if effect <= 0:
        explosive_powers.append(power)
        continue
    if power <= 0:
        firework_effects.appendleft(effect)
        continue
    result = effect + power

    if result % 3 == 0 and result % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
    elif result % 3 == 0 and not result % 5 == 0:
        fireworks['Palm Fireworks'] += 1
    elif result % 5 == 0 and not result % 3 == 0:
        fireworks['Willow Fireworks'] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_powers.append(power)

    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 and fireworks['Crossette Fireworks'] >= 3:
        firework_show = True
        break

if firework_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    firework_effects = [str(x) for x in firework_effects]
    print(f"Firework Effects left: {', '.join(firework_effects)}")
if explosive_powers:
    explosive_powers = [str(x) for x in explosive_powers]
    print(f"Explosive Power left: {', '.join(explosive_powers)}")

for firework, count in fireworks.items():
    print(f"{firework}: {count}")
