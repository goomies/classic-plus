import logging
from pathlib import Path
import flet as ft
import flet_fastapi
from gallerydata import GalleryData
from left_navigation_menu import LeftNavigationMenu
from controls_grid import ControlsGrid
from layouts_view import LayoutsView

gallery = GalleryData()

logging.basicConfig(level=logging.INFO)


async def main(page: ft.Page):
    page.window_width = 655
    page.window_height = 350
    page.window_resizable = True
    page.title = "Classic Plus"
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }

    def get_route_list(route):
        route_list = [item for item in route.split("/") if item != ""]
        return route_list

    async def route_change(e):
        route_list = get_route_list(page.route)
        if len(route_list) == 0:
            await page.go_async("/scripts")
        elif len(route_list) == 1:
            await display_controls_grid(control_group_name=route_list[0])
        elif len(route_list) == 2:
            layouts_view.control_group_name = route_list[0]
            layouts_view.control_name = route_list[1]
            await display_control_layouts()
        else:
            print("Invalid route")

    async def display_controls_grid(control_group_name):
        controls_grid.display(control_group_name)
        left_nav.rail.selected_index = gallery.destinations_list.index(
            controls_grid.control_group
        )
        layouts_view.visible = False
        layouts_view.layouts.controls = []
        await page.update_async()

    async def display_control_layouts():
        layouts_view.display()
        left_nav.rail.selected_index = gallery.destinations_list.index(
            layouts_view.control_group
        )
        controls_grid.visible = False

        await page.update_async()

    left_nav = LeftNavigationMenu(gallery=gallery)
    controls_grid = ControlsGrid(gallery=gallery)
    layouts_view = LayoutsView(gallery=gallery)

    page.theme_mode = ft.ThemeMode.DARK
    page.on_error = lambda e: print("Page error:", e.data)

    await page.add_async(
        ft.Row(
            [left_nav, ft.VerticalDivider(
                width=1), controls_grid, layouts_view],
            expand=True,
        )
    )

    page.on_route_change = route_change
    print(f"Initial route: {page.route}")
    await page.go_async(page.route)


app = flet_fastapi.app(
    main, assets_dir=str(Path(__file__).resolve().parent.joinpath("assets"))
)

if __name__ == "__main__":
    ft.app(main, assets_dir="assets")
