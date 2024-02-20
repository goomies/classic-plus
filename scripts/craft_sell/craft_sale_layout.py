import pyautogui
import flet as ft
import threading
import time

# Variable globale pour le contrôle de l'exécution du clic automatique
clic_auto_actif = False


def clic_position(x, y):
    # Déplace le curseur à la position spécifiée (x, y) et effectue un clic
    pyautogui.click(x, y)


def clic_position_percent(x_percent, y_percent):
    # Récupère la résolution de l'écran
    screen_width, screen_height = pyautogui.size()
    # Calcule la position x en pourcentage
    x = int(screen_width * (x_percent / 100))
    # Calcule la position y en pourcentage
    y = int(screen_height * (y_percent / 100))
    pyautogui.click(x, y)  # Effectue le clic à la position calculée


def start_auto_clic():
    global clic_auto_actif
    clic_auto_actif = True
    while clic_auto_actif:
        # Clic droit sur le vendeur
        clic_position(10, 10)
        pyautogui.rightClick(10, 10)
        time.sleep(1)
        # Clic pour parler au vendeur
        clic_position_percent(50, 61)
        clic_position_percent(50, 61)
        # Clic maccrox
        clic_position(20, 120)
        clic_position(20, 120)
        time.sleep(10)  # Attente de 12 secondes entre chaque clic


def stop_auto_clic():
    global clic_auto_actif
    clic_auto_actif = False


def start_button_clicked(e):
    # Action à effectuer lors du clic sur le bouton "Start"
    print("Bouton 'Start' cliqué")
    # Démarrer le thread pour effectuer des clics automatiques
    threading.Thread(target=start_auto_clic).start()


def stop_button_clicked(e):
    # Action à effectuer lors du clic sur le bouton "Stop"
    print("Bouton 'Stop' cliqué")
    # Arrêter les clics automatiques
    threading.Thread(target=stop_auto_clic).start()


def layout():
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.AUTO_FIX_HIGH),
                        title=ft.Text("Auto craft & Sell"),
                        subtitle=ft.Text(
                            "every 12 secondes craft, Sell a Greater Magic Wand and buy one Simple Wood."
                        ),
                    ),
                    ft.Row(
                        [ft.OutlinedButton(
                            "Start",
                            on_click=start_button_clicked
                        ),
                            ft.TextButton("Stop", on_click=stop_button_clicked)],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )


def main():
    layout()


if __name__ == "__main__":
    main()
