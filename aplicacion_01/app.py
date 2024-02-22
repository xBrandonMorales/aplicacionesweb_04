import web

urls = (
    '/', 'hello',
    "/pagina2", "pagina2"
)
app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'HOli guapa'


class pagina2:
    def GET(self):
        return "Hola amigo"

if __name__ == "__main__":
    app.run()
