FROM ubuntu:latest

RUN apt-get update -y 
RUN apt install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install pandas
RUN pip3 install mysql-connector-python 
RUN pip3 install numpy
RUN pip3 install scikit-learn
RUN pip3 install sklearn
RUN pip3 install os

WORKDIR /usr/Modelo/
COPY  . .

CMD ["python3", "./Modelling.py"]