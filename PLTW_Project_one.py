import random 

def hangman():
    art = [
"""---------- 
|         | 
| 
|
|
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|
|
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|         |
|
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|        /|
|
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|        /|\\ 
| 
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|        /|\\ 
|        / 
| 
| 
| """
,
"""---------- 
|         | 
|         O 
|        /|\\ 
|        / \\ 
| 
| 
| """]

    art_index = 0
    bad_letters = []
    word_bank = ['g']
    guesses = 6
    
    word = random.choice(word_bank)
    word_split = list(word)
    space = '-' * len(word)
    space = list(space)
    
    while guesses > 0:
        print(art[art_index])
        print("Letters used: {}".format("".join(bad_letters)))
        
        if "".join(space) == word:
            print("You have correctly guesses the word!")
            
        
hangman()