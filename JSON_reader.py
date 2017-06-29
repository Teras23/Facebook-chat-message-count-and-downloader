import json
import os
from pprint import pprint
from operator import itemgetter

path = os.path.join(os.getcwd(), "JSON/All")

#15:28 = 18:28 irl

times = {}
hours = {}

totals = {}

total = 0

for files in os.listdir(path):
    if files == "<CHAT_NAME_IF_YOU_WANT_SIGNLE>.txt":
        pass
    elif True: #comment this line if you want a single chat with the last command
        try:
            print(os.path.join(path, files))
            with open(os.path.join(path, files), "r", encoding="utf8") as file:
                data = json.load(file)

                firstLine = True

                chat_total = 0

                for chunk in data:
                    if firstLine:
                        chunk = chunk['data']
                        firstLine = False

                    for message in chunk:
                        time = message['created_time']
                        message_text = message['message']
                        sender = message['from']['name']

                        date = time[0:10]
                        #date = time[0:7] #per month count
                        hour = time[11:16]

                        if date in times:
                            times[date] += 1
                        else:
                            times[date] = 1
                        chat_total += 1

                        if hour in hours:
                            hours[hour] += 1
                        else:
                            hours[hour] = 1

                total += chat_total
                totals[files] = chat_total

        except IOError as e:
            print(e)

#pprint(times)
#pprint(hours)
print(total)

with open("dates.txt", 'w') as file:
    for key, value in times.items():
        file.write(key + " " + str(value) + "\n")

with open("hours.txt", "w") as file:
    for key, value in hours.items():
        file.write(key + " " + str(value) + "\n")
