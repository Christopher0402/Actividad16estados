import os

def procesar():
    try:
        if not os.path.exists('data.txt'):
            print("Error: data.txt no existe")
            return

        with open('data.txt', 'r', encoding='utf-8') as f:
            lineas = f.readlines()
        
        encabezado = lineas[0].strip()
        registros = lineas[1:]

        with open('resultado.txt', 'w', encoding='utf-8') as f:
            f.write("--- REPORTE DETALLADO DE ESTADOS ---\n")
            f.write(f"Columnas detectadas: {encabezado}\n")
            f.write("-" * 40 + "\n")
            
            for linea in registros:
                if linea.strip():
                    # Aquí puedes hacer cálculos, por ejemplo sumar costos
                    datos = linea.strip().split(',')
                    estado = datos[0]
                    costo_total = int(datos[3]) + int(datos[4])
                    f.write(f"Estado: {estado} | Costo Total (Alojamiento + Transporte): ${costo_total}\n")
        
        print("resultado.txt generado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    procesar()