# calendar
绘制日历图

### 导入
```python
import calendar
```

### sample
```python
# 年日历图
calendar.calendar(2021)
# 月日历图
calendar.month(dt.year, dt.month)
# 判断是否为闰年
calendar.isleap(dt.year)
# weekday: 本月第一天是所在周的第几天（周一从 0 开始）
# day: 当前月有多少天
weekday, days = calendar.monthrange(dt.year, dt.month)
```



















