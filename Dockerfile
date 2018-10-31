FROM python:3.7

RUN apt-get update
RUN apt-get -y install vim

RUN mkdir /work
WORKDIR /work

RUN pip install --upgrade pip
RUN pip install dash==0.28.5
RUN pip install dash-html-components==0.13.2
RUN pip install dash-core-components==0.35.1
RUN pip install pandas
RUN pip install -U scikit-learn

