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
        conjunto_union.update(dni)  # Agrega todos los dígitos del DNI al conjunto
    return sorted(conjunto_union)  


def interseccion_dnis(DNIs):
    """Calcula los dígitos comunes en todos los DNIs usando el operador &"""
    if not DNIs:
        return []  #Si no hay DNIs, retorna una lista vacía (esto evita errores con listas vacías)
    
    # Convertimos cada DNI a un conjunto de sus dígitos
    conjuntos = [set(dni) for dni in DNIs]
    
    # Iniciamos con el primer conjunto
    resultado = conjuntos[0]
    
    # Aplicamos intersección con cada conjunto siguiente usando &
    for conjunto in conjuntos[1:]:
        resultado = resultado & conjunto  # Operador & aquí
        if not resultado:  # Si no hay elementos comunes, terminamos
            break
    
    return sorted(resultado)


def diferencia(DNIs):
    return

def diferencia_simetrica(DNIs):
    return


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
        print(f"Intersección de dígitos comunes: {interseccion_dnis(DNIs)}")#INTERSECCION


# Ejecutar programa principal
if __name__ == "__main__":
    main()        