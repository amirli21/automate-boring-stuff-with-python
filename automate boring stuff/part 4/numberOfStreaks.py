# Write your code here :-)
import random
numberOfStreaks = 0
trialResult = ''
for experimentNumber in range(10_000):
    for i in range(100):
        trialResult += 'head' if random.randint(0, 1) == 0 else 'tail'
    numberOfStreaks += trialResult.count('head'*6)/10_000
    numberOfStreaks += trialResult.count('tail'*6)/10_000

print('Chance of streak: %s%%' %(numberOfStreaks/100))
