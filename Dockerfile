ARG PYTHON_VERSION

FROM python:$PYTHON_VERSION
MAINTAINER Marco Graziano mgrazianodecastro@gmail.com

RUN apt-get update && \
	apt-get install -y vim && \
	apt-get install -y git

WORKDIR /usr/src/local

RUN git clone https://github.com/Marcopopom/WData

COPY ./requirements.txt /usr/src/local/WData

WORKDIR /usr/src/local/WData

RUN pip install -r requirements.txt

COPY ./a_data_processing/YouTube/config/Key.txt /usr/src/local/WData/a_data_processing/YouTube/config/
