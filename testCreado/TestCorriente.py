from model.CorrienteDTO import CorrienteDTO


class TestCorriente:
    def __init__(self):
        self._numeroCuenta = 100
        self._saldo = 1000
        self._fechaApertura = "2023-11-01"
        self._tasaInteres = 13
        self._ultimoMovimiento = "2023-11-01"
        self._idSucursal = 1
        self._idUsuario = 0

        self.corriente = CorrienteDTO(self._numeroCuenta, self._saldo, self._fechaApertura, self._tasaInteres,
                                      self._ultimoMovimiento, self._idSucursal, self._idUsuario)

    def crear(self):
        self.corriente.crearCorriente()  ## PASS

    def buscar(self):
        self.corriente.buscarCorriente()  ## PASS

    def consultar(self):
        self.corriente.consultarCorriente()  ## PASS
