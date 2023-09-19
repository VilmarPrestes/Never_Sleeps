#pip install pyautogui

import pyautogui as pa 
import time

"""
#Descobrir coordenada desejada: 

time.sleep(2) # Tempo de espera até selecionar local desejado
x, y = pa.position()
print(f"Coordenadas do cursor: x={57}, y={494}")

"""

x, y = 57, 494  # Define as coordenadas (da tela) para clicar
intervalo = 30 * 60  # Tempo para clicar na tela (30 minutos)

try:
    while True:
        pa.click(x, y)
        time.sleep(intervalo)

except KeyboardInterrupt:
    print("Finalizado!")  # Mensagem ao interromper com Ctrl+C
