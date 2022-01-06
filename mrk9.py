import json
shopping={"shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
item=input("enter the item::")
number=int(input("enter the number:"))
list1=shopping["shopping_list"][item]
remove_number=int(list1)-number
shopping["shopping_list"][item]=remove_number
a=json.dumps(shopping)
print(a)

