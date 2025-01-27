"""
Analizar el archivo preproinsulin-seq.txt
"""
import re

def analizar():
    # 1) Leer el archivo con los datos originales
    with open("preproinsulin-seq.txt", "r") as f:
        raw_text = f.read() # Lectura del archivo
        
    # 2) Limpieza de inicio (Eliminar ORIGIN, 1, 61, //)
    cleaned_text = re.sub(r'(?i)ORIGIN', '', raw_text) # Eliminando la cadena ORIGIN buscando tanto en mayusculas como en minusculas
    cleaned_text = cleaned_text.replace('//', '')
    
    # 3) Eliminar todo lo que no sea letras
    cleaned_sequence = re.sub(r'[^a-zA-Z]', '', cleaned_text).lower()
    
    # 4) Verificar la longitud de la secuencia limpia
    seq_length = len(cleaned_sequence)
    print(f"La longitud de la secuencia limpia es: {seq_length}.")
    
    if seq_length != 110:
        print("Se esperaban 110 caracteres, algo salio mal")
    else:
        print("La secuencia tiene 110 carctres")
    
    # 5) Guardar los datos limpios
    with open("preproinsulin-seq-clean.txt", "w") as f:
        f.write(cleaned_sequence)
        
    # 6) extraer las secciones de la secuencia
    lsinsulin = cleaned_sequence[0:24]
    binsulin = cleaned_sequence[24:54]
    cinsulin = cleaned_sequence[54:89]
    ainsulin = cleaned_sequence[89:110]
    
    # 7) Guardar cada procion de la secuencia en su archivo
    with open("lsinsulin-seq-clean.txt", "w") as f:
        f.write(lsinsulin)
    
    with open("binsulin-seq-clean.txt", "w") as f:
        f.write(binsulin)
    
    with open("cinsulin-seq-clean.txt", "w") as f:
        f.write(cinsulin)
    
    with open("ainsulin-seq-clean.txt", "w") as f:
        f.write(ainsulin)
    
    print(f"lsinsulin: {len(lsinsulin)} caracteres esperados 24")
    print(f"binsulin: {len(binsulin)} caracteres esperados 30")
    print(f"cinsulin: {len(cinsulin)} caracteres esperados 35")
    print(f"ainsulin: {len(ainsulin)} caracteres esperados 21")
    
    print("Proceso de limpieza completado!!")


# Llamada a la función
analizar()