import allure
import pytest

from app.modules.application import Application
from app.src.base_classes.response import Response
from app.src.schemas.user_schem import UserModel, SuccessfulRequestModel


@allure.suite('User Module')
@pytest.mark.user
class TestUserModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create User /POST')
    def test_create_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/createUser """

        Response(app.user.create_user()).assert_status_code(200).validate_schem(SuccessfulRequestModel)

    @allure.title('Get Users info /GET')
    def test_get_users_info(self, app: Application):
        """ https://petstore.swagger.io/#/user/getUserByName """

        Response(app.user.get_created_user()).assert_status_code(200).validate_schem(UserModel)

    @allure.title('Change Users info /PUT')
    def test_change_users_info(self, app: Application):
        """ https://petstore.swagger.io/#/user/updateUser """

        Response(app.user.change_user_info()).assert_status_code(200).validate_schem(SuccessfulRequestModel)

    @allure.title('Login as created User /GET')
    def test_login_as_created_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/loginUser """

        Response(app.user.login_as_created_user()).assert_status_code(200).validate_schem(SuccessfulRequestModel)

    @allure.title('Delete User /DELETE')
    def test_delete_user(self, app: Application):
        """ https://petstore.swagger.io/#/user/deleteUser """

        Response(app.user.delete_user()).assert_status_code(200).validate_schem(SuccessfulRequestModel)

    @allure.title('Create list of Users /POST')
    def test_create_list_of_users(self, app: Application):
        """ https://petstore.swagger.io/#/user/createUsersWithListInput """

        Response(app.user.create_list_of_users()).assert_status_code(200).validate_schem(SuccessfulRequestModel)
