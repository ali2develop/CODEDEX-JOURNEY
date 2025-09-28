import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1+die2
while total != 2:
    print("Nope")
    # 2. Reroll the dice (THIS IS THE CRITICAL MISSING STEP)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # 3. Recalculate the total
    total = die1 + die2
print("Snake Eyes !")
