FROM python:3.7
MAINTAINER Wannaphong Phatthiyaphaibun <wannaphong@kkumail.com>
WORKDIR /usr/src/app
EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]