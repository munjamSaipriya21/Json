a=["sai,priya","neetu,kumari","saipriya,Munjam"]
i=0
b=[]
while i<len(a):
    if "," in a[i]:
        c= a[i].replace(",","")
        b.append(c)
    i+=1
print(b)