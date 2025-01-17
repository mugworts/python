class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')

print(date2, is_date)


class Kls(object):
    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

ik1 = Kls('arun')
ik2 = Kls('seema')
ik1.printd()
ik2.printd()

