data = [(25923, 7.312), (25904, 7.115), (25897, 7.046), (25908, 7.208), (25937, 7.276)]

sum_bytes = 0
sum_time = 0
for d in data:
    sum_bytes += d[0]
    sum_time += d[1]

mean = sum_bytes / sum_time
print(f'Total mean time: {mean}')
