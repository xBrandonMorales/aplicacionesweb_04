import web

render = web.template.render('mvc/views/')

class Index:
    def GET(self):
        try:
            return render.indece()
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Upsi algo salio mal"
        