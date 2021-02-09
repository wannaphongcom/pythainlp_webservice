FROM python:3.7
MAINTAINER Wannaphong Phatthiyaphaibun <wannaphong@kkumail.com>
WORKDIR /app
EXPOSE 8000

COPY requirements.txt ./
RUN apt-get update
RUN apt-get install -y python3-dev
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app"]
