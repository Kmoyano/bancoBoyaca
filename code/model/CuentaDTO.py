class CuentaDTO:
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento):
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo
        self._fechaApertura = fechaApertura
        self._tasaInteres = tasaInteres
        self._ultimoMovimiento = ultimoMovimiento
