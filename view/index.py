from fastapi import Request

from view.templates import templates

def principalView(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={
            "request":request
        }
    )


# Crear usuario
def register_User(request: Request):
    return templates.TemplateResponse(
        "registro.html",
        context={
            "request": request,
            "cedula":cedulaUsuario,
            "nombre": nombreUsuario,
            "apellido":apeliidosUsuario,
            "direccion":direccion,
            "telefono":telefono,
            "correo":correo,
            "contraseña":contraseña,
            "rol": rol,
            "fechaNacimiento":fechaNacimiento,
            "fechaExpedicion": fechaExpedicion,
            "estado":estado,
            "idMunicipio":municipio,
        }
    )

#Actualizar Usuario
def update_User(request:Request):
    return templates.TemplateResponse(
        "actualizarUsuario.html",
        context={
            "request":request,
            "cedula": cedula,
            "nombre": nombreUsuario,
            "apellido": apeliidosUsuario,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "contraseña": contraseña,
            "rol": rol,
            "fechaNacimiento": fechaNacimiento,
            "fechaExpedicion": fechaExpedicion,
            "estado": estado,
            "idMunicipio": municipio,
        }
    )
#Deshabilitar Usuario
def disable_User(request: Request, listaUsuarios):
    return templates.TemplateResponse(
        "deshabilitarUsuario.html",
        context={
            request:request,
            "id_usuarios": listaUsuarios,
            "estado":estado,
        }
    )

#Emergente Crear Usuario
def emergenteRegisterUser(request: Request):
    return templates.TemplateResponse(
        "emergenteCrearUsuario.html",
        context={
            "request": request
        }
    )
#Crear Sucursal
def register_Sucursal(request: Request):
    return templates.TemplateResponse(
        "crearSucursal.html",
        context={
            "request": request,
            "idSucursal": idSucursal,
            "nombreSucursal":nombreSucursal,
            "direccion":direccion,
            "telefono":telefono,
        }
    )
#Actualizar Sucursal
def update_Sucursal(request: Request):
    return templates.TemplateResponse(
        "actualizarSucursal.html",
        context={
            "request": request,
            "idSucursal": idSucursal,
            "nombreSucursal":nombreSucursal,
            "direccion":direccion,
            "telefono":telefono,
        }
    )
#Deshabilitar Sucursal
def disable_Sucursal(request: Request, listaSucursal):
    return templates.TemplateResponse(
        "deshabilitarSucursal.html",
        context={
            "request":request,
            "id_sucursal": listaSucursal,
            "estado":estado,
        }
    )

#Crear CDT
def register_CDT(request:Request):
    return templates.TemplateResponse(
        "crearCDT.html",
        context={
            "response":response,
            "numeroCuenta":numeroCDT,
            "idSucursal":idSucursal,
            "saldo": saldo,
            "fechaApertura":fechaApertura,
            "tasaInteres":tasaInteres,
            "ultimoMovimiento":ultimoMovimiento,
            "idUsuario":cedula,
            "clausula":clausula,
            "retencion":retencion,
            "fechaFinalizacion":fechaFinalizacion,
            "aproxInteres":interesAprox,
        }
    )

#Emergente Crear CDT
def emergenteRegisterCDT(request: Request):
    return templates.TemplateResponse(
        "emergenteCrearCDT.html",
        context={
            "request": request
        }
    )
#Crear Credito
def register_Credito(request:Request):
    return templates.TemplateResponse(
        "crearCredito.html",
        context={
            "response":response,
            "numeroCuenta":numeroCredito,
            "idSucursal":idSucursal,
            "saldo": saldo,
            "fechaApertura":fechaApertura,
            "tasaInteres":tasaInteres,
            "ultimoMovimiento":ultimoMovimiento,
            "idUsuario":cedula,
        }
    )

#Emergente Crear Credito
def emergenteRegisterCredito(request: Request):
    return templates.TemplateResponse(
        "emergenteCrearCredito.html",
        context={
            "request": request
        }
    )
#Crear Corriente
def register_Corriente(request:Request):
    return templates.TemplateResponse(
        "crearCredito.html",
        context={
            "response":response,
            "numeroCuenta":numeroCuenta,
            "idSucursal":idSucursal,
            "saldo": saldo,
            "fechaApertura":fechaApertura,
            "tasaInteres":tasaInteres,
            "ultimoMovimiento":ultimoMovimiento,
            "idUsuario":cedula,
        }
    )
#Emergente Crear Cuenta Corriente
def emergenteRegisterCorriente(request: Request):
    return templates.TemplateResponse(
        "emergenteCrearCuenta.html",
        context={
            "request": request
        }
    )
#Consultar Historial
def consult_Historial(request: Request):
    return templates.TemplateResponse(
        "consultarHistorial.html",
        context={
            "response": response,
            "numeroCuenta":numeroCuenta,
            "saldo":saldo,
            "movimiento":movimiento,
            "fechaMovimiento":fechaMovimiento,
            "descripcion":descripcion,

        }
    )
