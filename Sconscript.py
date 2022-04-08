print('[Mensaje] Generando libreria estatica latino-regex')

import platform
sistema = platform.system()

Import('entorno','ruta_librerias')

entorno.StaticLibrary(target=ruta_librerias+"regex",source="src/regex.c")
#entorno.SharedLibrary(target=ruta_librerias+"regex",source="src/regex.c")