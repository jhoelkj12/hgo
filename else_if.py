ingreso_mensual=125
gasto=20000
if ingreso_mensual>10000:
    if ingreso_mensual-gasto>3000:
        print("ESTAS BIEN")
    else:
        print("estas gastnado demasiado")

elif ingreso_mensual>1000:
    print("estas masomenis")
else:
    print("sos pobre")
