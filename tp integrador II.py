#DEFINICION DE FUNCIONES
#conjuntos unicos
def conjuntos_unicos(DNIs):
    CONJUNTOS_UNICOS = []
    conjunto = ''
    for documento in DNIs:
        for num in documento:
            if num not in conjunto:
                conjunto += num
    CONJUNTOS_UNICOS.append(sorted(conjunto))
    return CONJUNTOS_UNICOS


#conteo digitos x dni
def conteo_frecuencia(dni):
    check_list = {}
    for num in dni:
        if num not in check_list:
            continue   
            #insert en check_list
        else:
            continue
            #update value de num en la check_list

    return check_list
   
#suma digitos de dni
def suma_total(dni):
    suma = 0
    for num in dni:
        suma += int(num)
    return suma
   
#union de dos o mas conjuntos
def union(dni_opreaciones):
    return 1
    
#interseccion de dos o mas conjuntos   
def interseccion(dni_operaciones):
    return 1
    
#diferencia de conjuntos
def diferencia(dni_operaciones):
    return 1

#diferencia simétrica de conjuntos
def diferencia_simetrica(dni_operaciones):
    return 1


#COMIENZO DE PROGRAMA
DNIs = []
dni_operaciones = []
cantidad = int(input("Ingrese la cantidad de documentos que desea registrar:"))
for i in range(1, cantidad+1):
    tmp_dni = input(f"Ingrese el DNI número {i}:")
    DNIs.append(tmp_dni)

for item in (DNIs):
    print(item)
    print(f"La suma total de los dígitos del documento es {suma_total(item)}")
    print(conjuntos_unicos(item)[0])

print("Listado de operaciones:\n"
      "1. Unión\n"
      "2. Intersección\n" 
      "3. Diferencia\n"
      "4. Diferecia simétrica")
opcion_operacion = int(input("Introduce el número de operación que deseas realizar:"))

print("Conjuntos registrados a partir de documentos:")
for i in range(len(DNIs)):
    tmp_conjunto = ",".join(map(str, conjuntos_unicos(DNIs[i])[0]))
    print(f"{i+1}. {tmp_conjunto}")
operaciones = input("Ingrese el número de opcion de documentos separados con coma:")

if opcion_operacion == 1:
    print(union())
elif opcion_operacion == 2:
    print(interseccion())
elif opcion_operacion == 3:
    print(diferencia())
elif opcion_operacion == 4:
    print(diferencia_simetrica())