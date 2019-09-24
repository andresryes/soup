FROM python:3-alpine

ENV DEVELOPER="Andres Bolaños"

ARG PHASE

ENV PHASE=$PHASE

ADD / home

WORKDIR /home

RUN pip install -r requirements.txt

WORKDIR /home/soup

CMD ["python", "main.py"]
