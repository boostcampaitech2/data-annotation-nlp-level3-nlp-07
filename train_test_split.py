from sklearn.model_selection import train_test_split
import pandas as pd
import os

FILE_NAME = "./new_dataset.csv"
SAVE_DIR = "./data/"
RANDOM_SEED = 42

df = pd.read_csv(FILE_NAME)
train, test = train_test_split(df, test_size=0.1, stratify=df['relation'], random_state=RANDOM_SEED)

if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)
    
train.to_csv(os.path.join(SAVE_DIR, "train.csv"), index=False)
test.to_csv(os.path.join(SAVE_DIR, "test.csv"), index=False)