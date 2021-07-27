# datetime

常用类有 4 个：
* date：日期类，包括属性年、月、日及相关方法
* time：时间类，包括属性时、分、秒等及相关方法
* datetime：日期时间，继承于 date，包括属性年、月、日、时、分、秒等及相关方法，其中年月日必须参数
* timedelta：两个 datetime 值的差，比如相差几天（days）、几小时（hours）、几分（minutes）等

### 导入
```python
from datetime import date, datetime, time, timedelta
```


### date
```python
# 当前日期
date.today()
# 当前日期格式化为字符串
date.strftime(dt, '%Y-%m-%d')
# 字符日期转日期格式
datetime.strptime('2021-07-27', '%Y-%m-%d')
```


### datetime
```python
# 当前时间
dt = datetime.now()
# 当前时间的日期
dt.date()
# 当前时间的时间
dt.time()
# 当前时间格式化为字符串
datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
# 字符时间转时间类型
datetime.strptime('2021-07-27 17:02:25', '%Y-%m-%d %H:%M:%S')
```


### timedelta
```python

```


















