from kss import split_sentences
from glob import glob
import os
from tqdm.auto import tqdm

data_path = "./data/"
txt_list = glob(os.path.join(data_path, "*"))

if not os.path.exists("./new_data/"):
    os.mkdir("./new_data/")

for idx in tqdm(range(len(txt_list)), desc="sentence being splitted"):
    print(f"Document {idx+1} splitting!")
    with open(txt_list[idx], "r") as f:
        lines = f.readlines()

    with open(os.path.join('./new_data/', txt_list[idx].split("/")[-1]), "w") as f:
        for line in lines:
            splitted = split_sentences(line)
            for sp_sent in splitted:
                f.write(sp_sent + '\n')