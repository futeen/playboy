import time

# 以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用
a = time.clock()

# Convert a time tuple to a string, return --> Sat Jul 28 14:05:40 2018
b = time.asctime()

# Convert a time in seconds since the Epoch to a string in local time. return --> Thu Jan  1 08:00:50 1970
c = time.ctime(50)

# Get information of the specified clock.
# d = time.get_clock_info()

# Convert seconds since the Epoch to a time tuple expressing UTC, return--> time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=50, tm_wday=3, tm_yday=1, tm_isdst=0)
e = time.gmtime(50)

# Convert seconds since the Epoch to a time tuple expressing local time, return -->time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=50, tm_wday=3, tm_yday=1, tm_isdst=0)
f = time.localtime(50)

# Convert a time tuple in local time to seconds since the Epoch.
g = time.mktime(time.gmtime(0))

# 系统启动后过去的时间
h = time.monotonic()

# 返回系统运行时间
i = time.perf_counter()

# 返回当前进程使用CPU的时间。要放到一个进程(def)的头和尾才能用
j = time.process_time()

'''
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
'''
k = time.strftime('%Y-%m-%d %H:%M:%S', (2018, 2, 15, 23, 59, 59, 3, 46, -1))
l = time.strftime('%Y-%m-%d %H', (2018, 2, 15, 23, 59, 59, 3, 46, -1))



