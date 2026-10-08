import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fun_divide_number(a,b):
    try:
        result = a / b
        return result
    except Exception as msg:
        logger.exception(msg)

fun_divide_number(10,0)
print("End of Program")