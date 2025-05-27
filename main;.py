import keyboard
import winsound  # Only works on Windows
import time

print("Druk op de spatiebalk om een piep te horen. Druk op ESC om te stoppen.")

try:
    while True:
        if keyboard.is_pressed('space'):
            print("Piepen!")
            winsound.Beep(1000, 200)  # 1000 Hz, 200 ms
            while keyboard.is_pressed('space'):
                time.sleep(0.1)  # wacht tot spatiebalk losgelaten wordt

        if keyboard.is_pressed('esc'):
            print("Programma gestopt.")
            break
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Gestopt door gebruiker.")
