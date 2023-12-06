#!/bin/bash

docker build -t api-tests -f docker/Dockerfile .
docker compose -f docker/docker-compose.yml up
docker cp "$(docker ps -a -q | head -1)":/opt/api_tests/allure-result .
allure serve allure-result
