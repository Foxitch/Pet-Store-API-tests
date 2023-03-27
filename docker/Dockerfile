FROM --platform=linux/amd64 ubuntu

RUN apt-get update
RUN apt install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb -y

RUN apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa -y && apt install python3.10
RUN apt-get install python3-pip -y

WORKDIR /opt/ui_tests

COPY ../requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
