# Usa una imagen base de Python
FROM python:3.9

# Instala las dependencias necesarias para Tkinter y X11
RUN apt-get update && \
    apt-get install -y python3-tk && \
    apt-get clean

# Crea un directorio de trabajo
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . .

# Establece la variable de entorno para usar el display
ENV DISPLAY=host.docker.internal:0

# Comando para ejecutar la aplicación
CMD ["python", "EditorM.py"]
