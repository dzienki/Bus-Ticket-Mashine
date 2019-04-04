class Tickets:
    def __init__(self):
        self.priceToPay=0
        self.tickets={}
        self.tickets[2.80]="Bilet normalny 20 min"
        self.tickets[1.40]="Bilet ulgowy 20 min"
        self.tickets[3.80]="Bilet normalny 40 min"
        self.tickets[1.90]="Bilet ulgowy 40 min"
        self.tickets[5.00]="Bilet normalny 60 min"
        self.tickets[3.00]="Bilet ulgowy 60 min"
        self.tickets[15.00]="Bilet normalny 24h"
        self.tickets[7.50]="Bilet ulgowy 24h"
        self.tickets[24.00]="Bilet normalny 48h"
        self.tickets[12.00]="Bilet ulgowy 48h"
        self.boughtTickets=[]
    def addTickets(self,key):
        self.boughtTickets.append(key)
        self.priceToPay+=key
        return self.tickets[key]+"\n"
    def delTicket(self):
        tmp=self.boughtTickets.pop()
        self.priceToPay-=tmp
        return tmp
