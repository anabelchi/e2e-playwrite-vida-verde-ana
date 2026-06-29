from playwright.sync_api import Page, expect


class ConfirmacionPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/confirmation"

    def verificar_mensaje_exito(self, mensaje):
        expect(self.page.get_by_role(
            "heading", name=mensaje)).to_be_visible()

    def verificar_no_mensaje_exito(self, mensaje):
        expect(self.page.get_by_text(mensaje)).not_to_be_visible()

    def verificar_nombre_del_producto(self, nombre):
        expect(self.page.get_by_text(nombre)).to_be_visible()

    def verificar_precio_del_producto(self, precio):
        expect(self.page.get_by_role("listitem").filter(
            has_text=precio).locator("data")).to_be_visible()

    def verificar_subtotal(self, subtotal):
        expect(self.page.get_by_role("definition").filter(
            has_text=subtotal).locator("data")).to_be_visible()

    def verificar_iva(self, iva):
        expect(self.page.get_by_role("definition").filter(
            has_text=iva).locator("data")).to_be_visible()

    def verificar_coste_envio(self, envio):
        expect(self.page.get_by_role("definition").filter(
            has_text=envio).locator("data")).to_be_visible()

    def verificar_total(self, total):
        expect(self.page.get_by_role("definition").filter(
            has_text=total).locator("data")).to_be_visible()

    def ir_al_inicio(self):
        self.page.get_by_role("link", name="Ir al Inicio", exact=True).click()
