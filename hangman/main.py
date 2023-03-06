
import random
from hangmanwords import word_list
chosen_word=random.choice(word_list)
lives=6

from hangmanlogo import logo
print(logo)

print(f"Psst,the solution is {chosen_word}")
display=[]
word_lengt=len(chosen_word)
for _ in range(word_lengt):
    display.append("_")
print(display)
end_of_game=False

while not end_of_game:
    guess=input("Guess a letter :").lower()    
    if guess in display:
        print(f"You have already guessed {guess}")
    for possition in range(word_lengt):
        letter=chosen_word[possition]
        if letter==guess:
            display[possition]=letter           
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word.you lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("you lose")            
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You win. ")
    from hangmanarts import stages    
    print(stages[lives])    