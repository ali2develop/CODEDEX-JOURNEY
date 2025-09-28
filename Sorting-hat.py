
#ALl the values set to zero first
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print("==========================Q1==========================")

print("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk""")
answer1 = int(input("Enter your answer (1-2):"))

if answer1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input. Q1")

print("==========================Q2==========================")

print("""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold""")
answer2 = int(input("Enter your answer (1-4):"))

if answer2 == 1:
  Hufflepuff +=2
elif answer2 == 2:
  Slytherin +=2
elif answer2 == 3:
  Ravenclaw +=2
elif answer2 == 4:
  Gryffindor +=2
else:
  print("Wrong input. Q2")

print("===========================Q3=========================")

print("""Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum""")
answer3 = int(input("Enter your answer (1-4):"))
if answer3 == 1:
  Slytherin +=4
elif answer3 == 2:
  Hufflepuff +=4
elif answer3 == 3:
  Ravenclaw +=4
elif answer3 == 4:
  Gryffindor +=4
else:
  print("Wrong input. Q3")

print("=========================SCORES=======================")

print("Score for 🦁 Gryffindor: ",Gryffindor)
print("Score for 🦅 Ravenclaw: ",Ravenclaw)
print("Score for 🦡 Hufflepuff: ",Hufflepuff)
print("Score for 🐍 Slytherin: ",Slytherin)














