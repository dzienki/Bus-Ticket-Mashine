from tkinter import *
from Window import Application

def main():
    try:
        root = Tk()
        app = Application(master=root)
        root.resizable(width=False, height=False)
        app.mainloop()
    except:
        print("Błąd w module main!!\nTworzenie okna głównego ")

if __name__=="__main__":
    main()
