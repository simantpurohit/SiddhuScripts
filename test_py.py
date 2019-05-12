import requests
import time
import json

base_url = "https://api.bseindia.com/BseIndiaAPI/api/MeetingDetails/w?mid={}&srno={}"

continue_forward = True
count_until_no_sr = 0

current_mid = 24651
current_sr = 1

while continue_forward:
    print("Getting data for meeting {} and resolution {}".format(current_mid, current_sr))
    try:
        response = requests.get(base_url.format(current_mid, current_sr))
        meeting_data = response.json()
    except Exception:
        print("Exception. Retrying after 5 seconds")
        time.sleep(5)
        continue

    if meeting_data != {}:
        if len(meeting_data["Table1"]) == 0:
            current_mid += 1
            current_sr = 1
            continue

        with open("/home/simantpurohit/meeting_data/meeting_{}_resolution_{}".format(current_mid, current_sr), 'w') as outfile:
            outfile.write(json.dumps(meeting_data))
            # time.sleep(1)
            current_sr += 1
            continue

    if meeting_data == {}:
        current_sr += 1
        count_until_no_sr += 1

    if count_until_no_sr > 0:
        current_mid += 1
        current_sr = 1
        count_until_no_sr = 0

    if current_mid > 99999:
        continue_forward = False
    
    # time.sleep(1)
