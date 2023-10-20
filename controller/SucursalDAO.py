from controller.Conexion import Conexion


class SucursalDAO:
    def __init__(self):
        pass

    def consultarSucursal(self, idSucursal):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT * FROM sucursal WHERE id_sucursal = {idSucursal}")
        buscar = cursor.fetchone()

        return buscar

    def buscarSucursal(self, idSucursal):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT id_sucursal FROM sucursal WHERE id_sucursal = {idSucursal}")
        buscar = cursor.fetchone()

        if (buscar == idSucursal):
            return True
        return False

    def crearSucursal(self, idSucursal, nombreSucursal, direccion, telefono):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(
                f"INSERT INTO sucursal (id_sucursal, nombre_sucursal, direccion, telefono, id_municipio_sucursal)"
                f" VALUES (\"{idSucursal}\", \"{nombreSucursal}\", \"{direccion}\", \"{telefono}\")")
            cdb.commit()
            return True
        except Exception as e:
            return False


    def deshabilitarSucursal(self, idSucursal, estado):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"UPDATE sucursal"
                           f" SET estado = \"{estado}\""
                           f" where id_sucursal = {idSucursal}")
            cdb.commit()
            return True
        except Exception as e:
            return False

    def actualizarSucursal(self, idSucursal, nombreSucursal, direccion, telefono):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"UPDATE sucursal"
                           f" SET nombre_sucursal = \"{nombreSucursal}\", direccion = \"{direccion}\", telefono = \"{telefono}\""
                           f" WHERE id_sucursal = \"{idSucursal}\"")
            cdb.commit()
            return True
        except Exception as e:
            return False
