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
   <img src="https://user-images.githubusercontent.com/80743307/142759807-4339a54d-3077-49be-8e44-f04008ce9a17.png" style="width:1000px;"/>
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

   

# 4. How to Use

## **Installation**

다음과 같은 명령어로 필요한 libraries를 다운 받습니다.

`pip install -r requirements.txt`

termcolor 모듈 - tagging.py(자체 개발 annotation tool)  \

`pip install termcolor`

<br/>
<p align="center">
   <img src="https://user-images.githubusercontent.com/80743307/142759673-0c07b7ed-2508-478e-9fe7-77d39974ed3e.png" style="width:1000px;"/>
</p>
<br/>
Relation Annotation 프로그램 화면 예시  
자세한 사용 방법 : https://nonstop-agenda-2a1.notion.site/Data-Viz-Tagging-Annotation-Tool-356681da873f4da49146965040fec3fd


## **Dataset**

디렉토리 : data

## **Data Analysis**

디렉토리 : modern_music

## **Data preprocessing**

파일 : tagging_csv.py, tagging.py

## **Modeling**

디렉토리 : code
  
  

- `code` 파일 안에는 각각 구축된 dataset을 BERT 모델을 통해 학습을 실행시킬 수 있는 파일이 들어있습니다.
- `tagging_csv.py` 파일은 Tagtog 을 통해 작업한 파일들을 `code` 디렉토리에서 실행 가능하도록 변환합니다.
- `tagging.py` 파일은 자체 제작 relation annotation tool로 추출된 entity pair에 대해 관계 라벨링을 수월하게 하도록 합니다.
