data = []
count = 0
sumreview = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        sumreview += len(line)
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('total record is ', len(data))
print(data[0])
print('------------')
print(data[1])
print('average review is ', sumreview / count)