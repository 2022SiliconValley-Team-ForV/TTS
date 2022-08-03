# TTS
 팀원 5명의 목소리로 원하는 문장을 음성 변환하는 서비스
 <!-- 동작하는 gif 같이 첨부 -->
<hr>

## 목차
  - [1. 목적](#1-목적)
  - [2. 아키텍처](#2-아키텍처)
  - [3. 기술 스택](#3-기술-스택)
  - [4. 실행 방법](#4-실행-방법)
  - [5. database](#5-database)
  - [6. api 문서](#6-api-문서)
  - [7. 파일 구조](#7-파일-구조)
  - [8. 팀원](#8-팀원)
  - [9. reference](#9-reference)
  - [10. copyright](#10-copyright)

<hr>

## 1. 목적
❤️‍🔥최애의 목소리로 자신이 입력한 문장을 읽어주는 기능을 목표로 하고있습니다.  

🗣️TTS를 이용해 <b>아이돌 그룹</b>이나 <b>아티스트</b>를 효과적으로 <b>홍보</b>합니다.

<hr>

## 2. 아키텍처
<img width="921" alt="스크린샷 2022-08-03 오후 8 56 10" src="https://user-images.githubusercontent.com/70627982/182602386-c5919ba2-ac66-43a0-86c2-ed7f12c6d3f2.png">

<hr>

## 3. 기술 스택
- <b>Front-End</b>  
  <img src="https://img.shields.io/badge/react-02569B?style=for-the-badge&logo=react&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  
- <b>Back-End</b>  
<img src="https://img.shields.io/badge/django-007396?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/flask-6DB33F?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/celery-000000?style=for-the-badge&logo=celery&logoColor=white"> <img src="https://img.shields.io/badge/rabbitmq-FF6F00?style=for-the-badge&logo=rabbitmq&logoColor=white">

- <b>DevOps</b>    
  <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <!-- <img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white"> -->


- <b>AI (Tools, Env)</b>    
  <img src="https://img.shields.io/badge/colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white"> <img src="https://img.shields.io/badge/pytorch-F7931E?style=for-the-badge&logo=pytorch&logoColor=white">  
  
- <b>UI/UX, MockUp Design </b>    
  <img src="https://img.shields.io/badge/figma-34A7C1?style=for-the-badge&logo=figma&logoColor=white"> <img src="https://img.shields.io/badge/zeplin-31A8FF?style=for-the-badge&logo=zeplin&logoColor=white"> 
  
- <b>Team Collaboration Tool</b>    
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/notion-0052CC?style=for-the-badge&logo=notion&logoColor=white"> <img src="https://img.shields.io/badge/slack-D24939?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/zoom-2496ED?style=for-the-badge&logo=zoom&logoColor=white">

<hr>

## 4. 실행 방법

### Git clone
```
git clone https://github.com/2022SiliconValley-Team-ForV/TTS.git
```

### Django setting
`TTS/backend/apiserver/config` 경로에 `my_settings.py` 파일을 세팅합니다. 

```
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


MY_SECRET = {
    "SECRET_KEY" : ''
}

MY_DATABASES = {
    'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'tts', 
        'USER': 'root', 
        'PASSWORD': '1234', 
        'HOST': 'ttsmysql', 
        'PORT': '3306', 
     } 
}
```

## Run
모델파일 용량이 크므로 docker container, image, volume 공간을 확보해주세요!
```
docker-compose up --build
```

<hr>

## 5. database
![image](https://user-images.githubusercontent.com/70627982/182619271-eba06844-0b6e-4861-8e7d-76645acf0fd0.png)

<hr>

## 6. api 문서
<details>
<summary>swagger</summary>
<div markdown="1">

<br>
  
![image](https://user-images.githubusercontent.com/70627982/182622232-264fd05c-487a-4ba9-98f5-5f7b2fc45344.png)
  
![image](https://user-images.githubusercontent.com/70627982/182622359-09d1961c-72d5-4634-be02-abe055142fc1.png)

</div>
</details>
<hr>

## 7. 파일 구조

<details>
<summary> File Tree </summary>
<div markdown="1">

```txt
TTS
├── LICENSE
├── README.md
├── backend
│   ├── apiserver
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   ├── config
│   │   ├── db_init.py
│   │   ├── erl_crash.dump
│   │   ├── mainApp
│   │   ├── manage.py
│   │   ├── model_init.py
│   │   ├── requirements.txt
│   │   └── wait-for-mysql.sh
│   └── modelserver
│       ├── Dockerfile
│       ├── README.md
│       ├── TTS
│       ├── app.py
│       ├── celery_app.py
│       ├── micro-handler.json
│       ├── requirements.txt
│       ├── requirements_TTS.txt
│       ├── simple_task.py
│       ├── temp
│       ├── test_tasks.py
│       ├── tts_modules.py
│       └── voice_model
├── docker-compose.yml
└── frontend
    ├── Dockerfile
    ├── README.md
    ├── package.json
    ├── public
    │   ├── favicon.ico
    │   ├── index.html
    │   ├── logo192.png
    │   ├── logo512.png
    │   ├── manifest.json
    │   └── robots.txt
    └── src
        ├── App.css
        ├── App.js
        ├── Font
        ├── Images
        ├── Styles
        ├── Views
        ├── index.css
        ├── index.js
        ├── reportWebVitals.js
        ├── reset.css
        └── setupTests.js"
```
</div>
</details>
  
<hr>

## 8. 팀원

| Name    | <center>배준일</center>|<center>최준혁</center> |<center> 이수현 </center> | <center>김혜진</center> | <center>구지혜</center>
| ------- | --------------------------------------------- | ------------------------------------ | --------------------------------------------- | --------------------------------------- | --------------------------------------- |
| Profile | <img width="150px" src="https://avatars.githubusercontent.com/u/70627982?v=4" />|<img width="150px" src="https://avatars.githubusercontent.com/u/98803599?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/105929978?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/76868442?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/105404542?v=4" />|
| role    | <center>Team Leader, <br>Backend & DevOps</center>   | <center>Backend & AI</center>    | <center>DevOps  </center>  | <center>Frontend</center> | <center>Frontend</center> |
| Github  | <center>[@bjo6300](https://github.com/bjo6300)</center> | <center>[@hi-june](https://github.com/hi-june)</center> | <center>[@suhyeon3484](https://github.com/suhyeon3484)</center> | <center>[@llmeajinll](https://github.com/llmeajinll)</center> | <center>[@jihye9549](https://github.com/jihye9549) </center>| 

<hr>

## 9. reference

<details>
<summary>참고 자료</summary>
<div markdown="1">

- [내 목소리로 TTS 만들기](https://sce-tts.github.io/#/v2/index)

- [flask & g2pk in Docker](https://github.com/litsynp/flask-g2pk)

</div>
</details>

<hr>

## 10. copyright

Distributed under the MIT License. See `LICENSE` for more information.

