FROM python:3.11

RUN apt-get update && apt-get install -y python3-pip && apt install allure -y

WORKDIR /api_tests

VOLUME /allure-result

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x app/run_tests.sh

CMD app/run_tests.sh app/tests/
