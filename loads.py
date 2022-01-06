import json
json_str='''{"name": "priya",
        "age": 21,
        "salary": 25000.0,
        "ismarried": true,
        "is having boyfriend": null}'''
emp_dict= json.loads(json_str)
print((emp_dict))
print("employee name:",emp_dict["name"])
print("employee age:",emp_dict["age"])
print("employee salary:",emp_dict["salary"])
print("Is employee married:",emp_dict["ismarried"])
print("Is employee is having BF:",emp_dict["is having boyfriend"])

