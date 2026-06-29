from playwright.sync_api import Page, expect


class ProductosPage:

    def __init__(self, page: Page):
        self.page = page  # Esto nos dice que está usando la página de productos - Es un estándar
        # Establecemos la url como una variable
        self.url = "https://web-qa.dev.adalab.es/products"

    def visitar_productos(self):
        self.page.goto(self.url)

    def verificar_titulo(self):
        expect(self.page.get_by_role(
            "heading", name="Catálogo de Productos")).to_be_visible()

    def verificar_categoria(self, categoria):
        expect(self.page.get_by_text(categoria).nth(2)).to_be_visible()

    def verificar_nombre_producto(self, nombre):
        expect(self.page.get_by_role("heading", name=nombre)).to_be_visible()

    def verificar_precio_producto(self, precio):
        expect(self.page.get_by_text(precio)).to_be_visible()

    def verificar_mensaje_sin_resultados(self):
        expect(self.page.get_by_text(
            "No se encontraron productos")).to_be_visible()

    def filtrar_por_nombre(self, nombre):
        self.page.get_by_role("searchbox", name="Nombre").fill(nombre)

    def filtrar_por_categoria(self, categoria):
        self.page.get_by_label("Categoría").select_option(categoria)

    def filtrar_por_precio_minimo(self, precio_minimo):
        self.page.get_by_role(
            "spinbutton", name="Precio mínimo").fill(precio_minimo)

    def filtrar_por_precio_maximo(self, precio_maximo):
        self.page.get_by_role(
            "spinbutton", name="Precio máximo").fill(precio_maximo)

    def agregar_al_carrito(self):
        self.page.get_by_role(
            "button", name="Añadir Juego de Palas al").click()

    def finalizar_compra(self):
        self.page.get_by_role("link", name="Finalizar Compra").click()
