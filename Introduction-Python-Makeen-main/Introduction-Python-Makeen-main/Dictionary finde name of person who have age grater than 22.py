dec1={1:{"name":"p1", "age":22},
       2:{"name":"p2", "age":27}}

for key,value in dec1.items():
        if value['age']>22:
            print(value['name'])
   
