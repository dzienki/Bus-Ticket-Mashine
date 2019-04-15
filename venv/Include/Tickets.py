class Bilety(object):
    def __init__(self):
        self.priceToPay = 0
        self.tickets = {2.80: "Bilet normalny 20 min", 1.40: "Bilet ulgowy 20 min", 3.80: "Bilet normalny 40 min",
                        1.90: "Bilet ulgowy 40 min", 5.00: "Bilet normalny 60 min", 3.00: "Bilet ulgowy 60 min",
                        15.00: "Bilet normalny 24h", 7.50: "Bilet ulgowy 24h", 24.00: "Bilet normalny 48h",
                        12.00: "Bilet ulgowy 48h"}
        self.boughtTickets = []

    def addTickets(self, key):
        self.boughtTickets.append(key)
        self.priceToPay += key
        return self.tickets[key] + "\n"

    def delTicket(self):
        tmp = self.boughtTickets.pop()
        self.priceToPay -= tmp
        return tmp
