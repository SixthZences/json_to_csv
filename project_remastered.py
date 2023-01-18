import time
import json
import csv
import jsonpath_rw_ext as jp
from jsonpath_ng import jsonpath, parse
from pandas import period_range
with open("ir_j2.json", encoding="UTF-8", errors="surrogateescape") as json_file:
    json_data = json.load(json_file)
data_file = open('table.csv', 'w', encoding="UTF-8")
header = ['Platform', 'Begin_date', 'End_date', 'Metric_type', 'Count', 'Item_ID_Type',
          'Item_ID_Value', 'Access_Type', 'Title', 'Publisher_ID_Type', 'Publisher_ID_Value', 'Publisher']
csv_writer = csv.DictWriter(data_file, fieldnames=header)
csv_writer.writeheader()
values_dict = {}
c = 0


report_items = jp.match('$.Report_Items[:]',json_data)
started=time.time()
print("Processing ...")

for i in range(len(report_items)):
    print(f"{i+1} / {len(report_items)} ( {((i+1)/len(report_items))*100}% )")
    platform = report_items[i]['Platform'] 
    access_type = report_items[i]['Access_Type']
    title = report_items[i]['Title']
    publisher_id_type = report_items[i]['Publisher_ID'][0]['Type']
    publisher_id_value = report_items[i]['Publisher_ID'][0]['Value']
    publisher = report_items[i]['Publisher']
    values_dict['Platform']=platform
    values_dict['Access_Type']=access_type
    values_dict['Title']=title
    values_dict['Publisher_ID_Type']=publisher_id_type
    values_dict['Publisher_ID_Value']=publisher_id_value
    values_dict['Publisher']=publisher
    c=0
    for j in range(len(report_items[i]['Performance'])):

        begin_date = report_items[i]['Performance'][j]['Period']['Begin_Date']
        end_date = report_items[i]['Performance'][j]['Period']['End_Date']
        values_dict['Begin_date']=begin_date
        values_dict['End_date']=end_date

        max_list=[]
        max_list.append(len(report_items[i]['Performance'][j]['Instance']))
        max_list.append(len(report_items[i]['Item_ID']))
        for k in range(max(max_list)):

            try:
                metric_type = report_items[i]['Performance'][j]['Instance'][k]['Metric_Type']
                count = report_items[i]['Performance'][j]['Instance'][k]['Count']
                values_dict['Metric_type']=metric_type
                values_dict['Count']=count
            except IndexError :
                values_dict['Metric_type']=""
                values_dict['Count']=""
                
            try:
                item_id_type = report_items[i]['Item_ID'][k]['Type']
                item_id_value =  report_items[i]['Item_ID'][k]['Value']
                if k < len(report_items[i]['Item_ID']) and c!=0:
                    values_dict['Item_ID_Type']=""
                    values_dict['Item_ID_Value']=""
                else:
                    values_dict['Item_ID_Type']=item_id_type
                    values_dict['Item_ID_Value']=item_id_value
            except IndexError :
                values_dict['Item_ID_Type']=""
                values_dict['Item_ID_Value']=""
            csv_writer.writerow(values_dict)
            values_dict.clear()
        c+=1


print("Complete !")
end=time.time()
print(f"Processing time : {end-started}")
data_file.close()
json_file.close()
