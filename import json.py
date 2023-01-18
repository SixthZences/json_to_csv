import json
import csv
with open('pr.json') as json_file:
    data = json.load(json_file)
datadict = data['Report_Items']
print(type(datadict))
print(type(datadict[0]))
a=datadict[0].keys()
dtd=datadict[0]
print(type(a))
for key in datadict[0]:
    print(type(dtd[key]))
    if type(dtd[key])==list and type(dtd[key])!=str:
        length=len(dtd[key])
        b=dtd[key]
        print(type(b[0]))
        print(type(b[1]))
       # for i in range(0,length):
            #if type (b[i])==list and type(b[i])!=str:
                #print(len(b[i]))
