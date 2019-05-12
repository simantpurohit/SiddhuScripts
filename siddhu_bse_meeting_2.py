import requests
import time

base_url = "https://api.bseindia.com/BseIndiaAPI/api/VotingResults/w?fromdt=&scripcode={}&todt=&type=0"

output_csv = open('bse_meeting_resolutions.csv', 'w')
error_csv = open('bse_meeting_resolutions_not_found.csv', 'w')

def get_resolutions(r_url):
    try:
        resolutions = requests.get(r_url).json()
    except Exception as e:
        time.sleep(5)
        resolutions = requests.get(r_url).json()
    
    return resolutions

with open('bse_codes.csv', 'r') as bse_codes:
    codes_list = bse_codes.readlines()

    headers=["Description","Fld_AgendaDetails","Fld_AgendaInterest","Fld_MasterID","Fld_MeetingDate","Fld_ResolTypeID","Fld_Scripcode","Fld_XMLName","ScripName","fld_srno"]
    output_csv.write(",".join(headers))
    output_csv.write("\n")

    for code in codes_list:
        c = code.strip()
        print(c)
        r_url = base_url.format(c)
        resolutions = get_resolutions(r_url)
        if(len(resolutions['Table']) == 0):
            error_csv.write(c)
            error_csv.write("\n")

        for resolution in resolutions['Table']:
            row = []
            for k,v in sorted(resolution.items()):
                value = str(v).replace(',', ';').replace('\r', ' ').replace('\n', ' ')
                row.append(value)
            
            output_csv.write(",".join(row))
            output_csv.write("\n")
            

error_csv.close()
output_csv.close()
    
