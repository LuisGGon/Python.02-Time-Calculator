def add_time(start, duration, day = ''):

    
    hour24 = convert_24h(start)
    end_time = sum_time(hour24,duration)
    
    days = end_time[0]
    time = end_time[1:3]
    
    hour = format_time(time)
    
    
               
    
    if day == '':
        if days == 0:
            new_time = hour
            return new_time
        elif days == 1:
            new_time = hour + ' (next day)'
            return new_time
        else:
            new_time = hour + ' (' + str(days) + ' days later)'
            return new_time

    else:
        week_d = day_of_week(day, days)
        if days == 0:
            new_time = hour + ', ' + week_d
            return new_time
        elif days == 1:
            new_time = hour + ', ' + week_d + ' (next day)'
            return new_time
        else:
            new_time = hour + ', ' + week_d+ ' (' + str(days) + ' days later)'
            return new_time



def convert_24h(hour):

    ed_hour = hour.replace(':',' ')
    split = ed_hour.split(' ')

    if split[2] == 'PM':
        split[0] = str(int(split[0])+12)
        hour24 = split[0]+':'+split[1]
        return hour24
    else:
        hour24 = split[0]+':'+split[1]
        return hour24

    
def sum_time(start, add):
    
    sp_start = start.split(':')
    sp_add = add.split(':')
    
    h_start = int(sp_start[0])
    m_start = int(sp_start[1])
    h_add = int(sp_add[0])
    m_add = int(sp_add[1])
    
    m_int = m_start + m_add
    q1, r1 = divmod(m_int,60)
    
    h_int = h_start + h_add + q1
    q2, r2 = divmod(h_int,24)
    
    res = [q2, r2, r1]

    return res

def format_time(time):
    
    if time[1] <10:
        time[1] = '0'+str(time[1])
    else:
        time[1] = str(time[1])
    
    if time[0] > 12:
        time[0] = str(time[0]-12)
        time.append('PM')
    elif time[0] == 12:
        time[0] = str(time[0])
        time.append('PM')
    elif time[0] == 0:
        time[0]='12'
        time.append('AM')
    else:
        time[0] = str(time[0])
        time.append('AM')
    hour = time[0] +':'+ time[1] + ' ' + time[2]
    return hour

def day_of_week(day, num_days):
    
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    
    index = week.index(day.capitalize())
        
    days7 = (num_days + index)%7
        
    return week[days7]