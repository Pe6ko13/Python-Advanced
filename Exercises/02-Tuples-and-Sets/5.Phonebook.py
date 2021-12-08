def read_contacts():
    contacts = {}
    while True:
        text = input()
        if text.isnumeric():
            break
        name, phone = text.split('-')
        contacts[name] = phone

    return contacts, int(text)

def print_person(contacts, n):
    for _ in range(n):
        name = input()

        if name in contacts:
            print(f"{name} -> {contacts[name]}")
        else:
            print(f"Contact {name} does not exist.")


contacts, n = read_contacts()
print_person(contacts, n)



2.
line = input().split('-')
phonebook = {}

while not len(line) == 1:
    name = line[0]
    number = line[1]
    phonebook[name] = number
    line = input().split('-')

n = int(line[0])

for i in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")




