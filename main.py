import flet as ft
from controller import TaskController
from view import build_main_view

def main(page: ft.Page):
    controller = TaskController(page)
    build_main_view(page, controller)

if __name__ == '__main__':
    ft.app(target=main)