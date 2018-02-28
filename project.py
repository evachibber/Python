import random

guesses =0

print("hello!What's your name?")
name=input()
number=random.randint(1,20)
print(name+", i am thinking of a number between 1 to 20")

while guesses<6:
  print("Make a guess")
  guess=int(input())
  
  guesses=guesses+1
  
  if guess<number:
    print("the guess you made is low")
    
  if guess>number:
    print("the guess you made is high")
    
  if guess==number:
    break
  
if guess==number:
  guesses=str(guesses)
  print("Great"+name+"you guessed my number in"+guesses+"guesses.")

if guess!=number:
  number=str(number)
  print("u guessed it wrong.The number i was guessing was"+number)