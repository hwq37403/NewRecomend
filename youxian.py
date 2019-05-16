
def youxianji(times,user_times,flag):
    try:
        riqi = int(times[5:7]) - int(user_times[5:7])  # 月
        youxian = int(times[-2::]) - int(user_times[-2::])
        if riqi == 0:  # 说明在一个月
            if youxian > -3 and youxian < 3:  # 说明在三天内
                if youxian == 0:
                    flag = 1  # 优先级
                elif youxian == 1 or youxian == -1:
                    flag = 2  # 优先级设为2
                else:
                    flag = 3  # 优先级设为3
            else:  # 不在三天
                flag = 9999

        elif riqi == 1:  # 不在一个月
            if youxian > 27 and youxian < 30:
                if youxian == 29 or youxian == -29:
                    flag = 1  # 优先级
                elif youxian == 28 or youxian == -28:
                    flag = 2  # 优先级设为2
                else:
                    flag = 3  # 优先级设为3
            else:
                flag = 9999
        else:
            flag = 9999
    except ValueError:
        flag=9999
    return flag
