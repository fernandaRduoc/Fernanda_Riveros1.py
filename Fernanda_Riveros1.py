import random 
import csv

trabajadores = [
    "Juan Pérez", "María García", "carlos López", 
    "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", 
    "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos aleatorios asignados correctamente")
    
def clasificar_sueldos():
    print("Clasificación de Sueldos:")
    print("Sueldos menores a $800.000")
    print("TOTAL:", sum(1 for sueldo in sueldos if sueldo<800000))
    for i, sueldos in enumerate(sueldos):
        if sueldo < 800000:
            print(f"{trabajadores[i]} ${sueldo}")
    print("\nSueldos entre $800.000 y $2.000.000")
    print("TOTAL:",sum(1 for sueldo in sueldos if 800000<= sueldos <=2000000))
    for i, sueldo in enumerate(sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"{trabajadores[i]} ${sueldo}")
    print("\nSueldos superiores a $2.000.000")
    print("TOTAL:", sum(1 for sueldo in sueldos if sueldo > 2000000))
    for i, sueldo in enumerate(sueldos):
        if sueldo > 2000000:
            print(f"{trabajadores[i]} ${sueldo}")
    print("\nTOTAL SUELDOS: $", sum(sueldos))
    
def ver_estadisticas():
    print("Estadísticas:")
    print("sueldo más alto:", max(sueldos))
    print("sueldo más bajo:", min(sueldos))
    print("Promedio de sueldos:", sum(sueldos) / len(sueldos))
    # Cálculo de la media de geométrica
    media_geom = 1
    for sueldo in sueldos:
        media_geom *= sueldo
    media_geom = media_geom ** (1 /len(sueldos))
    print("Media geométrica:", media_geom)

def reporte_de_sueldos():
    print("Reporte de Sueldos:")
    print("Nombre empleado, Sueldo Base, Descuento Salud, Descuento AFP, Sueldo Líquido")
    for i, sueldo in enumerate(sueldos):
        desc_salud = sueldo * 0.07
        desc_afp = sueldo * 0.12
        sueldo_liquido = sueldo - desc_salud - desc_afp
        print(f"{trabajadores[i]}, ${sueldo}, ${desc_salud}, ${desc_afp}, ${sueldo_liquido}")
        
    # Exportar a archivo CSV
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        for i, sueldo in enumerate(sueldos):
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            writer.writerow([trabajadores[i], sueldo, desc_salud, desc_afp, sueldo_liquido])
            
def main():
    while True:
        print("\nMenú:")
        print("1. Asignar Sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")    
        
        opcion = input("selecione una opión: ")
        
        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            reporte_de_sueldos
        elif opcion == "5":
            print("Finalizando programa...")
            print("Desarrollado por Fernanda Riveros")
            print("Rut 22.130.071-8")
            break
        else:
            print("Opción no válida. Intente nuevamente ")
            
if __name__ == "__main__":
    main()