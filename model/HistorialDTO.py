class HistorialDTO:
    def __init__(self, numeroCuenta, saldo, movimiento, fechaMovimiento, descripcion):
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo
        self._movimiento = movimiento
        self._fechaMovimiento = fechaMovimiento
        self._descripcion = descripcion