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

#COMIENZO DE PROGRAMA
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


# Ejecutar programa principal
if __name__ == "__main__":
    main()        