class Zadanie:

    def __init__(self, slowa):
        self.slowo = slowa
        self.cons = ["b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z"]
        self.wss = 0
        self.ws2 = 0

    def przestaw(self):
        qwe =[]

        for i in range(0, len(self.slowo)):
            for j in range(0, len(self.cons)):
                if self.cons[j] == self.slowo[i]:
                    ws = self.slowo[i]


    def zad(self):
        for i in self.slowo:
            if i in self.cons:
                if self.wss == len(self.cons):
                    self.ws2 += self.cons[0]
                else:
                    self.ws2 += self.cons[self.wss-1]
                    self.wss += 1
            else:
                self.ws2 += i
        return self.ws2


d1 = Zadanie("kaczka")
print(d1.przestaw())
print(d1.zad())
