class Conta:
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo classe-objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
    def deposita(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor
    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)
        #akljsklajslkasjklkjalsjkaljkas
    def pega_saldo(self):
        return self.saldo
    def devolve_titular(self):
        return self.titular
    def retorna_limite(self):
        return self.limite



    def get_saldo(self):
        return self.saldo
    def get_titular(self):
        return self.titular

    def get_limite(self):
        return self.limite






    def  set_limite(self, limite):
        self.limite = limite

    @property
    def saldo(self):
        return self.saldo

    @property
    def titular(self):
        return self.titular

    @property
    def limite(self):
        return self.limite

    @limite.setter
    def limite(self, limite):
        self.limite = limite

    @saldo.setter
    def saldo(self, value):
        self._saldo = value
