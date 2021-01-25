import random

play_condition = True

while play_condition:

    '''
    GAME RULES
    HANGMAN GAME
    '''
    print("Hello, this is Hangman game, in this you have to guess the letters of the words before you ran out of lives."
          "\nCommon let's play some games shall we?"
          "\nOkay, enough intro,"
          "\nLet's jump right onto the game"
          "\nHere below is the board which you need to fill by guessing the right words."
          "\nEnjoy!!\n\n")

    # These words are just from top of my head
    words = ["apple", "mango", "pizza", "rick", "nebula", "razer", "omen", "sider", "siri", "popcorn"]
    lives = 5
    state = "loose"
    args = ""
    word_set = random.choice(words).lower()

    board = "_ " * len(word_set)
    board = board.split()

    print("\t" + " ".join(board))

    def find_all_indicies(k, l):
        ans = [x for x in range(len(l)) if l.startswith(k, x)]
        return ans
    while lives:
        if "_" not in board:
            state = "win"
            break
        print(f"You have {lives} guess remaining.")
        guess = input("Guess: ").lower()
        if guess in word_set:
            print("Correct")
            guess_indexes = find_all_indicies(guess, word_set)
            for i in guess_indexes:
                board[i] = guess
            lives += 1
        else:
            print("OOps! You guessed wrong")
        print("\t" + " ".join(board))
        lives -= 1

    if state == "loose":
        args = "You ran out of lives"
    elif state == "win":
        args = "You won, Hurrah"
    play_again = input(f"{args}. Press 'Y' to play again or 'N' to quit.").upper()
    if play_again == 'Y':
        play_condition = True
    else:
        play_condition = False
        print("Will see ya soon!! :-)")
