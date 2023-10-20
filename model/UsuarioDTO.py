import hashlib

from controller.UsuarioDAO import UsuarioDAO

class UsuarioDTO:
    def __init__(self, cedula, nombre, apellido, direccion, telefono, correo, contraeña, rol, idMunicipio,
                 fechaNacimiento, fechaExpedicion, estado):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._contaseña = contraeña
        self._rol = rol
        self._idMunicipio = idMunicipio
        self._fechaNacimiento = fechaNacimiento
        self._fechaExpedicion = fechaExpedicion
        self._estado = estado


    def autenticarUsuarios(self):
        contraseña = self.encriptarContraseña()

        usuario = UsuarioDAO.consultarUsuario(self._cedula, contraseña)
        rolusuario = usuario[7]
        if(rolusuario == "usuario"):
            ## ir a vista usuario
            pass
        elif(rolusuario == "administrador"):
            ## ir a Vista administrador
            pass
        ## mandar mensaje de no rol no encontrado


    def crearUsuario(self):
        contraseña = self.encriptarContraseña()

        usuario = UsuarioDAO.crearUsuario(self._cedula, self._nombre, self._apellido, self._direccion, self._telefono,
                                          self._correo, contraseña, self._rol, self._fechaNacimiento,
                                        self._fechaExpedicion, self._estado, self._idMunicipio)

        if (usuario == True):
            # ir a usuario se creo
            pass
            # ir a usuario no se creo

    def deshavilitarUsuario(self):
        usuario = UsuarioDAO.deshabilitarUsuario(self._cedula, self._estado)
        if (usuario == True):
            # ir a usuario eliminado
            pass
        # ir a usuario no actualizado

    def actualizarUsuario(self):
        usuario = UsuarioDAO.actualizarUsuario(self._cedula, self._nombre, self._apellido, self._direccion, self._telefono,
                                          self._correo, self._contaseña, self._rol, self._fechaNacimiento, self._fechaExpedicion)

        if (usuario == True):
            # ir a usuario eliminado
            pass
        # ir a usuario no actualizado

    def encriptarContraseña(self):
        contraseñaSTR = str(self._contaseña)
        contrasenaeEncriptada = hashlib.sha256(contraseñaSTR.encode()).hexdigest()
        return contrasenaeEncriptada
