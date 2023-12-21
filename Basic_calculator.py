import PySimpleGUI as sg
import math
layout = [
    [sg.Text("Introduce dos números")],
    [sg.InputText(),sg.InputText()],
    [sg.Submit(),sg.Cancel()]
]

window = sg.Window("Calculadora", layout, size = (600,600))
while True:
    event,values = window.read()
    if event == 'Submit':
        number1 = int(values[0])
        number2 = int(values[1])
        suma = number1 + number2
        sg.popup(f"La suma es {suma}")
        break
window.close()


