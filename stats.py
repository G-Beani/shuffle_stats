import random
import matplotlib.pyplot as plt
import numpy as np

#resolution of the simulation
resolution = 30

#max number of shuffles that will be shown on graph
max = 10

#deck creation
deck_size = 100 #even is safer
deck = []
for i in list(range(0, deck_size)):
    deck.append(i)

#function for inserting a in b
def insert(a,b):
    temp = deck[a]
    while a > b:
        deck[a] = deck[a-1]
        a = a-1
    deck[b] = temp
    return None

#function for rotating
def simplify():
    while(deck[0]) != 0:
        insert(deck_size-1,0)
    return None
    
#functions for shuffling n times
def computerShuffle(n):
    for i in list(range(0,n)):
        random.shuffle(deck)
    return None
    
def riffleShuffle(n):
    half = int(deck_size/2)
    for i in list(range(0,n)):
        temp_deck = []
        for j in list(range(0, half)):
            if bool(random.getrandbits(1)):
                temp_deck.append(deck[j])
                temp_deck.append(deck[half+j])
            else:
                temp_deck.append(deck[half+j])
                temp_deck.append(deck[j])
        for k in list(range(0, deck_size)):
            deck[k] = temp_deck[k]
    return None
    
#function for verifying if deck is ordered
def ordered():
    ordered = True
    for i in list(range(0,deck_size-1)):
        ordered = ordered*(deck[i]<deck[i+1])
    return ordered

#function for measuring randomness
def countSteps():
    simplify()
    
    steps = 0
    pop = 1
    pos = 2
    
    while ordered() == False:
        pop_val = deck[pop]
        pos_val = deck[pos]
        
        if pop_val > pos_val:
            new_loc = 0
            comparative = deck[new_loc]
            while comparative < pos_val:
                new_loc += 1
                comparative = deck[new_loc]
            insert(pos,new_loc)
            #print(deck)
            steps += 1
        pop = pos
        pos += 1
    
    return steps
    
#trials

x = list(range(1, max))

Computer_List = []
for i in x:
    computerShuffle(i)
    avg = countSteps()
    for j in list(range(1, resolution)):
        computerShuffle(i)
        avg = (avg + countSteps())/2
    Computer_List.append(int(round(avg)))

Riffle_List = []
for i in x:
    riffleShuffle(i)
    avg = countSteps()
    for j in list(range(1, resolution)):
        riffleShuffle(i)
        avg = (avg + countSteps())/2
    Riffle_List.append(int(round(avg)))

fig, ax = plt.subplots()

ax.plot(x, Computer_List, linewidth=2.0, label = "Computer")
ax.plot(x, Riffle_List, linewidth=2.0, label = "Riffle")
ax.set_xlabel('Times shuffled')
ax.set_ylabel('Randomness')
fig.suptitle('Deck size: 100 - Average of 30 experiments')

plt.legend()
plt.text(0, 35, 'Randomness measured by number of steps needed to restore order', dict(size=10))
plt.show()
