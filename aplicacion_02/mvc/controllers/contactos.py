import web
from mvc.models.modelo_contactos import ModeloContactos

render = web.template.render('mvc/views/', base='layout')

m_contactos = ModeloContactos()

class Contactos:
    def GET(self):
        try:
            resultado = m_contactos.consultarContactos()
            return render.contactos(resultado)
        except Exception as e:
            print(f"Error 102 - Contactos {e.args}")
            return "Upsi algo salio mal"
