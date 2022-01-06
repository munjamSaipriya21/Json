import json
data_txt={'Name': 'Abhishek','Designation': 'CEO of navgurukul','Gender':'male', 'Age': 29}
d=json.dumps(data_txt)
print(d)
print(type(data_txt))
print(type(d))

with open('mrk7 data_txt.json','w') as f:
    json.dump(data_txt,f)