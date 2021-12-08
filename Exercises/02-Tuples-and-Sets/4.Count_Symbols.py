from collections import defaultdict

text = input()

letters = defaultdict(int)
# letters = {}

for i in text:

    letters[i] += 1                              # option 1

    # if i not in letters:
        #letters[i] = 0                          # option 2
    # letters[i] += 1


    # letters[i] = letters.get(i, 0) + 1         # option 3


sorted = sorted(letters.items(), key=lambda x: x[0])
for letter, count in sorted:
    print(f"{letter}: {count} time/s")

# for letter in sorted(letters):
#     print(f'{letter}: {letters[letter]} time/s')



2.
