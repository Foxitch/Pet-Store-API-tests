FROM python:3.11

RUN apt-get update && apt-get install -y python3-pip && apt install allure -y

WORKDIR /api_tests

VOLUME /allure-result

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod +x app/run_tests.sh

CMD app/run_tests.sh app/tests/

#Эту команду мы запускаем чтобы собрать наш контейнер
#docker build -t api-tests .

#Эта команда нужна чтобы запустить наш созданый контейнер
#docker run api-tests

#Эти 2 команды нам нужны чтобы скопировать данные из контейнера и чтобы сгенерировать из результата репорт
#docker cp $(docker ps -a -q | head -1):/solveme_pytest/allureress .
#allure serve allureress/
#Две команды ниже, помогут вам в эксперементах, чтобы после них почистить свой компьютер
#docker rm $(docker ps -a -q)
#docker kill $(docker ps -q)