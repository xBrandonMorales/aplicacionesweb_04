import web

render = web.template.render('mvc/views/')

class Contactos:
    def GET(self):
        try:
            return render.contactos()
        except Exception as e:
            print(f"Error 102 - contactos {e.args}")
            return "Upsi algo salio mal"