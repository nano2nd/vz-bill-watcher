from verizon_bill_tracker.scrapper_tools.scrapper import Scrapper
import secrets


class App:

    def __init__(self):
        self._my_private_var = 3

    @staticmethod
    def start():
        balance = Scrapper.get_balance()
        print(balance)
