class Skarbonka(object):
    def __init__(self):
        self.cashInMashine= []
        self.OrderCash = 0
        self.bilonAmmount = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}

    def ThrowMoney(self, key):
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
        if self.OrderCash > 0:
            raise ValueError

    def Canwithdraw(self, reszta):
        priceToPay = reszta
        tmpBillons = self.bilonAmmount
        for valueMoney in self.bilonAmmount:
            tmp = priceToPay/valueMoney
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
