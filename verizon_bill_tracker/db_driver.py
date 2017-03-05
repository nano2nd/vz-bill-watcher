from datetime import datetime
import shelve
import secrets


def write_balance(balance):
    with shelve.open(secrets.DB_NAME) as db:
        date_key = str(datetime.now().date())
        db[date_key] = balance

    output()


def read_last_balance():
    with shelve.open(secrets.DB_NAME) as db:
        if not db:
            return None

        date_keys = (datetime.strptime(d, '%Y-%m-%d') for d in db.keys())
        sorted_keys = sorted(date_keys)
        return db[str(sorted_keys[-1].date())]


def output():
    with shelve.open(secrets.DB_NAME) as db:
        with open(secrets.DB_OUTPUT_NAME, 'w') as db_output:
            db_output.writelines('{} -> {}\n'.format(item, db[item]) for item in db.keys())
