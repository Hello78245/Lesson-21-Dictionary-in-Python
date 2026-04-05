student_data={
    "id1":{'name':"Jack", "Class": 'V',"subject": "English"},
    "id2":{'name':"Emily","Class":'V',"subject":"English,Math,Science"},
    "id3":{'name':"Emily","Class":'G',"subject":"Science, History, Math"},
    "id4":{'name':"Issac","Class":'V',"subject":"Art, Science, Math"},
    "id4":{'name':"Issac","Class":'V',"subject":"Art, Science, Math"}
}
result={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_key=(details["name"],details["Class"],details["subject"])
    if unique_key is not seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details
for g,v in result.items():
    print(g,":",v)