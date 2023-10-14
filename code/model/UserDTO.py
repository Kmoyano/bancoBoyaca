class UserDTO:
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
