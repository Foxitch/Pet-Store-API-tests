#!/bin/sh

echo "API tests started"

result=$(python3.11 -m pytest "$1" --alluredir=allure-result | grep -o "FAILED\|ERROR" | wc -l)

if [ "$result" -eq 0 ]
then
    echo "API tests finished without errors"
else
    echo "API tests finished with $result errors"
fi
