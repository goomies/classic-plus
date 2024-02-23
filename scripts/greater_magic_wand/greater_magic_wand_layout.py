import pyautogui
import flet as ft
import threading
import time

# Global variable to control the automatic click execution
click_auto_active = False

# Global variable to control the loading state
loading_in_progress = False


def click_position(x, y):
    # First move the cursor to the specified position
    pyautogui.moveTo(x, y)
    # Wait a short moment for the cursor to move
    time.sleep(0.5)
    # Then perform the click at the current cursor position
    pyautogui.click()


def click_position_percent(x_percent, y_percent):
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()
    # Calculate the x position in percentage
    x = int(screen_width * (x_percent / 100))
    # Calculate the y position in percentage
    y = int(screen_height * (y_percent / 100))
    # First move the cursor to the specified position
    pyautogui.moveTo(x, y)
    # Wait a short moment for the cursor to move
    time.sleep(0.5)
    # Then perform the click at the current cursor position
    pyautogui.click(x, y)


def start_auto_click():
    global click_auto_active

    click_auto_active = True
    while click_auto_active:
        # Select on the vendor
        click_position(10, 10)
        # Speak to the vendor
        pyautogui.rightClick(10, 10)
        time.sleep(2)
        # Open the vendor's inventory
        click_position_percent(50, 62)
        time.sleep(2)
        # Click macro
        click_position(20, 120)
        # Wait for 12 seconds for the wand creation
        time.sleep(12)


def stop_auto_click():
    global click_auto_active
    click_auto_active = False


def start_button_clicked(e):
    global loading_in_progress

    # Start the loading in progress
    loading_in_progress = True
    # Start the thread to perform automatic clicks
    threading.Thread(target=start_auto_click).start()


def stop_button_clicked(e):
    global loading_in_progress

    # Stop the loading once finished
    loading_in_progress = False
    # Stop the automatic clicks
    threading.Thread(target=stop_auto_click).start()


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
                        [
                            ft.ProgressRing(
                                visible=True, width=10, height=10),
                            ft.OutlinedButton(
                                "Start",
                                on_click=start_button_clicked,
                                icon=ft.icons.PLAY_ARROW_ROUNDED
                            ),
                            ft.TextButton(
                                "Stop",
                                on_click=stop_button_clicked,
                                icon=ft.icons.STOP_ROUNDED
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
