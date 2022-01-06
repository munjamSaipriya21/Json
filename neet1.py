list1=[["priya","Bsc Mpc",20,"qualifiction","age"],["neetu","intermediate","age","qualifiction",21],["sai","10th","age","qualifiction",19]]
dic={}
empt="user"
i=0
while i<len(list1):
    dic[empt+str(i)]={}
    j=0
    while j<len(list1[i]):
        # print(list1[i].index(list1[i][j])
        if list1[i].index(list1[i][j])==0:
            dic[empt+str(i)]["name"]=list1[i][j]
        elif list1[i].index(list1[i][j])==2:
            dic[empt+str(i)]["Age"]=list1[i]
        if list1[i].index(list1[i][j])==1:
            dic[empt+str(i)]["qualifiction"]=list1[i][j]
        j=j+1
    i=i+1
print(dic)