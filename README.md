API doc: https://petstore.swagger.io/#/

Version of python required: 3.10+

### EXECUTE ON THE LOCAL MACHINE ###

1. Install the Allure Report: https://docs.qameta.io/allure-report/
2. Install requirements:
`pip3 install -r requirements.txt`
3. Execute the test run:
`./run_tests.sh ./app/tests/`
4. Generate an allure report with results:
`allure serve allure-result/`

### EXECUTION IN THE DOCKER  ###

1. Install the Docker: https://www.docker.com/products/docker-desktop/
2. Launch the Docker
3. Execute this [run_build.sh](./run_build.sh) script
