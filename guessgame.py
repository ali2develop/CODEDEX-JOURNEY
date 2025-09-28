# Write code below 💖

guess = 0
tries = 0 
while guess != 6 and tries < 6:
  tries += 1
  guess = int(input('Guess the number: '))

if guess != 6:
  print("You ran out of tries !")
else:
  print("You got it !")
