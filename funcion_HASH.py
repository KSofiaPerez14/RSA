import hashlib


# Función para calcular el hash de una cadena de texto
def calcular_hash_cadena(texto):
    # Convertir el texto a bytes
    texto_bytes = texto.encode('utf-8')

    # Calcular el hash MD5
    hash_md5 = hashlib.md5(texto_bytes).hexdigest()

    # Calcular el hash SHA-256
    hash_sha256 = hashlib.sha256(texto_bytes).hexdigest()

    return hash_md5, hash_sha256


# Ejemplo de cadena de texto de 8 bits
cadena_8_bits = "abcdefgh"
hash_8_bits_md5, hash_8_bits_sha256 = calcular_hash_cadena(cadena_8_bits)
print("Hash MD5 de cadena de 8 bits:", hash_8_bits_md5)
print("Hash SHA-256 de cadena de 8 bits:", hash_8_bits_sha256)

# Ejemplo de cadena de texto de 1024 bits
cadena_1024_bits = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce suscipit, purus quis feugiat consectetur, urna nunc convallis sem, a tincidunt quam orci ac mauris."
hash_1024_bits_md5, hash_1024_bits_sha256 = calcular_hash_cadena(cadena_1024_bits)
print("Hash MD5 de cadena de 1024 bits:", hash_1024_bits_md5)
print("Hash SHA-256 de cadena de 1024 bits:", hash_1024_bits_sha256)
# Función para calcular el hash de un archivo
def calcular_hash_archivo(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        contenido = archivo.read()
        hash_md5 = hashlib.md5(contenido).hexdigest()
        hash_sha256 = hashlib.sha256(contenido).hexdigest()
    return hash_md5, hash_sha256

# Ejemplo de calcular el hash de un archivo PDF
archivo_pdf = "Actividad2.pdf"
hash_pdf_md5, hash_pdf_sha256 = calcular_hash_archivo(archivo_pdf)
print("Hash MD5 del archivo PDF:", hash_pdf_md5)
print("Hash SHA-256 del archivo PDF:", hash_pdf_sha256)