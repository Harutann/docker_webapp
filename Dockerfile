# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements4.txt requirements4.txt
RUN pip3 install -r requirements4.txt
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]


