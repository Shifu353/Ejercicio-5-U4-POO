from Paciente import Paciente
from ObjectEncoder import ObjectEncoder
from ManejadorPaciente import ManejadorPacientes

class RespositorioPacientes(object):
    __conn=None
    __manejador=None
    def __init__(self, conn):
        self.__conn = conn
        diccionario=self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, Paciente):
        return Paciente.getApellido(), Paciente.getNombre(), Paciente.getTelefono(), Paciente.getAltura(), Paciente.getPeso()

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()

    def agregarPaciente(self, paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente

    def modificarPaciente(self, paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente

    def borrarPaciente(self, paciente):
        self.__manejador.deletePaciente(paciente)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
    def Imcresultado(self,indice):
        r=self.__manejador.imcresultado(indice)
        return r
    def Corporal(self,resultado):
        c=self.__manejador.corporal(resultado)
        return c
