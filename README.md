# Bot de Telegram para monitoreo de humedad y temperatura

Este proyecto muestra una forma de automatizar datos de un sensor usando raspberry, python y telegram para crear tareas automatizadas que se pueden ejecutar desde un teléfono por medio de un bot de telegram.

Ver [tareas en Notion](https://malachite-clock-422.notion.site/Smart-home-Raspberry-bot-d060d796ccdd4b58a55fde02253e6614?pvs=74)

# Configuración de raspberry
Se necesita un paquete linux llamado OpenBLAS para trabajar con numpy y crear las gráficas. Ejecuta el siguiente el comando para instalar el paquete:
```bash
sudo apt-get install libopenblas-dev
```

# Lista de comandos

### Crear entorno virtual 
Para  trabajar con dependecias y paquetes, es necesario crear un entorno virtual para que los paquetes no sean accesibles por fuera del directorio y sea seguro.

```powershell
python -m venv
```

### Activar entorno virtual

(powershell)
```powershel
.venv/Scripts/activate
```

### Installar dependencias
(poershell)
```powershell
pip install -r requirements.txt

```
