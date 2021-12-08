box = []
for clothing in input().split():
    box.append(int(clothing))

rack_capacity = int(input())
racks = 1
rack_weight = 0

for i in range(len(box)):
    current_clothing = box.pop()
    if current_clothing + rack_weight > rack_capacity:
        racks += 1
        rack_weight = 0
    rack_weight += current_clothing

print(racks)