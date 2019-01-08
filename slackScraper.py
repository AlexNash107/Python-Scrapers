import re
import pyperclip
import itertools

time_pattern = re.compile(r'''

# 8:24 11:24 11:24
(((\d\d)|(\d)) # the 8 in 8:24 or 11 in 11:24
: # first separator so : in 8:24
\d\d
)

''', re.VERBOSE)
           
#time_pattern = "((\d\d|\d):\d\d)"
#
times = pyperclip.paste()

returnTimes = time_pattern.findall(times)

timeList = []
for time_pattern in returnTimes:
    timeList.append(time_pattern[0])

#print(timeList)

# used the list replace method to remove the :
zzz = [s.replace(':', '') for s in timeList]
bbb = list(map(int, zzz))

bbb = [i/100 for i in bbb]
print(bbb)

count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0


for i in bbb:
    if i > -1 and i < 1:
        count0 += 1
for i in bbb:
    if i > 1 and i < 2:
        count1 += 1
for i in bbb:
    if i > 2 and i < 3:
        count2 += 1
for i in bbb:
    if i > 3 and i < 4:
        count3 += 1
for i in bbb:
    if i > 4 and i < 5:
        count4 += 1
for i in bbb:
    if i > 5 and i < 6:
        count5 += 1
for i in bbb:
    if i > 6 and i < 7:
        count6 += 1
for i in bbb:
    if i > 7 and i < 8:
        count7 += 1
for i in bbb:
    if i > 8 and i < 9:
        count8 += 1
for i in bbb:
    if i > 9 and i < 10:
        count9 += 1
for i in bbb:
    if i > 10 and i < 11:
        count10 += 1
for i in bbb:
    if i > 11 and i < 12:
        count11 += 1
for i in bbb:
    if i > 12 and i < 13:
        count12 += 1
for i in bbb:
    if i > 13 and i < 14:
        count13 += 1
for i in bbb:
    if i > 14 and i < 15:
        count14 += 1
for i in bbb:
    if i > 15 and i < 16:
        count15 += 1
for i in bbb:
    if i > 16 and i < 17:
        count16 += 1
for i in bbb:
    if i > 17 and i < 18:
        count17 += 1
for i in bbb:
    if i > 18 and i < 19:
        count18 += 1
for i in bbb:
    if i > 19 and i < 20:
        count19 += 1
for i in bbb:
    if i > 20 and i < 21:
        count20 += 1
for i in bbb:
    if i > 21 and i < 22:
        count21 += 1
for i in bbb:
    if i > 22 and i < 23:
        count22 += 1
for i in bbb:
    if i > 23 and i < 24:
        count23 += 1

print('Breakdown by hour: \n')

#print(f'12:00AM - 1:00 AM: {count0}\n')
#print(f'1:00AM - 2:00 AM: {count1}\n')
#print(f'2:00AM - 3:00 AM: {count2}\n')
#print(f'3:00AM - 4:00 AM: {count3}\n')
#print(f'4:00AM - 5:00 AM: {count4}\n')
#print(f'5:00AM - 6:00 AM: {count5}\n')
#print(f'6:00AM - 7:00 AM: {count6}\n')
#print(f'7:00AM - 8:00 AM: {count7}\n')
print(f' {count8}')
print(f' {count9}')
print(f' {count10}')
print(f' {count11}')
print(f' {count12}')
print(f' {count13}')
print(f' {count14}')
print(f' {count15}')
print(f' {count16}')
print(f' {count17}')
print(f' {count18}')
#print(f' {count19}')
#print(f'8:00PM - 9:00 PM: {count20}\n')
#print(f'9:00PM - 10:00 PM: {count21}\n')
#print(f'10:00PM - 11:00 PM: {count22}\n')
#print(f'11:00PM - 12:00 AM: {count23}\n')

print('', len(timeList))
print('Total ^')
