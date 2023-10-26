otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5

#duracion de crudos
crudo_promedio=5
crudo_dalto=3.5


diferencia_con_min=100-dalto_curso/otros_cursos_min*100
diferencia_con_max=100-dalto_curso/otros_cursos_max*100
diferencia_con_promedio=100-dalto_curso/otros_cursos_promedio*100

vacio_crudo_otros=100-otros_cursos_promedio*1000//crudo_promedio/10
vacio_crudo_dalto=100-dalto_curso*1000//crudo_dalto/10


print(f'el curso de dalto duraun{diferencia_con_min}% menos que el mas rapido')
print(f'el curso de dalto duraun{diferencia_con_max}% menos que el mas rapido')
print(f'el curso de dalto duraun{diferencia_con_promedio}% menos que el mas rapido')
print("_____________________")
#crudo promedio
print(f'el crudo promedio elimina{vacio_crudo_otros}% menos que el mas rapido')
print(f'el crudo de dalto elmina{vacio_crudo_dalto}% menos que el mas rapido')
print("_____________________")

#mostardiferecias de otros cursos
print(f'ver 10 horas de curso dalto, equivale a {otros_cursos_promedio*100//dalto_curso/10}horas de otros cursos')
print(f'ver 10 horas de otros cursos aquivale a {dalto_curso*100//otros_cursos_promedio/10}horas de otros cursos')
print("_____________________")



