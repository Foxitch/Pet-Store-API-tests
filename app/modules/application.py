import os

from dotenv import load_dotenv

from app.modules.pet_module import PetModule
from app.modules.store_module import StoreModule
from app.modules.user_module import UserModule
from app.src.base_classes.ApiBase import ApiBase


load_dotenv()


class Application:

    def __init__(self):
        self.api_base = ApiBase(os.getenv('BASE_URL'))
        self.pet = PetModule(self)
        self.store = StoreModule(self)
        self.user = UserModule(self)
