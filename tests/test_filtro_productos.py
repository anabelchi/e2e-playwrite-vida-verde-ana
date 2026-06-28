from playwright.sync_api import Page, expect

from pages.productos_page import ProductosPage

# Definimos una función que filtre por nombre, precio y categoría con resultados


def test_filtrar_con_resultados(page: Page):

    productos_page = ProductosPage(page)

    print("Given el usuario abre la página de productos 'https://web-qa.dev.adalab.es/products'")
    productos_page.visitar_productos()

    print("When filtra por nombre 'Sanse'")
    productos_page.filtrar_por_nombre("Sanse")

    print("And filtra por categoria 'Plantas'")
    productos_page.filtrar_por_categoria("Plantas")

    print("And filtra por precio minimo '10'")
    productos_page.filtrar_por_precio_minimo("10")

    print("And filtra por precio máximo '25'")
    productos_page.filtrar_por_precio_maximo("25")

    print("Then debe ver el producto 'Sansevieria'")
    productos_page.verificar_nombre_producto("Sansevieria")

    print("And debe ver la categoria 'Plantas'")
    productos_page.verificar_categoria("Plantas")

    print("And debe ver el precio 22.00 €'")
    productos_page.verificar_precio_producto("22.00 €")

# Definimos una función que filtre por nombre de producto sin resultado


def test_filtrar_sin_resultado(page: Page):

    productos_page = ProductosPage(page)

    print("Given la usuaria visita la página de productos 'https://web-qa.dev.adalab.es/products'")
    productos_page.visitar_productos()

    print("When filtra por nombre no existente “Test”")
    productos_page.filtrar_por_nombre("test")

    print("Then ve el mensaje 'No se encontraron productos")
    productos_page.verificar_mensaje_sin_resultados()
