from controller.Conexion import Conexion

class CreditoDTO:
    def __init__(self):
        pass

    def crearCorriente(self, numeroCuneta):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"INSERT INTO creditos (numero_cuenta) VALUES = \"{numeroCuneta}\"")
            cursor.commit()
            return True
        except Exception as e:
            return False

    def buscarCorriente(self, numeroCuenta):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT * FROM creditos WHERE numero_cuenta = \"{numeroCuenta}\"")
        buscar = cursor.fetchone()

        if (buscar == []):
            return False
        return buscar