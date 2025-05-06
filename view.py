import flet as ft


def build_main_view(page: ft.Page, controller):
    page.title = "TaskManager"
    page.scroll = "adaptive"

    # Ряд кнопок управления
    save_button = ft.Button(
        "Сохранить задачи",
        expand=True,
        on_click=controller.save_tasks,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue")
    )
    was_success_button = ft.Button(
        "Выполненные задачи",
        expand=True,
        on_click=controller.show_success_tasks,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue")
    )
    clr_button = ft.Button(
        "Отчистить сохранённые задачи",
        expand=True,
        on_click=controller.clear_tasks,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue")
    )
    page.add(ft.Row([save_button, clr_button, was_success_button]))

    # Поле ввода новой задачи и выбор времени
    new_task = ft.TextField(hint_text="Чтобы вы хотели сделать?", expand=True)

    # Создаём виджет для выбора времени и кнопку для его открытия
    time_button = ft.ElevatedButton("Выбрать время", width=120)
    time_picker = ft.TimePicker(
        confirm_text="Выбрать",
        cancel_text="Отмена",
        help_text="Выбери время",
        on_change=lambda e: controller.pick_time(e, time_button)
    )
    time_button.on_click = lambda e: page.open(time_picker)

    add_button = ft.ElevatedButton(
        "Добавить в список",
        width=200,
        on_click=lambda e: controller.add_task(e, new_task, time_picker, time_button)
    )
    page.add(ft.Row([new_task, time_button, add_button]))

    # Отображаем список задач, находящихся в процессе выполнения
    for task in controller.model.in_progress:
        page.add(ft.Checkbox(label=task, on_change=controller.mark_success))
