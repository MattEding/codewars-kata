from collections import namedtuple
from functools import partial


Time = namedtuple('Time', 'year day hour minute second')

def expand_unit(rate, measure):
    """Takes a measure as a tuple and expands it into larger units using the rate."""
    head, tail = measure[0], measure[1:]
    return divmod(head, rate) + tail

sec_to_min  = partial(expand_unit, 60)
min_to_hour = partial(expand_unit, 60)
hour_to_day = partial(expand_unit, 24)
day_to_year = partial(expand_unit, 365)

def sec_to_year(sec):
    min_ = sec_to_min(sec)
    hour = min_to_hour(min_)
    day  = hour_to_day(hour)
    year = day_to_year(day)
    return year

def format_duration(seconds):
    """Return a formatted time given seconds to convert."""
    sec = (seconds,)
    time = Time(*sec_to_year(sec))
    fmt = []
    for unit, meas in time._asdict().items():
        if not meas:
            continue
        elif meas > 1:
            unit += 's'
        msg = '{meas} {unit}'.format(meas=meas, unit=unit)
        fmt.append(msg)

    try:
        init, last = fmt[:-1], fmt[-1]
    except IndexError:
        return 'now'
    if init:
        seq = ', '.join(init)
        return '{seq} and {last}'.format(seq=seq, last=last)
    return last
