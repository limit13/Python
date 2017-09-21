def add_gigasecond(x):
    from datetime import timedelta, date, time
    t=x+timedelta(seconds=1000000000)
    return t
