import random
import os
import sys
from tkinter import *
from tkinter.ttk import *
#https://www.geeksforgeeks.org/open-a-new-window-with-a-button-in-python-tkinter/?ref=gcse connect two pages


def press(b):
    expression=""
    expression= expression + str(b)
    return expression


# type this if want the button shown on output field
#prediction.set(expression)

def keyboard():
    global output
    key = int(radio.get())
    first_word = str(wordArea.get())


    message = first_word

    data_sample = "215.txt"
    text_data = open(data_sample, 'r').read()
    text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").split(' ')
    markov_lib = {}

    for i in range(len(text_data) - key):
        word = " ".join(text_data[i:i + key])
        if word.lower() in markov_lib.keys():
            markov_lib[word.lower()].append(text_data[i + key])
        else:
            markov_lib[word.lower()] = [text_data[i + key]]

    while(True):
        global prediction
        os.system('cls')
        first_word = " ".join(message.split()[0-key:])
        try:
            predicted_next_word = random.choice(markov_lib[first_word.lower()])
        except KeyError as e:
            expression_field.config=Entry(win, textvariable="-------------------------\nThe training text is not big enough to predict the next word. Exited")
            sys.exit(1)
        
        r = message +" ["+predicted_next_word+"] "
        prediction.set(r)
        
        
        if press(b) == "t":
            #os.system('cls')
            message = message + " " + predicted_next_word
            prediction.set(message)
        if expression == "f":
            os.system('cls')
            response = message + " " + {resArea.get()}
            message = message + " " +response
            prediction.set(message)

        if expression == "e":
            prediction.set(message)
            break
        expression = ""

if __name__ == "__main__":
    win = Tk()
    win.title("Keyboard")

    win.geometry('600x600')
    prediction = StringVar()

    radio = IntVar()
    Label(text="Accuracy level", font=('Aerial 11')).pack()
    r1 = Radiobutton(win, text="Accuracy level 1", variable=radio, value=1)
    r1.pack(anchor=N)
    r2 = Radiobutton(win, text="Accuracy level 2", variable=radio, value=2)
    r2.pack(anchor=N)
    r3 = Radiobutton(win, text="Accuracy level 3", variable=radio, value=3)
    r3.pack(anchor=N)
    

    wlbl = Label(win, text = "Input word")
    wlbl.pack()
    wordArea = Entry(win, width=10)
    wordArea.pack()

    rlbl = Label(win, text = "Input response")
    rlbl.pack()
    resArea = Entry(win, width=10)
    resArea.pack()

    lbl = Label(win, text = "Result")
    lbl.pack()
    expression_field = Entry(win, textvariable=prediction) #the result box value can be change due to changes in code
    expression_field.pack()
    button_t = Button(win, text=' Tab ',
        command=lambda: press("t"))
    button_t.pack()
    button_f = Button(win, text=' Nob ',
        command=lambda: press("f"))
    button_f.pack()
    button_e = Button(win, text=' End ',
        command=lambda: press("e"))
    button_e.pack()
    button_s = Button(win, text=' Submit ',
        command=keyboard)
    button_s.pack()
win.mainloop()