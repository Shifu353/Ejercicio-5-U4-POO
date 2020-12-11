from vistaPacientes import ViewPacientes,ShowIMC,FormularioPaciente,NewPaciente,UpdateFormularioPaciente,ShowIMC
from ManejadorPaciente import ManejadorPacientes

class ControladorPacientes(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
        # comandos de que se ejecutan a través de la vista
    def crearPaciente(self):
        nuevoPaciente = NewPaciente(self.vista).show()
        if nuevoPaciente:
            pacien = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(pacien)
            self.vista.agregarPaciente(pacien)
    def seleccionarPaciente(self, index):
        self.seleccion = index
        pacien = self.pacientes[index]
        self.vista.verPacienteEnForm(pacien)
    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        pacien = self.repo.modificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = pacien
        self.vista.modificarPaciente(pacien, self.seleccion)
        self.seleccion=-1
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion=-1
    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
    def Imc(self):
        indice=self.seleccion
        r=self.repo.Imcresultado(indice)
        c=self.repo.Corporal(r)
        ShowIMC(self.vista,r,c).show()
        self.vista.limpiarImc()
