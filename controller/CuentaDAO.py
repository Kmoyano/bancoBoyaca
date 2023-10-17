

from controller.Conexion import Conexion

class CuentaDAO:
    def __init__(self):
        pass

    def consultarCuenta(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT c.numero_cuenta, c.saldo, c.fecha_apertura, c.tasa_interes, c.ultimo_movimiento FROM cuenta AS c"
                       f" WHERE c.numero_cuenta = \"{numeroCuenta}\"")
        lista = cursor.fetchone()
        return lista

    def buscarCuenta(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT numero_cuenta FROM cuenta WHERE numero_cuenta = \"{numeroCuenta}\"")
        buscar = cursor.fetchone()

        if(buscar == numeroCuenta):
            return True
        return False

