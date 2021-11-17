import os
from typing import DefaultDict
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import json
import csv
import random

json_path='./NLP/ann.json/master/pool'
html_path='./NLP/plain.html/pool'
json_ext='ann.json'
html_ext='plain.html'

ann_dict={
    'e_1':'GEN',
    'e_2':'ART',
    'e_3':'POH',
    'e_4':'DAT',
    'e_5':'LOC',
    'e_9':'COM'
}

doc_titles=os.listdir('./NLP/ann.json/master/pool')
with open('./dataset.csv','w') as f:
    id=0
    writer=csv.writer(f)
    writer.writerow(['id','sentence','subject_entity','object_entity','title','relation'])
    for genre in ['재즈']:
        json_dir=os.path.join(json_path,genre)
        html_dir=os.path.join(html_path,genre)
        files=os.listdir(json_dir)
        for file in files:
            json_file=os.path.join(json_dir,file)
            html_file=os.path.join(html_dir,re.sub(json_ext,'',file)+html_ext)
            with open(html_file,'r') as hf:
                soup=BeautifulSoup(hf,'html.parser')
                sentence=soup.find(id='s1s1v1').text
            with open(json_file,'r') as jf:
                data=json.load(jf)
                entities=data['entities']
                entities_dict=defaultdict(dict)
                size=0
                for entity in entities:
                    offsets=entity['offsets'][0]
                    text=offsets['text']
                    offset=f"{offsets['start']},{offsets['start']+len(text)-1}"
                    entities_dict[entity['classId']].update({offset:text})
                    size+=1
                relations=data['relations']
                applied=set()
                for relation in relations:
                    ents=relation['entities']
                    subj_ent=tuple(ents[0].split('|')[1:]) #('e_i','n,m')꼴
                    obj_ent=tuple(ents[1].split('|')[1:])
                    subj={'word':entities_dict[subj_ent[0]][subj_ent[1]],'start_idx':int(subj_ent[1].split(',')[0]),'end_idx':int(subj_ent[1].split(',')[1]),'type':ann_dict[subj_ent[0]]}
                    obj={'word':entities_dict[obj_ent[0]][obj_ent[1]],'start_idx':int(obj_ent[1].split(',')[0]),'end_idx':int(obj_ent[1].split(',')[1]),'type':ann_dict[obj_ent[0]]}
                    applied.add((subj_ent,obj_ent))
                    writer.writerow([id,sentence,subj,obj,genre,'org'])
                    id+=1
                max_size=size*(size-1)
                if len(applied)<max_size:
                    for tag in list(set(entities_dict.keys())):
                        for _ in range(3):
                            subj_ent=(tag,random.choice(list(entities_dict[tag].keys())))
                            while True:
                                sel_tag=random.choice(list(entities_dict.keys()))
                                obj_ent=(sel_tag,random.choice(list(entities_dict[sel_tag].keys())))
                                if subj_ent!=obj_ent:
                                    break
                            if (subj_ent,obj_ent) not in applied:
                                subj={'word':entities_dict[subj_ent[0]][subj_ent[1]],'start_idx':int(subj_ent[1].split(',')[0]),'end_idx':int(subj_ent[1].split(',')[1]),'type':ann_dict[subj_ent[0]]}
                                obj={'word':entities_dict[obj_ent[0]][obj_ent[1]],'start_idx':int(obj_ent[1].split(',')[0]),'end_idx':int(obj_ent[1].split(',')[1]),'type':ann_dict[obj_ent[0]]}
                                applied.add((subj_ent,obj_ent))
                                writer.writerow([id,sentence,subj,obj,genre,'arb'])
                                id+=1

