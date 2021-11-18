import pandas as pd
from tqdm.auto import tqdm

df = pd.read_csv("./train/dataset.csv")
df.rename(columns={"id,sentence,subject_entity,object_entity,relation,Unnamed: 5,Unnamed: 6":"id"}, inplace=True)
df['id'] = list(range(len(df['id'])))

mapping = {
    "gen:origin" : 0,
    "gen:alternate_name" : 1,
    "gen:super_genre" : 2,
    "genre:sub_genre" : 3,
    "genre:artist" : 4,
    "gen:artist" : 4,
    "artist:member_of" : 5,
    "producer:product" : 6,
    "artist:product" : 6,
    "product:origin" : 7,
    "no_relation" : 8
}

def filter_df(df):
    sentence = list(df['sentence'])
    subject_entity = [eval(ent) for ent in list(df['subject_entity'])]
    object_entity = [eval(ent) for ent in list(df['object_entity'])]
    relation = list(df['relation'])
    new_sent, new_sub, new_obj, new_rel = [], [], [], []
    for idx in tqdm(range(len(sentence))):
        if relation[idx] not in mapping.keys():
            continue
        if subject_entity[idx]['word'] == object_entity[idx]['word']:
            continue
        new_sent.append(sentence[idx])
        new_sub.append(subject_entity[idx])
        new_obj.append(object_entity[idx])
        new_rel.append(mapping[relation[idx]])
    new_df = pd.DataFrame({"id":list(range(len(new_sent))), "sentence":new_sent, "subject_entity":new_sub, "object_entity":new_obj, "relation":new_rel})
    return new_df


new_df = filter_df(df)
new_df.to_csv("./new_dataset.csv", index=False)