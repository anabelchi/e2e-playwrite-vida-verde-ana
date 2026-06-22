from playwright.sync_api import Page, expect

# Definimos una función para ver los productos y sus detalles


def test_ver_produtos_y_detalles(page: Page):
    print("Given el usuario abre la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products")

    print("Then el usuario debe ver el título 'Catálogo de Productos'")
    expect(page.get_by_role("heading", name="Catálogo de Productos")).to_be_visible()

    print("Then el usuario debe ver la categoría del producto 'plantas'")
    expect(page.get_by_text("Plantas").nth(2)).to_be_visible()

    print("and el usuario debe ver el nombre del producto 'Ficus Lyrata'")
    expect(page.get_by_role("heading", name="Ficus Lyrata")).to_be_visible()

    print("and el usuario debe ver el precio del producto '35.00€'")
    expect(page.get_by_text("35.00 €")).to_be_visible()
