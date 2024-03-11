from datetime import date, datetime, time, timedelta


day = date(2023, 3, 18)

start_time = datetime.combine(day, time(8, 0))
end_time = datetime.combine(day, time(14, 0))


def generate_time(start_time, iteration):
    return datetime.combine(day, (start_time + timedelta(minutes=20) * iteration).time())


def count_intervals(start_time, end_time ):
    return int((end_time - start_time).seconds / 60 / 20)


all_times = [generate_time(start_time, i)
             for i in range(count_intervals(start_time, end_time))]


busy_times = [datetime.combine(day, time(8, 40)),
              datetime.combine(day, time(11, 40)),
              datetime.combine(day, time(13, 0))]  # тут уже в правильном формате будет


for busy_time in busy_times:
    del all_times[all_times.index(busy_time)]


print('\n'.join([all_time.strftime('%Y/%m/%d %H:%M') for all_time in all_times]))
