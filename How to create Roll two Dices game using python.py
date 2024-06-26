from tkinter import * 
import random

root = Tk()
root.geometry("700x450")
root.title("Roll Dice")

label = Label(root, text="", font=("times", 260))
label.pack()

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}')

button = Button(root, text="Let's Roll...", width=40, height=5, font=10, bg="white",
                bd=2, command=roll)
button.pack(padx=10, pady=10)

root.mainloop()
