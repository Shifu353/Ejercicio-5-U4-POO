from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Paciente import Paciente
class ListaPacientes(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    def insertar(self, paciente, index=tk.END):
        text = "{}, {}".format(paciente.getApellido(), paciente.getNombre())
        self.lb.insert(index, text)
    def borrar(self, index):
        self.lb.delete(index, index)
    def modificar(self, pacient, index):
        self.borrar(index)
        self.insertar(pacient, index)
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class ShowIMC(tk.Toplevel):
    def __init__(self,parent,imc,corporal):
        super().__init__(parent)
        self.title('IMC')
        self.geometry("330x105")
        self.resizable(0,0)
        
        self.__entryIMC = IntVar()
        self.__entryComp = StringVar()
        self.__entryIMC.set(imc)
        self.__entryComp.set(corporal)

        self.lblIMC = ttk.Label(self,text = 'IMC')
        self.lblComp = ttk.Label(self,text='Composición Corporal')
        self.entryIMC = ttk.Entry(self,textvariable = self.__entryIMC)
        self.entryComp = ttk.Entry(self,textvariable = self.__entryComp, width=25)
        self.btnBack = ttk.Button(self, text = 'Volver', width = 20,command = self.destroy)

        self.lblIMC.grid(row = 0, column = 0, sticky = 'nw')
        self.entryIMC.grid(row = 0, column = 1, sticky = 'nw')
        self.lblComp.grid(row = 1, column = 0, sticky = 'nw')
        self.entryComp.grid(row = 1, column = 1, sticky = 'nw')
        self.btnBack.grid(row = 2, column = 0, sticky = 'nwse')
    def show(self):
        self.grab_set()
        self.wait_window()

class FormularioPaciente(tk.LabelFrame):
    fields = ("Apellido", "Nombre", "Telefono", "Peso", "Altura")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", padx=10, pady=10,**kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def mostrarEstadoPacienteEnFormulario(self, paciente):
        values = (paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(),paciente.getPeso(),paciente.getAltura())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def crearPacienteDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        paciente=None
        try:
            paciente = Paciente(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return paciente
    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class NewPaciente(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.paciente = None
        self.form = FormularioPaciente(self)
        self.btn_add = tk.Button(self, text="Confirmar",command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)
    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()
    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente

class UpdateFormularioPaciente(FormularioPaciente):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_IMC = tk.Button(self, text="Ver IMC")
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_IMC.pack(side=tk.LEFT, ipadx=5, padx=5, pady=5)
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
    def bind_verIMC(self,callback):
        self.btn_IMC.config(command=callback)


class ViewPacientes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.list = ListaPacientes(self, height=15)
        self.form = UpdateFormularioPaciente(self)
        self.btn_new = tk.Button(self, text="Agregar Paciente")
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        self.btn_new.pack(side=tk.BOTTOM, pady=5)

    def setControlador(self, ctrl):
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_verIMC(ctrl.Imc)

    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)

    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    def limpiarImc(self):
        self.formulario.limpiar()        

    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()

    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)
