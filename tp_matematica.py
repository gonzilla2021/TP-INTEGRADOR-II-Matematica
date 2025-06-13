def conjuntos_unicos(dni):
    """Retorna los dígitos únicos de un DNI como lista ordenada"""
    conjunto = set()           # Usa set() para eliminar duplicados automáticamente
    for num in dni:
        conjunto.add(num)      # Agrega cada dígito al set
    return sorted(list(conjunto))  # Convierte a lista ordenada


def conteo_frecuencia(dni):
    """Cuenta la frecuencia de cada dígito en el DNI"""
    check_list = {}
    for num in dni:
        if num not in check_list:
            check_list[num] = 1      # Primera aparición = 1
        else:
            check_list[num] += 1     # Incrementa contador
    return check_list


def suma_total(dni):
    """Suma todos los dígitos del DNI"""
    suma = 0
    for num in dni:
        suma += int(num)
    return suma

########### OPERACIONES CON CONJUNTOS ###################################


def union_dnis(DNIs):
    """Realiza la unión de todos los dígitos únicos de los DNIs registrados"""
    conjunto_union = set()
    for dni in DNIs:
        # Agrega todos los dígitos del DNI al conjunto
        conjunto_union.update(dni)
    return sorted(conjunto_union)


def verificarAltaDiversidad(DNIs):
    for dni in DNIs:
        if len(dni) < 6:
            return f"{DNIs}, NO cumple la Diversidad!"
    return f"{DNIs}, Cumple la Diversidad!"


def interseccion_dnis(DNIs):
    """Calcula los dígitos comunes en todos los DNIs usando el operador &"""
    if not DNIs:
        # Si no hay DNIs, retorna una lista vacía (esto evita errores con listas vacías)
        return []

    # Convertimos cada DNI a un conjunto de sus dígitos
    conjuntos = [set(dni) for dni in DNIs]

    # Iniciamos con el primer conjunto
    resultado = conjuntos[0]

    # Aplicamos intersección con cada conjunto siguiente usando &
    for conjunto in conjuntos[1:]:
        resultado = resultado & conjunto  # Operador & (interseccion)
        if not resultado:  # Si no hay elementos comunes, terminamos
            break

    return sorted(resultado)


def conjuntoParImpar(DNIs):
    pares = 0
    impares = 0
    for dni in DNIs:
        if len(dni) % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    if pares > impares:
        return f"Grupo Par (Pares: {pares}, Impares: {impares})"
    else:
        return f"Grupo Impar (Pares: {pares}, Impares: {impares})"


def diferencia_dnis(DNIs):
    """Calcula los dígitos únicos que están en el primer DNI pero no en los demás"""
    if len(DNIs) < 2:
        return []

    # Convertimos cada DNI a un conjunto
    conjuntos = [set(dni) for dni in DNIs]

    # Diferencia entre el primer DNI y la unión de los demás
    otros_dnis = set().union(*conjuntos[1:])
    return sorted(conjuntos[0] - otros_dnis)


def diferencia_simetrica_dnis(DNIs):
    """Calcula los dígitos que están en un DNI pero no en todos (diferencia simétrica)"""
    if len(DNIs) < 2:
        return []

    # Convertimos cada DNI a un conjunto
    conjuntos = [set(dni) for dni in DNIs]

    # Diferencia simétrica entre todos
    resultado = set()
    for conjunto in conjuntos:
        resultado ^= conjunto  # Operador de diferencia simétrica

    return sorted(resultado)


def es_bisiesto(años_nacimiento):
    for año in años_nacimiento:
        año=int(año)
        if año % 4 == 0:
            if año % 100 == 0 and año % 400 == 0:
                print("Tenemos un año especial")
        else:
            continue


def par_impar_2000(años_nacimiento):
    count = 0   
    for año in años_nacimiento:
        año=int(año)
        if año % 2 == 0:
            print(f"El año {año} es par")
        else:
            print(f"El año {año} es impar")

        if año > 2000:
            count += 1
    if count == len(años_nacimiento):
        print("Grupo Z")

def prod_cartesiano(años_nacimiento):
    producto_años = []
    for año in años_nacimiento:
        año = int(año)
        producto_años.append(año*(2025-año))
    print("El producto cartesiano entre años de nacimiento y edades es:\n" f"{producto_años}") 


#######################COMIENZO DE PROGRAMA#############################################
def main():
    DNIs = []
    
    # Recolección de DNIs
    cantidad = int(input("Ingrese la cantidad de documentos que desea registrar: "))
    for i in range(1, cantidad+1):
        tmp_dni = input(f"Ingrese el DNI número {i}: ")
        DNIs.append(tmp_dni)

    # Mostrar información de cada DNI
    print("\n=== INFORMACIÓN DE CADA DNI ===")
    for item in DNIs:
        print(f"\nDNI: {item}")
        print(f"Suma total de los dígitos: {suma_total(item)}")
        print(f"Dígitos únicos: {conjuntos_unicos(item)}")
        print(f"Frecuencia de dígitos: {conteo_frecuencia(item)}") 
    # Mostrar unión de todos los DNIs
    if len(DNIs) > 1:
        print("\n=== OPERACIONES CON LOS CONJUNTOS DE TODOS LOS DNIs ===")
        print(f"UNION= {union_dnis(DNIs)}") #UNION
        print(f"INTERSECCION: {interseccion_dnis(DNIs)}")#INTERSECCION

        #########################################################################################
        # Recolección de DNIs Para la diferencia y diferencia simetrica
    DNIs = []
        
    cantidad = int(input("Ingrese la cantidad de documentos que desea registrar: "))
    for i in range(1, cantidad+1):
        tmp_dni = input(f"Ingrese el DNI número {i}: ")
        DNIs.append(tmp_dni)
        print(f"Diferencia entre conjuntos: {diferencia_dnis(DNIs)}")#DIFERENCIA
        print(f"Diferencia simétrica entre conjuntos: {diferencia_simetrica_dnis(DNIs)}")#DIFERENCIA SIMETRICA


    anios= input("Ingrese años de nacimiento: ").split()

    par_impar_2000(anios) 
    es_bisiesto(anios)
    prod_cartesiano(anios)  


# Ejecutar programa principal
if __name__ == "__main__":
    main()
