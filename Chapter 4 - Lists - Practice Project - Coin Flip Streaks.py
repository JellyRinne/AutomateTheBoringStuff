import random
numberOfStreaks = 0
#0 is heads
#1 is tails
for experimentNumber in range(10000):
    flips = []
    for i in range(100):
        if random.randint(0,1):
            flips.append('H')
        else:
            flips.append('T')
    
    for x in range(100 - 6):
        if flips[x] == flips[x + 1] == flips[x + 2] == flips[x + 3] == flips[x + 4] == flips[x + 5]:
            numberOfStreaks += 1
            break

print('Streaks: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100))