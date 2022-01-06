#  convert to pthon to json
import json
employee={"name":"priya","age":21,"salary":25000.0,"ismarried":True ,"is having boyfriend":None}
json_string= json.dumps(employee)
print(json_string)
# print(type(json_string))

# with open('emp.json','w') as f:
#     json.dump(employee,f)

# import json
# employee={"name":"priya","age":21,"salary":25000.0,"ismarried":True ,"is having boyfriend":None}
# json_string= json.dumps(employee,indent=5)
# print(json_string)

# with open('emp.json','w') as f:
#     json.dump(employee,f,indent=5)

# import json
# a={"name":"priya","class":15 ,"Rlno":10.0, "married":None, "dics":True}
# b=json.dumps(a)
# print(b)