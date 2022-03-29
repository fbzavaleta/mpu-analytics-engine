FROM ubuntu:latest

RUN apt-get update -y 
RUN apt install python3 -y
RUN apt-get install python3-pip -y

COPY  requirements.txt .
RUN pip install -r requirements.txt

RUN pip3 install mysql-connector-python

WORKDIR /usr/app/
COPY . .

CMD ["python3", "main.py"]