import datetime
class OpenerCounter:
    def __enter__(self):
        self.enter_time = datetime.datetime.now()
        print('Entry time ', self.enter_time)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_time = datetime.datetime.now()
        print('Exit time ', self.exit_time)
        self.res = self.exit_time - self.enter_time
        print('Spent: ', self.res)
