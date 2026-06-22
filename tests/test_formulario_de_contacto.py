from playwright.sync_api import Page, expect

# Definimos una función que valide el envío del formulario con campos obligatorios válidos


def test_campos_obligatorios_validos(page: Page):
    print("Given el usuario abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre con 'Reyes Cuesta'")
    page.get_by_role("textbox", name="Nombre *").fill("Reyes Cuesta")

    print("And rellena el campo email con 'test@gmail.com'")
    page.get_by_role("textbox", name="Email *").fill("test@gmail.com")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")

    print("And envia el formulario")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then debe ver un mensaje de éxito")
    expect(page.get_by_role(
        "heading", name="¡Mensaje enviado con éxito!")).to_be_visible()
    expect(page.get_by_text(
        "Gracias por contactarnos. Te responderemos lo antes posible")).to_be_visible()

# Definimos una función que valide el envío del formulario con el campo email inválido


def test_email_invalido(page: Page):
    print("Given el usuario abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre con 'Reyes Cuesta'")
    page.get_by_role("textbox", name="Nombre *").fill("Reyes Cuesta")

    print("And rellena el campo email con 'test'")
    page.get_by_role("textbox", name="Email *").fill("test")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")

    print("And envia el formulario")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("El formato del email no es válido")).to_be_visible()


# Definimos una función que valide el envío del formulario con el campo email vacío

def test_email_vacio(page: Page):
    print("Given el usuario abre la página de contacto 'https://web-qa.dev.adalab.es/contact'")
    page.goto("https://web-qa.dev.adalab.es/contact")

    print("When rellena el campo nombre con 'Reyes Cuesta'")
    page.get_by_role("textbox", name="Nombre *").fill("Reyes Cuesta")

    print("And rellena el campo mensaje con 'Mensaje de prueba'")
    page.get_by_role("textbox", name="Mensaje *").fill("Mensaje de prueba")

    print("And envia el formulario")
    page.get_by_role("button", name="Enviar Mensaje").click()

    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("El email es obligatorio")).to_be_visible()
