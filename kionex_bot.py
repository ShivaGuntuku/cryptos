# -*- coding: utf-8 -*-

import requests
from datetime import datetime
# import time
# import csv
# import os


# def dict_to_csv(current_dict, file_name):
#     with open(file_name, 'a') as f:
#         w = csv.DictWriter(f, current_dict.keys())
#         if f.tell() == 0:
#             w.writeheader()
#             w.writerow(current_dict)
#         else:
#             w.writerow(current_dict)


# while True:
r = requests.get("https://koinex.in/api/ticker")
y = r.json()['prices']
current_dict = {'date_time':
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
current_dict.update(y)

# print(y)
print(current_dict)

    # file_name = '{0}.csv'.format(datetime.now().strftime('%Y-%m-%d'))
    # if not os.path.isfile(file_name):
    #     dict_to_csv(current_dict, file_name)
    # else:
    #     dict_to_csv(current_dict, file_name)
    # time.sleep(300)
