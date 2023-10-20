from model.CuentaDTO import CuentaDTO

class CreditoDTO(CuentaDTO):
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento):
        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, )
