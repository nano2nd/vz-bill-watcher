from verizon_bill_tracker.scrapper_tools.scrapper import Scrapper


class App:

    def __init__(self):
        self._my_private_var = 3

    def start(self):
        Scrapper.logon()
