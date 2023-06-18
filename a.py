import datetime
time_str = "08:14:12.5963"
if len(time_str) == 8:  # فرمت hh:mm:ss
    
    time_str = datetime.now().strftime("%Y-%m-%d ") + time_str
    print(time_str)
elif len(time_str) < 19:  # فرمت hh:mm:ss.x
    time_str = datetime.now().strftime("%Y-%m-%d ") + time_str
    print(time_str)    
    # تکمیل اعشار به 8 رقم
    decimal_length = len(time_str) - time_str.rindex('.') - 1
    if decimal_length < 6:
        time_str += '0' * (6 - decimal_length)
print(time_str)