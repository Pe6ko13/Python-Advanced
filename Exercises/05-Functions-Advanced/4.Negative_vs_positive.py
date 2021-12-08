numbers = list(map(int, input().split()))

neg = sum(filter(lambda x: x < 0, numbers))
pos = sum(filter(lambda x: x > 0, numbers))

print(neg)
print(pos)

if abs(neg) > pos:
    print("The negatives are stronger than the positives")

else:
    print("The positives are stronger than the negatives")
