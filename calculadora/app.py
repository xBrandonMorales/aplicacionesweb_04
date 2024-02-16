"""Framework web.py """
import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.calculadora.Calculadora'
)

app = web.application(urls, globals())

# Punto de entrada
if __name__ == "__main__":
    web.config.debug = False
    app.run()
