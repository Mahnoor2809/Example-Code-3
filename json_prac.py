import json
with open('students.json','w') as fdes:
    lst = ['Inam', 'Ai', 6436]
    di = {"Name": 'Inam', 'Class': "Ai"}
    # json.dump(lst,fdes)
    # json.dump(di,fdes)
with open('students.json','r') as fdes:
    data = json.load(fdes)
    print(data)    
    