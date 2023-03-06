stages=['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O  |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
      ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
  /     |
       ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
word_list=["cherry",'lion','camel']
import random
chosen_word=random.choice(word_list)
print(f"Psst,the solution is {chosen_word}")
display=[]
word_lengt=len(chosen_word)
for _ in range(word_lengt):
    display.append("_")
print(display)
end_of_game=False

while not end_of_game:

    guess=input("Guess a letter :").lower()

    for possition in range(word_lengt):
        letter=chosen_word[possition]
        if letter==guess:
            display[possition]=letter
        
    print(display)
    if "_" not in display:
        end_of_game=True
        print("You win. ")