from sensor.exception import SensorException
import sys, os

def test_exception():
    try:
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)
    

if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)
