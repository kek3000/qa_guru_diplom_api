import allure
from pytest_voluptuous import S

from schemas.schemas import *


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Create user')
def test_create_user(reqres):
    created_user = reqres.post("api/users", {"name": "Nikita", "job": "Tester"})

    assert created_user.status_code == 201
    assert S(create_user) == created_user.json()
    assert created_user.json()["name"] == "Nikita"
    assert created_user.json()["job"] == "Tester"


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Update user by put')
def test_update_user_by_put(reqres):
    update_user = reqres.put("api/users/2", {"name": "nikitaalekseev", "job": "aqa"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "nikitaalekseev"
    assert update_user.json()["job"] == "aqa"


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Update user by patch')
def test_update_user_by_patch(reqres):
    update_user = reqres.put("api/users/2", {"name": "Alekseev", "job": "sdet"})

    assert update_user.status_code == 200
    assert S(create_update_user) == update_user.json()
    assert update_user.json()["name"] == "Alekseev"
    assert update_user.json()["job"] == "sdet"


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Delete user')
def test_delete_user(reqres):
    delete_user = reqres.delete("api/users/2")

    assert delete_user.status_code == 204


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Successful register')
def test_successful_register(reqres):
    user_register = reqres.post("api/register", {"email": "eve.holt@reqres.in", "password": "pistol"})

    assert user_register.status_code == 200
    assert S(register_user) == user_register.json()
    assert user_register.json()['id']
    assert user_register.json()['token']


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful register')
def test_unsuccessful_register(reqres):
    user_register = reqres.post("api/register", {"email": "b9@ya.ru"})

    assert user_register.status_code == 400
    assert S(unregister_user) == user_register.json()
    assert user_register.json()['error'] == 'Missing password'
