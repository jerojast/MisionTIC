import pandas as pd

rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

def listaPeliculas(rutaFileCsv: str) -> str:
    if rutaFileCsv.split(".")[2] == "csv?raw=true":
        try:
            base_Datos = pd.read_csv(rutaFileCsv)
            subconjunto = base_Datos[["Country", "Language", "Gross Earnings"]]

        except:
            print("Error al leer el archivo de datos.")
        else:
            Tabla_dinamica = subconjunto.pivot_table(index=["Country", "Language"])
      
            return Tabla_dinamica.head(10)
    else:
        print("Extensión inválida.")
    return

print(listaPeliculas(rutaFileCsv))
    