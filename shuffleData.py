import random

file = open("output/filtered_sms_sample.txt")
o = open('output/sampleData.txt', 'w')
count = 0
temp = random.randint(0, 100)
while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for i, line in enumerate(lines):
        if i % 100 == temp:
            temp = random.randint(0, 100)
            count += 1
            o.write(line)
o.close()
file.close()
