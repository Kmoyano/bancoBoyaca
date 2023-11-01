from controller.SucursalDAO import SucursalDAO


class SucursalDTO:
    def __init__(self, idSucursal, nombreSucursal, direccion, telefono, idMunicipio, estado):
        self._idSucursal = idSucursal
        self._nombreSucursal = nombreSucursal
        self._direccion = direccion
        self._telefono = telefono
        self._idMunicipio = idMunicipio
        self._estado = estado

    def consultarSucursal(self):
        sucursal = SucursalDAO.consultarSucursal(self, self._idSucursal)
        if (sucursal == None):
            # mandar a informacion no encontrada
            print("No")
        else:
            # mandar informacion
            print(sucursal)

    def crearSucursal(self):
        sucursal = SucursalDAO.crearSucursal(self, self._idSucursal, self._nombreSucursal, self._direccion,
                                             self._telefono, self._idMunicipio, self._estado)
        if (sucursal == True):
            # manda a vista de creacion exitosa
            print("Si")
        else:
            # manda a vista no creada
            print("NO")

    def deshabilitarSucursal(self):
        sucursal = SucursalDAO.deshabilitarSucursal(self, self._idSucursal, self._estado)
        if (sucursal == True):
            # manda a vista de eliminacion exitosa
            print("Si")
        else:
            # manda a vista de no se elimino
            print("No")

    def actualizarSucursal(self):
        sucursal = SucursalDAO.actualizarSucursal(self, self._idSucursal, self._nombreSucursal, self._direccion,
                                                  self._telefono)
        if (sucursal == True):
            # manda vista de actualizacion exitosa
            print("Si")
        else:
            # manda vista de no se pudo actualizar
            print("No")
