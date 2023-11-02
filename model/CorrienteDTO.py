from controller.CorrienteDAO import CorrienteDAO
from controller.CuentaDAO import CuentaDAO
from model.CuentaDTO import CuentaDTO


class CorrienteDTO(CuentaDTO):
    def __init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento):
        CuentaDTO.__init__(self, numeroCuenta, saldo, fechaApertura, tasaInteres, ultimoMovimiento)

    def crearCorriente(self):
        cuenta = CuentaDAO.crearCuenta(self, self._numeroCuenta, self._idSucursal, self._saldo, self._fechaApertura,
                                       self._tasaInteres, self._ultimoMovimiento, self._idUsuario)
        if (cuenta):
            corriente = CorrienteDAO.crearCorriente(self, self._numeroCuenta)
            if (corriente):
                # se creo correctamente la cuenta corriente
                print("Si")
            else:
                # No se creo
                print("No")
        else:
            print("no cuenta")

    def buscarCorriente(self):
        corriente = CorrienteDAO.buscarCorriente(self, self._numeroCuenta)
        if (corriente == False):
            # No encontrado
            print("No")
        else:
            print(corriente)

    def consultarCorriente(self):
        cuenta = CuentaDAO.consultarCuenta(self, self._numeroCuenta)
