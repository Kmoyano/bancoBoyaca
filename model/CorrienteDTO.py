from model.CuentaDTO import CuentaDTO

class CorrienteDTO(CuentaDTO):
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento):
        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento)