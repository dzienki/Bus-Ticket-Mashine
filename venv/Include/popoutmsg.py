from tkinter import *
def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Informacja")
    label = Label(popup, text=msg, font=("Verdana", 17))
    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    label.pack(side=TOP, fill=X)
    B1 = Button(popup, text="Zamknij", font=("Verdana", 17), bg="#6d6e70", fg="red", height=2,
                command=popup.destroy)
    B1.pack(side=BOTTOM, fill=X)
    popup.mainloop()

class Error(Exception):
    pass
class ValueTooSmall(Error):
    pass
