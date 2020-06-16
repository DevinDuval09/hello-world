
#Created on Jun 14, 2020

@author: devin


def helloworld(sentence):
    import tkinter as tk
    from tkinter import ttk
    popup = tk.Tk()
    popup.geometry("500x200")
    popup.wm_title("")
    label2 = ttk.Label(popup,text = "Hello World", font=("Helvetica",20))
    label2.pack(side="top", ipadx=10, ipady=10)
    label = ttk.Label(popup, text=sentence, font=("Helvetica",10))
    label.pack(ipadx=10, ipady=10)
    B1 = ttk.Button(popup, text="Okay", command=quit)
    B1.pack(side="bottom", ipadx=10, ipady=10)
    popup.mainloop()