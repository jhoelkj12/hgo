class Estudiante:
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    nombre = input("digame su nombre: ")
    edad = input("edad: ")
    grado= input("grado: ")
        
estudiante1 = Estudiante(nombre,edad,grado)

print(f"""
      
      datos del estudiante \n\n
      nombre: {estudiante1.nombre} \n
      edad: {estudiante1.edad} \n
      grado: {estudiante1.grado} \n
      
      """)
estudiar = input()
if (estudiar.lower == "estudiar"):
    estudiante1.estudiar()