import fitbit
from credentials import FITBIT

from pprintpp import pprint as pp 
import json
import datetime

fitbit_client = fitbit.Fitbit(FITBIT['CONSUMER_ID'], 
							FITBIT['CONSUMER_SECRET'],
                            access_token=FITBIT['ACCESS_TOKEN'], 
                            refresh_token=FITBIT['REFRESH_TOKEN'])

activity_stats = fitbit_client.activity_stats()
food_goal = fitbit_client.food_goal()
Aug_1_2016 = datetime.date(2016, 8, 1)
get_sleep = fitbit_client.get_sleep(Aug_1_2016)
get_devices = fitbit_client.get_devices()
get_alarms = fitbit_client.get_alarms(FITBIT['DEVICE_ID'])

now = datetime.datetime.now()
now_plus_3 = now + datetime.timedelta(minutes = 2)
add_alarm = fitbit_client.add_alarm(FITBIT['DEVICE_ID'], now_plus_3, ['SATURDAY'])

pp(get_alarms)
pp(add_alarm)
pp(get_alarms)