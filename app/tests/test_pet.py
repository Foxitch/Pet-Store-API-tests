import allure
import pytest

from app.modules.application import Application
from app.src.base_classes.ResponseValidator import ResponseValidator
from app.src.schemas.pet_schem import PetModel, DeletedPet


@allure.suite('Pet Module')
@pytest.mark.pet
class TestPetModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create pet /POST')
    def test_create_pet(self, app: Application):
        """ https://petstore.swagger.io/#/pet/addPet """

        ResponseValidator(app.pet.create_pet()).validate_status_code(200).validate_response_model(PetModel)

    @allure.title('Get pet by ID /GET')
    def test_get_pet_by_id(self, app: Application):
        """ https://petstore.swagger.io/#/pet/getPetById """

        ResponseValidator(app.pet.get_pet_by_id()).validate_status_code(200).validate_response_model(PetModel)

    @allure.title('Change pet info /PUT')
    def test_change_pet_info(self, app: Application):
        """ https://petstore.swagger.io/#/pet/updatePet """

        ResponseValidator(app.pet.change_pet_info()).validate_status_code(200).validate_response_model(PetModel)

    @allure.title('Find pets by status /GET')
    def test_find_pets_by_status(self, app: Application):
        """ https://petstore.swagger.io/#/pet/findPetsByStatus """

        response, status = app.pet.find_pets_by_status()
        ResponseValidator(response).validate_status_code(200).validate_response_model(PetModel). \
            assert_pet_status(status)

    @allure.title('Delete pet /DELETE')
    def test_delete_pet(self, app: Application):
        """ https://petstore.swagger.io/#/pet/deletePet """

        ResponseValidator(app.pet.delete_pet()).validate_status_code(200).validate_response_model(DeletedPet)
