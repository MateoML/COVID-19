#Carga de datos

print("Diagnostico de COVID-19")
edad = int(input("Introduzca su edad: "))
temp = int(input("Introduzca su temperatura: "))
neumo = int(input("Si ha tenido nueumonía sin explicación clínica introduzca 1, si no ha tenido nueumonía intoduzca 2: "))

#Proceso

if neumo == 1:
    print("Usted es considerado caso sospechoso")
elif temp > 37:
    tos = int(input("Si padece tos introduzca 1, si no la padece introduzca 2: "))
    odinofagia = int(input("Si padece de odinofagia introduzca 1, si no la padece introduzca 2: "))
    dificultad_respiratoria = int(input("Si padece de dificultad respiratoria introduzca 1, si no la padece introduzca 2: "))
    if tos == 1 or odinofagia == 1 or dificultad_respiratoria == 1:
        ps = int(input("Si es personal de salud introduzca 1, si no lo es introduzca 2: "))
        cc = int(input("Si a estado en contacto con casos confirmados en los últimos 14 días introduzca 1, si no a estado en contacto introduzca 2: "))
        ve = int(input("Si a viajo al exterior en los últimos 14 días introdusca 1, sino introduzca 2: "))
        tl = int(input("Si estuvo en zonas de casos de transmisión local confirmados introduzca 1, sino introduzca 2: "))
        if ps == 1 or cc == 1 or ve == 1 or tl == 1 or edad >= 60:
           print("Usted es un caso sospechoso", end = " " )
        if ps == 2 and cc == 2 and ve == 2 and tl == 1:
           print("Y es considerado caso autóctono")
    else:
         print("Usted no es considerado un caso sospechoso")
else: print("UsteD no es considerado un caso sospechoso")







