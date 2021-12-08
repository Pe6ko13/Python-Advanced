from collections import deque


# def min_cycles_for_job(jobs, job_index):
#     sorted_jobs = sorted(
#         [(v, i) for (i, v) in enumerate(jobs)]
#     )
#     cycles = 0
#     for (job, index) in sorted_jobs:
#         cycles += job
#         if index == job_index:
#             break
#     return cycles
#
#
# line = [int(x) for x in input().split(', ')]
# n = int(input())
# result = min_cycles_for_job(line, n)
# print(result)

line = [int(x) for x in input().split(', ')]
n = int(input())
count = 0
cycles = deque(sorted([(line[index], index) for index in range(len(line))]))

while cycles:
    number, index = cycles.popleft()
    count += 1
    if index == n:
        print(count)
        break

