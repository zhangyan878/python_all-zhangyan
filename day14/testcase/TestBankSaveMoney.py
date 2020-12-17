import unittest
from day14.yinhang.bank import bank_saveMoney
class TestBankSaveMoney(unittest.TestCase):
    def testSaveMoney(self):
        ac = "2367"
        money = 900
        status = False

        s = bank_saveMoney(ac,money)
        self.assertEqual(status,s)