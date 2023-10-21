FROM python:latest
COPY . usr/src/app
WORKDIR /usr/src/app
COPY requirements_.txt app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r ./app/requirements.txt
ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload