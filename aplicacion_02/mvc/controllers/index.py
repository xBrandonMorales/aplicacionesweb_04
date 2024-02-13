import web
from mvc.models.modelo_index import ModeloIndex

render = web.template.render('mvc/views/', base='layout')

m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            resultado  = m_index.consultarProducto()
            return render.index(resultado)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Upsi algo salio mal"
        