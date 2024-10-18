from .import jalali 

from django.utils import timezone

def JalaliConverter(time):
    jmonth=['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']
    time=timezone.localtime(time)
    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list=list(time_to_tuple)
    for index,month in enumerate(jmonth):
        if time_to_list[1]==index+1:
            time_to_list[1]=month
            break
    return time_to_list