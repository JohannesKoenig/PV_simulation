# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /pv_simulator
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "src.main"]