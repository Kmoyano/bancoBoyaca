from model.SucursalDTO import SucursalDTO


class TestSucursal:
    def __init__(self):
        self._idSucursal = 4
        self._nombreSucursal = "Banco el Bosque Tunja"
        self._direccion = "carrera 11, calle 10, numero 10"
        self._telefono = 7983918
        self._idMunicipio = 15001
        self._estado = "activo"
        self.sucursal = SucursalDTO(self._idSucursal, self._nombreSucursal, self._direccion, self._telefono,
                                    self._idMunicipio, self._estado)

    def conusltar(self):
        self.sucursal.consultarSucursal()  # PASS

    def crear(self):
        self.sucursal.crearSucursal()  # PASS

    def estado(self):
        self.sucursal.deshabilitarSucursal()  # PASS

    def actualizar(self):
        self.sucursal.actualizarSucursal()  # PASS
