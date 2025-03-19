class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

<<<<<<< HEAD
def listarTareas(self):
   for tarea in self.tareas:
       if tarea.estaLista():
           print(f"La tarea {tarea.obtenerNombre()} está lista")
           
=======

    
>>>>>>> 0664a7b70725c7e69e232e0acdd39c615919a19b
