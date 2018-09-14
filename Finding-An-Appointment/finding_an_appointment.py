import datetime


def parse_time(time):
    hour, minute = [int(t) for t in time.split(':')]
    return datetime.timedelta(hours=hour, minutes=minute)


def format_time(seconds):
    hour = seconds // 3600
    minute = (seconds % 3600) // 60
    time = datetime.time(hour=hour, minute=minute)
    return time.strftime('%H:%M')


def time_range(interval):
    start, stop = [parse_time(t) for t in interval]
    return range(start.seconds, stop.seconds, 60)


def get_start_time(schedules, duration):
    """Return the earliest time from schedules of businesspeople such that
    each person can attend a meeting of duration length.
    """

    work_times = time_range(['09:00', '19:00'])
    busy_times = [[time_range(i) for i in s] for s in schedules]

    elapsed = 0
    for wt in work_times:
        if any(any(wt in t for t in bt) for bt in busy_times):
            elapsed = 0
        else:
            result = wt - 60 * (duration - 1)
            elapsed += 1

        if elapsed == duration:
            result = format_time(result)
            break
    else:
        result = None

    return result
