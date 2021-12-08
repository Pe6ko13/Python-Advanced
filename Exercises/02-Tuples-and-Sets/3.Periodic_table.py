# n = int(input())
# element = set()
# for i in range(n):
#     elements = input().split()
#     for el in elements:
#         element.add(el)
# [print(elem) for elem in element]


n = int(input())
elements = set()
for i in range(n):
    elements = elements.union(set(input().split()))
[print(elem) for elem in elements]
