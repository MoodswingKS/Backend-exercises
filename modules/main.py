# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this
import time
import math
import datetime
import sys
from greet import supergreeting

def wait(seconds):
    return time.sleep(seconds)

def my_sin(float):
    return math.sin(float)

def iso_now():
    return datetime

def platform():
    return sys.platform

def supergreeting_wrapper(name):
    return supergreeting(name)