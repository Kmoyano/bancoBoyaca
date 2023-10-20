from model.CuentaDTO import CuentaDTO
from controller.CDTDAO import CDTDAO
from controller.CuentaDAO import CuentaDAO

class CDTDTO(CuentaDTO):
    def __init__(self, clausula, retencion, fechaFinalizacion, aproxInteres, numeroCuenta, saldo, fechaApertura,
                 tasaInteres, ultimoMovimiento, idSucursal, idUsuario):

        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idSucursal, idUsuario)

        self._clausula = clausula
        self._retencion = retencion
        self._fechaFinalizacion = fechaFinalizacion
        self._aproxInteres = aproxInteres

    def crearCDT(self):
        cuenta = CuentaDAO.crearCuenta(self._numeroCuenta, self._idSucursal, self._saldo, self._fechaApertura, self._tasaInteres,
                              self._ultimoMovimiento, self._idUsuario)
        if (cuenta == True):
            CDT = CDTDAO.crearCDT(self._numeroCuenta, self._clausula, self._retencion, self._fechaFinalizacion, self._aproxInteres)
            if (CDT == True):
                return True
        return False

    def calcularSinGuardarCDT(self):
        pass

    def calculoCDT(self):
        pass
