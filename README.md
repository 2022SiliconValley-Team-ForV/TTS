# TTS
### 사이트에 목소리를 학습한 파일을 서버에 두어 사이트 내에서 원하는 문장을 넣어 TTS 문장을 들을 수 있습니다.
<!-- 동작하는 gif 같이 첨부 -->
<hr>

## 목차
  - [1. 목적](#1-목적)
  - [2. 아키텍처](#2-아키텍처)
  - [3. database](#3-database)
  - [4. api 문서](#4-api-문서)
  - [5. 실행 방법](#5-실행-방법)
  - [6. 파일 구조](#6-파일-구조)
  - [7. 팀원](#7-팀원)
  - [8. reference](#8-reference)
  - [9. copyright](#9-copyright)

<hr>

## 1. 목적

<hr>

## 2. 아키텍처
<img width="921" alt="스크린샷 2022-08-03 오후 8 56 10" src="https://user-images.githubusercontent.com/70627982/182602386-c5919ba2-ac66-43a0-86c2-ed7f12c6d3f2.png">

<hr>

## 3. database
![image](https://user-images.githubusercontent.com/70627982/182619271-eba06844-0b6e-4861-8e7d-76645acf0fd0.png)

<hr>

## 4. api 문서
![image](https://user-images.githubusercontent.com/70627982/182622232-264fd05c-487a-4ba9-98f5-5f7b2fc45344.png)
![image](https://user-images.githubusercontent.com/70627982/182622359-09d1961c-72d5-4634-be02-abe055142fc1.png)

<hr>

## 5. 실행 방법
git clone/download zip으로 파일을 다운받는다.
TTS/backend/apiserver/config에 my_settings.py를 넣는다.
TTS/backend/apiserver에 mnesia파일을 넣는다.
TTS/backend/modelserver/voice_model의 glow-tts, hifigan-v2 각각에 checkoutpoint.pth.tar, config.json, scale_stats.npy파일을 넣어준다.
npm install
docker compose up --build
<hr>

## 6. 파일 구조
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
<hr>

## 7. 팀원

| Name    | <center>배준일</center>|<center>최준혁</center> |<center> 이수현 </center> | <center>김혜진</center> | <center>구지혜</center>
| ------- | --------------------------------------------- | ------------------------------------ | --------------------------------------------- | --------------------------------------- | --------------------------------------- |
| Profile | <img width="150px" src="https://avatars.githubusercontent.com/u/70627982?v=4" />|<img width="150px" src="https://avatars.githubusercontent.com/u/98803599?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/105929978?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/76868442?v=4" />| <img width="150px" src="https://avatars.githubusercontent.com/u/105404542?v=4" />|
| role    | <center>Team Leader, <br>Backend & DevOps</center>   | <center>Backend & AI</center>    | <center>DevOps  </center>  | <center>Frontend</center> | <center>Frontend</center> |
| Github  | <center>[@bjo6300](https://github.com/bjo6300)</center> | <center>[@hi-june](https://github.com/hi-june)</center> | <center>[@suhyeon3484](https://github.com/suhyeon3484)</center> | <center>[@llmeajinll](https://github.com/llmeajinll)</center> | <center>[@jihye9549](https://github.com/jihye9549) </center>| 

<hr>

## 8. reference

<details>
<summary>참고 자료</summary>
<div markdown="1">

- [내 목소리로 TTS 만들기](https://sce-tts.github.io/#/v2/index)

- [flask & g2pk in Docker](https://github.com/litsynp/flask-g2pk)

</div>
</details>

<hr>

## 9. copyright

Distributed under the MIT License. See `LICENSE` for more information.

