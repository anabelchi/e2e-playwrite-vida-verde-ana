from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/checkout"

    def verificar_resumen_de_pedido(self):
        expect(self.page.get_by_role(
            "heading", name="Resumen del Pedido")).to_be_visible()

    def verificar_nombre_del_producto(self, nombre):
        expect(self.page.get_by_role("listitem").filter(
            has_text=nombre)).to_be_visible()

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

    def verificar_mensaje_tarjeta_erronea(self, mensaje_tarjeta_error):
        expect(self. page.get_by_text(mensaje_tarjeta_error)).to_be_visible()

    def rellenar_nombre(self, nombre):
        self.page.get_by_role(
            "textbox", name="Nombre Completo *").fill(nombre)

    def rellenar_email(self, email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def rellenar_dirección(self, direccion):
        self.page.get_by_role(
            "textbox", name="Dirección *").fill(direccion)

    def rellenar_tarjeta_credito(self, tarjeta_num):
        self.page.get_by_role(
            "textbox", name="Número de Tarjeta de Crédito *").fill(tarjeta_num)

    def completar_compra(self):
        self.page.get_by_role("button", name="Completar Compra").click()
