print('[Mensaje] Generando libreria compartida latino-regex')

import platform
sistema = platform.system()

Import('entorno','ruta_librerias')

entorno.SharedLibrary(target=ruta_librerias+"regex2",source="src/regex.c")