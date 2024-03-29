import importlib.util
import os
import sys
from os.path import isfile, join
from pathlib import Path

import flet as ft


class GridItem:
    def __init__(self, id):
        self.id = id
        self.name = None
        self.items = []
        self.description = None
        self.parent = None


class Item:
    def __init__(self):
        self.name = None
        self.file_name = None
        self.icon = None
        self.order = None
        self.layout = None
        self.source_code = None


class ControlGroup:
    def __init__(self, name, label, icon, selected_icon):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.grid_items = []


class GalleryData:
    def __init__(self):
        self.import_modules()

    destinations_list = [
        ControlGroup(
            name="scripts",
            label="Scripts",
            icon=ft.icons.DESCRIPTION,
            selected_icon=ft.icons.DESCRIPTION_SHARP,
        ),
    ]

    def list_control_dirs(self, dir):
        file_path = os.path.join(str(Path(__file__).parent), dir)
        control_dirs = [
            f
            for f in os.listdir(file_path)
            if not isfile(f)
            and f not in ["index.py", "images", "__pycache__", ".venv", ".git"]
        ]
        return control_dirs

    def list_example_files(self, control_group_dir, control_dir):
        file_path = os.path.join(
            str(Path(__file__).parent), control_group_dir, control_dir
        )
        example_files = [f for f in os.listdir(
            file_path) if not f.startswith("_")]
        return example_files

    def import_modules(self):
        for control_group_dir in self.destinations_list:
            for control_dir in self.list_control_dirs(control_group_dir.name):
                grid_item = GridItem(control_dir)

                for file in self.list_example_files(
                    control_group_dir.name, control_dir
                ):
                    file_name = os.path.join(
                        control_group_dir.name, control_dir, file)
                    module_name = file_name.replace(
                        "/", ".").replace(".py", "")

                    if module_name in sys.modules:
                        print(f"{module_name!r} already in sys.modules")
                    else:
                        file_path = os.path.join(
                            str(Path(__file__).parent), file_name)

                        spec = importlib.util.spec_from_file_location(
                            module_name, file_path
                        )
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        print(f"{module_name!r} has been imported")
                        if file == "index.py":
                            grid_item.name = module.name
                            grid_item.description = module.description
                            grid_item.icon = module.icon
                            grid_item.parent = control_group_dir
                        else:
                            item = Item()
                            item.layout = module.layout

                            item.file_name = (
                                module_name.replace(".", "/") + ".py"
                            )
                            item.name = "See code on github"
                            item.order = file[
                                :2
                            ]  # first 2 characters of example file name (e.g. '01')
                            grid_item.items.append(item)
                grid_item.items.sort(key=lambda x: x.order)
                control_group_dir.grid_items.append(grid_item)
