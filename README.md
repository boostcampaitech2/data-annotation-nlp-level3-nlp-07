# Boostcamp Machine Reading Comprehension Competition
## **Table of contents**

1. [Introduction](#1-introduction)
2. [Project Outline](#2-project-outline)
3. [Solution](#3-solution)
4. [How to Use](#4-how-to-use)

# 1. Introduction  
<br/>
<p align="center">
   <img src="https://user-images.githubusercontent.com/62708568/140640556-b2a0406c-09cd-48be-ae37-4c65e206b693.JPG" style="width:1000px;"/>
</p>

<br/>


## 🐶 TEAM : 조지KLUE니
### 🔅 Members  

김보성|김지후|김혜수|박이삭|이다곤|전미원|정두해
:-:|:-:|:-:|:-:|:-:|:-:|:-:
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|![image6][image6]|![image7][image7]
[Github](https://github.com/Barleysack)|[Github](https://github.com/JIHOO97)|[Github](https://github.com/vgptnv)|[Github](https://github.com/Tentoto)|[Github](https://github.com/DagonLee)|[Github](https://github.com/ekdub92)|[Github](https://github.com/Doohae)


### 🔅 Contribution

`김보성`  Entity Tagging • Relation Tagging • RE Tool 개선

`김지후`   Entity Tagging • Relation Tagging

`김혜수`  Entity Tag Set • Relation Tagging • Annotate

`박이삭`  Entity 정의 • Relation 정의 • Random entity pair 추출

`이다곤`  Entity Tagging • Relation Tagging

`전미원`  Data Preprocessing • Entity Tagging • Relation Tagging • Data Pilot

`정두해`  RE program 개발 • 한국어 문법 특성 정리 • Entity Tagging • Relation Tagging • Random Entity Pair 추출

[image1]: https://avatars.githubusercontent.com/u/56079922?v=4
[image2]: https://avatars.githubusercontent.com/u/57887761?v=4
[image3]: https://avatars.githubusercontent.com/u/62708568?v=4
[image4]: https://avatars.githubusercontent.com/u/80071163?v=4
[image5]: https://avatars.githubusercontent.com/u/43575986?v=4
[image6]: https://avatars.githubusercontent.com/u/42200769?v=4
[image7]: https://avatars.githubusercontent.com/u/80743307?v=4

<br/>


# 2. Project Outline

- Task : 한국어 Relation Extraction task를 위한 데이터 코퍼스 구축
- Date : 2021.11.08 - 2021.11.19 (2 weeks)
- Description : 한국어 및 다른 언어에서의 자연어처리 데이터셋의 유형 및 포맷이 어떠한지, 그리고 데이터셋을 구축하는 일반적인 프로세스가 무엇인지 학습하고 위키피디아 원시 말뭉치를 활용하여 직접 관계 추출 태스크에 쓰이는 주석 코퍼스 구축


### 🏆 Final Score
<br/>
<p align="center">
   <img src="https://user-images.githubusercontent.com/62708568/140643039-32a5da8a-0643-48f6-b272-4fbb6d58c57b.png" style="width:1000px;"/>
</p>
<br/>
대회 사이트 : [AI stage](https://stages.ai/competitions/79/overview/description)

## **Hardware**

AI stage에서 제공한 server, GPU

- GPU: V100

# 3. Solution

### KEY POINT

- ODQA Task (Open Domain Question Answering) : Retrieval + Reader 모델이 결합된 Hybrid model
- DPR 논문의 negative sample 추가 학습 + Dense Retriever 모델을 차용해 elasticsearch와 결합하여 retriever 모델 구현
- GPT-2를 활용해 wiki 데이터의 context에 paired된 질의를 생성해 Retrieval Dense Encoder 모델 학습
- Data Augmentation을 통해 지문의 길이를 늘린 후 학습 데이터로 이용
- 대량의 한국어 데이터로 사전학습 되어 있는 `klue/roberta-large` 모델을 리더 모델로 사용

### Checklist

- [x]  EDA
- [x]  Data Preprocessing(`special character removal`, `getting answer spans' start position with special character tokens`)
- [x]  Data Augmentation(`Back translation`, `Question generation`)
- [x]  Data Postprocessing
- [x]  Experimental Logging (`WandB`)
- [x]  Retrieval (`dense -- FAISS,using simple dual-encoders`, `sparse -- TF-IDF,BM25,Elastic search`, `Dense+Sparse -- using a linear combination of dense and sparse scores as the new raking function`)
- [x]  Custom Model Architecture(`Roberta with BiLSTM`, `Roberta with Autoencoder`)
- [x]  Re-ranker ( combining the reader score with the retriever score via linear combination `inspired by BERTserini`)
- [x]  Ensemble
- [ ]  Don't stop Pretraining (additional MLM Task, TAPT + DAPT)
- [ ]  K-fold cross validation
- [ ]  Shorten inference time when using elastic search

### Experiments

| Tried Experiments | Pipeline | Performance Improvement |
| --- | --- | --- |
| `TF-IDF` | `Retrieval` | <ul><li><center> [x] </center></li> | 
| `ElasticSearch config setting` | `Retrieval` | <ul><li> [ ] </li> | 
| `Question Generation (using GPT-2)` | `Retrieval` | <ul><li> [ ] </li> |
| `hard negative (using BM25 + ElasticSearch)` | `Retrieval` | <ul><li> [x] </li> |
| `DPR implementation` | `Retrieval` | <ul><li> [x] </li> |
| `Dense+Sparse` | `Retrieval` | <ul><li> [x] </li> |
| `Roberta with Bi-LSTM` | `Reader` | <ul><li> [ ] </li> |
| `Roberta with Autoencoder` | `Reader` | <ul><li> [ ] </li> |
| `Back-Translation` | `Reader` | <ul><li> [ ] </li> |
| `Context Concat(hard negative)` | `Reader` | <ul><li> [x] </li> |
| `Retrival+Reader Re-Ranker`  | `Inference` | <ul><li> [x] </li> |
   

# 4. How to Use

## **Installation**

다음과 같은 명령어로 필요한 libraries를 다운 받습니다.

`pip install -r requirements.txt`

Elasticsearch 모듈 (출처 : [서중원 멘토님 깃허브](https://github.com/thejungwon/search-engine-tutorial))
```
apt-get update && apt-get install -y gnupg2
wget -qO - [https://artifacts.elastic.co/GPG-KEY-elasticsearch](https://artifacts.elastic.co/GPG-KEY-elasticsearch) | apt-key add -
apt-get install apt-transport-https
echo "deb [https://artifacts.elastic.co/packages/7.x/apt](https://artifacts.elastic.co/packages/7.x/apt) stable main" | tee /etc/apt/sources.list.d/elastic-7.x.list
apt-get update && apt-get install elasticsearch
service elasticsearch start
cd /usr/share/elasticsearch
bin/elasticsearch-plugin install analysis-nori
service elasticsearch restart
pip install elasticsearch
```

BM25 모듈

`pip install rank_bm25`

Google deep_translator 모듈

`pip install -U deep-translator`

## **Dataset**

파일: data/train_dataset/train, data/train_dataset/validation, data/test_dataset/validation 

## **Data Analysis**

파일: code/notebooks/(folder)

## **Data preprocessing**

파일: preprocess.py, process_data.py, back_translation.py

## **Modeling**

파일: train.py, inference.py, golden_retriever.py, golden_serini.py, inference_serini.py

## **Ensemble**

파일: mixing_bowl.ipynb, mixing_bowl (1).ipynb

## Directory

```
.
├── mrc-level2-nlp-07
|    ├── code
│        ├── outputs
│        ├── dense_encoder
│        ├── retriever
|    ├── data
│        ├── train_dataset
|            ├── train
|            ├── validation
│        ├── test_dataset
|            ├── validation
|        ├── wikipedia_passages.json
```

- `code` 파일 안에는 각각 **data preprocessing** • **train** • **inference**가 가능한 라이브러리가 들어있습니다.
- `train.py`를 실행시키면 logs, results, best_model 폴더에 결과들이 저장됩니다.
- 사용자는 전체 코드를 내려받은 후, argument 옵션을 지정하여 개별 라이브러리 모델을 활용할 수 있습니다.
