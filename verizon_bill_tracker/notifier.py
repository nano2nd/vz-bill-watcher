
class Notifier():

    def __init__(self, email_address, last_balance, todays_balance, date_due):
        self._email_address = email_address
        self._last_balance = last_balance
        self._todays_balance = todays_balance
        self._date_due = date_due

    def send_paid_bill_notification(self):
        print((
            'Verizon bill paid in the amount ${}. '
            'You owe ${} on your Verizion bill, it is due {}.'
            .format(self._last_balance - self._todays_balance,
                    self._todays_balance,
                    self._date_due
                    )
        ))

    def send_new_bill_notification(self):
        print('The verizon bill is ready. The total bill is ${} and is due {}.'
              .format(self._todays_balance, self._date_due))
