import abc


class Mom(abc.ABC):
    @abc.abstractmethod
    def f1(self):
        print("mom")


class Sonu(Mom):
    def f1(self):
        print("sonu")


class Monu(Mom):
    def f1(self):
        print("monu")


obj1 = Sonu()
obj2 = Monu()

obj1.f1()
obj2.f1()
