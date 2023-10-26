# le pedimos al usuario que nos diga una frase (o varias)
frase =input("decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas=frase.split(" ")
#usanos len() para ver Ia cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)
#caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("flaco tampoco te pedi un testamento")
#Calculamos cuanto tardaría en decir las palabras y se lo dec imos
print(f'Dijiste{cantidad_de_palabras} palabras y tardarías{cantidad_de_palabras/2} segundos en decirlo' )
print(f'Da1to lo diria en ({cantidad_de_palabras*100//2*0.3/100} segundos ')