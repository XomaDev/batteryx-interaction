from time import sleep
from psutil._common import BatteryTime

import psutil;
import requests as requests


def update():
    # Paste you're script ID here
    scriptID = "AKfycbyAt5VUml-zQfiwZ26tf6HpRVBMrEB2RUemOrOMX7xlA4iIwo8"

    # Interval between post requests
    interval = .7  # 0.7 seconds

    while True:
        # Script URL
        scriptURL = "https://script.google.com/macros/s/" + scriptID + "/exec" + "?values=";

        # Battery
        battery = psutil.sensors_battery()

        # Time left for the battery to drain-out
        timeLeft = battery.secsleft;

        # If the computer is charging, the battery time cannot be counted. So it's infinite.
        if timeLeft == BatteryTime.POWER_TIME_UNLIMITED:
            timeLeft = "infinite";

        # Preparing thr script URL
        scriptURL = scriptURL + \
                    '{ "remainingBattery":"' + str(battery.percent) + '",' \
                                                                      '"pluggedIn":' + '"' + str(
            battery.power_plugged) + \
                    '","timeLeft":"' + str(timeLeft) + '"}';

        # Do post request
        post = requests.post(scriptURL)

        # If failed, script will no longer run
        if post.status_code != 200:
            print("Unable to perform post request");
            break
        else:
            sleep(interval);


if __name__ == '__main__':
    update()
