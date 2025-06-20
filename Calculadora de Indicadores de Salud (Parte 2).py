def IMC(peso, altura): return float(peso/(altura**2))

def clasificar_imc(imc):
    if imc >= 30: return "Obesidad"
    elif imc >= 25: return "Sobrepeso"
    elif imc >= 18.5: return "Normal"
    else: return "Bajo peso"
        
def FCM(edad): return 220 - edad

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
