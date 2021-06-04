import random
from tkinter import *
from tkinter import ttk
import sys;
import os;
import shutil;


wordList = [];
def create_wordList():
    with open("words.txt","r") as myfile:
        for  line in myfile.readlines():
            if(len(line) > 5):
                wordList.append(line.replace("\n",""))

def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1 

def select_Random_Word():
    return wordList[random.randrange(0, len(wordList))];

def create_puzzle():
    _str = ""
    for i in range(0,len(current_Word)):
        if(random.randrange(0,2)):
            _str += " _"
        else:
            _str+=" " +current_Word[i]
    return _str
    
create_wordList()
current_Word = select_Random_Word();
current_puzzle = create_puzzle()
used_words = []

remaining_count = 7
print(":"+current_puzzle + " " + str(len(current_puzzle)))
print(":"+current_Word + " " + str(len(current_Word)))
def buttonClicked():
    global remaining_count
    global current_puzzle
    global current_Word
    print(current_Word.find(guess.get()))
    if(current_Word.find(guess.get()) ==-1):
       used_words.append(guess.get())
       remaining_count = remaining_count -1
       remaining.set(remaining_count)
       if(remaining_count == 0):
           remaining.set("Game over")
       guess.set("")
    else:
        index = (current_Word.find(guess.get())*2)+1
        current_puzzle = current_puzzle[:index] + guess.get() + current_puzzle[index+1:]
        hint.set(current_puzzle)
        guess.set("")

    print(list(current_Word))
    temp = current_puzzle.split("_")
    temp = listToString(temp).split(" ")
    if(temp[0] ==""):
        temp.pop(0)
    print(temp)

    if(list(current_Word) == temp):
        remaining.set("Game finished")
   
    
root = Tk()
root.title('Word Guessing Game')  ## window title


frame = ttk.Frame(root, padding='3 3 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

guess = StringVar()
output = StringVar()
hint = StringVar()
remaining = StringVar()
result = StringVar()
hint.set(current_puzzle)

remaining.set(remaining_count)
a_label = ttk.Label(frame, text='Enter a letter to guess: ')
a_label.grid(column=1, row=1, sticky=E)
a_entry = ttk.Entry(frame, width=7, textvariable=guess)
a_entry.grid(column=2, row=1,sticky=E)

b_label = ttk.Label(frame, textvariable=output)

c_label = ttk.Label(frame, text='Current Hint: ')
c_label.grid(column=1, row=3, sticky=E)
d_label = ttk.Label(frame, textvariable=hint)
d_label.grid(column=2, row=3)

e_label = ttk.Label(frame, text='Guesses Remaining: ')
e_label.grid(column=1, row=4, sticky=E)
f_label = ttk.Label(frame, textvariable=remaining)
f_label.grid(column=2, row=4)

button = ttk.Button(frame, text='Submit', command=buttonClicked)
button.grid(column=3, row=5)

g_label = ttk.Label(frame, textvariable=result)
g_label.grid(column=1, row=6)


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>',)

root.mainloop()



