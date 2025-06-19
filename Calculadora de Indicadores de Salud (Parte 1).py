from funciones import *
  
# Main    
lista_usuarios = []
lista_usuarios = solicitar_datos(lista_usuarios)
print ("\n--- Salud App ---\n")
for datos in lista_usuarios:
    imc = IMC(datos['peso'], datos['altura'])
    c_imc, fcm = clasificar_imc(imc), FCM(datos['edad'])
    print (f"Sr/ita. {datos['nombre']}.\n\n {'-'*(50+len(c_imc))}\n|\tSu IMC es {imc:.1f} y se encuentra con {c_imc}.{' '*8}|\n|\tY su FMC es de: {fcm}.{' '*(23+len(c_imc))}|\n|{'_'*(50+len(c_imc))}|\n")  
