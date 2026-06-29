from playwright.sync_api import Page, expect


class InicioPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://web-qa.dev.adalab.es/"

    def verificar_url(self, url):
        expect(self.page).to_have_url(url)

    def verificar_titulo_heading(self, titulo):
        expect(self.page.get_by_role("heading", name=titulo)).to_be_visible()

    def verificar_titulo_pagina(self, titulo_pagina):
        expect(self.page).to_have_title(titulo_pagina)

    def verificar_boton_ver_productos(self, nombre_boton):
        expect(self.page.get_by_role("link", name=nombre_boton)).to_be_visible()
