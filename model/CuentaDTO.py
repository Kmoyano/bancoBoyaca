class CuentaDTO:
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idSucursal, idUsuario):
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo
        self._fechaApertura = fechaApertura
        self._tasaInteres = tasaInteres
        self._ultimoMovimiento = ultimoMovimiento
        self._idSucursal = idSucursal
        self._idUsuario = idUsuario
