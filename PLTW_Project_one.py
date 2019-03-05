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
    word_bank = ['acres', 'adult', 'advice', 'arrangement', 'attempt', 'august','Autumn','border','breeze','brick','calm','canal','Casey','cast','chose','claws','coach','constantly'
            ,'contrast','cookies','customs','damage','Danny','deeply','depth','discussion','doll','donkey','essential','exchange','exist','explanation',
            'facing','film','finest','fireplace','floating','folks','fort','garage','grabbed','grandmother','habit','happily','heading','hunter',
            'image','independent','instant','kids','label','lungs','manufacturing','mathematics','melted','memory','mill','mission','moneky','mount','mysterious','neighborhood',
            'nuts','occasionally','official','ourselves','palace','plates','poetry','policemen','positive','possibly','practical','prode','promised','recall','relationship',
            'remarkable','require','rhyme','rocky','rubbed','rush','sale','satellites','satisfied','selection','shake','shaking','shallow','shout','silly','simplest','slight',
            'slip','slope','soap','solar','species','spin','stiff','swung','tales','thumb','tobacco','toy','trap','treated','vapor','vessels','wealth','wolf','zoo']

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