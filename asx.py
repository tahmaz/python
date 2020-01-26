import requests
import pandas as pd
import MySQLdb
import sys
pd.set_option('display.max_colwidth', -1)

print(sys.version)
print("db connection")
#db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                     user="stockmarket",         # your username
#                     passwd="aFdw7R05G5gW",  # your password
#                     db="stockmar_wp918")        # name of the data base

def title_logic(title):
    title = title.upper()
    if title.find('APPENDIX 3B') >- 1:
        return 'Appendix 3B'

    if title.find('APPENDIX 3Y') >- 1:
        return 'Appendix 3Y'

    if (title.find('HALF') >- 1 and title.find('YEARLY') >- 1  and title.find('REPORT') >- 1) or title.find('APPENDIX 4D') >- 1:
        return 'Half Yearly Report'

    if title.find('DIRECTOR') >- 1 and title.find('APPOINTMENT') >- 1  :
        return 'Director Appointment'
    else:
        return 'No Category'



def get_json(url):
    r    = requests.get(url)
    j    = r.json()
    return j

pg                   = 1
announcements_list   = []
announcements_df     = pd.DataFrame()

print("while start")
while pg <= 1:
    url  = 'http://origin.asx.gomeekisystems.com/json/announcements_'+str(pg)+'.json'
    j = get_json(url)
    announcements = j['Announces']

    for a in announcements:
        title = a['title'].replace(",","").replace("'","")
        a['title'] = title
        a['title_logic'] = title_logic(title)
        announcements_list.append(a)

    announcements_df = pd.DataFrame(announcements_list)
    pg += 1

companies_url  = 'http://origin.asx.gomeekisystems.com/json/companies.json'
companies_json = get_json(companies_url)
companies_df   = pd.DataFrame(companies_json['Companies'])

announcement_and_compnay_df = pd.merge(announcements_df, companies_df, left_on='code', right_on='code', how='left')

gsic_code  = 'http://origin.asx.gomeekisystems.com/json/gsic_code.json'
gsic_json  = get_json(gsic_code)
gsic_df    = pd.DataFrame(gsic_json['GSIC_Codes'])

merged_announcement_df = pd.merge(announcement_and_compnay_df, gsic_df, left_on='gsic_code_x', right_on='gsic_code', how='left')
#merged_announcement_df['industry_group'].fillna('Unknown', inplace=True)
merged_announcement_df.fillna('Unknown', inplace=True)

# Column select
final_output = merged_announcement_df[['time_release','code','name','title','title_logic','IssuerName','industry_group','pdf_url']]

#Column rename
final_output = final_output.rename(index=str, columns={
 "time_release": "Released"
,"code":"Code"
,"name":"Name"
,"title":"Title"
,"title_logic":"Category"
,"IssuerName":"Issuer_Name"
,"industry_group":"Industry"
,"pdf_url":"PDF"
})

#final_output.to_csv('ASX.csv', index = False)

final_output_dict = final_output.to_dict('records')

print("db update")
#cursor = db.cursor()
for item in final_output_dict:
    cols   = item.keys()
    col    = ",".join(cols)

    values = item.values()
    row = '","'.join(values)
    row = '"'+row+'"'

#    insert_syntax = 'INSERT IGNORE INTO stockmar_wp918.asx_announce('+col+') VALUES('+row+");"
#    cursor.execute(insert_syntax)
#    db.commit()

print("end")
