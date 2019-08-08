# encoding = utf-8
__author__ = "Ang Li"

def hangman(word):
    stages = ["________________",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    wrong = 0
    guess_list = ["_" for x in range(len(word))]
    word_list = list(word)
    while wrong < len(stages):
        print(" ".join(guess_list))
        guess = str(input("Ple Enter your gess >>> "))
        if guess in word_list:
            guess_pos = word_list.index(guess)
            guess_list[guess_pos] = guess
            word_list[guess_pos] = "_"
        else:
            wrong += 1
            for i in range(wrong):
                print(stages[i])
        if "_" not in guess_list:
            print("{}\nGood, you got it.".format(" ".join(guess_list)))
            break
    else:
        print("you lose ! It was {}".format(word))

hangman("attach")
