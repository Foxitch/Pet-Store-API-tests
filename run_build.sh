#!/bin/sh


docker build -t api-tests .
docker run api-tests
docker cp $(docker ps -a -q | head -1):/api_tests/allure-result .
allure serve allure-result
