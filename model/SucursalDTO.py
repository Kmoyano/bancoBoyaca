from controller.SucursalDAO import SucursalDAO


class SucursalDTO:
    def __init__(self, idSucursal, nombreSucursal, direccion, telefono, estado):
        self._idSucursal = idSucursal
        self._nombreSucursal = nombreSucursal
        self._direccion = direccion
        self._telefono = telefono
        self._estado = estado

    def consultarSucursal(self):
        sucursal = SucursalDAO.consultarSucursal(self._idSucursal)
        if (sucursal == []):
            # mandar a informacion no encontrada
            pass
        else:
            # mandar informacion
            pass

    def crearSucursal(self):
        sucursal = SucursalDAO.crearSucursal(self._idSucursal, self._nombreSucursal, self._direccion, self._telefono)
        if (sucursal == True):
            # manda a vista de creacion exitosa
            return sucursal
        # manda a vista no creada
        return sucursal

    def deshabilitarSucursal(self):
        sucursal = SucursalDAO.deshabilitarSucursal(self._idSucursal, self._estado)
        if (sucursal == True):
            # manda a vista de eliminacion exitosa
            return sucursal
        # manda a vista de no se elimino
        return sucursal

    def actualizarSucursal(self):
        sucursal = SucursalDAO.actualizarSucursal(self._idSucursal, self._nombreSucursal, self._direccion,
                                                  self._telefono)
        if (sucursal == True):
            # manda vista de actualizacion exitosa
            return sucursal
        # manda vista de no se pudo actualizar
        return sucursal
