from tkinter import *
from monety import Skarbonka

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.skarbonka = Skarbonka()
        self.viewedText = "aaa"
        self.create_widgets()
        self.center()



    def create_widgets(self):
        self.master.title("Automat biletowy MPK")

        leftFrame = Frame(self)
        leftFrame.pack(side=LEFT,fill=Y)
        middleFrame = Frame(self)
        middleFrame.pack(side=LEFT,fill=Y)
        rightFrame= Frame(self)
        rightFrame.pack(side=LEFT,fill=Y)
        moneyFrame= Frame(self)
        moneyFrame.pack(side=RIGHT,fill=Y)


        b_ticket1= Button(leftFrame, text="Bilet normalny 20 min\n2,80zł",height=5, width=20, bg="#3887d1",
                          overrelief=SUNKEN)
        b_ticket1.pack(anchor=N)
        b_ticket2 = Button(middleFrame, text="Bilet ulgowy 20 min\n1,40zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket2.pack(anchor=N)
        b_ticket3 = Button(leftFrame, text="Bilet normalny 40 min\n3,80zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket3.pack(anchor=N)
        b_ticket4 = Button(middleFrame, text="Bilet ulgowy 40 min\n1,90zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket4.pack(anchor=N)
        b_ticket5 = Button(leftFrame, text="Bilet normalny 60 min\n5,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket5.pack(anchor=N)
        b_ticket6 = Button(middleFrame, text="Bilet ulgowy 60 min\n3,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket6.pack(anchor=N)
        b_ticket7 = Button(leftFrame, text="Bilet normalny 24h\n15,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket7.pack(anchor=N)
        b_ticket8 = Button(middleFrame, text="Bilet ulgowy 24h\n7,50zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket8.pack(anchor=N)
        b_ticket9 = Button(leftFrame, text="Bilet normalny 48h\n24,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket9.pack(anchor=N)
        b_ticket10 = Button(middleFrame, text="Bilet ulgowy 48h\n12,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN)
        b_ticket10.pack(anchor=N)

        #Wyświetlanie tekstu
        self.screen = Text(rightFrame, width=25, height=10, wrap=WORD)
        self.screen.pack(fill=Y, anchor=N)
        self.screen.insert(0.0,self.viewedText+"\nWrzucono: "+str(self.skarbonka.GetOrderCash())+" zl")


        self.quit = Button(rightFrame, text="QUIT", fg="red",height=5, width=20,
                              command=self.master.destroy,overrelief=SUNKEN)
        self.quit.pack(side=BOTTOM)

        photo1 = PhotoImage(file="images/1.png")
        b_money001= Button(moneyFrame,image=photo1, overrelief=SUNKEN)
        b_money001.pack(side=LEFT,anchor=N)
        photo2 = PhotoImage(file="images/2.png")
        b_money002 = Button(moneyFrame, image=photo2, overrelief=SUNKEN, anchor=N)
        b_money002.pack(side=LEFT,anchor=N)
    def center(self):
        #centrowanie okna na ekranie
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

