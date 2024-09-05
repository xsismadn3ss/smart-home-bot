import datetime

def current_time() ->str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
