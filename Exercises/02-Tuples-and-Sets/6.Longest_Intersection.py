number = int(input())

line_1 = set()
line_2 = set()

max_len = 0
longest_line = set()

for i in range(number):
    line1, line2 = input().split('-')
    start, end = line1.split(',')  #  /  [int(el) for el in line1.split(',')]
    start = int(start)
    end = int(end)
    start1, end1 = line2.split(',')
    start1 = int(start1)
    end1 = int(end1)
    line_1 = set(range(start, end + 1))
    line_2 = set(range(start1, end1 + 1))
    intersection = list(line_1.intersection(line_2))

    if len(intersection) > max_len:
        max_len = len(intersection)
        longest_line = intersection
    line_1 = set()
    line_2 = set()

print(f"Longest intersection is [{', '.join([str(el) for el in longest_line])}] with length {len(longest_line)}")

# longest = sorted(intersection, key=lambda x: -len(x))[0]
