import pyautogui
import flet as ft
import threading
import time

# Variable globale pour le contrôle de l'exécution du clic automatique
clic_auto_actif = False


def clic_position(x, y):
    # Déplace d'abord le curseur à la position spécifiée
    pyautogui.moveTo(x, y)
    # Attend un court instant pour que le curseur ait le temps de se déplacer
    time.sleep(0.5)
    # Effectue ensuite le clic à la position actuelle du curseur
    pyautogui.click()


def clic_position_percent(x_percent, y_percent):
    # Récupère la résolution de l'écran
    screen_width, screen_height = pyautogui.size()
    # Calcule la position x en pourcentage
    x = int(screen_width * (x_percent / 100))
    # Calcule la position y en pourcentage
    y = int(screen_height * (y_percent / 100))
    # Déplace d'abord le curseur à la position spécifiée
    pyautogui.moveTo(x, y)
    # Attend un court instant pour que le curseur ait le temps de se déplacer
    time.sleep(0.5)
    # Effectue ensuite le clic à la position actuelle du curseur
    pyautogui.click(x, y)  # Effectue le clic à la position calculée


def start_auto_clic():
    global clic_auto_actif
    clic_auto_actif = True
    while clic_auto_actif:
        # Selectionne sur le vendeur
        clic_position(10, 10)
        # Parle au vendeur
        pyautogui.rightClick(10, 10)
        time.sleep(2)
        # Ouvre l'inventaire du vendeur
        clic_position_percent(50, 62)
        time.sleep(2)
        # Clic maccro
        clic_position(20, 120)
        # Attente de 12 secondes pout la création de la baguette
        time.sleep(12)


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
                            "Loop to craft & sell a Greater Magic Wand and buy one Simple Wood."
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
