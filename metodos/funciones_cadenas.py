cadena1="hola"
cadena2="bienvenidos"
resultado=cadena1.upper()
#primera mayuscula
# resultado1=cadena2.capitalize()
# print(resultado1)
# busqueda=cadena1.find("a")
# print(busqueda)
# #busdqueda cadena tra cadena, lanza una excepion
# busqueda_index=cadena1.index("a")
# print(busqueda_index)
# es_numerico=cadena1.isnumeric()
# print(es_numerico)
# es_alfanumerico=cadena1.isalpha()
# print(es_alfanumerico)
contar=cadena1.count("la")
print(contar)
# valor="1D"
# valor2=2
# contar=valor.isnumeric()
# print(contar)
# cadena=valor.count("D")
#cuantos careactrerds tiene unA cadena
contar_carateres=len(cadena1)
print(contar_carateres)
#verificar si una cadena  empieza con otra cadena
empieza=cadena1.startswith("h")
empieza1=cadena1.endswith("l")
print(empieza)
print(empieza1)
#remplza la cadena 
cadenanueva=cadena1.replace("hola","lu como estas")
cadenanueva2=cadenanueva.capitalize()
print(cadenanueva)
print(cadenanueva2)
cadena_separada=cadenanueva2.split()
print(cadena_separada[2])

