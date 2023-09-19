import random 
import Day_7_hangman_words
import Day_7_hangman_art
#initiate data
stages = Day_7_hangman_art.stages
words = Day_7_hangman_words.word_list

#starting screen
print(Day_7_hangman_art.logo)
input("press enter to start playing")

#randomize word pick and display
chosen_word = random.choice(words)
displayword = list("_" * len(chosen_word))
condition = 0           # end game if condition is 1. 
lives=6                 # lose game if 0

# game loop
while condition == 0 :
    print(displayword)
    attempt = input("guess a letter!\n").lower()
    if (chosen_word.count(attempt) > 0 ):
        for index in range(len(chosen_word)) :
            if chosen_word[index] == attempt :
                if displayword[index] == attempt : 
                    print(f"You already guessed the letter {attempt}!")
                    break
                displayword[index] = attempt
                if (displayword.count("_") == 0):
                    print(displayword)
                    print("you win!")
                    condition = 1 
                    break
    else:
        lives -= 1
        print(stages[lives])
        print(f"The letter {attempt} is not in the word")
        if lives <= 0:
            print(f"You lose. the word was {chosen_word}")
            condition = 1
        
