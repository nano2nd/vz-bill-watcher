from verizon_bill_tracker.scrapper_tools.scrapper import Scrapper
from verizon_bill_tracker.db_driver import DbDriver
from verizon_bill_tracker.notifier import Notifier
import secrets


class App:

    @staticmethod
    def start():
        # Get my balance
        todays_balance_text, date_due_text = Scrapper.get_balance_data()
        last_balance_text = DbDriver.read_last_balance()

        # Test values
        #todays_balance_text = '$80.00'
        #last_balance_text = '150.00'
        #date_due_text = '1/2/2017'

        if last_balance_text is None:
            DbDriver.write_balance(todays_balance_text)
            return

        last_balance = Scrapper.to_decimal(last_balance_text)
        todays_balance = Scrapper.to_decimal(todays_balance_text)

        if last_balance == 0:
            DbDriver.write_balance(todays_balance_text)
            return

        notifier = Notifier(secrets.NOTIFICATION_ADDRESS, last_balance,
                            todays_balance, date_due_text)

        if todays_balance > last_balance:
            notifier.send_new_bill_notification()

        if todays_balance < last_balance:
            notifier.send_paid_bill_notification()

        # Write today's balance to the database file
        DbDriver.write_balance(todays_balance_text)
