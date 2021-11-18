import os
import pandas as pd

csv_files=os.listdir('./IAA')

complete=None
for csv_file in csv_files:
    df=pd.read_csv('./IAA/'+csv_file)
    if complete is None:
        complete=pd.DataFrame({csv_file[:-4]:list(df['relation'])})
    else:
        complete=pd.concat([complete,pd.DataFrame({csv_file[:-4]:list(df['relation'])})],axis=1)

relation_dict={
    'gen:origin':9,
    'gen:alternate_name':1,
    'gen:super_genre':2,
    'genre:sub_genre':3,
    'genre:artist':4,
    'gen:sub_genre':3,
    'gen:artist':4,
    'artist:member_of':5,
    'producer:product':6,
    'product:origin':7,
    'no_relation':8
}

for key in relation_dict:
    complete.replace(key,relation_dict[key],inplace=True)
complete.to_csv('./complete.csv',index=False)
