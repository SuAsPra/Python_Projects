Welcome to Smiley Savior, a word building quiz game. Created using python, the project uses simple features of the language and modules 
such as pickle, random, time, os and sys. Pushed by the account user https://github.com/SuAsPra on Date:31-12-2024.

The project has a text file that has words to be used in the quiz along with three hints for each word.
The word and the three hints are stored one after the other in different lines. Any user can add the words of 
their choice along with the hints in the text file. There must be three hints exactly. So do not leave any blank lines, 
instead type None or No Hints in that line.
There is a converter function that runs every time inside the program to transfer all the data present 
in the text file into binary database file. Users can also create their own text file consisting of the words and 
hints and then change the path mentioned in the program from the # to their own file.
Users can alter the data in the text file anyway, but ensure  the usual format of one word followed by three hints in separate lines

The converter function has been used once and it is now deactivated by commenting it. The database file is also not present, but it will be created when the program is run once.
If the new user has added any data to the text file or introduced a new text file, they have to activate the converter function by uncommenting it. Currently, the text file used by the creator has 120 words. And when its filtered and used with the converter function, ignoring repetitive words, 111 words were transferred to the database file. The reader function takes the data from the database and the randomise function returns a random word and hints from the pool of data. Then the program enters the showdown function which displays the main menu of the game. Then it enters the app function which runs the game.

Points to note:
When the game runs, always enter a single lowercase alphabet. Not doing so, will rerun the entire program.
This was created on windows OS. For Linux OS, change the following line os.system('cls') into os.system('close') in the program file.