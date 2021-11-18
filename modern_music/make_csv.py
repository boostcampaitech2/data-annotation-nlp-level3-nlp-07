import pandas as pd
from glob import glob
import os
from tqdm.auto import tqdm

data_path = "./complete_txt/"
csv_path = "./csv/"
txt_list = glob(os.path.join(data_path, "*"))

if not os.path.exists(csv_path):
    os.mkdir(csv_path)

for idx in tqdm(range(len(txt_list)), desc="csv processing"):
    with open(txt_list[idx], "r") as f:
        lines = f.read()
    
    df = pd.DataFrame({"sentence":lines.split('\n')})
    df.to_csv(os.path.join(csv_path, txt_list[idx].split('/')[-1].split('.')[0] + '.csv'), index=False)