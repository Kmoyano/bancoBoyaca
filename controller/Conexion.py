import mysql.connector


class Conexion:
    def __init__(self):
        pass

    def conectarBD(self):
        try:
            self._conn = mysql.connector.connect(
                host="localhost",
                database="bancoBoyaca",
                user="root",
                password="alejandro")
            if (self._conn.is_connected()):
                print("Conecto")
                return self._conn
        except:
            return False