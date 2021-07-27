import time

# 当前时间
dt = time.time()

# 时间转化
local_time = time.localtime(dt)
print(local_time)
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=27, tm_hour=16, tm_min=25, tm_sec=47, tm_wday=1, tm_yday=208, tm_isdst=0)

# 转换为时间字符串
print(time.asctime(local_time))
# 'Tue Jul 27 16:25:47 2021'

# 格式化字符串
format_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(format_time)
# '2021-07-27 16:25:47'









