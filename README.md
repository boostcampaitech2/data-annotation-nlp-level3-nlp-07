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


# 3. Solution

### KEY POINT

- Problem Definition : `KLUE` 논문을 바탕으로 관계 추출 태스크에 쓰이는 데이터셋 구축 방식을 학습하고 팀원들간 합의하는 방식 경험
- Data Analysis : 분량을 나누어 문서들을 각자 읽어 특성을 파악하고 `kss` 모듈을 활용해 문장 분리 및 한국어 언어 특성 학습
- Pilot Tagging : 가볍게 원시 데이터를 훑어보면서 가능한 Relation 및 Entity Tag set 구상
- Guideline : 3차례에 걸친 파일럿 태깅 과정에서 팀원들간 논의 및 합의된 내용을 바탕으로 `가이드라인`과 `Relation Map` 구축 + 지속적으로 피드백 반영해 updating
- Entity Processing : `Tagtog`을 활용해 `Relation Map`에서 정의한 Entity에 해당하는 단어 모두 추출 및 샘플 학습 파일 양식에 맞추어 변형하는 코드 작성
- Relation Extraction :`Tagtog`, `Google SpreadSheet`, `termcolor 모듈을 활용해 만든 자체 제작 프로그램`을 이용해 Entity pair 태깅
- Evaluation : 전체 10% 샘플에 대해 Fleiss Kappa를 활용한 `IAA` (Inter-Annotator Agreement) 측정
- Testing : klue/roberta-large를 활용하여 구축한 데이터 테스트 및 `EDA`진행


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

termcolor 모듈
`pip install termcolor`


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
