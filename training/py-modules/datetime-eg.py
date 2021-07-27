from datetime import date, datetime, time, timedelta

# ------ date --------
print('------ date --------')

# 当前日期
dt = date.today()
print('dt: ', dt)
# dt:  2021-07-27
print('date.max: ', date.max)
print('date.min: ', date.min)

# 当前日期格式化为字符串
format_str = date.strftime(dt, '%Y-%m-%d')
print('format_str: ', format_str, type(format_str))
# format_str:  2021-07-27 <class 'str'>

# 字符日期转日期格式
format_date = datetime.strptime('2021-07-27', '%Y-%m-%d')
print('format_date: ', format_date, type(format_date))
# format_date:  2021-07-27 00:00:00 <class 'datetime.datetime'>


# ------ datetime --------
print('------ datetime --------')

# 当前时间
# dt = datetime.today()
dt = datetime.now()
# dt = datetime.utcnow()
print('dt: ', dt)
# dt:  2021-07-27 17:07:02.103298
print('datetime.max: ', datetime.max)
print('datetime.min: ', datetime.min)
print('dt.year: ', dt.year)
print('dt.month: ', dt.month)
print('dt.day: ', dt.day)
print('dt.hour: ', dt.hour)
print('dt.minute: ', dt.minute)
print('dt.second: ', dt.second)
print('dt.microsecond: ', dt.microsecond)
print('dt.tzinfo: ', dt.tzinfo)
print('dt.date: ', dt.date())
# dt.date:  2021-07-27
print('dt.time: ', dt.time())
# dt.time:  17:07:02.103298
print('dt.weekday:', dt.weekday())
# 1 (今天周二，周一从 0 开始)
print('dt.isoweekday: ', dt.isoweekday())
# 2 (今天周二，周一从 1 开始)

# 当前时间格式化为字符串
format_str = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
print('format_str: ', format_str, type(format_str))
# format_str:  2021-07-27 17:01:28 <class 'str'>

# 字符时间转时间类型
format_dt = datetime.strptime('2021-07-27 17:02:25', '%Y-%m-%d %H:%M:%S')
print('format_dt: ', format_dt, type(format_dt))
# format_dt:  2021-07-27 17:02:25 <class 'datetime.datetime'>


# ------ timedelta --------
print('------ timedelta --------')
dt = datetime.now()
# 获取昨天日期
last_day = dt.date() - timedelta(1)
# last_day = dt.date() + timedelta(-1)
print('last_day: ', last_day)
# 获取明天
next_day = dt.date() + timedelta(1)
print('next_day: ', next_day)
# 获取当前月第一天
cur_date = date(dt.year, dt.month, 1)
print('cur_date: ', cur_date)
next_time = dt + timedelta(hours=2)
print('next_time: ', next_time)





# ------ time类似于date --------
print('------ time --------')
# 当前时间
dt = time()
print('dt: ', dt)


