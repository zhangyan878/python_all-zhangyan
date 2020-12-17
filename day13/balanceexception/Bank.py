from balanceexception.BException import BalanceException
class Bank:
    __money = None

    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money

    def number(self):
        if self.__money <= 3000:
            print("账户当前余额为：",3000-self.__money)
        else:
            raise BalanceException("账户余额不足！")