class Date(object):

    baseDate = "20190526"

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


# 实例（类Date）
date1 = Date(26, 5, 2019)
date1.nextDay = "20190527"
# 初始化，自动调用 __init___
print("初始化: year %s mounth %s day %s, nextDay %s" %
      (date1.year, date1.month, date1.day, date1.nextDay))

# 类方法
date2 = Date.from_string('26-05-2019')
print(date2)
print("类方法: year %s mounth %s day %s" % (date2.year, date2.month, date2.day))

# 实例方法
is_date = Date.is_date_valid('11-09-2012')
print("实例方法: %s" % (is_date))
# 类属性
print("类属性： %s, id: %s" % (Date.baseDate, id(Date.baseDate)))
# 重新复制类属性
Date.baseDate = "20200101"
print("fake🆕类属性： %s, id: %s" % (Date.baseDate, id(Date.baseDate)))
