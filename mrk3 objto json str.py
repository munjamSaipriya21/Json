import json
emp={"name":"priya","age":21,"salary":25000.0,"ismarried":True ,"is having boyfriend":None}
emp_str=json.dumps(emp)
print(emp_str)
print(type(emp))
print(type(emp_str))
