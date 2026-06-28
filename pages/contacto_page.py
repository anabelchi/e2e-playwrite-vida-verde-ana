from playwright.sync_api import Page, expect


class ContactoPage:

    def __init__(self, page: Page):
        self.page = page  # Esto nos dice que está usando la página de productos - Es un estándar
        # Establecemos la url como una variable
        self.url = "https://web-qa.dev.adalab.es/contact"

    def visitar_contacto(self):
        self.page.goto("https://web-qa.dev.adalab.es/contact")

    def rellenar_nombre(self, nombre):
        self.page.get_by_role("textbox", name="Nombre *").fill(nombre)

    def rellenar_email(self, email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def rellenar_mensaje(self, mensaje):
        self.page.get_by_role("textbox", name="Mensaje *").fill(mensaje)

    def enviar_formulario(self):
        self.page.get_by_role("button", name="Enviar Mensaje").click()

    def verificar_mensaje_error(self):
        expect(self.page.get_by_text(
            "El formato del email no es válido")).to_be_visible()

    def verificar_mensaje_exito_contacto(self):
        expect(self.page.get_by_role(
            "heading", name="¡Mensaje enviado con éxito!")).to_be_visible()

    def verificar_email_obligatorio(self):
        expect(self.page.get_by_text("El email es obligatorio")).to_be_visible()
