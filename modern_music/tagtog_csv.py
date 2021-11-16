import os
import json
from glob import glob
import pandas as pd
import re
from random import randint
import random
from collections import deque

###### 폴더명 & csv 파일명 설정 #######
folder = "./NLP/"
csv_name = "./tagtog_NLP_status.csv"
genre_json = os.path.join(folder, "ann.json/master/pool/")
genre_html = os.path.join(folder, "plain.html/pool/")
###################################

# entity, relation 맵핑
with open(os.path.join(folder, "annotations-legend.json"), "r") as f:
    mapping = json.load(f)


# json폴더와 html폴더 탐색하여 genre_list에 ("A.json", "A.html") 형식으로 저장
genre_json_folder = os.listdir(genre_json)
genre_list = []

for genre in genre_json_folder:
    json_sub_list = glob(os.path.join(genre_json+genre, "*"))
    json_files = [file.split('/')[-1].split('.ann')[0] for file in json_sub_list]
    html_sub_list = [os.path.join(genre_html+genre, file) + ".plain.html" for file in json_files if os.path.exists(os.path.join(genre_html+genre, file) + ".plain.html")]
    assert len(json_sub_list)==len(html_sub_list), "mismatch in number of sentences!"

    added_list = [(j, h) for j, h in zip(json_sub_list, html_sub_list)]
    genre_list.extend(added_list)


# html로부터 문장 추출하는 함수
def get_context_from_html(html_file):
    html_file = re.sub(r"\n","", html_file)
    return re.findall("(<pre.+>)(.+)(</pre>)",html_file)[0][1]


# 높은 확률로 no_relation을 만들기 위한 random (sub, obj) pair 만들기
def get_random_entities(entities):
    assert len(entities)>2, "number of entities must be more than 2"
    num_entities = len(entities)
    sub, obj = random.sample(range(num_entities), 2)
    return entities[sub], entities[obj]


# {"classId":"r_11",
# "type":"linked",
# "directed":false,
# "entities":["s1s1v1|e_1|13,13","s1s1v1|e_5|33,34"],
# "confidence":{"state":"pre-added","who":["user:Doohae"],"prob":1}}

# 위 형태의 relation_dict와 문장을 입력으로 들어올 때 train.csv 형식에 맞게 subject, object, relation 반환
def relation_set(relation_dict, sentence, mapping=mapping):
    relation = mapping[relation_dict['classId']]
    sub_start_idx, sub_end_idx = tuple(map(int, relation_dict['entities'][0].split('|')[-1].split(',')))
    obj_start_idx, obj_end_idx = tuple(map(int, relation_dict['entities'][1].split('|')[-1].split(',')))
    sub_type = mapping[relation_dict['entities'][0].split('|')[1]]
    obj_type = mapping[relation_dict['entities'][1].split('|')[1]]
    sub_word = sentence[sub_start_idx:sub_end_idx+1]
    obj_word = sentence[obj_start_idx:obj_end_idx+1]
    return {'word':sub_word, 'start_idx':sub_start_idx, 'end_idx':sub_end_idx, 'type':sub_type}, \
            {'word':obj_word, 'start_idx':obj_start_idx, 'end_idx':obj_end_idx, 'type':obj_type}, \
            relation

# [{'classId': 'e_1',
#   'part': 's1s1v1',
#   'offsets': [{'start': 0, 'text': '비밥'}],
#   'coordinates': [],
#   'confidence': {'state': 'pre-added', 'who': ['user:vgptnv'], 'prob': 1},
#   'fields': {},
#   'normalizations': {}},
#  {'classId': 'e_1',
#   'part': 's1s1v1',
#   'offsets': [{'start': 3, 'text': 'bebop'}],
#   'coordinates': [],
#   'confidence': {'state': 'pre-added', 'who': ['user:vgptnv'], 'prob': 1},
#   'fields': {},
#   'normalizations': {}}]

# "relations":[{"classId":"r_11",
#                 "type":"linked",
#                 "directed":false,
#                 "entities":["s1s1v1|e_1|13,13","s1s1v1|e_5|33,34"],
#                 "confidence":{"state":"pre-added","who":["user:Doohae"],"prob":1}},
#             {"classId":"r_21",
#                 "type":"linked",
#                 "directed":false,
#                 "entities":["s1s1v1|e_1|0,1","s1s1v1|e_1|3,7"],
#                 "confidence":{"state":"pre-added","who":["user:Doohae"],"prob":1}}]


# sentence, ent1, ent2, relation 묶음 만들기
def get_sentence_re(json_path, html_path):
    with open(html_path, "r") as f:
        html_file = f.read()
    sentence = get_context_from_html(html_file)
    assert type(sentence)==type("abc"), "sentence type incorrect!"

    with open(json_path, "r") as f:
        json_file = json.load(f)
    entities = json_file['entities']
    ent_list = []
    for ent in entities:
        # {'word':'뉴질랜드', 'start_idx':0, 'end_idx':3, 'type':'ORG'} 형식으로 만들기
        ent_type = mapping[ent['classId']]
        word = ent['offsets'][0]['text']
        start_idx = ent['offsets'][0]['start']
        end_idx = start_idx + len(word) - 1
        ent_list.append({'word':word, 'start_idx':start_idx, 'end_idx':end_idx, 'type':ent_type})
    
    relations = json_file['relations']
    if len(relations) == 0:
        pass
    else:
        pass