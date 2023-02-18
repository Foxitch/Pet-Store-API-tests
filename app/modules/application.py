import os

from dotenv import load_dotenv

from app.modules.pet import PetModule
from app.modules.store import StoreModule
from app.src.base_classes.common import Common


load_dotenv()


class Application:

    def __init__(self):
        self.common = Common(os.getenv('BASE_URL'))
        self.pet = PetModule(self)
        self.store = StoreModule(self)
