import random
from datetime import datetime

from faker import Faker
from app.src.generated_data.data import PetData, StoreData, UserData

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_pet_data():
    status = ['available', 'pending', 'sold']

    yield PetData(
        name=faker_en.first_name(),
        status=random.choice(status)
    )


def generated_store_data():
    yield StoreData(
        petId=random.randint(1, 1000),
        quantity=random.randint(1, 10),
        shipDate=datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        status=faker_en.word(),
        complete=random.choice([True, False])
    )


def generated_user_data():
    yield UserData(
        username=faker_en.user_name(),
        firstName=faker_en.first_name(),
        lastName=faker_en.last_name(),
        email=faker_en.email(),
        password=faker_en.password(),
        phone=faker_en.phone_number(),
        userStatus=random.randint(1, 10)
    )
