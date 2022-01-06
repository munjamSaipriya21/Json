list1=[['neelam','programer',24,2400],
['komal','trainer',24,20000],
['anuradha','HR',25,40000],
['Abhishek','manager',29,63000]]
dict={}
str1='emp'
i=0
while i<len(list1):
    dict[str1+str(i)]={}
    j=0
    while j<len(list1[i]):
        # print(list1[i].index(list1[i][j]))
        if list1[i].index(list1[i][j])==0:
            dict[str1+str(i)]["name"]=list1[i][j]
        elif list1[i].index(list1[i][j])==1:
            dict[str1+str(i)]["Designation"]=list1[i][j]
        elif list1[i].index(list1[i][j])==2:
            dict[str1+str(i)]["Age"]=list1[i][j]
        if list1[i].index(list1[i][j])==1:
            dict[str1+str(i)]["Salary"]=list1[i][j]
        j=j+1
    i=i+1
print(dict)
    