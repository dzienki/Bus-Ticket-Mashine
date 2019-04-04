
class Skarbonka(object):
    def __init__(self):
        self.cashInMashine=0
        self.OrderCash=0
        self.bilonAmmount={}
        self.bilonAmmount[0.1]=0
        self.bilonAmmount[0.2]=0
        self.bilonAmmount[0.5]=0
        self.bilonAmmount[1]=0
        self.bilonAmmount[2]=0
        self.bilonAmmount[5]=0
        self.bilonAmmount[10]=0
        self.bilonAmmount[20]=0
        self.bilonAmmount[50]=0
        self.bilonAmmount[100]=0
    def ThrowMoney(self,key):
        self.bilonAmmount[key]+=1
        self.OrderCash+=key
    def GiveBack(self,key):
        if self.bilonAmmount[key]<=0:
            print("Brak Monet! o nominale: ", key)
            return
        if self.ammount-key<0:
            print("Error")
            raise ValueError()
        self.bilonAmmount[key]-=1
        self.OrderCash-=key
    def GetCashInMashine(self):
        return self.cashInMashine
    def GetOrderCash(self):
        return self.OrderCash
    def SetOrderCash(self,temp):
        self.OrderCash=temp
    def EndOrder(self):
        self.OrderCash=0
    def Canwithdraw(self):
        return True



