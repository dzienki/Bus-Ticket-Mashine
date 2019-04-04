from tkinter import *
from Window import Application

def main():
    root = Tk()
    app = Application(master=root)
    root.resizable(width=False, height=False)
    app.mainloop()

main()
