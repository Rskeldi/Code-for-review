FROM python:3.8.10

RUN mkdir /webapp
WORKDIR /webapp

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
