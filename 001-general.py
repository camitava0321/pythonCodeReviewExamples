# -*- coding: utf-8 -*-
# author : Amitava Chakraborty

from amodule import aMODULE
from amodule import amodule
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

unUsed = 0
# %%


def rollDice():
    roll = random.randint(1, 100)
    return roll


def checkRoll(roll):
    if roll == 100:
        # print roll,'roll was 100, you lose. What are the odds?! Play again!'
        return False
    elif roll <= 51:
        # print roll,'roll was 1-50, you lose.'
        return False
    elif 100 > roll >= 51:
        # print roll,'roll was 51-99, you win! *pretty lights flash* (play more!)'
        return True


'''
Simple bettor, betting the same amount each time.
'''


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    # wager X
    wX = []
    # value Y
    vY = []

    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    # starts with 1, to avoid confusion so we start @ wager 1
    currentWager = 1

    while currentWager <= wager_count:
        roll = rollDice()
        if checkRoll(roll):
            value += wager
        else:
            value -= wager

        wX.append(currentWager)
        vY.append(value)
        currentWager += 1
        plt.plot(wX, vY)
        if value < 0:
            value = 'Broke!'
            break
        # print 'Attempt: ',currentWager, 'Funds:', value


def complex_bettor(funds):
    value = funds
    # Complexity 1: Random Initial (or Fixed) Wager
    wager = random.randrange(100, value/10, 100)
    # Complexity 2: Max How many times to play
    maxWagers = random.randrange(80, 120, 10)
    # wager X
    wX = []
    # value Y
    vY = []

    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    # starts with 1, to avoid confusion so we start @ wager 1
    currentWager = 1

    while value > 0:
        quitted = False
        roll = rollDice()
        if checkRoll(roll):
            value += wager
        else:
            value -= wager

        wX.append(currentWager)
        vY.append(value)
        # Complexity 3: Next wager is always 10th of the value remaining, minimum 100
        wager = min(100, value/10)
        currentWager += 1
        plt.plot(wX, vY)
        #print ('Attempt: ',currentWager, 'Funds:', value)
        if currentWager == maxWagers:
            break
        # Complexity 4: After 75% of the game, player is given choice to quit
        gameFraction = float(currentWager)/float(maxWagers)
        if gameFraction >= 0.75:
            quitted = quitGame(gameFraction, value/funds)
            # print(quitted)
            if quitted == True:
                break
    return currentWager, value, quitted


def quitGame(gameFraction, valueFraction):
    numberOfFalses = np.full(int(gameFraction*100), False)
    numberOfTruths = np.full(int(valueFraction*100), True)
    listOfTrueFalses = np.concatenate(
        (numberOfFalses, numberOfTruths), axis=None)
    print(listOfTrueFalses)
    return random.choice(listOfTrueFalses)


# %%
simple_bettor(10000, 100, 100)


def quitGame(gameFraction, valueFraction):
    numberOfFalses = np.full(int(gameFraction*100), False)
    numberOfTruths = np.full(int(valueFraction*100), True)
    listOfTrueFalses = np.concatenate(
        (numberOfFalses, numberOfTruths), axis=None)
    print(listOfTrueFalses)
    return random.choice(listOfTrueFalses)


# %%
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
while x < 10000:
    simple_bettor(10000, 1000, 10)
    x += 1
plt.show()

# %%
x = 0

# start this off @ 1, then add, and increase 50 to 500, then 1000
playersShare = 0
casinoShare = 0
while x < 100:
    wagers, finalFund, quitted = complex_bettor(10000)
    print("Player: ", x, "---# of wagers: ", wagers,
          'Final Funds: ', finalFund, 'Quit: ', quitted)
    if finalFund > 10000:
        playersShare += finalFund
    else:
        casinoShare += abs(finalFund)
    x += 1

print("Total Fund Played: ", 10000*100, "Players: ",
      playersShare, "Casino: ", casinoShare)
plt.show()

# %%
# Now, just to test our dice, let's roll the dice 100 times.
x = 0
while x < 100:
    result = rollDice()
    print(result)
    x += 1


# %%
for _ in range(10):
    for _ in range(5):
        for _ in range(3):
            for _ in range(1):
                print("Baa, Baa, black sheep")

for _ in range(4):
    for _ in range(3):
        print("Have you any wool?")

for _ in range(10):
    for _ in range(5):
        for _ in range(3):
            if True:
                for _ in range(3):
                    print("Yes, sir, yes, sir!")


# %%
# list_primes.py
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def list_primes(upper):
    for number in range(2, upper):
        if is_prime(number):
            print(F"{number} is prime")


list_primes(10)

# %% 0 error-prone cases
# Ex 1


def foo(bar=[]):        # bar is optional and defaults to [] if not specified
    bar.append("baz")    # but this line could be problematic, as we'll see...
    return bar


# Ex 2
class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


# Ex 3
try:
    l = ["a", "b"]
    int(l[2])

except ValueError, IndexError:  # To catch both exceptions, right?
    pass

# Ex 4
x = 10


def foo():
    x += 1
    print x


# Ex 5
def odd(x): return bool(x % 2)


numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
    del numbers[i]  # BAD: Deleting item from a list while iterating over it

# 6: Confusing how Python binds variables in closures


def create_multipliers():
    return [lambda x: i * x for i in range(5)]


for multiplier in create_multipliers():
    print multiplier(2)


# 7: Failing to address differences between Python 2 and Python 3


def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)


def bad():
    e = None
    try:
        bar(int(sys.argv[1]))
    except KeyError as e:
        print('key error')
    except ValueError as e:
        print('value error')
    print(e)


# %%
print(amodule(50))

# %%
print(aMODULE(50))
