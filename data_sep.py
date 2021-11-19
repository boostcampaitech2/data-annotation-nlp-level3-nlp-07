import pandas as pd
from sklearn.model_selection import train_test_split
from collections import Counter

data=pd.read_csv('dataset - dataset.csv')
def make_rule(data):
    subj=[eval(x)['type'] for i,x in enumerate(data['subject_entity']) if data['relation'][i]!='no_relation']
    obj=[eval(x)['type'] for i,x in enumerate(data['object_entity']) if data['relation'][i]!='no_relation']
    rule=[x for x in zip(subj,obj)]
    return rule
rule=make_rule(data)
re=Counter(data['relation'])
relation_dict={
    'gen:origin':0,
    'gen:alternate_name':1,
    'gen:super_genre':2,
    'genre:sub_genre':3,
    'genre:artist':4,
    'gen:artist':4,
    'artist:member_of':5,
    'producer:product':6,
    'product:origin':7,
    'no_relation':8
}
for i in relation_dict:
    if i=='genre:artist':
        print('gen:artist',re[i]+re['gen:artist'])
    elif i=='gen:artist':
        continue
    elif i[:3]=='gen':
        print(i[:3]+':'+i.split(':')[1],re[i])
    else:
        print(i,re[i])
to=Counter(rule)
for key in to:
    print(key,to[key])
train,test=train_test_split(data[data['relation']!='no_relation'],test_size=0.2,stratify=rule)
print(len(rule))
print(len(train))
print(len(test))
def make_rule(data):
    subj=[eval(x)['type'] for i,x in enumerate(data['subject_entity'])]
    obj=[eval(x)['type'] for i,x in enumerate(data['object_entity'])]
    rule=[x for x in zip(subj,obj)]
    return rule
tr=Counter(make_rule(train))
te=Counter(make_rule(test))
for key in tr:
    try:
        print(key,tr[key],te[key])
    except:
        print(key)