import datetime
import sys
from random import randint


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def odd_even(is_even):
    print(*(i for i in range(0, 101, 2)) if is_even else (i for i in range(1, 100, 2)))


def moody():
    in_bad_mood = randint(0, 1)
    if in_bad_mood:
        raise ValueError("A cup of coffee is empty |(▼_▼)|")
    else:
        drink_some_coffee = True
