#!/bin/sh

echo "tests started"

result=$(python3.11 -m pytest "$1" --alluredir=allure-results | grep -o "FAILED\|ERROR" | wc -l)

if [ "$result" -eq 0 ]
then
    echo "Tests finished without errors"
else
    echo "Tests finished with $result errors"
fi
