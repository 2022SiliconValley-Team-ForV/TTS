# pull official base image
# 우분투
FROM python:3.8.3
USER root 
# environment 환경변수 지정, 컨테이너 안에서 실행중일 때 사용가능
# ex) django의 settings.py에서 secret_key = os.getenv('SECRET_KEY', 'foo')
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# WORKDIR : working directory 작업경로 
WORKDIR /backend/apiserver
# COPY : 호스트 컴퓨터(로컬)에서 requirements.txt를 
# 복사해서 도커 컨테이너의 backend 폴더에 넣겠다.
COPY requirements.txt /backend/apiserver/

RUN apt-get update && apt-get install -y python3-pip libffi-dev python3-dev && apt-get install -y default-libmysqlclient-dev 

# 리눅스 명령어를 실행하겠다 alpine : apk, ubuntu : sudo
# 연결하기 위한 드라이버를 깔았다고 생각하면 된다.
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# wait-for 적용
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
CMD /wait && /wait-for-mysql.sh

WORKDIR /backend