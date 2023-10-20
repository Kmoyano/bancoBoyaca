from controller.Conexion import Conexion

class CDTDAO:
    def __init__(self):
        pass

    def crearCDT(self, numeroCuenta, clausula, retencion, fechaFinalizacion, aproxInteres):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"INSERT INTO cdt (numero_cuenta, clausula, retencion, fecha_finalizacion, aprox_interes)"
                           f" VALUES = \"{numeroCuenta}\", \"{clausula}\", \"{retencion}\", \"{fechaFinalizacion}\","
                           f" \"{aproxInteres}\"")
            cursor.commit()
            return True
        except Exception as e:
            return False

    def buscarCDT(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT * FROM cdt WHERE numero_cuenta = \"{numeroCuenta}\"")
        buscar = cursor.fetchone()

        if (buscar == []):
            return False
        return buscar