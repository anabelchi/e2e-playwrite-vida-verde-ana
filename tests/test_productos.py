from playwright.sync_api import Page, expect

from pages.productos_page import ProductosPage

# Definimos una función para ver los productos y sus detalles


def test_ver_produtos_y_detalles(page: Page):

    productos_page = ProductosPage(page)

    print("Given la usuaria abre la página de productos 'https://web-qa.dev.adalab.es/products'")
    productos_page.visitar_productos()

    print("Then la usuaria debe ver el título 'Catálogo de Productos'")
    productos_page.verificar_titulo()

    print("Then la usuariao debe ver la categoría del producto 'plantas'")
    productos_page.verificar_categoria("Plantas")

    print("and la usuaria debe ver el nombre del producto 'Ficus Lyrata'")
    productos_page.verificar_nombre_producto("Ficus Lyrata")

    print("and la usuaria debe ver el precio del producto '35.00€'")
    productos_page.verificar_precio_producto("35.00 €")
