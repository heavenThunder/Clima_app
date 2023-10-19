FROM python:latest
COPY requirements_.txt /app/requirements.txt
COPY ./app usr/src/app
WORKDIR /usr/src/app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt