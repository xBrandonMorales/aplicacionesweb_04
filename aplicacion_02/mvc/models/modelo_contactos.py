import web

class ModeloContactos():
    def __init__(self):
        pass

    def consultarContactos(self):
        contactos = [
            {
                "nombre":"Salvador",
                "email":"salvador@gmail.com"
            },
            {
               "nombre":"Aldo",
                "email":"aldo@gmail.com" 
            },
            {
               "nombre":"Tania",
                "email":"tania@gmail.com" 
            },
            {
               "nombre":"Evelyn",
                "email":"evelyn@gmail.com" 
            }
        ]

        return contactos