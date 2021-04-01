FROM python:3.7-alpine

WORKDIR /srv
EXPOSE 8000

RUN apk add --update alpine-sdk

# Copy requirements.txt before code to let Docker cache Python dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /srv
