# time

* 假定一个零点基准，偏移长度换算为按秒的数值型
* 由 9 个整数组成的元组 struct_time 表示的时间


### 导入
```python
import time
```

### sample
```python
# 当前时间
dt = time.time()
# 时间数组
local_time = time.localtime(dt)
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=27, tm_hour=16, tm_min=20, tm_sec=34, tm_wday=1, tm_yday=208, tm_isdst=0)
# 转换为时间字符串
time.asctime(local_time)
# Tue Jul 27 16:23:02 2021
time.strftime('%Y-%m-%d %H:%M:%S', local_time)
# 解析( parse) 输入的时间字符串为 struct_time 类型的时间。
time.strptime(format_time, '%Y-%m-%d %H:%M:%S')
```


### 常用时间格式
* %y : 两位数的年份表示，取值 [00, 99]
* %Y : 四位数的年份表示，取值 [000, 9999]
* %m : 月，取值 [01,12]
* %d : 天，取值 [01,31]
* %H : 24小时制，取值 [00,23]
* %I : 12小时制，取值 [01, 12]  
* %M : 分钟，取值 [00,59]
* %S : 秒，取值 [00,61]
* %a : 本地简化星期名称
* %A : 本地完整星期名称
* %b : 本地简化的月份名称
* %B : 本地完整的月份名称
* %c : 本地相应的日期表示和时间表示
* %j : 年内的一天，取值 [001, 366]
* %p : 本地 A.M. 或 P.M. 的等价符
* %U : 一年内的星期数，星期天为星期开始，取值 [00, 53]
* %w : 星期，星期天为星期开始，取值 [0, 6]
* %W : 一年内的星期数，星期一为星期开始，取值 [00, 53]
* %x : 本地相应的日期表示
* %X : 本地相应的时间表示
* %Z : 当前时区名称
* %% : %号本身




















