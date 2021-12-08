n = int(input())
invaited = set()

for i in range(n):
    invaited.add(input())

ticket = input()

arrived = set()
while not ticket == 'END':
    arrived.add(ticket)
    ticket = input()

print(len(invaited.difference(arrived)))
print(invaited.difference(arrived))