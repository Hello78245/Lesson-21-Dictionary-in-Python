test_dict={"I am":2, "The":2, "Best":2, "Yipee":1}
print("The original dictionary:"+ str(test_dict))
b=2
res=0
for key in test_dict:
    if test_dict[key]==b:
        res=res+1
print("The frequency of b is:"+str(res))