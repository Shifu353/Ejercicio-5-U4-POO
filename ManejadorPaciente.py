from Paciente import Paciente
class ManejadorPacientes:
    indice=0
    __pacientes=None

    def __init__(self):
        self.__pacientes=[]

    def agregarPaciente(self, Paciente):
        Paciente.rowid = ManejadorPacientes.indice
        ManejadorPacientes.indice+=1
        self.__pacientes.append(Paciente)

    def getListaPacientes(self):
        return self.__pacientes
        
    def deletePaciente(self, Paciente):
        indice = self.obtenerIndicePaciente(Paciente)
        self.__pacientes.pop(indice)

    def ModificarPaciente(self,Paciente):
        indice=self.obtenerIndicePaciente(Paciente)
        self.__pacientes[indice]=Paciente

    def imcresultado(self,indice):
        peso=float(float(self.__pacientes[indice].getPeso())/(float(self.__pacientes[indice].getAltura())/100)**2)
        pesof=round(peso,2)
        return pesof

    def corporal(self,pesof):
        if pesof<18.5:
            return 'Peso Inferior Al Normal'
        elif pesof<24.9:
            return 'Peso Normal'
        elif pesof<29.9:
            return 'Peso Superior Al Normal'
        else:
            return 'Obesidad'

    def updatePaciente(self, Paciente):
        indice = self.obtenerIndicePaciente(Paciente)
        self.__pacientes[indice]=Paciente

    def obtenerIndicePaciente(self, Paciente):
        bandera = False
        i=0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == Paciente.rowid:
                bandera = True
            else:
                i+=1
            return i
        
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            Paciente = [Paciente.toJSON() for Paciente in self.__pacientes]
        )
        return d
