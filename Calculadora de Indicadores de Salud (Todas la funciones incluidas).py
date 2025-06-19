def IMC(peso, altura):
    return float(peso/(altura**2))

def clasificar_imc(imc):
    if imc >= 30: return "Obesidad"
    elif imc >= 25: return "Sobrepeso"
    elif imc >= 18.5: return "Normal"
    else: return "Bajo peso"
        
def FCM(edad):
    return 220 - edad

# ---------------------------------------------------------------------------------------------------------- #
#                                                                                                            #
#                                                    FORMA 1                                                 #
#                                                                                                            #
# ---------------------------------------------------------------------------------------------------------- #

def comprobar(dato, flag):
    while True:
        try:
            if flag == 0 and dato.strip() != '': return dato.title()    
            elif flag == 1 and int(dato) > 0: return int(dato)
            elif (flag == 2 or flag == 3) and float(dato) > 0.0: return float(dato)
            elif flag == 4 and dato.strip() != '' and dato.lower() in ('si', 'no'): return dato.lower()
            else: raise ValueError
        except ValueError:
            print ("Ingresa datos validos.")
            if flag == 0: dato = input("Ingresa el nombre: ")
            elif flag == 1: dato = input("Ingresa la edad: ")
            elif flag == 2: dato = input("Ingresa el peso: ")
            elif flag == 3: dato = input("Ingresa la altura: ")
            elif flag == 4: dato = input("Ingresa una respuesta (si/no): ")

def solicitar_datos(lista_usuarios):
    dict_usuarios = {}
    while True:
        nombre = input("Ingresa el nombre: ")
        nombre = comprobar(nombre, 0)
        edad = input("Ingresa la edad: ")
        edad = comprobar(edad, 1)
        peso = input("Ingresa el peso: ")
        peso = comprobar(peso, 2)
        altura = input("Ingresa la altura: ")
        altura = comprobar(altura, 3)
        resp =  input("¿Quieres seguir ingresando datos?\nIngreas una respuesta (si/no): ")
        resp = comprobar(resp, 4)
        dict_usuarios = {'nombre': nombre, 'edad': edad, 'peso': peso, 'altura': altura}
        lista_usuarios.append(dict_usuarios)
        if resp == 'no': break
    return lista_usuarios


# ---------------------------------------------------------------------------------------------------------- #
#                                                                                                            #
#                                                    FORMA 2                                                 #
#                                                                                                            #
# ---------------------------------------------------------------------------------------------------------- #

"""

def comprobar(_, flag):
    mensaje = {0: 'Ingresa el nombre: ', 1: 'Ingresa la edad: ', 2: 'Ingresa el peso: ', 3: 'Ingresa la altura: ', 4: 'Ingresa una respuesta (si/no): '}
    while True:        dato = input(mensaje.get(flag, "Ingresa un dato: ")).strip().lower()
        try:
            if flag == 0 and dato != '': return dato.title()
            elif flag in (1, 2, 3) and float(dato) > 0.0: return int(dato) if flag == 1 else float(dato)
            elif flag == 4 and dato in ('si', 'no'): return dato
            else: raise ValueError
        except ValueError:
            print("Dato inválido, por favor intenta nuevamente.")

def solicitar_datos(lista_usuarios):
    while True:
        nombre = comprobar(None, 0)
        edad = comprobar(None, 1)
        peso = comprobar(None, 2)
        altura = comprobar(None, 3)
        dict_usuarios = {'nombre': nombre, 'edad': edad, 'peso': peso, 'altura': altura}
        lista_usuarios.append(dict_usuarios)
        resp = comprobar(None, 4)
        if resp == 'no': break
    return lista_usuarios

"""

# Main
lista_usuarios = []
lista_usuarios = solicitar_datos(lista_usuarios)
print ("\n--- Salud App ---\n")
for datos in lista_usuarios:
    imc = IMC(datos['peso'], datos['altura'])
    c_imc, fcm = clasificar_imc(imc), FCM(datos['edad'])
    print (f"Sr/ita. {datos['nombre']}.\n\n {'-'*(50+len(c_imc))}\n|\tSu IMC es {imc:.1f} y se encuentra con {c_imc}.{' '*8}|\n|\tY su FMC es de: {fcm}.{' '*(23+len(c_imc))}|\n|{'_'*(50+len(c_imc))}|\n")  
