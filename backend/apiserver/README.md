### 가상환경 만들기
~~~
conda create -n tts python=3.8.5
~~~

### 가상환경 접속
~~~
conda activate tts
~~~
### 필요한 라이브러리 다운
~~~
pip install -r requirements.txt
~~~

### backend 폴더에 들어가기
~~~
cd backend
~~~

### django 서버 실행
~~~
python manage.py runserver
~~~