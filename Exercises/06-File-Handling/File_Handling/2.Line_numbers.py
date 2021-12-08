with open('input') as file:
    lines = [line.strip() for line in file.readlines()]

out = []
for idx, line in enumerate(lines):
    letter_count = sum([len(word) for word in line.split()])
    punctuation = sum([1 for word in line.split() for letter in word if word in r'-,\.!?\''])

    out.append(f'Line {idx + 1}: {line} ({letter_count - punctuation})({punctuation})')

with open('output', 'a') as out_file:
    out_file.writelines([line + '\n' for line in out])

