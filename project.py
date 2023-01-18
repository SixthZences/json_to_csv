import time
import json
import csv
from re import S
from unittest import result
from urllib import request
from jsonpath_ng import jsonpath, parse
from pandas import period_range
with open("ir_j2.json", encoding="UTF-8", errors="surrogateescape") as json_file:
    json_data = json.load(json_file)
data_file = open('table.csv', 'w', encoding="UTF-8")
header = ['Platform', 'Begin_date', 'End_date', 'Metric_type', 'Count', 'Item_ID_Type',
          'Item_ID_Value', 'Access_Type', 'Title', 'Publisher_ID_Type', 'Publisher_ID_Value', 'Publisher']
csv_writer = csv.DictWriter(data_file, fieldnames=header)
csv_writer.writeheader()
value = []
c = 0

# Input form for selected items that you want

#first = input("Please enter number for first items : ")
#last = input("Please enter number for last items : ")

report_items = parse('$.Report_Items[:]')
print("Processing ...")
started = time.time()

#for begin in range(len(report_items.find(json_data))): #this loop can access all items in report_items
#for begin in range(int(first), int(last)): # this loop can access selected items in report_items that reciceve input from above form
for begin in range(1):
    print(f'{begin+1} / {len(report_items.find(json_data))}')
    pf = parse('$.Report_Items[{0}:{1}].Performance[:]'.format(begin, begin+1))
    for start in range(len(pf.find(json_data))):
        results = []

        # Parsing
        platform = parse(
            '$.Report_Items[{0}:{1}].Platform'.format(begin, begin+1))
        begin_date = parse('$.Report_Items[{0}:{1}].Performance[{2}:{3}].Period[:].Begin_Date'.format(
            begin, begin+1, start, start+1))
        end_date = parse('$.Report_Items[{0}:{1}].Performance[{2}:{3}].Period[:].End_Date'.format(
            begin, begin+1, start, start+1))
        metric_type = parse('$.Report_Items[{0}:{1}].Performance[{2}:{3}].Instance[:].Metric_Type'.format(
            begin, begin+1, start, start+1))
        count = parse('$.Report_Items[{0}:{1}].Performance[{2}:{3}].Instance[:].Count[0:1]'.format(
            begin, begin+1, start, start+1))

        item_id_type = parse(
            '$.Report_Items[{0}:{1}].Item_ID[:].Type'.format(begin, begin+1))
        item_id_value = parse(
            '$.Report_Items[{0}:{1}].Item_ID[:].Value'.format(begin, begin+1))
        access_type = parse(
            '$.Report_Items[{0}:{1}].Access_Type'.format(begin, begin+1))
        title = parse('$.Report_Items[{0}:{1}].Title'.format(begin, begin+1))
        publisher_id_type = parse(
            '$.Report_Items[{0}:{1}].Publisher_ID[:].Type'.format(begin, begin+1))
        publisher_id_value = parse(
            '$.Report_Items[{0}:{1}].Publisher_ID[:].Value'.format(begin, begin+1))
        publisher = parse(
            '$.Report_Items[{0}:{1}].Publisher'.format(begin, begin+1))

        #  Platform
        for matching in platform.find(json_data):
            results.append(matching.value)

        #  Begin_date
        for matching in begin_date.find(json_data):
            results.append(matching.value)

        #  End_date
        for matching in end_date.find(json_data):
            results.append(matching.value)

        #  Metric_type
        for matching in metric_type.find(json_data):
            c += 1
            value.append(matching.value)
            if(c == len(metric_type.find(json_data))):
                results.append(value)
                value = []
                c = 0

        #  Count
        for matching in count.find(json_data):
            c += 1
            value.append(matching.value)
            if(c == len(count.find(json_data))):
                results.append(value)
                value = []
                c = 0

        #  Item_ID_Type
        for matching in item_id_type.find(json_data):
            c += 1
            value.append(matching.value)
            if(c == len(item_id_type.find(json_data))):
                results.append(value)
                value = []
                c = 0

        #  Item_ID_Value
        for matching in item_id_value.find(json_data):
            c += 1
            value.append(matching.value)
            if(c == len(item_id_value.find(json_data))):
                results.append(value)
                value = []
                c = 0

        #  access_type
        for matching in access_type.find(json_data):
            results.append(matching.value)

        #  title
        for matching in title.find(json_data):
            results.append(matching.value)

        #  publisher_id_type
        for matching in publisher_id_type.find(json_data):
            results.append(matching.value)

        #  publisher_id_value
        for matching in publisher_id_value.find(json_data):

            results.append(matching.value)

        #  publisher
        for matching in publisher.find(json_data):

            results.append(matching.value)

        # varaibles for writer
        l_mt = len(results[3])
        l_c = len(results[4])
        l_item_type = len(results[5])
        l_item_value = len(results[6])
        ml = 0
        ml_list = []
        ml_list.append(l_mt)
        ml_list.append(l_c)
        ml_list.append(l_item_type)
        ml_list.append(l_item_value)
        values_dict = {}
        values_dict.clear()

        # Main writer
        for l in range(max(ml_list)):  # UnicodeEncodeError

            if ml == 0 and start == 0:  # For starter each Platform
                # values_dict['Platform']=results[0]
                # values_dict['Begin_date']=results[1]
                # values_dict['End_date']=results[2]
                # values_dict['Metric_type']=results[3][l]
                # values_dict['Count']=results[4][l]
                # values_dict['Item_ID_Type']=results[5][l]
                # values_dict['Item_ID_Value']=results[6][l]
                # values_dict['Access_Type']=results[7]
                # values_dict['Title']=results[8]
                # values_dict['Publisher_ID_Type']=results[9]
                # values_dict['Publisher_ID_Value']=results[10]
                # values_dict['Publisher']=results[11]
                # csv_writer.writerow(values_dict)
                # values_dict.clear()
                csv_writer.writerow({'Platform': results[0], 'Begin_date': results[1], 'End_date': results[2], 'Metric_type': results[3][l], 'Count': results[4][l], 'Item_ID_Type': results[5][l],
                                    'Item_ID_Value': results[6][l], 'Access_Type': results[7], 'Title': results[8], 'Publisher_ID_Type': results[9], 'Publisher_ID_Value': results[10], 'Publisher': results[11]})
                ml += 1
            elif ml == 0:  # For starter each Begin_date and End_date
                # values_dict['Begin_date']=results[1]
                # values_dict['End_date']=results[2]
                # values_dict['Metric_type']=results[3][l]
                # values_dict['Count']=results[4][l]
                # csv_writer.writerow(values_dict)
                # values_dict.clear()
                csv_writer.writerow(
                    {'Begin_date': results[1], 'End_date': results[2], 'Metric_type': results[3][l], 'Count': results[4][l]})
                ml += 1
            else:  # For tails
                if l < l_mt:
                    values_dict['Metric_type'] = results[3][l]
                if l < l_c:
                    values_dict['Count'] = results[4][l]
                if l < l_item_type and start == 0:
                    values_dict['Item_ID_Type'] = results[5][l]
                if l < l_item_value and start == 0:
                    values_dict['Item_ID_Value'] = results[6][l]
                csv_writer.writerow(values_dict)
                values_dict.clear()
print("Complete !")
ending = time.time()
print("Time : ",ending - started)
data_file.close()
