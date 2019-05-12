import json

import csv

bse = {
    "Table": [
        {
            "Description": "AGM",
            "fld_masterid": 17927,
            "FLD_MEETINGDATE": "2017-07-24T00:00:00",
            "Fld_NoOfShareholder": 485627,
            "SHARE_PERSON": 330,
            "SHARE_Proxy": 0,
            "SHARE_Cumm": 330,
            "Promoter_PERSON": 327,
            "Promoter_Proxy": 0,
            "Promoter_Cumm": 327,
            "Public_PERSON": 3,
            "Public_Proxy": 0,
            "Public_Cumm": 3,
            "SHARE_Video": 0,
            "Promoter_Video": 0,
            "Public_Video": 0,
            "Fld_XMLName": "Voting_500180_2672017202213.xml"
        }
    ],
    "Table1": [
        {
            "Fld_SubSrNo": 1,
            "Fld_ProPubID": 1,
            "cOLUMNid": "PROM_POLL",
            "Fld_NoOfShrsHeld": 543216100,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 1,
            "Fld_ProPubID": 2,
            "cOLUMNid": "PROM_PostalBallot",
            "Fld_NoOfShrsHeld": 543216100,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 1,
            "Fld_ProPubID": 3,
            "cOLUMNid": "PROM_EVOTING",
            "Fld_NoOfShrsHeld": 543216100,
            "Fld_NoOfVtsPolled": 536087497,
            "Fld_PerVtsPolledOnOutsdngShrs": 98.688,
            "Fld_NoOfVtsInFvr": 536087497,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 100,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 1,
            "Fld_ProPubID": 4,
            "cOLUMNid": None,
            "Fld_NoOfShrsHeld": 543216100,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 1,
            "Fld_ProPubID": 10,
            "cOLUMNid": "PROM_TOTAL",
            "Fld_NoOfShrsHeld": 543216100,
            "Fld_NoOfVtsPolled": 536087497,
            "Fld_PerVtsPolledOnOutsdngShrs": 98.688,
            "Fld_NoOfVtsInFvr": 536087497,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 100,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 2,
            "Fld_ProPubID": 1,
            "cOLUMNid": "PUBLIC_POLL",
            "Fld_NoOfShrsHeld": 1170303683,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 2,
            "Fld_ProPubID": 2,
            "cOLUMNid": "PUBLIC_PostalBallot",
            "Fld_NoOfShrsHeld": 1170303683,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 2,
            "Fld_ProPubID": 3,
            "cOLUMNid": "PUBLIC_EVOTING",
            "Fld_NoOfShrsHeld": 1170303683,
            "Fld_NoOfVtsPolled": 992089002,
            "Fld_PerVtsPolledOnOutsdngShrs": 84.772,
            "Fld_NoOfVtsInFvr": 991563916,
            "Fld_NoOfVts": 525086,
            "Fld_PerVtsInFvrOnVtsPolled": 99.947,
            "Fld_PerVtsAgnstOnVtsPolled": 0.053,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 2,
            "Fld_ProPubID": 4,
            "cOLUMNid": None,
            "Fld_NoOfShrsHeld": 1170303683,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 2,
            "Fld_ProPubID": 11,
            "cOLUMNid": "PUBLIC_TOTAL",
            "Fld_NoOfShrsHeld": 1170303683,
            "Fld_NoOfVtsPolled": 992089002,
            "Fld_PerVtsPolledOnOutsdngShrs": 84.772,
            "Fld_NoOfVtsInFvr": 991563916,
            "Fld_NoOfVts": 525086,
            "Fld_PerVtsInFvrOnVtsPolled": 99.947,
            "Fld_PerVtsAgnstOnVtsPolled": 0.053,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 3,
            "Fld_ProPubID": 1,
            "cOLUMNid": "PUBLNonINS_POLL",
            "Fld_NoOfShrsHeld": 860363534,
            "Fld_NoOfVtsPolled": 120016,
            "Fld_PerVtsPolledOnOutsdngShrs": 0.014,
            "Fld_NoOfVtsInFvr": 115221,
            "Fld_NoOfVts": 4795,
            "Fld_PerVtsInFvrOnVtsPolled": 96.005,
            "Fld_PerVtsAgnstOnVtsPolled": 3.995,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 3,
            "Fld_ProPubID": 2,
            "cOLUMNid": "PUBLNonINS_PostalBallot",
            "Fld_NoOfShrsHeld": 860363534,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 3,
            "Fld_ProPubID": 3,
            "cOLUMNid": "PUBLNonINS_EVOTING",
            "Fld_NoOfShrsHeld": 860363534,
            "Fld_NoOfVtsPolled": 40432843,
            "Fld_PerVtsPolledOnOutsdngShrs": 4.7,
            "Fld_NoOfVtsInFvr": 40431734,
            "Fld_NoOfVts": 1109,
            "Fld_PerVtsInFvrOnVtsPolled": 99.997,
            "Fld_PerVtsAgnstOnVtsPolled": 0.003,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 3,
            "Fld_ProPubID": 4,
            "cOLUMNid": None,
            "Fld_NoOfShrsHeld": 860363534,
            "Fld_NoOfVtsPolled": 0,
            "Fld_PerVtsPolledOnOutsdngShrs": 0,
            "Fld_NoOfVtsInFvr": 0,
            "Fld_NoOfVts": 0,
            "Fld_PerVtsInFvrOnVtsPolled": 0,
            "Fld_PerVtsAgnstOnVtsPolled": 0,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 3,
            "Fld_ProPubID": 12,
            "cOLUMNid": "PUBLNonINS_TOTAL",
            "Fld_NoOfShrsHeld": 860363534,
            "Fld_NoOfVtsPolled": 40552859,
            "Fld_PerVtsPolledOnOutsdngShrs": 4.713,
            "Fld_NoOfVtsInFvr": 40546955,
            "Fld_NoOfVts": 5904,
            "Fld_PerVtsInFvrOnVtsPolled": 99.985,
            "Fld_PerVtsAgnstOnVtsPolled": 0.015,
            "Fld_SrNo": 12
        },
        {
            "Fld_SubSrNo": 4,
            "Fld_ProPubID": 1,
            "cOLUMNid": "Total_EVOTING",
            "Fld_NoOfShrsHeld": 2573883317,
            "Fld_NoOfVtsPolled": 1568729358,
            "Fld_PerVtsPolledOnOutsdngShrs": 60.948,
            "Fld_NoOfVtsInFvr": 1568198368,
            "Fld_NoOfVts": 530990,
            "Fld_PerVtsInFvrOnVtsPolled": 99.966,
            "Fld_PerVtsAgnstOnVtsPolled": 0.034,
            "Fld_SrNo": 12
        }
    ],
    "Table2": [
        {
            "Fld_MasterID": 17927,
            "ScripName": "HDFC Bank Ltd",
            "Fld_Scripcode": 500180,
            "Description": "AGM",
            "Fld_AgendaDetails": "To receive, consider and adopt the audited financial statements (standalone and consolidated) of the Bank for the year ended March 31, 2017 and the reports of the Board of Directors and Auditors thereon",
            "Fld_MeetingDate": "2017-07-24T00:00:00",
            "Fld_ResolTypeID": "Ordinary # 1",
            "Fld_AgendaInterest": False,
            "fld_srno": 1,
            "Fld_XMLName": "Voting_500180_2672017202213.xml"
        }
    ]
}


# # open a file for writing

# meeting_csv = open('/tmp/EmployData.csv', 'w')

# # create the csv writer object

# csvwriter = csv.writer(meeting_csv)

headers = ["Table__Description","Table__FLD_MEETINGDATE","Table__Fld_NoOfShareholder","Table__Fld_XMLName","Table__Promoter_Cumm","Table__Promoter_PERSON","Table__Promoter_Proxy","Table__Promoter_Video","Table__Public_Cumm","Table__Public_PERSON","Table__Public_Proxy","Table__Public_Video","Table__SHARE_Cumm","Table__SHARE_PERSON","Table__SHARE_Proxy","Table__SHARE_Video","Table__fld_masterid","Table1__Fld_NoOfShrsHeld","Table1__Fld_NoOfVts","Table1__Fld_NoOfVtsInFvr","Table1__Fld_NoOfVtsPolled","Table1__Fld_PerVtsAgnstOnVtsPolled","Table1__Fld_PerVtsInFvrOnVtsPolled","Table1__Fld_PerVtsPolledOnOutsdngShrs","Table1__Fld_ProPubID","Table1__Fld_SrNo","Table1__Fld_SubSrNo","Table1__cOLUMNid","Table2__Description","Table2__Fld_AgendaDetails","Table2__Fld_AgendaInterest","Table2__Fld_MasterID","Table2__Fld_MeetingDate","Table2__Fld_ResolTypeID","Table2__Fld_Scripcode","Table2__Fld_XMLName","Table2__ScripName","Table2__fld_srno"]

file = open("siddhu_bse_meetings.csv", "w")
file.write(",".join(headers))
file.write("\n")

# table = bse["Table"][0]
# table1 = bse["Table1"][0]
# table2 = bse["Table2"][0]

# # write first line
# row = []
# for k,v in sorted(table.items()):
#     row.append(str(v))

# for k,v in sorted(table1.items()):
#     row.append(str(v))

# for k,v in sorted(table2.items()):
#     if k == 'Fld_AgendaDetails':
#         value = '\"{}\"'.format(v)
#         row.append(str(value))
#     else:
#         row.append(str(v))

# print(",".join(row))
# print(len(row))
# print(len(headers))
# w_row = ",".join(row)
# print(w_row.count(","))

# file = open("test_meeting.csv", "w")
# file.write(",".join(headers))
# file.write("\n")
# file.write(w_row)
# file.write("\n")

# left_pad = ",,,,,,,,,,,,,,,,"
# right_pad = ",,,,,,,,,"
# middle_data = []

# table1_list = bse["Table1"]
# for t in range(1,len(table1_list)):
#     middle_data = []
#     for k,v in sorted(table1_list[t].items()):
#         middle_data.append(str(v))
#     row = "{},{},{}".format(left_pad, ",".join(middle_data), right_pad)
#     print(row)
#     file.write(row)
#     file.write("\n")
    

# file.close()



import os

directory = "meeting_data/"
count = 0
for filename in os.listdir(directory):
    count += 1
    print("File:{}".format(count))
    rfile = open(os.path.join(directory, filename), "r")
    bse = json.loads(rfile.read())
    rfile.close()

    table = bse["Table"][0]
    table1 = bse["Table1"][0]
    table2 = bse["Table2"][0]

    # write first line
    row = []
    for k,v in sorted(table.items()):
        row.append(str(v))

    for k,v in sorted(table1.items()):
        row.append(str(v))

    for k,v in sorted(table2.items()):
        if k == 'Fld_AgendaDetails':
            value = '\"{}\"'.format(v)
            row.append(str(value))
        else:
            row.append(str(v))

    w_row = ",".join(row)

    file.write(w_row)
    file.write("\n")

    left_pad = ",,,,,,,,,,,,,,,,"
    right_pad = ",,,,,,,,,"
    middle_data = []

    table1_list = bse["Table1"]
    for t in range(1,len(table1_list)):
        middle_data = []
        for k,v in sorted(table1_list[t].items()):
            middle_data.append(str(v))
        row = "{},{},{}".format(left_pad, ",".join(middle_data), right_pad)
        file.write(row)
        file.write("\n")
        
    file.write("\n")
    file.write("\n")

file.close()