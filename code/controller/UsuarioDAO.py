from controller.Conexion import Conexion


class UsuarioDAO:
    def __init__(self):
        pass

    def consultarUsuario(self, cedula, contraseña):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"SELECT * FROM usuario WHERE cedula = \"{cedula}\" AND constaseña = \"{contraseña}\"")
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
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"UPDATE usuario"
                       f" SET nombre = {nombre}, apellidos = {apellido}, direccion = {direccion}, telefono = {telefono},"
                       f" correo = {correo}, contraseña = {contraseña}, rol = {rol}, fecha_nacimiento = {fechaNacimeinto},"
                       f" fecha_expedicion = {fechaExpedicion} WHERE cedula = \"{cedula}\"")
        cdb.commit()

        return True

    def deshabilitarUsuario(self, cedula, estado):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"UPDATE usuario"
                       f" SET estado = \"{estado}\""
                       f" WHERE cedula = \"{cedula}\"")
        cdb.commit()

        return True

    def crearUsuario(self, cedula, nombre, apellido, direccion, telefono, correo, contraseña, rol, fechaNacimiento,
                     fechaExpedicion, estado, idMunicipio):
        conexion = Conexion()
        cdb = conexion.conectarBD()
        cursor = cdb.cursor()
        cursor.execute(f"INSERT INTO usuario (cedula, nombre, apellidos, direccion, telefono, correo, constraseña, rol,"
                       f" id_municipio_usuario, fecha_naciemiento, fecha_expedicion, estado)"
                       f" VALUES (\"{cedula}\", \"{nombre}\", \"{apellido}\", \"{direccion}\", \"{telefono}\", \"{correo}\","
                       f" \"{contraseña}\", \"{rol}\", \"{idMunicipio}\", \"{fechaNacimiento}\", \"{fechaExpedicion}\", \"{estado}\")")
        cdb.commit()
        return True
