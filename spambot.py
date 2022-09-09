import pyautogui
import webbrowser as web
from time import sleep

#Script para enviar un mensaje a un contacto
web.open("https://web.whatsapp.com/send?phone=+51960650700")
#Se debe agregar una url 'https://web.whatsapp.com/send?phone="+codigo del pais""Numero de celular"'
sleep(10)
    
for i in range(100):
        pyautogui.typewrite("Quiero enchiladas")
        pyautogui.press("enter")