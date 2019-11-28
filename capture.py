import pyautogui
import tkinter as tk
from datetime import datetime

# Habilitar permiso para la aplicacion
root = tk.Tk()

# Funcion para realizar captura de pantalla
def take_screenshot():
    # Crear instancia
    my_screenshot = pyautogui.screenshot()
    print(pyautogui.position())
    now = datetime.now()  # current date and time
    # path_filename = r'C:\Windows\Temp\\'+ now.strftime("%d%m%Y") + "_" + now.strftime("%H%M%S") + ".png"
    path_filename = r'D:\\'+ now.strftime("%d%m%Y") + "_" + now.strftime("%H%M%S") + ".png"
    print(path_filename)
    # Guardar imagen
    my_screenshot.save(path_filename)

# Inicializar captura en tiempo de ejecucion
take_screenshot()