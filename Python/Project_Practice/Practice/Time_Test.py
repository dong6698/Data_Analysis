import time

# 函数time.time()用于获取当前时间戳
time_0 = time.time()
print("LocalTime is :", time_0)

# 从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
time_1 = time.localtime(time.time())
print("LocalTime is :", time_1)

# 最简单的获取可读的时间模式的函数是asctime():
time_2 = time.asctime(time.localtime(time.time()))
print("LocalTime is :", time_2)

# 格式化成2016-03-20 11:45:39形式
print("LocalTime is :", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成2016/03/20 11:45:39形式
print("LocalTime is :", time.strftime("%Y/%/%d %H:%M:%S", time.localtime()))

# 格式化成2016-03-20形式
print("LocalTime is :", time.strftime("%Y-%m-%d", time.localtime()))

# 格式化成11:45:39形式
print("LocalTime is :", time.strftime("%H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print("LocalTime is :", time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print("LocalTime is :", time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''