import allure

from app.modules.application import Application
from app.src.base_classes.response import Response
from app.src.schemas.store_schem import StoreModel, DeletedStoresOrderModel, StoresInventoryModel


@allure.suite('Store Module')
class TestStoreModule:
    """ https://petstore.swagger.io/#/ """

    @allure.title('Create Order /POST')
    def test_create_order(self, app: Application):
        """ https://petstore.swagger.io/#/store/placeOrder """

        Response(app.store.create_store_order()).assert_status_code(200).validate_schem(StoreModel)

    @allure.title('Get Order by ID /GET')
    def test_get_order_by_id(self, app: Application):
        """ https://petstore.swagger.io/#/store/getOrderById """

        Response(app.store.get_order_by_id()).assert_status_code(200).validate_schem(StoreModel)

    @allure.title('Delete Order /DELETE')
    def test_delete_order(self, app: Application):
        """ https://petstore.swagger.io/#/store/deleteOrder """

        Response(app.store.delete_order()).assert_status_code(200).validate_schem(DeletedStoresOrderModel)

    @allure.title('Get stores inventory /GET')
    def test_get_stores_inventory(self, app: Application):
        """ https://petstore.swagger.io/#/store/getInventory """

        Response(app.store.get_inventory()).assert_status_code(200).validate_schem(StoresInventoryModel)
