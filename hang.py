import random
 

 
words = ['rainbow', 'computer', 'science', 'programming', 
         'python', 'mathematics', 'player', 'condition', 
         'reverse', 'water', 'board', 'geeks'] 
 
# random word
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 7
 
 
while turns > 0:
     
    failed = 0
    for char in word: 
         
        # comparing that character with
        # the character in guesses
        if char in guesses: 
            print(char)
             
        else: 
            print("_")
             
            # incremented in failure
            failed += 1
             
 
    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win") 
         
        # this print the correct word
        print("The word is: ", word) 
        break
     
    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")
     
    # every input character will be stored in guesses 
    guesses += guess 
     
    #  input with the character in word
    if guess not in word:
         
        turns -= 1
         
        # if the character doesn’t match the word
        # then “Wrong” will be given as output 
        print("Wrong")
        print("You have", + turns, 'more guesses')
         
         
        if turns == 0:
            print("You Loose")
