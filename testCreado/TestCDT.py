from model.CDTDTO import CDTDTO


class TestCDT:
    def __init__(self):
        self._clausula = "X"
        self._retencion = "Y"
        self._fechaFinalizacion = "2023-12-12"
        self._aproxInteres = 100
        self._numeroCuenta = 300
        self._saldo = 100
        self._fechaApertura = "2023-11-01"
        self._tasaInteres = 13
        self._ultimoMovimiento = "2023-11-01"
        self._idSucursal = 1
        self._idUsuario = 0

        self.cdt = CDTDTO(self._clausula, self._retencion, self._fechaFinalizacion, self._aproxInteres,
                          self._numeroCuenta, self._saldo, self._fechaApertura, self._tasaInteres,
                          self._ultimoMovimiento, self._idSucursal, self._idUsuario)

    def crear(self):
        self.cdt.crearCDT()  ## PASS
