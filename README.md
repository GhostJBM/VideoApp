# VideoApp
aplicación de API REST BACKEND en python


## estructura del proyecto
--Main.py #punto de entrada de la aplicación API REST, FASTAPI


  entidades/ #Directorio de la aplicación
    |- __init__.py
    |- disco.py
    |- usuario.py
    |- venta.py
    |- alquiler.py
    |- catalogo.py
  ## Instalaciones necesarias
  1. clonar el repositorio GIT
     git clone https://github.com/usuario/VideoApp
  2. cd VideoApp
  3. Crear y activar el entorno virtual (Opcional)
  4. python -m venv venv
  5. sours venv/bin/activate #Linux
  6.  venv\Scripts\Active #Windows
  7.  instalar dependecias
      7.1. pip install fastapi uvicorn pydantic
  8. Ejecutar el servidor
     8.1. uvicorn main:app --reload
  9. Acceder a la API
      *Documentación interactiva: http://127.0.0.1:8000/docs
      *Documentación interactiva (ReDoc): http://127.0.0.1:8000/redoc

  ## Endpoints principales (versión inicial)
  Metodo Endpoint Descripción
  GET    /discos/  Lista los discos disponibles
  POST   /discos/  Agrega un nuevo disco
  PUT    /discos/{id}  Actualizar información de un disco
  DELETE /discos/{id}  Elimina un disco por el id
  POST   /usuarios/    Registra un nuevo usuario
  POST   /Ventas/   registra ventas
  POST   /alquileres/ registra un alquiler

  ## Tecnologías utilizadas
  * Python 3.12.0
  * FastAPI
  * Uvicorn (Servidor ASGI)

 ## Proyecto desarrollado como casa de estudio
 * Nombre : **Josiel Morales** <josiel.benavidez24400730@estu.unan.edu.ni>
 * GitHub : @Ghost
