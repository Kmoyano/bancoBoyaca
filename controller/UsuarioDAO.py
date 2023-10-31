from controller.Conexion import Conexion


class UsuarioDAO:
    def __init__(self):
        return

    def consultarUsuario(self, cedula, contraseña):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT * FROM usuario WHERE cedula = \"{cedula}\" AND contrasena = \"{contraseña}\"")
        buscar = cursor.fetchone()
        return buscar

    def buscarUsuario(self, cedula):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT cedula FROM usuario WHERE cedula = \"{cedula}\"")
        buscar = cursor.fetchone()

        if (buscar == cedula):
            return True
        return False

    def actualizarUsuario(self, cedula, nombre, apellido, direccion, telefono, correo, contraseña, rol, fechaNacimeinto,
                          fechaExpedicion):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"UPDATE usuario"
                           f" SET nombres = \"{nombre}\", apellidos = \"{apellido}\", direccion = \"{direccion}\", telefono = \"{telefono}\","
                           f" correo = \"{correo}\", contrasena = \"{contraseña}\", rol = \"{rol}\", fecha_nacimiento = \"{fechaNacimeinto}\","
                           f" fehca_expedicion = \"{fechaExpedicion}\" WHERE cedula = \"{cedula}\"")
            cdb.commit()
            return True
        except Exception as e:
            return False

    def deshabilitarUsuario(self, cedula, estado):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(f"UPDATE usuario"
                           f" SET estado = \"{estado}\""
                           f" WHERE cedula = \"{cedula}\"")
            cdb.commit()
            return True
        except Exception as e:
            return False

    def crearUsuario(self, cedula, nombre, apellido, direccion, telefono, correo, contraseña, rol, fechaNacimiento,
                     fechaExpedicion, estado, idMunicipio):
        try:
            conexion = Conexion()
            cdb = conexion.conectarBD()
            cursor = cdb.cursor()
            cursor.execute(
                f"INSERT INTO usuario (cedula, nombres, apellidos, direccion, telefono, correo, contrasena, rol,"
                f" id_municipio_usuario, fecha_nacimiento, fehca_expedicion, estado)"
                f" VALUES (\"{cedula}\", \"{nombre}\", \"{apellido}\", \"{direccion}\", \"{telefono}\", \"{correo}\","
                f" \"{contraseña}\", \"{rol}\", \"{idMunicipio}\", \"{fechaNacimiento}\", \"{fechaExpedicion}\", \"{estado}\")")
            cdb.commit()
            return True  # usuario creado satisfactoriamente
        except Exception as e:
            return False  # usuario no se creo
