from playwright.sync_api import Page, expect

from pages.contacto_page import ContactoPage

# Definimos una función que valide el envío del formulario con campos obligatorios válidos


def test_campos_obligatorios_validos(page: Page):

    contacto_page = ContactoPage(page)

    print("Given la usuaria abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre con 'Elena Nito del Bosque'")
    contacto_page.rellenar_nombre("Elena Nito del Bosque")

    print("And rellena el campo email con 'test@gmail.com'")
    contacto_page.rellenar_email("test@gmail.com")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el formulario")
    contacto_page.enviar_formulario()

    print("Then debe ver un mensaje de éxito")
    expect(page.get_by_role(
        "heading", name="¡Mensaje enviado con éxito!")).to_be_visible()

# Definimos una función que valide el envío del formulario con el campo email inválido


def test_email_invalido(page: Page):

    contacto_page = ContactoPage(page)

    print("Given la usuaria abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre con 'Elena Nito Del Bosque'")
    contacto_page.rellenar_nombre("Elena Nito Del Bosque")

    print("And rellena el campo email con 'test'")
    contacto_page.rellenar_email("test")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el formulario")
    contacto_page.enviar_formulario()

    print("Then debe ver un mensaje de error")
    contacto_page.verificar_mensaje_error()

# Definimos una función que valide el envío del formulario con el campo email vacío


def test_email_vacio(page: Page):

    contacto_page = ContactoPage(page)

    print("Given la usuaria abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    contacto_page.visitar_contacto()

    print("When rellena el campo nombre con 'Elena Nito del Bosque'")
    contacto_page.rellenar_nombre("Elena Nito del Bosque")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    contacto_page.rellenar_mensaje("Mensaje de prueba")

    print("And envia el formulario")
    contacto_page.enviar_formulario()

    print("Then debe ver un mensaje de error")
    contacto_page.verificar_email_obligatorio()
