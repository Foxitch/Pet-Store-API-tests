import allure

from app.modules.application import Application
from app.src.base_classes.response import Response
from app.src.schemas.pet_schem import PetModel, DeletedPet


@allure.suite('Pet Module')
class TestPetModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create pet /POST')
    def test_create_pet(self, app: Application):
        """ https://petstore.swagger.io/#/pet/addPet """

        Response(app.pet.create_pet()).assert_status_code(200).validate_schem(PetModel)

    @allure.title('Get pet by ID /GET')
    def test_get_pet_by_id(self, app: Application):
        """ https://petstore.swagger.io/#/pet/getPetById """

        Response(app.pet.get_pet_by_id()).assert_status_code(200).validate_schem(PetModel)

    @allure.title('Change pet info /PUT')
    def test_change_pet_info(self, app: Application):
        """ https://petstore.swagger.io/#/pet/updatePet """

        Response(app.pet.change_pet_info()).assert_status_code(200).validate_schem(PetModel)

    @allure.title('Find pets by status /GET')
    def test_find_pets_by_status(self, app: Application):
        """ https://petstore.swagger.io/#/pet/findPetsByStatus """

        response, status = app.pet.find_pets_by_status()
        Response(response).assert_status_code(200).validate_schem(PetModel).assert_pet_status(status)

    @allure.title('Delete pet /DELETE')
    def test_delete_pet(self, app: Application):
        """ https://petstore.swagger.io/#/pet/deletePet """

        Response(app.pet.delete_pet()).assert_status_code(200).validate_schem(DeletedPet)
