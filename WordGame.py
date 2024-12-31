import pickle
import random
import time
import sys
import os
def converter():
    f = open("hangmaninfo.txt",'r')
    s = f.read()
    f.close()
    p=[]
    q=[]
    k = s.split('\n')
    for i in k:
        if i=='':
            k.remove(i)
    for i in range(0,len(k)-3,4):
        p.append(k[i])
        q.append([k[i+1],k[i+2],k[i+3]])
    dictionary = {}
    ff = open("database.dat",'ab')
    for i in range(len(p)):
        dictionary[p[i]]=q[i]
        pickle.dump(dictionary,ff)
    ff.close()
def reader():
    f = open("database.dat",'rb')
    data = {}
    try:
        while True:
            data = pickle.load(f)
    except EOFError:
        f.close()
    return data
def randomise(data):
    num = random.randint(0, len(data)-1)
    words = list(data.keys())
    return words[num]
def man1():
    print("  ______________  ")
    print("  |            |  ")
    print("  |   ^    ^   |  ")
    print("  |            |  ")
    print("  |    \\__/    |  ")
    print("  |            |  ")
def man2():
    print("  ______________  ")
    print("  |            |  ")
    print("  |   ^    ^   |  ")
    print("  |            |  ")
    print("  |    ----    |  ")
    print("  |            |  ")
def man3():
    print("  ______________  ")
    print("  |            |  ")
    print("  |   ^    ^   |  ")
    print("  |    ____    |  ")
    print("  |   /    \\   |  ")
    print("  |            |  ")
def man4():
    print("  ______________  ")
    print("  |            |  ")
    print("  |   *    *   |  ")
    print("  |   '    '   |  ")
    print("  |   '    '   |  ")
    print("  |            |  ")
def man5():
    print("  ______________  ")
    print("  |            |  ")
    print("  |   X    X   |  ")
    print("  |            |  ")
    print("  |      O     |  ")
    print("  |            |  ")

def showdown():
    print("     .___   .    .   ___.___ .      .____  .    .       .___    .  .      . ___.___ ______. ____.         ")
    print("     |      /\\  /\\      |    |      |       \\  /        |      / \\  \\    /     |    |     | |   )        ")
    print("     \\__.  /  \\/  \\     |    |      |____    \\/         ----  /___\\  \\  /      |    |     | |__/                        ")
    print("     ___| /        \\ ___|___ |_____ |____    /          ___| /     \\  \\/    ___|___ |_____| |  \\                      ")
    print()
    print("WELCOME to the game of Smiley Savior!\nYou have to guess 3 words one by one. You can guess a letter based on the hint and an incomeplete word provided. ")
    print("For every turn, enter a letter you have guessed. If the letter is present in the word, the blanks get updated")
    print("For every correct letter provided, the savior\'s face stays happy or gets better.\nFor every wrong letter, the savior\'s face becomes sadder and eventually he gets knocked out, its GAME OVERR!!!")
    print("For every wrong guess, another hint will also appear.")
    print("Finding all the three words makes you the Winner!")
def app(word,hintlist,c,lvl):
    placeholder = ''
    gaps = []
    wait=0
    hint = hintlist[0].strip()
    man_lvl = lvl
    if c==1:
        placeholder = "first"
    if c==2:
        placeholder = "second"
    if c==3:
        placeholder = "third"
    for i in range(len(word)):
        gaps.append("_")
    done = []
    while man_lvl!=5:
        isit = 0
        print(placeholder,"word:",gaps,'\n',hint)
        s = input("Enter any letter:")
        if len(s)==1 and ord(s)>=97 and ord(s)<=122:
            pass
        else:
            return None
        if s in word and s not in done:
            done.append(s)
            p = word.index(s)
            for i in range(len(word)):
                if word[i]==s:
                    gaps[i]=s
            if man_lvl!=1:
                man_lvl = man_lvl -1 
        else:
            man_lvl = man_lvl +1
            wait =wait+1
            if wait ==1:
                hint = hint + '\n'+hintlist[1]
            elif wait==2:
                hint = hint + '\n'+hintlist[2]
        for i in word:
            if i in done:
                pass
            else:
                isit = isit+1
        if man_lvl ==1:
            man1()
        elif man_lvl ==2:
            man2()
        elif man_lvl ==3:
            man3()
        elif man_lvl ==4:
            man4()
        elif man_lvl ==5:
            man5()
        if man_lvl==5:
            print("The word was",word)
            print("GAME OVER!!!")
            time.sleep(5)
            ##
            sys.exit()
        if isit == 0:
            print("You have found the",placeholder,"word")
            print("The word is",word)
            if c == 3:
                print("YOU WON!!!")
                time.sleep(5)
                sys.exit()
            return man_lvl
            

if __name__ == "__main__":
    #converter is necessary only for the first time. To use converter, undo the comment in line 156.
    converter()
    data = reader()
    showdown()
    lvl = 1
    c = 0
    already = []
    while c!=3:
        word = randomise(data)
        if word not in already:
            c = c+1
            already.append(word)
            x =app(word.lower(),data[word],c,lvl)
            if x == None:
                os.system('cls')
                c=c-1
                print("You have enter the wrong character or in the wrong format. Try again")
                time.sleep(3)
            else:
                lvl = x
        else:
            pass
    pass
