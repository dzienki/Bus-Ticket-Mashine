
class Skarbonka(object):
    def __init__(self):
        print('created!')
        self.ammount=0
        self.bilonAmmount={}
        self.bilonAmmount[0.01]=0
        self.bilonAmmount[0.02]=0
        self.bilonAmmount[0.05]=0
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
        self.bilonAmmount[200]=0
        self.bilonAmmount[500]=0
    def ThrowMoney(self,key):
        self.bilonAmmount[key]+=1
        self.ammount+=key
    def GiveBack(self,key):
        if self.bilonAmmount[key]<=0:
            print("Brak Monet! o nominale: ", key)
            return
        if self.ammount-key<0:
            print("Error")
            raise ValueError()
        self.bilonAmmount[key]-=1
        self.ammount-=key
    def GetAmmount(self):
        return self.ammount




