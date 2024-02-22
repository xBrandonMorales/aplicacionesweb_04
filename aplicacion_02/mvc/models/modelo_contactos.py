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
               "nombre":"brandon",
                "email":"brandon@gmail.com" 
            },
            {
               "nombre":"miki",
                "email":"mikili@gmail.com" 
            },
            {
               "nombre":"Esmeralda",
                "email":"esme@gmail.com" 
            }
        ]

        return contactos