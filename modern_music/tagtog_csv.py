import os
import json
from glob import glob
import pandas as pd
import re
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


def get_random_entities():
    pass

def relation_set():
    pass


# sentence, ent1, ent2, relation 묶음 만들기
def get_sentence_re(json_path, html_path):
    with open(html_path, "r") as f:
        html_file = f.read()
    sentence = get_context_from_html(html_file)

    with open(json_path, "r") as f:
        json_file = json.load(f)

    try:
        relations = json_file['relations']

    except:
        pass

    


