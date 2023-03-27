FROM python:3.11

RUN apt-get update && apt-get install -y python3-pip && apt install allure -y

WORKDIR /opt/api_tests

VOLUME /opt/api_tests/allure-result

COPY ../requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x run_tests.sh
