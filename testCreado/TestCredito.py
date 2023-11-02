from model.CreditoDTO import CreditoDTO


class TestCredito:
    def __init__(self):
        self._numeroCuenta = 200
        self._saldo = 1000
        self._fechaApertura = "2023-11-01"
        self._tasaInteres = 13
        self._ultimoMovimiento = "2023-11-01"
        self._idSucursal = 1
        self._idUsuario = 0

        self.credito = CreditoDTO(self._numeroCuenta, self._saldo, self._fechaApertura, self._tasaInteres,
                                  self._ultimoMovimiento, self._idSucursal, self._idUsuario)

    def crear(self):
        self.credito.crearCredito()  ## PASS

    def buscar(self):
        self.credito.buscarCredito()  ## PASS

    def consultar(self):
        self.credito.consultarCredito()  ## PASS
