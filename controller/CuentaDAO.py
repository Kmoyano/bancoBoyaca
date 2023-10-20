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

    def buscarCuenta(self, idUsuario):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT numero_cuenta FROM cuenta WHERE id_usuario_cuenta = \"{idUsuario}\"")
        buscar = cursor.fetchall()

        if(buscar == []):
            return False
        return buscar

    def crearCuenta(self, numeroCuenta, idSucursal, saldo, fechaApertura, tasaInteres, ultimoMovimiento, idUsuario):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"INSERT INTO cuenta (numero_cuenta, id_sucursal_cuenta, saldo, fecha_apertura, tasa_interes,"
                       f" ultimo_movimiento, id_usuario_cuenta) VALUES \"{numeroCuenta}\", \"{idSucursal}\", \"{saldo}\","
                       f" \"{fechaApertura}\", \"{tasaInteres}\", \"{ultimoMovimiento}\", \"{idUsuario}\"")
        cursor.commit()

