from model.CuentaDTO import CuentaDTO

class CDTDTO(CuentaDTO):
    def __init__(self, clausula, retencion, fechaFinalizacion, aproxInteres, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento):

        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento)

        self._clausula = clausula
        self._retencion = retencion
        self._fechaFinalizacion = fechaFinalizacion
        self._aproxInteres = aproxInteres