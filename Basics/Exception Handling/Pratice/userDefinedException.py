from venv import logger


class NegativeError(Exception):
    def __init__(self):
        self.msg = '-ve Dimension'

    def __str__(self):
        return self.msg

"""
class NegativeError(Exception):
    pass
"""

def area(length, breadth):
    if length>0 and breadth>0:
        return length * breadth
    else:
        raise NegativeError()


try:
    result = area(-5,10)
except Exception as msg:
    logger.exception(msg)
