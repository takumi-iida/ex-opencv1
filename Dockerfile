FROM python:3.8-slim

WORKDIR /tmp/mydir

COPY requirements.txt ${PWD}

# opencv-devのインストール
RUN apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Opencvのインストール
RUN pip3 install -r requirements.txt

ARG wdir="/tmp/src"
ENV work tensor-docker
WORKDIR $wdir
