import web

render = web.template.render('mvc/views/')

class Productos:
    def GET(self):
        try:
            return render.productos()
        except Exception as e:
            print(f"Error 103 - productos {e.args}")
            return "algo ocurrio"