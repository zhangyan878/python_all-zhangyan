from balanceexception.Bank import Bank
from balanceexception.BException import BalanceException
b = Bank()
b.setMoney(1000)
try:
    b.number()
except BalanceException as e:
    print(e)