import flet as ft


def example():
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.AUTO_FIX_HIGH),
                        title=ft.Text("Greater Magic Wand"),
                        subtitle=ft.Text(
                            "Buy Greater Magic Essence at 15s."
                        ),
                    ),
                    ft.Row(
                        [ft.TextButton("Start"),
                         ft.TextButton("Stop")],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ]
            ),
            width=400,
            padding=10,
        )
    )
