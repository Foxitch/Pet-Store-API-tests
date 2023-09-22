import allure
import pytest

from app.modules.application import Application
from app.src.base_classes.ResponseValidator import ResponseValidator
from app.src.schemas.store_schem import StoreModel, DeletedStoresOrderModel, StoresInventoryModel


@allure.suite('Store Module')
@pytest.mark.store
class TestStoreModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create Order /POST')
    def test_create_order(self, app: Application):
        """ https://petstore.swagger.io/#/store/placeOrder """

        ResponseValidator(app.store.create_store_order()).validate_status_code(200).validate_response_model(StoreModel)

    @allure.title('Get Order by ID /GET')
    def test_get_order_by_id(self, app: Application):
        """ https://petstore.swagger.io/#/store/getOrderById """

        ResponseValidator(app.store.get_order_by_id()).validate_status_code(200).validate_response_model(StoreModel)

    @allure.title('Delete Order /DELETE')
    def test_delete_order(self, app: Application):
        """ https://petstore.swagger.io/#/store/deleteOrder """

        ResponseValidator(app.store.delete_order()).validate_status_code(200). \
            validate_response_model(DeletedStoresOrderModel)

    @allure.title('Get stores inventory /GET')
    def test_get_stores_inventory(self, app: Application):
        """ https://petstore.swagger.io/#/store/getInventory """

        ResponseValidator(app.store.get_inventory()).validate_status_code(200). \
            validate_response_model(StoresInventoryModel)
