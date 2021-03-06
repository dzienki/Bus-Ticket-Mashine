from popoutmsg import *
from imonety import *
class Skarbonka(iSkarbonka):
    def __init__(self):
        self.cashInMashine= []
        self.OrderCash = 0
        self.bilonAmmount = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}
        #self.bilonAmmount = {100: 3, 50: 3, 20: 3, 10: 3, 5: 4, 2: 5, 1: 5, 0.5: 4, 0.2: 4, 0.1: 4}


    def ThrowMoney(self, key, amount):
        try:
            tmp=int(amount)
            if tmp<=0:
                raise ValueTooSmall
        except ValueTooSmall:
            popupmsg("Wprowadz\nliczbe\ndodatnia")
        except ValueError:
            popupmsg("To nie\nliczba\ncalkowita!")
        else:
            for i in range(tmp):
                self.bilonAmmount[key] += 1
                self.OrderCash += key
                self.cashInMashine.append(key)

    def GiveBack(self, key):
        if self.bilonAmmount[key] <= 0:
            print("Brak Monet! o nominale: ", key)
            return
        if self.ammount - key < 0:
            print("Error")
            raise ValueError()
        self.bilonAmmount[key] -= 1
        self.OrderCash -= key

    def GetCashInMashine(self):
        return self.cashInMashine

    def GetOrderCash(self):
        return self.OrderCash

    def SetOrderCash(self, temp):
        self.OrderCash = temp

    def EndOrder(self):
        while len(self.cashInMashine)>0:
            tmp=self.cashInMashine.pop()
            self.bilonAmmount[tmp] -= 1
            self.OrderCash -= tmp
        if round(self.OrderCash,2) > 0:
            raise ValueError

    def Canwithdraw(self, reszta):
        priceToPay = reszta
        tmpBillons = self.bilonAmmount
        for valueMoney in self.bilonAmmount:
            tmp = int(priceToPay/valueMoney)
            if tmp >= 1:
                if self.bilonAmmount[valueMoney] > 0:
                    tmp2 = self.bilonAmmount[valueMoney]
                    if tmp2 > tmp:
                        tmpBillons[valueMoney]-=tmp
                        priceToPay -= tmp*valueMoney
                    else:
                        tmpBillons[valueMoney]-=tmp2
                        priceToPay -= tmp2*valueMoney
        if priceToPay > 0:
            return False
        self.bilonAmmount = tmpBillons
        print("mozna")
        return True
