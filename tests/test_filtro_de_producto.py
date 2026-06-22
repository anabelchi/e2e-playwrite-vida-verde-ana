from playwright.sync_api import Page, expect

# Definimos una función que filtre por nombre, precio y categoría con resultados


def test_filtrar_con_resultados(page: Page):
    print("Given el usuario abre la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products/")

    print("When filtra por nombre 'Sanse'")
    # Escribe Sanse en la caja Nombre
    page.get_by_role("searchbox", name="Nombre").fill("sanse")

    print("And filtra por categoria 'Plantas'")
    # Selecciona la categoría Plantas
    page.get_by_label("CategoríaTodas las categorí").select_option("Plantas")

    print("And filtra por precio minimo '10'")
    # Precio mínimo 10€
    page.get_by_role("spinbutton", name="Precio mínimo").fill("10")

    print("And filtra por precio máximo '25'")
    page.get_by_role("spinbutton", name="Precio máximo").fill("25")

    print("Then debe ver el producto 'Sansevieria'")
    expect(page.get_by_role("heading", name="Sansevieria")).to_be_visible()

    print("And debe ver la categoria 'Plantas'")
    expect(page.get_by_role("article").get_by_text("Plantas")).to_be_visible()

    print("And debe ver el precio 22'")
    expect(page.get_by_text("€")).to_be_visible()

# Definimos una función que filtre por nombre de producto sin resultado


def test_filtrar_sin_resultado(page: Page):
    print("Given la usuaria visita la página de productos 'https://web-qa.dev.adalab.es/products'")
    page.goto("https://web-qa.dev.adalab.es/products/")

    print("When filtra por nombre no existente “Test”")
    page.get_by_role("searchbox", name="Nombre").fill("test")

    print("Then ve el mensaje no se encontraron productos")
    expect(page.get_by_text("No se encontraron productos")).to_be_visible()
