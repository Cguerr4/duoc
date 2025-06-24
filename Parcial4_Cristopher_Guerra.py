##AUTOR:Cristopher_Guerra

def validar_repetidos(nombre_comprador_lista, nombre_comprador):
    for elemento in nombre_comprador_lista:
        if elemento == nombre_comprador:
            return False
    return True
def agregar_no_repetidos(nombre_comprador_lista, nombre_comprador):
    if validar_repetidos(nombre_comprador_lista, nombre_comprador):
        nombre_comprador_lista.append(nombre_comprador)
        return True
    else:
        return False
    
def validar_tipo_entrada(tipo_entrada):
    if tipo_entrada == "G" or tipo_entrada == "V":
        return True
    else:
        print("No se reconoce ese tipo de entrada, intente nuevamente.")
        return False

def validar_tipo_entrada_iluminados(tipo_entrada):
    if tipo_entrada == "CV" or tipo_entrada == "PAL":
        return True
    else:
        print("No se reconoce ese tipo de entrada, intente nuevamente.")
        return False
def validar_codigo_confirmacion(codigo_confirmacion):
    contador=0
    digito=0
    if len(codigo_confirmacion) >= 6:
        for caracter in codigo_confirmacion:
            if caracter.isupper():
                contador = contador + 1
            if contador >= 1:
                for caracter in codigo_confirmacion:
                    if caracter.isdigit():
                        digito= digito + 1
            if digito >= 1:           
                if " " not in codigo_confirmacion:
                        return True
    else:
        return False
  
def validar_codigo_confirmacion_iluminados(codigo_confirmacion):
    contador=0
    digito=0
    if len(codigo_confirmacion) >= 5:
        for caracter in codigo_confirmacion:
            if caracter.isupper():
                contador = contador + 1
            if contador >= 3:
                for caracter in codigo_confirmacion:
                    if caracter.isdigit():
                        digito= digito + 1
            if digito >= 1:           
                if " " not in codigo_confirmacion:
                        return True
    else:
        return False


print("Bienvenido al totem de autoservicio de Conciertos Rock and Chile.")
entradas_iluminados = 500
entradas_fortificados = 500 
nombre_comprador_lista=[]
opcion=input("1.-Comprar entrada a 'los Fortificados'.\n2.-Comprar entrada a 'los Iluminados'\n3.-Stock de entradas para ambos conciertos.\n4.-Salir")
while True:
    if opcion == "1":
        nombre_comprador=input("Ingrese nombre de comprador:")
        if validar_repetidos(nombre_comprador_lista, nombre_comprador):
            agregar_no_repetidos(nombre_comprador_lista, nombre_comprador)
            True
            while True:
                tipo_entrada=input("Ingrese tipo de entrada (G/V)")
                if validar_tipo_entrada(tipo_entrada) == True:
                    while True:
                        codigo_confirmacion=input("Ingrese codigo de confirmacion:")
                        if validar_codigo_confirmacion(codigo_confirmacion)== True:
                            entradas_fortificados = entradas_fortificados - 1
                            break                    
                    break
            continuar=input("Desea continuar?S/N")
            if continuar == "s":
                opcion=input("1.-Comprar entrada a 'los Fortificados'.\n2.-Comprar entrada a 'los Iluminados'\n3.-Stock de entradas para ambos conciertos.\n4.-Salir")
            else:
                opcion = "4"
        else:
            print(f"Este usuario ya compro una entrada.{nombre_comprador_lista}")
            
            
    elif opcion == "2":
        nombre_comprador=input("Ingrese nombre de comprador:")
        if validar_repetidos(nombre_comprador_lista, nombre_comprador):
            agregar_no_repetidos(nombre_comprador_lista, nombre_comprador)
            True
            while True:
                tipo_entrada=input("Ingrese tipo de entrada Cancha Vip o Palco (CV/PAL)")
                if validar_tipo_entrada_iluminados(tipo_entrada) == True:
                    while True:
                        codigo_confirmacion=input("Ingrese codigo de confirmacion:")
                        if validar_codigo_confirmacion_iluminados(codigo_confirmacion)== True:
                            entradas_fortificados = entradas_iluminados - 1
                            break                    
                    break
            continuar=input("Desea continuar?S/N")
            if continuar == "s":
                opcion=input("1.-Comprar entrada a 'los Fortificados'.\n2.-Comprar entrada a 'los Iluminados'\n3.-Stock de entradas para ambos conciertos.\n4.-Salir")
            else:
                opcion = "4"
        else:
            print(f"Este usuario ya compro una entrada.{nombre_comprador_lista}")
            
    elif opcion == "3":
        print(f"Las entradas disponbles son: los Fortificados:{entradas_fortificados} y los Iluminados {entradas_iluminados}")
        continuar=input("Desea continuar?S/N")
        if continuar == "s":
            opcion=input("1.-Comprar entrada a 'los Fortificados'.\n2.-Comprar entrada a 'los Iluminados'\n3.-Stock de entradas para ambos conciertos.\n4.-Salir")
        else:
            opcion = "4"
    elif opcion == "4":
        print("Programa terminado...")
        break
    else:
        print("Ingrese una opcion valida.")
        opcion=input("1.-Comprar entrada a 'los Fortificados'.\n2.-Comprar entrada a 'los Iluminados'\n3.-Stock de entradas para ambos conciertos.\n4.-Salir")
        



    