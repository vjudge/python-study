import calendar
from datetime import date

dt = date.today()

# 年日历图
calendar2021 = calendar.calendar(2021)
print(f"{dt.year}年的日历图：{calendar2021}\n")

# 月日历图
month202107 = calendar.month(dt.year, dt.month)
print(f"{dt.year}年-{dt.month}月的日历图：{month202107}\n")

# 判断是否为闰年
print('calendar.isleap: ', calendar.isleap(dt.year))
# calendar.isleap:  False

# weekday: 本月第一天是所在周的第几天（周一从 0 开始）
# day: 当前月有多少天
weekday, days = calendar.monthrange(dt.year, dt.month)
print('weekday: ', weekday)
# weekday:  3 (星期四)
print('days: ', days)
# days:  31

# 本月最后一天
curr_month_last_day = date(dt.year, dt.month, days)
print('curr_month_last_day: ', curr_month_last_day)
# curr_month_last_day:  2021-07-31





