import web

class ModeloIndex():
    def __init__(self):
        pass

    def consultarProducto(self):
        # conecion con BD
        # ejecutar la consulta
        # generar un json con los datos
        datos = (
            "Laptop HP",
            "Mouse Logitech",
            "Tableta 7",
            "HUB USB C",
            "Otro valor"
        )

        return datos