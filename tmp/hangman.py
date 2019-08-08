# encoding = utf-8
__author__ = "Ang Li"

'''
1．玩家一挑选一个秘密单词，单词中有多少个字母，则划多少条横线（这里用下划
线表示）。
2．玩家二每次猜一个字母。
3．如果玩家二猜测的字母正确，玩家一将下划线修改为正确的字母。在本书的游戏
版本中，如果单词中有一个字母出现两次，玩家二也必须猜两次。如果玩家二猜测错误，
玩家一则画出上吊的人的一部分身体（从头部开始），
4．如果玩家二在玩家一画完上吊的人之前猜对单词，玩家二胜利，反之失败。
5. 单词来自一个单词列表，随机生成。
'''

import random
words = ['Yesterday', 'the', 'moon', 'was', 'blue']
word = words[random.randint(0,len(words))]

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
        print(" ".join(guess_list),"\nType q to quit.")
        guess = str(input("Ple Enter your gess >>> "))
        if guess == "q":
            break
        if len(guess) != 1:
            print("Ple Enter one ")
            continue
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

hangman(word)
