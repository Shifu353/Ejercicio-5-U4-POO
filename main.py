from RepositorioPacientes import RespositorioPacientes
from vistaPacientes import ViewPacientes
from Controlador import ControladorPacientes
from ObjectEncoder import ObjectEncoder

def main():
    conn=ObjectEncoder("pacientes.json")
    repo=RespositorioPacientes(conn)
    vista=ViewPacientes()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == "__main__":
    main()
