# 주의 : 한번 돌리시면 원큐에 다 끝내실걸 가정하고 만든 프로그램입니다
# 특정 인덱스만 고치려고 하시는 경우 코드를 변형하거나 수기 라벨링 하시는걸 추천드립니다!
from termcolor import colored
import pandas as pd
import argparse
# 입력 파일명과 새로 저장할 파일명 설정
FILE_NAME = "./bosung.csv"
SAVE_NAME = "./new_label.csv"

df = pd.read_csv(FILE_NAME)

# 숫자 입력에 대해 맵핑
mapping = {
    0 : "gen:origin",
    1 : "gen:alternate_name",
    2 : "gen:super_genre",
    3 : "genre:sub_genre",
    4 : "genre:artist",
    5 : "artist:member_of",
    6 : "producer:product",
    7 : "product:origin",
    8 : "no_relation"
}

# subject, object, sentence 정보가 들어오면
# subject : 붉은색, object : 푸른색
# 하이라이트 적용하여 터미널에 출력
def word_highlight(sentence, sub_si, sub_ei, obj_si, obj_ei):
    mi, ni = max(sub_si, obj_si), min(sub_si, obj_si)
    sent1, sent2 = sentence[:mi], sentence[mi:]
    # subject가 앞에 있을 때
    if ni == sub_si:
        sub = colored(sent1[sub_si:sub_ei+1], None, "on_red")
        sent1 = sent1[:sub_si]+sub+sent1[sub_ei+1:]
        obj = colored(sent2[:obj_ei-obj_si+1], None, "on_blue")
        sent2 = obj+sent2[obj_ei-obj_si+1:]
    # object가 앞에 있을 때
    else:
        obj = colored(sent1[obj_si:obj_ei+1], None, "on_blue")
        sent1 = sent1[:obj_si]+obj+sent1[obj_ei+1:]
        sub = colored(sent2[:sub_ei-sub_si+1], None, "on_red")
        sent2 = sub+sent2[sub_ei-sub_si+1:]
    print(sent1+sent2)


# 라베링 대상이 되는 하이라이트 처리된 문장을 띄우고
# 사용자 입력을 받아 relation 맵핑 처리
def show_highlight(idx,sentence, sub, obj):
    
    print("-"*100)
    for k, v in mapping.items():
        print(k, v)
    print("-"*100)
    print("Insert proper number for relation!")
    print("-"*100)
    sub, obj = eval(sub), eval(obj)
    ssi, sei = sub['start_idx'], sub['end_idx']
    osi, oei = obj['start_idx'], obj['end_idx']
    word_highlight(sentence, ssi, sei, osi, oei)
    print("If you want to take some rest, type save. ")
    label = input("Insert integer type relation : ")
    if label == "save":
        print(f"We all need some break... you've done your job until {idx}")
        exit(0)
    else:
        label=int(label)
        assert label in range(9), "Insert Correct Number of Label"
        return mapping[label]


# 사용자가 입력을 할때마다 csv 파일 갱신
def correct_csv_all(checkpoint,file, save_path=SAVE_NAME):
    
    if checkpoint != 0:
        print("Checkpoint found, continue from checkpoint...")
        

    
    sentence = list(file.iloc[:, 1])
    sub, obj = list(file.iloc[:, 2]), list(file.iloc[:, 3])
    label = list(file.iloc[:, 4])
    
    for idx in range(checkpoint,len(label)):
        relation = show_highlight(idx,sentence[idx], sub[idx], obj[idx])
        label[idx] = relation
        file.iloc[:, 4] = label
        file.to_csv(save_path, index=False)


def main():
    global df
    parser = argparse.ArgumentParser()
    parser.add_argument('--cp',default=0,help='enter checkpoint!')
    args = parser.parse_args()
    checkpoint = int(args.cp)
    if checkpoint !=0:
        df = pd.read_csv(SAVE_NAME)
    correct_csv_all(checkpoint,df)


if __name__ == "__main__":
    main()