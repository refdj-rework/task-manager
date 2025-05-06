import flet as ft
from model import TaskModel
from view import build_main_view  # используется для обновления интерфейса при переходе назад

class TaskController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.model = TaskModel()

    def add_task(self, e, new_task: ft.TextField, time_picker: ft.TimePicker, time_button: ft.ElevatedButton):
        new_task.border_color = ""
        new_task.update()
        stripped = new_task.value.strip()
        if len(stripped) > 0:
            tmpckr = str(time_picker.value)
            task_with_time = stripped + " в " + tmpckr[0:5]
            # Создаём checkbox для новой задачи
            checkbox = ft.Checkbox(label=task_with_time, on_change=self.mark_success)
            self.page.add(checkbox)
            self.model.add_in_progress(task_with_time)
            new_task.value = ""
            new_task.focus()
            new_task.update()
            time_button.text = "Выбрать время"
            time_button.update()
        else:
            new_task.border_color = "RED"
            new_task.update()

    def mark_success(self, e: ft.ControlEvent):
        task_label = str(e.control.label)
        # Перемещаем задачу из in_progress в sucses
        self.model.add_success(task_label)
        self.model.remove_in_progress(task_label)
        e.control.page.remove(e.control)

    def pick_time(self, e, time_button: ft.ElevatedButton):
        tmpckr = str(e.control.value)
        time_button.text = tmpckr[0:5]
        time_button.update()

    def save_tasks(self, e):
        self.model.save_tasks()

    def clear_tasks(self, e):
        self.model.clear_tasks()
        # Перестраиваем основной интерфейс после очистки
        self.page.clean()
        build_main_view(self.page, self)

    def show_success_tasks(self, e):
        self.page.clean()

        # Локальная функция для возвращения назад
        def back(e_back):
            self.page.clean()
            build_main_view(self.page, self)

        def clear_success(e_clear):
            self.model.sucses.clear()
            self.page.clean()
            self.show_success_tasks(e)

        def delete_task(e_del):
            self.page.remove(e_del.control)

        back_btn = ft.ElevatedButton("Назад", on_click=back, width=300)
        clear_btn = ft.ElevatedButton("Отчистить", on_click=clear_success, width=250)
        self.page.add(ft.Row([back_btn, clear_btn]))
        for task in self.model.sucses:
            self.page.add(ft.TextButton(task, on_click=delete_task, icon=ft.CupertinoIcons.TRASH))
