def solution(num_people, TIMES):

    def check_time(minute, TIMES):
        num_people_tmp = 0
        for time in TIMES:
            num_people_tmp += minute//time

        if num_people_tmp >= num_people: return 1
        else: return -1



    minute_left = 0
    minute_right = min(TIMES)*num_people

    while minute_right-minute_left > 1:
        minute = (minute_right + minute_left) // 2

        if check_time(minute, TIMES) > 0: minute_right = minute
        else: minute_left = minute

    return minute_right
