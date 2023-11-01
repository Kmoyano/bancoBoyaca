from model.UsuarioDTO import UsuarioDTO


class TestUsuario:
    # Variables

    def __init__(self):
        self._cedula = 0
        self._nombre = "usuario1"
        self._apellido = "apellido1"
        self._direccion = "direccion"
        self._telefono = 300000
        self._correo = "correo@correo.com"
        self._contaseña = 1234
        self._rol = "usuario"
        self._idMunicipio = 15238
        self._fechaNacimiento = "2002-03-21"
        self._fechaExpedicion = "2020-08-03"
        self._estado = "activo"
        self.usuario = UsuarioDTO(self._cedula, self._nombre, self._apellido, self._direccion, self._telefono,
                                  self._correo, self._contaseña, self._rol, self._idMunicipio, self._fechaNacimiento,
                                  self._fechaExpedicion, self._estado)

    def autenticar(self):
        self.usuario.autenticarUsuarios()  ## PASS

    def crear(self):
        self.usuario.crearUsuario()  ## PASS

    def deshavilitar(self):
        self.usuario.deshavilitarUsuario()  ## PASS

    def actualizar(self):
        self.usuario.actualizarUsuario()  ## PASS
