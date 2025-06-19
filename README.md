# Práctica: Calculadora de Indicadores de Salud
- Objetivo
  - Desarrollar una aplicación en Python que:
    - Solicite datos del usuario (variables y tipos de datos).
    - Realice cálculos utilizando operadores aritméticos y lógicos.
    - Evalúe condiciones (condicionales).
    - Use bucles para repetir acciones.
    - Organice el código en funciones con parámetros, argumentos y retorno de valores.
      
- Enunciado
  - Crea un programa llamado "SaludApp" que permita al usuario registrar su información básica y calcular dos indicadores:
  - Índice de Masa Corporal (IMC):
    
        Fórmula: peso / (altura²)
- Clasificación:
    - < 18.5: Bajo peso
    - 18.5–24.9: Normal
    - 25–29.9: Sobrepeso
    - 30 o más: Obesidad
  - Frecuencia cardíaca máxima (FCM):

        Fórmula: 220 - edad
  - El programa debe repetirse hasta que el usuario decida salir.
    
- Requisitos técnicos
    - Solicitar: nombre (cadena), edad (entero), peso (float), altura (float).
    - Calcular IMC y clasificar el resultado con condicionales.
    - Calcular FCM.
    - Mostrar resultados de forma amigable.
    - Usar funciones para cada cálculo.
    - Permitir ingresar múltiples usuarios usando un bucle while.
    - Validar que los valores numéricos sean positivos.
      
- Aprendizajes
    - Uso correcto de variables y tipos de datos.
    - Aplicación de operadores aritméticos y lógicos.
    - Dominio de estructuras condicionales y bucles.
    - Creación y uso de funciones con parámetros, argumentos y retorno.
    - Comprensión del flujo general de un programa Python.

# Explicación del código

- Poseemos 5 funciones para este código:
  - IMC(peso, altura)
  - clasificar_imc(imc)
  - FCM(edad)
  - comprobar(dato, flag)
  - solicitar_datos(lista_usuarios)

- Estas funciones se encargan de:
  - IMC(peso, altura):
    - Retorna el calculo del imc como float.
  - clasificar_imc(imc):
    - Retorna como cadena a que grupo pertenece el individuo respecto al resultado del IMC.
  - FCM(edad):
    - Retorna el calculo del FCM.
  - comprobar(dato, flag):
    - En caso de que los datos sean validos según las siguientes validaciones:
      - Se encarga de validar la entrada de datos, para ello comprobaremos con la variable flag en que caso nos encontramos para determinar que explicitamente comprobar y que retornar.
      - Si pedimos el nombre, validará que no se ingrese una cadena vacia, retornando el valor transformado en titulo (para que todas las iniciales de cada fragmento de la cadena despues de un espacio sean mayucula).
      - Si pedimos la edad, validará que sea un numero mayor que 0 y retornará el valor como un entero.
      - Si pedimos el peso o la altura, validará que sea un numero mayor a 0.0, retornando el valor como float.
      - Al finalizar estas comprobaciones solo que ver si el usuario quiere seguir ingresando datos, para ello validamos si la respuesta que da es 'si' o 'no', retornando la cadena en minisculas.
      - Si no se aplica ninguno de estos casos por ABC motivo, se forzará un error.
    - En caso de que se generé cualquier tipo de error:
      - Mostrará por pantalla que el dato no es valido.
      - Según el caso en que nos encontrabamos pedirá y almacenará el dato con el cual estabamos trabajando.
  - solicitar_datos(lista_usuarios):
    - Se iniciará un diccionario vacio,
    - Se inicia un ciclo "While True" para pedir y comprobar los datos hasta que se eliga no seguir con la petición.
    - IMPORTANTE: Los datos se ingresan como cadena para realizar para comprobación de los datos en "comprobar(x)" y está función retorna el dato validado con el tipo de dato que se pidió inicialmente
    - Luego de realizar todas las comprobaciones respectivas, estos datos validados se agregan al diccionario, y dicho diccionario se añade a una lista u arreglo.
    - Finaliza con la validación de si él usuario desea seguir ingresando datos, si la respuesta es 'no' sale del bucle y retorna la lista_usuarios que ingresamos previamente como parametro.
   
- Entonces una vez creada estas 5 funciones:
  - En el "Main Program" crearemos un arreglo vacio, el cual usaremos como parametro para llamar a la funcion 'ingresar_datos(x)'.
  - Luego mostramos el detalle de los datos de manera amigable con el usuario de forma de que se recorra la lista retornada con los datos ingresados por consola.
  - Almacenamos y llamamos a la funcion 'imc(a, b)' para obtener su valor con los datos entregados.
  - Almacenamos y llamamos a la funcion 'clasificar_imc(x)' y 'FCM(x)' para obtener sus respectivos valores.
  - Una vez ya obtenido TODOS los datos a usar mostramos por pantalla de la manera que se estime conveniente los datos retornados, el nombre del individuo, el valor de su imc y a que grupo pertenece (el estado en que se encuentra) y por ultimo su FCM, esto se repetirá hasta que se haya recorrido el arreglo de diccionarios completamente y finaliza nuestro programa.   

# IMPORTANTE
- Para el caso del código que contiene 2 partes, la 'Parte 2' solo contiene las 5 funciones principales y la 'Parte 1' el 'Main Program' pero para hacer uso de ello ya que estan en 2 archivos diferentes debemos incluir el siguiente extracto de código:
  - TENER EN CUENTA - deben cambiar el nombre del archivo 'Calculadora de Indicadores de Salud (Parte 2).py' a 'Calculadora_de_Indicadores_de Salud_(Parte_2).py' para no tener errores, EN EL CODIGO APARECE COMO 'funciones' DEBEN CAMBIARLO:
      
        from Calculadora_de_Indicadores_de_Salud_(Parte_2) import *

  
