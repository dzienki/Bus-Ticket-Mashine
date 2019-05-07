# coding=utf-8
from tkinter import *
from monety import *
from Tickets import *
from popoutmsg import *


class Application(Frame, Skarbonka, Bilety):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        Skarbonka.__init__(self)
        Bilety.__init__(self)
        self.master = master
        self.pack()
        master.iconbitmap('images/mobileMPK_ico.ico')
        self.inicializephoto()
        self.viewedText = ""
        self.create_widgets()
        self.center()

    def inicializephoto(self):
        self.photo10 = PhotoImage(file="images/100.png")
        self.photo9 = PhotoImage(file="images/9.png")
        self.photo8 = PhotoImage(file="images/8.png")
        self.photo7 = PhotoImage(file="images/7.png")
        self.photo6 = PhotoImage(file="images/6.png")
        self.photo5 = PhotoImage(file="images/5.png")
        self.photo4 = PhotoImage(file="images/4.png")
        self.photo3 = PhotoImage(file="images/50.png")
        self.photo2 = PhotoImage(file="images/20.png")
        self.photo1 = PhotoImage(file="images/10.png")

    def create_widgets(self):

        self.master.title("Automat biletowy MPK")

        # ramki dla efektów stylistycznych
        leftFrame = Frame(self)
        leftFrame.pack(side=LEFT, fill=Y)
        middleFrame = Frame(self)
        middleFrame.pack(side=LEFT, fill=Y)
        rightFrame = Frame(self)
        rightFrame.pack(side=LEFT, fill=Y)
        moneyFrame1 = Frame(self)
        moneyFrame1.pack(side=LEFT, fill=Y)
        moneyFrame2 = Frame(self)
        moneyFrame2.pack(side=RIGHT, fill=Y)

        # Przyciski z biletami
        b_ticket1 = Button(leftFrame, text="Bilet normalny 20 min\n2,80zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(2.80))
        b_ticket1.pack(anchor=N)
        b_ticket2 = Button(middleFrame, text="Bilet ulgowy 20 min\n1,40zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(1.40))
        b_ticket2.pack(anchor=N)
        b_ticket3 = Button(leftFrame, text="Bilet normalny 40 min\n3,80zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(3.80))
        b_ticket3.pack(anchor=N)
        b_ticket4 = Button(middleFrame, text="Bilet ulgowy 40 min\n1,90zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(1.90))
        b_ticket4.pack(anchor=N)
        b_ticket5 = Button(leftFrame, text="Bilet normalny 60 min\n5,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(5.00))
        b_ticket5.pack(anchor=N)
        b_ticket6 = Button(middleFrame, text="Bilet ulgowy 60 min\n3,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(3.00))
        b_ticket6.pack(anchor=N)
        b_ticket7 = Button(leftFrame, text="Bilet normalny 24h\n15,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(15.00))
        b_ticket7.pack(anchor=N)
        b_ticket8 = Button(middleFrame, text="Bilet ulgowy 24h\n7,50zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(7.50))
        b_ticket8.pack(anchor=N)
        b_ticket9 = Button(leftFrame, text="Bilet normalny 48h\n24,00zł", height=5, width=20, bg="#3887d1",
                           overrelief=SUNKEN, command=lambda: self.AddTicket(24.00))
        b_ticket9.pack(anchor=N)
        b_ticket10 = Button(middleFrame, text="Bilet ulgowy 48h\n12,00zł", height=5, width=20, bg="#3887d1",
                            overrelief=SUNKEN, command=lambda: self.AddTicket(12.00))
        b_ticket10.pack(anchor=N)

        # Wyświetlanie tekstu
        self.screen = Text(rightFrame, width=25, height=10, wrap=WORD)
        self.screen.pack(fill=Y, anchor=N)
        self.write("")
        # kup bilety
        buyTicket = Button(rightFrame, height=3, text="Kup Bilety", bg="green", command=lambda: self.buyTickets())
        buyTicket.pack(anchor=N, fill=X)
        # platność karta
        buyViaCard = Button(rightFrame, height=3, text="Zapłać kartą", bg="green", command=lambda: self.buyViaCardm())
        buyViaCard.pack(anchor=N, fill=X)
        # zwrot kasy
        returnMoney = Button(rightFrame, height=3, text="Zwróć monety", bg="green",
                             command=lambda: self.giveMoneyBack())
        returnMoney.pack(anchor=N, fill=X)
        # usuwanie biletow
        returnTicket = Button(rightFrame, height=3, text="Usuń bilet", bg="green", command=lambda: self.deleteTicket())
        returnTicket.pack(anchor=N, fill=X)

        # exit button
        quit = Button(rightFrame, text="Wyjście", bg="red", fg="white", height=2, width=20,
                      command=self.master.destroy, overrelief=SUNKEN)
        quit.pack(side=BOTTOM)

        # Przyciski z monetami
        b_money010 = Button(moneyFrame1, image=self.photo4, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(0.1,w.get()), self.write("")))
        b_money010.pack(anchor=N)
        b_money020 = Button(moneyFrame1, image=self.photo5, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(0.2,w.get()), self.write("")))
        b_money020.pack(anchor=N)
        b_money050 = Button(moneyFrame1, image=self.photo6, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(0.5,w.get()), self.write("")))
        b_money050.pack(anchor=N)
        b_money100 = Button(moneyFrame2, image=self.photo7, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(1,w.get()), self.write("")))
        b_money100.pack(anchor=N)
        b_money200 = Button(moneyFrame2, image=self.photo8, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(2,w.get()), self.write("")))
        b_money200.pack(anchor=N)
        b_money500 = Button(moneyFrame2, image=self.photo9, overrelief=SUNKEN,
                            command=lambda: (self.ThrowMoney(5,w.get()), self.write("")))
        b_money500.pack(anchor=N)
        b_money1000 = Button(moneyFrame1, image=self.photo1, overrelief=SUNKEN,
                             command=lambda: (self.ThrowMoney(10,w.get()), self.write("")))
        b_money1000.pack(anchor=N)
        b_money2000 = Button(moneyFrame1, image=self.photo2, overrelief=SUNKEN,
                             command=lambda: (self.ThrowMoney(20,w.get()), self.write("")))
        b_money2000.pack(anchor=N)
        b_money5000 = Button(moneyFrame2, image=self.photo3, overrelief=SUNKEN,
                             command=lambda: (self.ThrowMoney(50,w.get()), self.write("")))
        b_money5000.pack(anchor=N)
        b_money10000 = Button(moneyFrame2, image=self.photo10, overrelief=SUNKEN,
                              command=lambda: (self.ThrowMoney(100,w.get()), self.write("")))
        b_money10000.pack(anchor=N)
        l= Label(moneyFrame1, text="Ilość Monet")
        l.pack()
        w = Spinbox(moneyFrame2, from_=1, to=100)
        w.pack(anchor=N)

    def center(self):
        # centrowanie okna na ekranie
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # text na ekranie
    def write(self, text):
        self.viewedText += text
        self.SetOrderCash(round(self.GetOrderCash(), 2))
        self.priceToPay = round(self.priceToPay, 2)
        self.screen.delete(0.0, END)
        self.screen.insert(0.0,
                           self.viewedText + "\nWrzucono: " + str(self.GetOrderCash()) + " zl" + "\nDo Zapłaty: " + str(
                               self.priceToPay) + " zl")

    def buyViaCardm(self):
        if (self.GetOrderCash() > 0):
            popupmsg("Wrzuciłeś\njuż\npieniądze")
            return
        if (self.viewedText == ""):
            popupmsg("Najpierw\nwybierz\nbilet")
            return
        self.priceToPay = 0.00
        self.viewedText = ""
        self.write("")
        popupmsg("Zapłacono kartą!\n Dziękujemy!")

    def giveMoneyBack(self):

        if (self.GetOrderCash() == 0):
            popupmsg("Nie\nwrzuciłeś\npieniedzy!")
        self.EndOrder()
        self.write("")
        popupmsg("Zabierz\nPieniądze")


    def AddTicket(self, key):
        self.viewedText += self.addTickets(key)
        self.write("")

    def deleteTicket(self):
        if (self.priceToPay == 0):
            popupmsg("Nie\ndodałeś\nżadnego\nbiletu")
            return
        tmp = self.delTicket()
        self.viewedText = self.viewedText.replace(self.tickets[tmp] + "\n", "", 1)
        self.write("")

    def buyTickets(self):
        reszta=round(self.OrderCash-self.priceToPay,2)
        if self.viewedText== "":
            popupmsg("Nie\nwybrałeś\nbiletu!")
        if self.GetOrderCash() < self.priceToPay:
            popupmsg("Wrzuciłeś\nza mało\npieniędzy!")
        elif self.priceToPay == self.GetOrderCash():
            self.SetOrderCash(0.00)
            self.priceToPay = 0.00
            self.viewedText = ""
            self.write("")
            self.cashInMashine.clear()
            print(self.bilonAmmount)
            popupmsg("Odbierz\nbilety!")
        elif self.Canwithdraw(reszta):
            self.SetOrderCash(0.00)
            self.SetOrderCash(0.00)
            self.priceToPay = 0.00
            self.viewedText = ""
            self.write("")
            print(self.bilonAmmount)
            popupmsg("Odbierz\nbilety\ni resztę\n"+str(reszta)+"zł")
        else:
            popupmsg("Wrzuć\nodliczoną\nkowtę!")


