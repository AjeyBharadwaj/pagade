import random
import itertools

no_of_dices = 2
no_on_dice = [1, 3, 4, 6] #Has to be sorted

no_of_runs = 100000

result_total = []
result_individual = []
result_combination = {}

#Will be using 1 as starting index

for i in range(0, no_of_dices * no_on_dice[-1]+1):
    result_total.append(0)
    result_individual.append(0)

possible_combinations = itertools.product(no_on_dice, repeat=no_of_dices)

for i in possible_combinations:
    result_combination[str(i)] = 0

for i in range(0, no_of_runs):
    total = 0
    outcomes = []
    for j in range(0, no_of_dices):
        no = random.choice(no_on_dice)
        result_individual[no] += 1
        total += no
        outcomes.append(no)
    
    result_combination[str(tuple(outcomes))] += 1
    result_total[total] += 1
    result_individual[total] += 1 #Total is also individual
    
#print("Result Total      : ", result_total)
#print("Result Individual : ", result_individual)    
#print("Result Individual : ", result_combination)    

max = result_total[0]
max_idx = 0
for i in range(1, len(result_total)):
    if result_total[i] > max:
        max = result_total[i]
        max_idx = i
        
print(f"Max is : {max_idx}")
