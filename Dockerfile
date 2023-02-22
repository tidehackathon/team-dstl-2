FROM python:3.10-slim
RUN apt update
RUN apt -y install curl
COPY ./requirements.txt /usr/local/src/app/
RUN pip3 install -r /usr/local/src/app/requirements.txt
COPY . /usr/local/src/app/
WORKDIR /usr/local/src/app/