from metawear_app_core import Sensor
import sys

def base_routine(name, seconds):
    """
    Connect to the Metawear sensor, and start collecting accelerometer data for 
    a given number of seconds. Then save the data as a .csv in the data folder.

    Params:
    -------
    name : string
    a description of the routine you're gathering data for

    seconds : int
    the number of seconds to record the data
    """
    s = Sensor()
    s.connect_to_sensor()
    s.gather_data(seconds)
    s.download_data(name)
    s.reset_device()
    print('Routine: ' + name + ' has completed.')

if __name__ == "__main__":
    base_routine(sys.argv[1], sys.argv[2])