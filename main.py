import psutil
import time
import tkinter as tk


def check_battery():
    battery = psutil.sensors_battery()
    print(f"Battery level: {battery.percent}% | Charging: {battery.power_plugged}")

    if battery.percent == 100 and battery.power_plugged:
        print("Battery is full and charging. Displaying popup...")
        show_popup()


def show_popup():
    root = tk.Tk()
    root.title("Baterai Penuh")

    root.overrideredirect(True)

    label = tk.Label(
        root, text="Baterai sudah penuh! Lepaskan charger.", font=("Arial", 14)
    )
    label.pack(padx=50, pady=50)

    root.eval("tk::PlaceWindow . center")

    root.geometry("400x200")
    root.resizable(False, False)

    while psutil.sensors_battery().power_plugged:
        root.update()
        time.sleep(1)

    print("Charger disconnected. Closing popup...")
    root.destroy()


while True:
    check_battery()
    time.sleep(60)
