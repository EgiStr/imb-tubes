
import pandas as pd
import time

def get_formatted_timestring():
    return time.strftime("%Y%m%d-%H%M%S")


def humanize_date(date):
    date = pd.to_datetime(date)
    # format sabtu, 21 august 2021
    return date.strftime("%A, %d %B %Y")


