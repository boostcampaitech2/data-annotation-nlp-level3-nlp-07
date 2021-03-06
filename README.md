# Boostcamp Data Annotation Competition
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


## ๐ถ TEAM : ์กฐ์งKLUE๋
### ๐ Members  

๊น๋ณด์ฑ|๊น์งํ|๊นํ์|๋ฐ์ด์ญ|์ด๋ค๊ณค|์ ๋ฏธ์|์ ๋ํด
:-:|:-:|:-:|:-:|:-:|:-:|:-:
![image1][image1]|![image2][image2]|![image3][image3]|![image4][image4]|![image5][image5]|![image6][image6]|![image7][image7]
[Github](https://github.com/Barleysack)|[Github](https://github.com/JIHOO97)|[Github](https://github.com/vgptnv)|[Github](https://github.com/Tentoto)|[Github](https://github.com/DagonLee)|[Github](https://github.com/ekdub92)|[Github](https://github.com/Doohae)


### ๐ Contribution

`๊น๋ณด์ฑ`ย  Entity Tagging โข Relation Tagging โข RE Tool ๊ฐ์ 

`๊น์งํ`   Entity Tagging โข Relation Tagging

`๊นํ์`ย  Entity Tag Set โข Relation Tagging โข Annotate

`๋ฐ์ด์ญ`ย  Entity ์ ์ โข Relation ์ ์ โข Random entity pair ์ถ์ถ

`์ด๋ค๊ณค`ย  Entity Tagging โข Relation Tagging

`์ ๋ฏธ์`ย  Data Preprocessing โข Entity Tagging โข Relation Tagging โข Data Pilot

`์ ๋ํด`  RE program ๊ฐ๋ฐ โข ํ๊ตญ์ด ๋ฌธ๋ฒ ํน์ฑ ์ ๋ฆฌ โข Entity Tagging โข Relation Tagging โข Random Entity Pair ์ถ์ถ โข kss ๋ฌธ์ฅ ๋ถ๋ฆฌ

[image1]: https://avatars.githubusercontent.com/u/56079922?v=4
[image2]: https://avatars.githubusercontent.com/u/57887761?v=4
[image3]: https://avatars.githubusercontent.com/u/62708568?v=4
[image4]: https://avatars.githubusercontent.com/u/80071163?v=4
[image5]: https://avatars.githubusercontent.com/u/43575986?v=4
[image6]: https://avatars.githubusercontent.com/u/42200769?v=4
[image7]: https://avatars.githubusercontent.com/u/80743307?v=4

<br/>


# 2. Project Outline

- Task : "ํ๋์ ์์" ์ฃผ์  ๊ด๋ จ ์ํคํผ๋์ ๋ฌธ์๋กค ์ด์ฉํด ํ๊ตญ์ด Relation Extraction task๋ฅผ ์ํ ๋ฐ์ดํฐ ์ฝํผ์ค ๊ตฌ์ถ
- Date : 2021.11.08 - 2021.11.19 (2 weeks)
- Description : ํ๊ตญ์ดย ๋ฐ ๋ค๋ฅธ ์ธ์ด์์์ ์์ฐ์ด์ฒ๋ฆฌ ๋ฐ์ดํฐ์์ ์ ํ ๋ฐ ํฌ๋งท์ด ์ด๋ ํ์ง, ๊ทธ๋ฆฌ๊ณ  ๋ฐ์ดํฐ์์ ๊ตฌ์ถํ๋ ์ผ๋ฐ์ ์ธ ํ๋ก์ธ์ค๊ฐ ๋ฌด์์ธ์ง ํ์ตํ๊ณ  ์ํคํผ๋์ ์์ ๋ง๋ญ์น๋ฅผ ํ์ฉํ์ฌ ์ง์ ย ๊ด๊ณ ์ถ์ถ ํ์คํฌ์ ์ฐ์ด๋ ์ฃผ์ ์ฝํผ์ค ๊ตฌ์ถ


### ๐ Final Score
<br/>
<p align="center">
   <img src="https://user-images.githubusercontent.com/80743307/142759807-4339a54d-3077-49be-8e44-f04008ce9a17.png" style="width:1000px;"/>
</p>
<br/>
๋ํ ์ฌ์ดํธ : [AI stage](https://stages.ai/competitions/79/overview/description)


# 3. Solution

### KEY POINT

- Problem Definition : `KLUE` ๋ผ๋ฌธ์ ๋ฐํ์ผ๋ก ๊ด๊ณ ์ถ์ถ ํ์คํฌ์ ์ฐ์ด๋ ๋ฐ์ดํฐ์ ๊ตฌ์ถ ๋ฐฉ์์ ํ์ตํ๊ณ  ํ์๋ค๊ฐ ํฉ์ํ๋ ๋ฐฉ์ ๊ฒฝํ
- Data Analysis : ๋ถ๋์ ๋๋์ด ๋ฌธ์๋ค์ ๊ฐ์ ์ฝ์ด ํน์ฑ์ ํ์ํ๊ณ  `kss` ๋ชจ๋์ ํ์ฉํด ๋ฌธ์ฅ ๋ถ๋ฆฌ ๋ฐ ํ๊ตญ์ด ์ธ์ด ํน์ฑ ํ์ต
- Pilot Tagging : ๊ฐ๋ณ๊ฒ ์์ ๋ฐ์ดํฐ๋ฅผ ํ์ด๋ณด๋ฉด์ ๊ฐ๋ฅํ Relation ๋ฐ Entity Tag set ๊ตฌ์
- Guideline : 3์ฐจ๋ก์ ๊ฑธ์น ํ์ผ๋ฟ ํ๊น ๊ณผ์ ์์ ํ์๋ค๊ฐ ๋ผ์ ๋ฐ ํฉ์๋ ๋ด์ฉ์ ๋ฐํ์ผ๋ก `๊ฐ์ด๋๋ผ์ธ`๊ณผ `Relation Map` ๊ตฌ์ถ + ์ง์์ ์ผ๋ก ํผ๋๋ฐฑ ๋ฐ์ํด updating
- Entity Processing : `Tagtog`์ ํ์ฉํด `Relation Map`์์ ์ ์ํ Entity์ ํด๋นํ๋ ๋จ์ด ๋ชจ๋ ์ถ์ถ ๋ฐ ์ํ ํ์ต ํ์ผ ์์์ ๋ง์ถ์ด ๋ณํํ๋ ์ฝ๋ ์์ฑ
- Relation Extraction :`Tagtog`, `Google SpreadSheet`, `termcolor ๋ชจ๋์ ํ์ฉํด ๋ง๋  ์์ฒด ์ ์ ํ๋ก๊ทธ๋จ`์ ์ด์ฉํด Entity pair ํ๊น
- Evaluation : ์ ์ฒด 10% ์ํ์ ๋ํด Fleiss Kappa๋ฅผ ํ์ฉํ `IAA` (Inter-Annotator Agreement) ์ธก์ 
- Testing : klue/roberta-large๋ฅผ ํ์ฉํ์ฌ ๊ตฌ์ถํ ๋ฐ์ดํฐ ํ์คํธ ๋ฐ `EDA`์งํ

   

# 4. How to Use

## **Installation**

๋ค์๊ณผ ๊ฐ์ ๋ช๋ น์ด๋ก ํ์ํ libraries๋ฅผ ๋ค์ด ๋ฐ์ต๋๋ค.

`pip install -r requirements.txt`

termcolor ๋ชจ๋ - tagging.py(์์ฒด ๊ฐ๋ฐ annotation tool)  \

`pip install termcolor`

<br/>
<p align="center">
   <img src="https://user-images.githubusercontent.com/80743307/142759673-0c07b7ed-2508-478e-9fe7-77d39974ed3e.png" style="width:1000px;"/>
</p>
<br/>
Relation Annotation ํ๋ก๊ทธ๋จ ํ๋ฉด ์์  

์์ธํ ์ฌ์ฉ ๋ฐฉ๋ฒ : https://nonstop-agenda-2a1.notion.site/Data-Viz-Tagging-Annotation-Tool-356681da873f4da49146965040fec3fd


## **Dataset**

๋๋ ํ ๋ฆฌ : data

## **Data Analysis**

๋๋ ํ ๋ฆฌ : modern_music

## **Data preprocessing**

ํ์ผ : tagtog_csv.py, tagging.py

## **Modeling**

๋๋ ํ ๋ฆฌ : code
  
  

- `code` ํด๋ ์์๋ ๊ฐ๊ฐ ๊ตฌ์ถ๋ dataset์ BERT ๋ชจ๋ธ์ ํตํด ํ์ต์ ์คํ์ํฌ ์ ์๋ ํ์ผ์ด ๋ค์ด์์ต๋๋ค.
- `tagtog_csv.py` ํ์ผ์ Tagtog ์ ํตํด ์์ํ ํ์ผ๋ค์ `code` ๋๋ ํ ๋ฆฌ์์ ์คํ ๊ฐ๋ฅํ๋๋ก ๋ณํํฉ๋๋ค.
- `tagging.py` ํ์ผ์ ์์ฒด ์ ์ relation annotation tool๋ก ์ถ์ถ๋ entity pair์ ๋ํด ๊ด๊ณ ๋ผ๋ฒจ๋ง์ ์์ํ๊ฒ ํ๋๋ก ํฉ๋๋ค.
