FROM python:3.6.15

# Python
RUN apt-get update && \
  apt-get install -y --no-install-recommends apt-utils && \
  apt-get -y install software-properties-common && \
  apt-get update --fix-missing && \
  apt-get -y install --fix-missing python3-pip && \
  python3 -m pip install pip --upgrade

RUN apt-get update -y && \
  apt-get install -y --no-install-recommends build-essential gcc \
  libsndfile1

# mecab start
RUN apt-get update && \
  apt-get install -y --no-install-recommends tzdata g++ git curl
RUN apt-get install python3-setuptools
RUN apt-get install -y default-jdk default-jre
# mecab end

# RUN mkdir app

WORKDIR /backend/modelserver

# volumes로 로컬 ./ 경로랑 컨테이너 /app 경로랑 공유하는데 왜 copy가 필요한가..
COPY requirements.txt .
COPY requirements_TTS.txt .

#RUN git clone --depth 1 https://github.com/sce-tts/TTS.git -b sce-tts

RUN pip install -r requirements.txt
RUN pip install -r requirements_TTS.txt

RUN pip install nltk==3.6.7
RUN pip install konlpy==0.6.0
RUN pip install mecab-ko==1.0.0
RUN pip install mecab-python==1.0.0
RUN pip install python-mecab-ko==1.0.14
RUN pip install g2pk==0.9.4

# mecab start
# RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# RUN update-alternatives --config python3
RUN cd . && \
  curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -s
# mecab end

RUN export LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

COPY . .
