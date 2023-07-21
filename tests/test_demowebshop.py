import allure
from selene import have


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests demowebshop')
@allure.title('Successful auth')
def test_auth(app):
    app.open("")
    with allure.step('Check authentification'):
        app.element(".account").should(have.text("b9@ya.ru"))


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests demowebshop')
@allure.title('Removing a product from the wishlist')
def test_delete_product_from_wishlist(demoshop, app):
    app.open("")
    with allure.step('Add a product to wishlist'):
        demoshop.post("addproducttocart/details/14/2", json={"addtocart_14.EnteredQuantity": '1'})
    with allure.step('Delete a product from wishlist'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests demowebshop')
@allure.title('Removing an item from the cart')
def test_delete_product_from_cart(demoshop, app):
    app.open("")
    with allure.step('Adding an item to the cart'):
        demoshop.post("addproducttocart/catalog/31/1/1")
    with allure.step('Checking if an item has been removed from the cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@allure.label('owner', 'Nikita Alekseev')
@allure.feature('Tests demowebshop')
@allure.title('Logout')
def test_logout(app):
    app.open("")
    with allure.step('Check logout'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
