import random 

print("Welcome to Hangman!")
words =  ["hacker", "bounty", "random"]
secret_word = random.choice(words)
print("You got 5 guesses")
word_list = []

for letter in secret_word:
  word_list += "_"
print(word_list)
  
num = 0
game_over = False

while not game_over:
  guess = input("Guess a letter ").lower()
  for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guess:
      word_list[position] = letter
  if guess not in secret_word:
    num += 1
    guess_left = 5 - num
    print(f"You have {guess_left} guesses left")
    if num >= 5:
      print("You lose")
      game_over = True
  print(word_list)
  
  if "_" not in word_list:
    print("You win")
    game_over = True

