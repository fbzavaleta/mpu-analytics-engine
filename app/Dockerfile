FROM ubuntu:latest

RUN apt-get update -y 
RUN apt install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install pandas
RUN pip3 install mysql-connector-python
RUN pip3 install requests

WORKDIR /usr/app/
COPY  . .

CMD ["python3", "./main.py"]