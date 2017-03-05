from datetime import datetime
import shelve
import os
import secrets


class DbDriver:

    def __init__(self, cwd):
        self._db_file = os.path.join(cwd, secrets.DB_NAME)
        self._output_file = os.path.join(cwd, secrets.DB_OUTPUT_NAME)

    def write_balance(self, balance):
        with shelve.open(self._db_file) as db:
            date_key = str(datetime.now().date())
            db[date_key] = balance

        self.output()

    def read_last_balance(self):
        with shelve.open(self._db_file) as db:
            if not db:
                return None

            date_keys = (datetime.strptime(d, '%Y-%m-%d') for d in db.keys())
            sorted_keys = sorted(date_keys)
            return db[str(sorted_keys[-1].date())]

    def output(self):
        with shelve.open(self._db_file) as db:
            with open(self._output_file, 'w') as db_output:
                db_output.writelines('{} -> {}\n'.format(item, db[item]) for item in db.keys())
