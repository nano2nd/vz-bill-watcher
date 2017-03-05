from verizon_bill_tracker.scrapper_tools.scrapper import Scrapper
from verizon_bill_tracker.notifier import Notifier
from verizon_bill_tracker.db_driver import DbDriver
import secrets


def start(cwd):
    notifier = Notifier(secrets.NOTIFICATION_ADDRESS)
    db_driver = DbDriver(cwd)

    # Get my balance
    try:
        todays_balance_text, date_due_text = Scrapper.get_balance_data()
        last_balance_text = db_driver.read_last_balance()
    except Exception as e:
        notifier.send_error(str(e))
        return

    # Test values
    ''' todays_balance_text = '$80.00'
    #last_balance_text = '150.00'
    #date_due_text = '1/2/2017' '''

    last_balance = 0
    if last_balance_text is not None:
        last_balance = Scrapper.to_decimal(last_balance_text)

    todays_balance = Scrapper.to_decimal(todays_balance_text)

    if todays_balance > last_balance:
        notifier.send_new_bill_notification(todays_balance)

    if todays_balance < last_balance:
        notifier.send_paid_bill_notification(todays_balance, last_balance)

    # Write today's balance to the database file
    db_driver.write_balance(todays_balance_text)
