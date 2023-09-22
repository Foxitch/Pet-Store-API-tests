import allure
import pytest

from app.modules.application import Application
from app.src.base_classes.ResponseValidator import ResponseValidator
from app.src.schemas.user_schem import UserModel, SuccessfulRequestModel


@allure.suite('User Module')
@pytest.mark.user
class TestUserModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create User /POST')
    def test_create_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/createUser """

        ResponseValidator(app.user.create_user()).validate_status_code(200). \
            validate_response_model(SuccessfulRequestModel)

    @allure.title('Get Users info /GET')
    def test_get_users_info(self, app: Application):
        """ https://petstore.swagger.io/#/user/getUserByName """

        ResponseValidator(app.user.get_created_user()).validate_status_code(200).validate_response_model(UserModel)

    @allure.title('Change Users info /PUT')
    def test_change_users_info(self, app: Application):
        """ https://petstore.swagger.io/#/user/updateUser """

        ResponseValidator(app.user.change_user_info()).validate_status_code(200). \
            validate_response_model(SuccessfulRequestModel)

    @allure.title('Login as created User /GET')
    def test_login_as_created_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/loginUser """

        ResponseValidator(app.user.login_as_created_user()).validate_status_code(200). \
            validate_response_model(SuccessfulRequestModel)

    @allure.title('Delete User /DELETE')
    def test_delete_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/deleteUser """

        ResponseValidator(app.user.delete_user()).validate_status_code(200). \
            validate_response_model(SuccessfulRequestModel)

    @allure.title('Create list of Users /POST')
    def test_create_list_of_users(self, app: Application):
        """ https://petstore.swagger.io/#/user/createUsersWithListInput """

        ResponseValidator(app.user.create_list_of_users()).validate_status_code(200). \
            validate_response_model(SuccessfulRequestModel)
