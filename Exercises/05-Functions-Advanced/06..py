permutations = set()


def generate(k: int, A: list):
    if k == 1:
        permutations.add(''.join(A))

    else:
        generate(k - 1, A)

        for i in range(k):
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]

            generate(k - 1, A)

s = list(input())
generate(len(s), s)

print('\n'.join(list(permutations)))


02.
def permutations(index, values, on_result):
    if index >= len(values):
        on_result(values)
        return

    for i in range(index, len(values)):
        values[index], values[i] = values[i], values[index]
        permutations(index + 1, values)
        values[index], values[i] = values[i], values[index]

def format_result(values):
    return ''.join(values)

permutations(0, list(input()), lambda x: print(format_result(x)))






