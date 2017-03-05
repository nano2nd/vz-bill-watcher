import smtplib
import secrets

class Notifier():

    def __init__(self, email_address, last_balance, todays_balance, date_due):
        self._email_address = email_address
        self._last_balance = last_balance
        self._todays_balance = todays_balance
        self._date_due = date_due

    def send_paid_bill_notification(self):
        self.send_email(
            'Verizon Bill Paid',
            'Verizon bill paid in the amount ${}. You owe ${} on your Verizon bill.'
            .format(self._last_balance - self._todays_balance, self._todays_balance),
            secrets.MAIL_FROM

        )

    def send_new_bill_notification(self):
        self.send_email('New Verizon Bill',
                        'The verizon bill is ready. The total bill is ${}.'
                        .format(self._todays_balance),
                        secrets.MAIL_FROM)

    def send_email(self, subject, body, from_):
        gmail_user = secrets.MAIL_USER
        gmail_pwd = secrets.MAIL_PASSWORD
        to = self._email_address if type(self._email_address) is list else [self._email_address]

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (from_, ", ".join(to), subject, body)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(from_, to, message)
            server.close()
        except Exception as e:
            print('failed to send mail\n' + str(e))
