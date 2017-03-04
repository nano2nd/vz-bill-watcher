from datetime import datetime
import shelve
import secrets


class DbDriver:

    @staticmethod
    def write_balance(balance):
        with shelve.open(secrets.DB_NAME) as db:
            date_key = str(datetime.now().date())
            db[date_key] = balance

    @staticmethod
    def read_last_balance():
        with shelve.open(secrets.DB_NAME) as db:
            if not db:
                return None

            while True:
                try:
                    date_key = str(datetime.now().date())
                    return db[date_key]

                except KeyError:
                    continue

    @staticmethod
    def output():
        with shelve.open(secrets.DB_NAME) as db:
            for r in db:
                print('{} -> {}'.format(r, db[r]))
