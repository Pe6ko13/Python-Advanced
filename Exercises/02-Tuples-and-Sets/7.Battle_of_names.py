n = int(input())
odd_num, even_num = set(), set()

for i in range(n):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)
    ascii_sum = ascii_sum // (i + 1)

    if ascii_sum % 2 ==0:
        even_num.add(ascii_sum)
    else:
        odd_num.add(ascii_sum)

even_sum = sum(even_num)
odd_sum = sum(odd_num)

if even_sum == odd_sum:
    result = even_num.union(odd_num)
elif even_sum > odd_sum:
    result = odd_num.symmetric_difference(even_num)
elif odd_sum > even_sum:
    result = odd_num.difference(even_num)

print(', '.join([str(x) for x in result]))

