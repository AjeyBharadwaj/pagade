import random
import itertools
import matplotlib.pyplot as plt

no_of_dices = 2
no_on_dice = [1, 3, 4, 6] #Has to be sorted

no_of_runs = 1000000

outcomes = [0]*max(no_on_dice)*2

for i in range(0, no_of_runs):
    total = 0
    for dice in range(0, no_of_dices):
        val = random.choice(no_on_dice)
        outcomes[val-1] += 1            # Check individual outcomes as well.
        total += val
    outcomes[total-1] += 1

stroutcomes = []
for outcome in outcomes:
    stroutcomes.append(str(outcome))

numbers = list(range(1, 13))


# function to add value labels
def addlabels(plt: plt, x, y):
    for i in range(len(x)):
        str = f"{y[i]} : {round(100*y[i]/sum(y), 2)}%"
        plt.text(i+1, y[i]//2, str, ha = 'center')

plt.bar(numbers, outcomes)
plt.title(f'Outcomes in {no_of_runs} times')
plt.xlabel('Number')
plt.ylabel('Outcome')
plt.xticks(numbers)
#plt.yticks(outcomes)
addlabels(plt, numbers, outcomes)
plt.show()
