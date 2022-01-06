import json
def data (a):
    if "i" in a:
        return complex(a['rel'],b['img'])
    return a 
b=json.loads('{"i":true,"rel":3,"img":2}')
print(data(b))
