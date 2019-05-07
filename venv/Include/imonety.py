class iSkarbonka(object):
    def ThrowMoney(self, key, amount):
        raise NotImplementedError()

    def GiveBack(self, key):
        raise NotImplementedError()

    def GetCashInMashine(self):
        raise NotImplementedError()

    def GetOrderCash(self):
        raise NotImplementedError()

    def SetOrderCash(self, temp):
        raise NotImplementedError()

    def EndOrder(self):
        raise NotImplementedError()

    def Canwithdraw(self, reszta):
        raise NotImplementedError()
